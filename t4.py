Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

allowedExts = Array("txt", "pdf", "xls", "doc", "xlsx", "docx", "ppt", "pptx", "rtf", "zip", "xml")

For i = 0 To WScript.Arguments.Count - 1
    filePath = WScript.Arguments(i)
    fileExt = LCase(fso.GetExtensionName(filePath))
    isValid = False

    For Each ext In allowedExts
        If fileExt = ext Then
            isValid = True
            Exit For
        End If
    Next

    If isValid Then
        WScript.Sleep 1000
        WshShell.SendKeys filePath
        WScript.Sleep 1000
        WshShell.SendKeys "{ENTER}"
    Else
        WScript.Quit 1 ' Invalid file extension
    End If
Next








Set WshShell = CreateObject("WScript.Shell")
Set args = WScript.Arguments

For i = 0 To args.Count - 1
    WScript.Sleep 1000
    WshShell.SendKeys args(i)
    WScript.Sleep 1000
    WshShell.SendKeys "{ENTER}"
Next





var vbs = WDS.vars.get("vbsPath");
var file1 = WDS.vars.get("filepath1");
var file2 = WDS.vars.get("filepath2");

// Add quotes to file paths
var quotedFile1 = '"' + file1 + '"';
var quotedFile2 = '"' + file2 + '"';

// Build the command
var command = 'wscript "' + vbs + '" ' + quotedFile1 + ' ' + quotedFile2;
WDS.log.info("Executing: " + command);

// Execute
var proc = java.lang.Runtime.getRuntime().exec(command);
var exitCode = proc.waitFor();