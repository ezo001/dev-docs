Attribute VB_Name = "FindEMFImages"
' FindEMFImages - Lists page numbers of EMF images in the active Word document.
' Use: Open a .docx, run macro "FindEMFImagesInDocument", view the dialog.
' To install: Word > Developer > Visual Basic > File > Import File > select this .bas

Option Explicit

Private Const WdActiveEndPageNumber As Long = 3
' Diagnostic message when embedded EMF scan fails (set by CollectEmbeddedEMFPages)
Private gEMFDiag As String

' Word does not have Application.Wait (Excel only). Use Timer + DoEvents.
Private Sub WaitSeconds(ByVal secs As Single)
    Dim endTime As Double
    endTime = Timer + secs
    Do While Timer < endTime
        DoEvents
    Loop
End Sub

Public Sub FindEMFImagesInDocument()
    Dim doc As Document
    Dim results As Collection
    Dim msg As String
    Dim i As Long
    Dim s As String
    Dim pageList As String

    Set doc = ActiveDocument

    If doc.Path = "" Then
        MsgBox "Please save the document first (as .docx) so EMF parts can be detected.", vbExclamation
        Exit Sub
    End If

    Set results = New Collection
    Application.StatusBar = "Scanning for EMF images..."
    ' 1) Find linked EMF pictures (source path ends with .emf)
    CollectLinkedEMFPages doc, results
    ' 2) Find embedded EMF by reading docx package (document.xml.rels + document.xml)
    CollectEmbeddedEMFPages doc, results
    Application.StatusBar = False

    If results.Count = 0 Then
        If Len(gEMFDiag) > 0 Then
            MsgBox "No EMF images found in this document." & vbCrLf & vbCrLf & gEMFDiag, vbInformation, "EMF Images"
        Else
            MsgBox "No EMF images found in this document.", vbInformation
        End If
        Exit Sub
    End If

    ' Build unique page list (sorted)
    pageList = BuildSortedPageList(results)
    msg = "EMF images found: " & results.Count & vbCrLf & vbCrLf & _
          "Page number(s) that include EMF image(s):" & vbCrLf & vbCrLf & pageList
    MsgBox msg, vbInformation, "EMF Images – Page Numbers"
End Sub

' Collect page numbers for linked pictures whose source is .emf
Private Sub CollectLinkedEMFPages(ByVal doc As Document, ByRef results As Collection)
    Dim ish As InlineShape
    Dim sh As Shape
    Dim pageNum As Long
    Dim key As String
    Dim src As String

    On Error Resume Next
    For Each ish In doc.InlineShapes
        If ish.Type = 3 Or ish.Type = 4 Then ' wdInlineShapePicture or wdInlineShapeLinkedPicture
            src = ""
            If ish.Type = 4 Then src = ish.LinkFormat.SourceFullName
            If LCase(Right(src, 4)) = ".emf" Then
                pageNum = ish.Range.Information(WdActiveEndPageNumber)
                key = "P" & pageNum
                If Not ContainsKey(results, key) Then results.Add pageNum, key
            End If
        End If
    Next ish

    For Each sh In doc.Shapes
        If sh.Type = 11 Or sh.Type = 13 Then ' msoLinkedPicture, msoPicture
            src = ""
            If sh.Type = 11 Then src = sh.LinkFormat.SourceFullName
            If LCase(Right(src, 4)) = ".emf" Then
                pageNum = sh.Anchor.Information(WdActiveEndPageNumber)
                key = "P" & pageNum
                If Not ContainsKey(results, key) Then results.Add pageNum, key
            End If
        End If
    Next sh
    On Error GoTo 0
End Sub

' Collect page numbers for embedded EMF by reading the docx (zip) package.
' Uses only Shell.Application (no cmd/tar) so it works when IT blocks cmd.exe (TAP).
Private Sub CollectEmbeddedEMFPages(ByVal doc As Document, ByRef results As Collection)
    Dim fso As Object
    Dim docPath As String
    Dim zipPath As String
    Dim basePath As String
    Dim extractPath As String
    Dim relsPath As String
    Dim docXmlPath As String
    Dim emfRids As Collection
    Dim paraIndices As Collection
    Dim i As Long
    Dim pageNum As Long
    Dim key As String
    Dim waitCount As Long
    Dim sh As Object
    Dim paraIdx As Long

    gEMFDiag = ""
    docPath = doc.FullName
    If LCase(Right(docPath, 5)) <> ".docx" Then Exit Sub

    Set fso = CreateObject("Scripting.FileSystemObject")
    basePath = fso.GetSpecialFolder(2).Path & "\FindEMF_" & Format(Now, "yyyymmddhhnnss")
    zipPath = basePath & "\doc.zip"
    extractPath = basePath & "\extract"
    fso.CreateFolder basePath
    fso.CreateFolder extractPath

    relsPath = extractPath & "\word\_rels\document.xml.rels"
    docXmlPath = extractPath & "\word\document.xml"

    On Error GoTo Cleanup
    ' Copy docx to zip inside base folder; extract to subfolder (avoids Shell quirks with sibling zip/folder)
    fso.CopyFile docPath, zipPath, True
    Set sh = CreateObject("Shell.Application")
    sh.NameSpace(extractPath).CopyHere sh.NameSpace(zipPath).Items(), 4 + 16 + 512
    WaitSeconds 3
    waitCount = 0
    Do While Not fso.FileExists(relsPath) And waitCount < 45
        WaitSeconds 1
        waitCount = waitCount + 1
    Loop
    If Not fso.FileExists(relsPath) Or Not fso.FileExists(docXmlPath) Then
        gEMFDiag = "Extraction did not complete in time: word\_rels\document.xml.rels or word\document.xml missing after " & waitCount & "s. Try closing other programs and run again."
        GoTo Cleanup
    End If

    Set emfRids = GetEmfRelationshipIds(relsPath)
    If emfRids Is Nothing Then
        gEMFDiag = "Could not parse document.xml.rels (XML load failed)."
        GoTo Cleanup
    End If
    If emfRids.Count = 0 Then
        gEMFDiag = "No EMF relationships found in document (rels parsed but no .emf targets)."
        GoTo Cleanup
    End If

    Set paraIndices = GetParagraphIndicesForBlips(docXmlPath, emfRids)
    If paraIndices Is Nothing Then
        gEMFDiag = "Could not parse word\document.xml (XML load failed)."
        GoTo Cleanup
    End If
    If paraIndices.Count = 0 Then
        gEMFDiag = "Found " & emfRids.Count & " EMF image(s) in package but could not match them to paragraphs in document.xml."
        GoTo Cleanup
    End If

    ' Map paragraph indices to page numbers (Word body paragraphs match document.xml w:p order)
    For i = 1 To paraIndices.Count
        paraIdx = paraIndices(i)
        If paraIdx < 1 Then paraIdx = 1
        If paraIdx > doc.Paragraphs.Count Then paraIdx = doc.Paragraphs.Count
        If doc.Paragraphs.Count >= 1 Then
            pageNum = doc.Paragraphs(paraIdx).Range.Information(WdActiveEndPageNumber)
            key = "P" & pageNum
            If Not ContainsKey(results, key) Then results.Add pageNum, key
        End If
    Next i

Cleanup:
    On Error Resume Next
    Application.StatusBar = False
    If fso.FolderExists(basePath) Then fso.DeleteFolder basePath, True
    On Error GoTo 0
End Sub

' Get r:embed value from a blip node (handles namespaced attribute in OOXML)
Private Function GetBlipEmbedId(ByVal blip As Object) As String
    Dim k As Long
    On Error Resume Next
    GetBlipEmbedId = blip.getAttribute("embed")
    If Len(GetBlipEmbedId) > 0 Then Exit Function
    GetBlipEmbedId = blip.getAttribute("r:embed")
    If Len(GetBlipEmbedId) > 0 Then Exit Function
    For k = 0 To blip.Attributes.Length - 1
        If LCase(blip.Attributes(k).nodeName) = "embed" Or InStr(1, blip.Attributes(k).nodeName, "embed", vbTextCompare) > 0 Then
            GetBlipEmbedId = blip.Attributes(k).nodeValue
            Exit Function
        End If
    Next k
    On Error GoTo 0
End Function

' Parse document.xml.rels and return collection of Relationship Id values where Target ends with .emf
Private Function GetEmfRelationshipIds(ByVal relsPath As String) As Collection
    Dim xml As Object
    Dim nodeList As Object
    Dim node As Object
    Dim target As String
    Dim id As String
    Dim c As Collection
    Dim fso As Object
    Dim f As Object

    Set c = New Collection
    Set xml = CreateObject("MSXML2.DOMDocument.6.0")
    xml.async = False
    xml.setProperty "SelectionLanguage", "XPath"
    xml.setProperty "SelectionNamespaces", "xmlns:r='http://schemas.openxmlformats.org/package/2006/relationships'"
    On Error Resume Next
    If Not xml.Load(relsPath) Then
        Set fso = CreateObject("Scripting.FileSystemObject")
        Set f = fso.OpenTextFile(relsPath, 1, False, -1)
        xml.LoadXML f.ReadAll
        f.Close
    End If
    On Error GoTo 0
    If xml.parseError.ErrorCode <> 0 Then Exit Function

    Set nodeList = xml.SelectNodes("//*[local-name()='Relationship' and @Target]")
    If nodeList Is Nothing Then Exit Function
    Dim i As Long
    For i = 0 To nodeList.Length - 1
        Set node = nodeList(i)
        target = node.getAttribute("Target")
        If InStr(1, target, ".emf", vbTextCompare) > 0 Then
            id = node.getAttribute("Id")
            If Len(id) > 0 Then
                On Error Resume Next
                c.Add id, id
                On Error GoTo 0
            End If
        End If
    Next i
    Set GetEmfRelationshipIds = c
End Function

' Parse word/document.xml and return 1-based paragraph indices for paragraphs that contain a:blip with r:embed in emfRids
Private Function GetParagraphIndicesForBlips(ByVal docXmlPath As String, ByVal emfRids As Collection) As Collection
    Dim xml As Object
    Dim ns As String
    Dim paraNodes As Object
    Dim para As Object
    Dim blip As Object
    Dim embedId As String
    Dim rid As Variant
    Dim c As Collection
    Dim idx As Long
    Dim i As Long
    Dim j As Long

    Set c = New Collection
    Set xml = CreateObject("MSXML2.DOMDocument.6.0")
    xml.async = False
    xml.setProperty "SelectionLanguage", "XPath"
    ns = "xmlns:w='http://schemas.openxmlformats.org/wordprocessingml/2006/main' " & _
         "xmlns:a='http://schemas.openxmlformats.org/drawingml/2006/main' " & _
         "xmlns:r='http://schemas.openxmlformats.org/officeDocument/2006/relationships'"
    xml.setProperty "SelectionNamespaces", ns
    On Error Resume Next
    If Not xml.Load(docXmlPath) Then
        Dim fsoDoc As Object
        Dim fDoc As Object
        Set fsoDoc = CreateObject("Scripting.FileSystemObject")
        Set fDoc = fsoDoc.OpenTextFile(docXmlPath, 1, False, -1)
        xml.LoadXML fDoc.ReadAll
        fDoc.Close
    End If
    On Error GoTo 0
    If xml.parseError.ErrorCode <> 0 Then Exit Function

    Set paraNodes = xml.SelectNodes("//w:p")
    If paraNodes Is Nothing Then Exit Function

    idx = 0
    For i = 0 To paraNodes.Length - 1
        idx = idx + 1
        Set para = paraNodes(i)
        Set blip = para.SelectSingleNode(".//a:blip[@r:embed]")
        If blip Is Nothing Then Set blip = para.SelectSingleNode(".//*[local-name()='blip' and @*[local-name()='embed']]")
        If Not blip Is Nothing Then
            embedId = GetBlipEmbedId(blip)
            If Len(embedId) = 0 Then embedId = blip.getAttribute("r:embed")
            If Len(embedId) = 0 Then embedId = blip.getAttribute("embed")
            For j = 1 To emfRids.Count
                If emfRids(j) = embedId Then
                    c.Add idx
                    Exit For
                End If
            Next j
        End If
    Next i
    Set GetParagraphIndicesForBlips = c
End Function

Private Function ContainsKey(ByVal c As Collection, ByVal key As String) As Boolean
    On Error Resume Next
    c.Item key
    ContainsKey = (Err.Number = 0)
    On Error GoTo 0
End Function

Private Function BuildSortedPageList(ByVal c As Collection) As String
    Dim arr() As Long
    Dim i As Long
    Dim j As Long
    Dim t As Long
    Dim out As String

    If c.Count = 0 Then BuildSortedPageList = "(none)": Exit Function
    ReDim arr(1 To c.Count)
    For i = 1 To c.Count
        arr(i) = c(i)
    Next i
    ' Sort (bubble)
    For i = 1 To UBound(arr) - 1
        For j = i + 1 To UBound(arr)
            If arr(j) < arr(i) Then t = arr(i): arr(i) = arr(j): arr(j) = t
        Next j
    Next i
    out = ""
    For i = 1 To UBound(arr)
        out = out & "  Page " & arr(i) & vbCrLf
    Next i
    BuildSortedPageList = out
End Function
