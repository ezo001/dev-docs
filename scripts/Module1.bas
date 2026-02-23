Attribute VB_Name = "Module1"
Option Explicit

' =========================================================
' Safe utilities (shared by all macros)
' =========================================================

Private Function IsCodeFontName(ByVal nm As String) As Boolean
    If Len(nm) = 0 Then Exit Function
    nm = LCase$(nm)
    IsCodeFontName = (InStr(nm, "consolas") > 0) Or _
                     (InStr(nm, "courier new") > 0) Or _
                     (InStr(nm, "courier") > 0)
End Function

Private Function NonCodeTextFromParagraph(p As Paragraph) As String
    Dim r As Range, buf As String
    Set r = p.Range
    
    If r.Characters.count <= 1 Then Exit Function
    
    Dim i As Long
    For i = 1 To r.Characters.count - 1
        If Not IsCodeFontName(r.Characters(i).Font.Name) Then
            buf = buf & r.Characters(i).text
        End If
    Next i
    
    NonCodeTextFromParagraph = buf
End Function

Private Function IsHeadingPara(p As Paragraph) As Boolean
    On Error Resume Next
    IsHeadingPara = (InStr(p.Style.NameLocal, "Heading") > 0)
    On Error GoTo 0
End Function

Private Function ContainsXMLTag(text As String) As Boolean
    Dim i As Long
    For i = 1 To Len(text) - 1
        If Mid$(text, i, 1) = "<" Then
            Dim nextChar As String
            nextChar = Mid$(text, i + 1, 1)
            If nextChar >= "A" And nextChar <= "Z" Then
                ContainsXMLTag = True
                Exit Function
            End If
        End If
    Next i
    ContainsXMLTag = False
End Function

Private Function ContainsSmartQuotes(text As String) As Boolean
    ContainsSmartQuotes = (InStr(text, ChrW(8216)) > 0) Or _
                          (InStr(text, ChrW(8217)) > 0) Or _
                          (InStr(text, ChrW(8220)) > 0) Or _
                          (InStr(text, ChrW(8221)) > 0)
End Function

Private Function CountOccurrences(findText As String) As Long
    Dim count As Long
    count = 0
    
    With ActiveDocument.Content.Find
        .ClearFormatting
        .text = findText
        .Forward = True
        .Wrap = wdFindStop
        .Format = False
        
        Do While .Execute
            count = count + 1
        Loop
    End With
    
    CountOccurrences = count
End Function

' Returns count of hyperlinks and plain-text occurrences of greetings.accenture.com; reportText is filled with details.
Private Sub CheckGreetingsAccentureLinks(ByRef linkCount As Long, ByRef reportText As String)
    Const GREETINGS_DOMAIN As String = "greetings.accenture.com"
    Dim h As Hyperlink
    Dim addr As String
    Dim foundAddresses As String
    Dim findCount As Long
    
    linkCount = 0
    reportText = ""
    foundAddresses = ""
    
    ' Check hyperlinks
    On Error Resume Next
    For Each h In ActiveDocument.Hyperlinks
        addr = h.Address
        If Len(addr) > 0 And InStr(1, addr, GREETINGS_DOMAIN, vbTextCompare) > 0 Then
            linkCount = linkCount + 1
            If Len(foundAddresses) < 800 Then
                foundAddresses = foundAddresses & "� " & Left$(addr, 100) & vbCrLf
            End If
        End If
    Next h
    On Error GoTo 0
    
    ' Check plain text (e.g. pasted URLs) via Find
    With ActiveDocument.Content.Find
        .ClearFormatting
        .Replacement.ClearFormatting
        .text = GREETINGS_DOMAIN
        .Forward = True
        .Wrap = wdFindStop
        .MatchCase = False
        .MatchWholeWord = False
        findCount = 0
        Do While .Execute
            findCount = findCount + 1
        Loop
    End With
    
    If linkCount > 0 Or findCount > 0 Then
        reportText = "greetings.accenture.com links (consider replacing with internal or approved image hosting):" & vbCrLf
        If linkCount > 0 Then
            reportText = reportText & "Hyperlinks: " & linkCount & vbCrLf & foundAddresses
            If findCount > 0 Then reportText = reportText & vbCrLf
        End If
        If findCount > 0 Then reportText = reportText & "Plain text occurrences: " & findCount
    End If
End Sub

' =========================================================
' CHECKER - Read-only analysis
' =========================================================
Public Sub CheckMDXCompatibility()
    Dim p As Paragraph
    Dim textNC As String
    Dim issues As String
    Dim count As Long
    
    Application.ScreenUpdating = False
    Application.StatusBar = "Checking for MDX issues..."
    
    issues = ""
    count = 0
    
    For Each p In ActiveDocument.Paragraphs
        textNC = NonCodeTextFromParagraph(p)
        If Len(Trim$(textNC)) = 0 Then GoTo NextPara
        
        If InStr(textNC, "<") > 0 And InStr(textNC, "@") > 0 And InStr(textNC, ">") > 0 Then
            issues = issues & "� Email with <brackets>: " & Left$(Trim$(textNC), 80) & vbCrLf
            count = count + 1
        End If
        
        If ContainsXMLTag(textNC) Then
            issues = issues & "� XML-like tag: " & Left$(Trim$(textNC), 80) & vbCrLf
            count = count + 1
        End If
        
        If ContainsSmartQuotes(textNC) Then
            issues = issues & "� Smart quotes: " & Left$(Trim$(textNC), 80) & vbCrLf
            count = count + 1
        End If
        
        If InStr(textNC, "{") > 0 Or InStr(textNC, "}") > 0 Then
            issues = issues & "� Curly braces: " & Left$(Trim$(textNC), 80) & vbCrLf
            count = count + 1
        End If
        
        If IsHeadingPara(p) Then
            If InStr(textNC, "@") > 0 Or InStr(textNC, "{") > 0 Or InStr(textNC, "<") > 0 Then
                issues = issues & "� Special chars in heading: " & Left$(Trim$(textNC), 80) & vbCrLf
                count = count + 1
            End If
        End If
        
NextPara:
    Next p
    
    ' Check for greetings.accenture.com links (often image URLs)
    Dim greetingsCount As Long
    Dim greetingsReport As String
    CheckGreetingsAccentureLinks greetingsCount, greetingsReport
    If greetingsCount > 0 Or Len(greetingsReport) > 0 Then
        issues = issues & vbCrLf & "� " & greetingsReport & vbCrLf
        count = count + 1
    End If
    
    Application.ScreenUpdating = True
    Application.StatusBar = ""
    
    If count = 0 Then
        MsgBox "No MDX issues found! Document is ready.", vbInformation, "PASSED"
    Else
        Dim report As String
        report = "Found " & count & " issue(s):" & vbCrLf & vbCrLf
        
        If Len(issues) > 1200 Then
            report = report & Left$(issues, 1200) & vbCrLf & "..."
        Else
            report = report & issues
        End If
        
        report = report & vbCrLf & "TIP: Format code with Consolas/Courier."
        
        MsgBox report, vbExclamation, "FAILED - " & count & " issues"
    End If
End Sub

' =========================================================
' CHECKER - greetings.accenture.com links (e.g. image URLs)
' =========================================================
Public Sub CheckGreetingsAccentureImageLinks()
    Dim linkCount As Long
    Dim reportText As String
    
    Application.ScreenUpdating = False
    Application.StatusBar = "Checking for greetings.accenture.com links..."
    
    CheckGreetingsAccentureLinks linkCount, reportText
    
    Application.ScreenUpdating = True
    Application.StatusBar = ""
    
    If Len(reportText) = 0 Then
        MsgBox "No greetings.accenture.com links found.", vbInformation, "PASSED"
    Else
        MsgBox "greetings.accenture.com links found (often image URLs; consider replacing with internal or approved hosting):" & vbCrLf & vbCrLf & reportText, vbExclamation, "Check greetings.accenture.com"
    End If
End Sub

' =========================================================
' FIX 1: Smart Quotes
' =========================================================
Public Sub Fix1_SmartQuotes()
    Dim leftSingle As Long, rightSingle As Long
    Dim leftDouble As Long, rightDouble As Long
    
    Application.ScreenUpdating = False
    
    leftSingle = CountOccurrences(ChrW(8216))
    rightSingle = CountOccurrences(ChrW(8217))
    leftDouble = CountOccurrences(ChrW(8220))
    rightDouble = CountOccurrences(ChrW(8221))
    
    Dim totalFound As Long
    totalFound = leftSingle + rightSingle + leftDouble + rightDouble
    
    If totalFound = 0 Then
        MsgBox "No smart quotes found.", vbInformation, "Nothing to Fix"
        Exit Sub
    End If
    
    Dim msg As String
    msg = "Found smart quotes:" & vbCrLf & vbCrLf
    If leftSingle > 0 Then msg = msg & "� Left single: " & leftSingle & vbCrLf
    If rightSingle > 0 Then msg = msg & "� Right single: " & rightSingle & vbCrLf
    If leftDouble > 0 Then msg = msg & "� Left double: " & leftDouble & vbCrLf
    If rightDouble > 0 Then msg = msg & "� Right double: " & rightDouble & vbCrLf
    msg = msg & vbCrLf & "Replace all?"
    
    If MsgBox(msg, vbYesNo + vbQuestion) = vbNo Then Exit Sub
    
    With ActiveDocument.Content.Find
        .ClearFormatting
        .Replacement.ClearFormatting
        .text = ChrW(8216)
        .Replacement.text = "'"
        .Forward = True
        .Wrap = wdFindContinue
        .Execute Replace:=wdReplaceAll
    End With
    
    With ActiveDocument.Content.Find
        .text = ChrW(8217)
        .Replacement.text = "'"
        .Execute Replace:=wdReplaceAll
    End With
    
    With ActiveDocument.Content.Find
        .text = ChrW(8220)
        .Replacement.text = chR(34)
        .Execute Replace:=wdReplaceAll
    End With
    
    With ActiveDocument.Content.Find
        .text = ChrW(8221)
        .Replacement.text = chR(34)
        .Execute Replace:=wdReplaceAll
    End With
    
    Application.ScreenUpdating = True
    
    MsgBox "Replaced " & totalFound & " smart quotes.", vbInformation, "Complete"
End Sub

' =========================================================
' FIX 2: Dashes
' =========================================================
Public Sub Fix2_Dashes()
    Application.ScreenUpdating = False
    
    With ActiveDocument.Content.Find
        .ClearFormatting
        .Replacement.ClearFormatting
        .text = ChrW(8211)
        .Replacement.text = "-"
        .Forward = True
        .Wrap = wdFindContinue
        .Execute Replace:=wdReplaceAll
    End With
    
    With ActiveDocument.Content.Find
        .text = ChrW(8212)
        .Replacement.text = "-"
        .Execute Replace:=wdReplaceAll
    End With
    
    Application.ScreenUpdating = True
    
    MsgBox "En/Em dashes converted to hyphens.", vbInformation, "Complete"
End Sub

' =========================================================
' FIX 3: NBSP
' =========================================================
Public Sub Fix3_NonBreakingSpaces()
    Application.ScreenUpdating = False
    
    With ActiveDocument.Content.Find
        .ClearFormatting
        .Replacement.ClearFormatting
        .text = ChrW(160)
        .Replacement.text = " "
        .Forward = True
        .Wrap = wdFindContinue
        .Execute Replace:=wdReplaceAll
    End With
    
    Application.ScreenUpdating = True
    
    MsgBox "NBSP replaced with regular spaces.", vbInformation, "Complete"
End Sub

' =========================================================
' FIX 4: Zero-width
' =========================================================
Public Sub Fix4_ZeroWidthChars()
    Application.ScreenUpdating = False
    
    With ActiveDocument.Content.Find
        .ClearFormatting
        .Replacement.ClearFormatting
        .text = ChrW(8203)
        .Replacement.text = ""
        .Forward = True
        .Wrap = wdFindContinue
        .Execute Replace:=wdReplaceAll
    End With
    
    With ActiveDocument.Content.Find
        .text = ChrW(8204)
        .Replacement.text = ""
        .Execute Replace:=wdReplaceAll
    End With
    
    With ActiveDocument.Content.Find
        .text = ChrW(8205)
        .Replacement.text = ""
        .Execute Replace:=wdReplaceAll
    End With
    
    Application.ScreenUpdating = True
    
    MsgBox "Zero-width characters removed.", vbInformation, "Complete"
End Sub

' =========================================================
' Empty paragraphs
' =========================================================
Public Sub DeleteEmptyParagraphs()
    Dim para As Paragraph
    Dim deleteCount As Long
    Dim i As Long
    
    deleteCount = 0
    Application.ScreenUpdating = False
    
    For i = ActiveDocument.Paragraphs.count To 1 Step -1
        Set para = ActiveDocument.Paragraphs(i)
        
        If Len(Trim(para.Range.text)) <= 1 Then
            para.Range.Delete
            deleteCount = deleteCount + 1
        End If
    Next i
    
    Application.ScreenUpdating = True
    
    If deleteCount > 0 Then
        MsgBox "Deleted " & deleteCount & " empty paragraphs.", vbInformation, "Complete"
    Else
        MsgBox "No empty paragraphs found.", vbInformation, "Complete"
    End If
End Sub

' =========================================================
' DEBUG: Show where curly braces are found
' =========================================================
Public Sub Debug_FindCurlyBraces()
    Dim p As Paragraph
    Dim textNC As String
    Dim findings As String
    Dim count As Long
    
    Application.ScreenUpdating = False
    
    findings = ""
    count = 0
    
    For Each p In ActiveDocument.Paragraphs
        textNC = NonCodeTextFromParagraph(p)
        
        If InStr(textNC, "{") > 0 Or InStr(textNC, "}") > 0 Then
            count = count + 1
            
            ' Show the full paragraph and what fonts are used
            Dim fontInfo As String
            fontInfo = GetParagraphFontInfo(p)
            
            findings = findings & "=== Issue #" & count & " ===" & vbCrLf
            findings = findings & "Text: " & Left$(Trim$(p.Range.text), 100) & vbCrLf
            findings = findings & "Fonts: " & fontInfo & vbCrLf
            findings = findings & "Non-code text: " & Left$(textNC, 100) & vbCrLf & vbCrLf
            
            If count >= 10 Then
                findings = findings & "... (showing first 10 only)"
                Exit For
            End If
        End If
    Next p
    
    Application.ScreenUpdating = True
    
    If count = 0 Then
        MsgBox "No curly braces found outside code fonts.", vbInformation
    Else
        ' Create a new document with the findings
        Dim newDoc As Document
        Set newDoc = Documents.Add
        newDoc.Content.text = "CURLY BRACE DEBUG REPORT" & vbCrLf & _
                              "Found " & count & " paragraphs with curly braces" & vbCrLf & _
                              String(50, "=") & vbCrLf & vbCrLf & findings
        
        MsgBox "Debug report created in new document. Review it to see where the braces are.", vbInformation
    End If
End Sub

Private Function GetParagraphFontInfo(p As Paragraph) As String
    Dim r As Range
    Dim i As Long
    Dim fonts As String
    Dim lastFont As String
    
    Set r = p.Range
    fonts = ""
    lastFont = ""
    
    ' Sample up to 20 characters
    Dim limit As Long
    limit = r.Characters.count
    If limit > 20 Then limit = 20
    
    For i = 1 To limit
        Dim fontName As String
        fontName = r.Characters(i).Font.Name
        
        If fontName <> lastFont Then
            If fonts <> "" Then fonts = fonts & ", "
            fonts = fonts & fontName
            lastFont = fontName
        End If
    Next i
    
    GetParagraphFontInfo = fonts
End Function

