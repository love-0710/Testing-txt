Set WshShell = CreateObject("WScript.Shell")
WScript.Sleep 2000
WshShell.SendKeys "C:\path\to\your\file.txt"
WScript.Sleep 1000
WshShell.SendKeys "{ENTER}"



"wscript C:/path/to/fileUpload.vbs".execute().waitFor()