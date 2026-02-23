' Run with: cscript //nologo FindEMFDiagnose.vbs "C:\path\to\file.docx"
' Diagnoses why EMF detection might fail (extraction, XML, paths).
Option Explicit
Dim fso, wsh, docPath, zipPath, extractPath, relsPath, docXmlPath
Dim psCmd, relsExists, docExists, xmlRels, xmlDoc, nodeList, node
Dim target, id, emfCount, c, blipCount, ns

If WScript.Arguments.Count < 1 Then
  WScript.Echo "Usage: cscript FindEMFDiagnose.vbs ""path\to\document.docx"""
  WScript.Quit 1
End If

docPath = WScript.Arguments(0)
Set fso = CreateObject("Scripting.FileSystemObject")
If Not fso.FileExists(docPath) Then
  WScript.Echo "File not found: " & docPath
  WScript.Quit 1
End If

extractPath = fso.GetSpecialFolder(2).Path & "\FindEMF_diag_" & Replace(Replace(Replace(Now(), "/", ""), ":", ""), " ", "")
zipPath = extractPath & ".zip"
fso.CreateFolder extractPath

WScript.Echo "Step 1: Copy docx to " & zipPath
fso.CopyFile docPath, zipPath, True

WScript.Echo "Step 2: Extract with tar (Windows 10+)"
Set wsh = CreateObject("WScript.Shell")
wsh.Run "cmd /c tar -xf """ & zipPath & """ -C """ & extractPath & """", 0, True
WScript.Sleep 500

relsPath = extractPath & "\word\_rels\document.xml.rels"
docXmlPath = extractPath & "\word\document.xml"
relsExists = fso.FileExists(relsPath)
docExists = fso.FileExists(docXmlPath)
WScript.Echo "Step 3: rels exists=" & relsExists & " docXml exists=" & docExists
WScript.Echo "  relsPath=" & relsPath
WScript.Echo "  docXmlPath=" & docXmlPath

If Not relsExists Then
  WScript.Echo "FAIL: document.xml.rels not found after extract."
  Cleanup
  WScript.Quit 1
End If

' Load rels and count EMF relationships
Set xmlRels = CreateObject("MSXML2.DOMDocument.6.0")
xmlRels.async = False
xmlRels.setProperty "SelectionLanguage", "XPath"
xmlRels.setProperty "SelectionNamespaces", "xmlns:r='http://schemas.openxmlformats.org/package/2006/relationships'"
If Not xmlRels.Load(relsPath) Then
  WScript.Echo "FAIL: Could not Load rels file. Parse error: " & xmlRels.parseError.reason
  Cleanup
  WScript.Quit 1
End If

Set nodeList = xmlRels.SelectNodes("//*[local-name()='Relationship' and @Target]")
emfCount = 0
For Each node In nodeList
  target = node.getAttribute("Target")
  If InStr(1, target, ".emf", 1) > 0 Then emfCount = emfCount + 1
Next
WScript.Echo "Step 4: EMF relationships found: " & emfCount

' Load document.xml and count blips
If Not docExists Then
  WScript.Echo "FAIL: document.xml not found."
  Cleanup
  WScript.Quit 1
End If
Set xmlDoc = CreateObject("MSXML2.DOMDocument.6.0")
xmlDoc.async = False
xmlDoc.setProperty "SelectionLanguage", "XPath"
ns = "xmlns:w='http://schemas.openxmlformats.org/wordprocessingml/2006/main' xmlns:a='http://schemas.openxmlformats.org/drawingml/2006/main' xmlns:r='http://schemas.openxmlformats.org/officeDocument/2006/relationships'"
xmlDoc.setProperty "SelectionNamespaces", ns
If Not xmlDoc.Load(docXmlPath) Then
  WScript.Echo "FAIL: Could not Load document.xml. Parse error: " & xmlDoc.parseError.reason
  Cleanup
  WScript.Quit 1
End If

Set nodeList = xmlDoc.SelectNodes("//w:p")
WScript.Echo "Step 5: Total //w:p count: " & nodeList.Length
Set nodeList = xmlDoc.SelectNodes("//*[local-name()='blip']")
blipCount = 0
If Not nodeList Is Nothing Then blipCount = nodeList.Length
WScript.Echo "Step 6: Total blip elements (any): " & blipCount
Set nodeList = xmlDoc.SelectNodes("//a:blip[@r:embed]")
c = 0
If Not nodeList Is Nothing Then c = nodeList.Length
WScript.Echo "Step 7: a:blip with r:embed count: " & c

WScript.Echo "Diagnosis complete. If emfCount>0 and blips exist, macro should find pages."
Cleanup
WScript.Quit 0

Sub Cleanup
  On Error Resume Next
  If fso.FolderExists(extractPath) Then fso.DeleteFolder extractPath, True
  If fso.FileExists(zipPath) Then fso.DeleteFile zipPath
End Sub
