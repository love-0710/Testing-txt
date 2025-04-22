If isValid Then
    WScript.Sleep 2000
    WshShell.SendKeys filePath
    WScript.Sleep 1000
    WshShell.SendKeys "{ENTER}"
Else
    WScript.Quit 1  ' Exit with failure code
End If




def proc = "wscript C:/path/to/upload.vbs".execute()
int exitCode = proc.waitFor()

if (exitCode != 0) {
    log.warn("Invalid file type. Upload aborted.")
    SampleResult.setSuccessful(false)
    SampleResult.setResponseMessage("Upload failed: Invalid file type.")
} else {
    log.info("File uploaded successfully.")
    SampleResult.setSuccessful(true)
}