Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' Get file path from the command-line argument
filePath = WScript.Arguments(0)

' Get file extension in lowercase
fileExt = LCase(fso.GetExtensionName(filePath))

' List of allowed extensions
allowedExts = Array("txt", "pdf", "xls", "doc", "xlsx", "docx", "ppt", "pptx", "rtf", "zip", "xml")

' Check if extension is allowed
isValid = False
For Each ext In allowedExts
    If fileExt = ext Then
        isValid = True
        Exit For
    End If
Next

If isValid Then
    WScript.Sleep 2000
    WshShell.SendKeys filePath
    WScript.Sleep 1000
    WshShell.SendKeys "{ENTER}"
Else
    WScript.Quit 1  ' Tell JMeter this failed
End If






def filePath = vars.get("filePath")
def proc = "wscript C:/path/to/upload.vbs \"${filePath}\"".execute()
int exitCode = proc.waitFor()

if (exitCode != 0) {
    log.warn("Invalid file type: " + filePath)
    SampleResult.setSuccessful(false)
    SampleResult.setResponseMessage("Upload failed: Invalid file type.")
} else {
    log.info("File uploaded successfully: " + filePath)
    SampleResult.setSuccessful(true)
    SampleResult.setResponseMessage("File upload completed.")
}
