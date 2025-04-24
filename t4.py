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