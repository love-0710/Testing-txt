#NoEnv
SendMode Input
SetTitleMatchMode, 2
SetWorkingDir %A_ScriptDir%

logFile := "C:\SQLDbxLogs\log.txt"
screenshotDir := "C:\SQLDbxLogs\Screenshots"
FileCreateDir, %screenshotDir%

Log(msg) {
    FormatTime, time,, yyyy-MM-dd HH:mm:ss
    FileAppend, [%time%] %msg%`n, %logFile%
}

CaptureScreenshot(step) {
    FormatTime, ts,, yyyyMMdd_HHmmss
    file := screenshotDir . "\\step_" . step . "_" . ts . ".png"
    ; Save screen to clipboard
    Send, {PrintScreen}
    Sleep, 1000
    ; Save using MS Paint (built-in)
    Run, mspaint.exe
    WinWaitActive, ahk_exe mspaint.exe
    Send, ^v
    Sleep, 1000
    Send, ^s
    Sleep, 500
    Send, %file%
    Sleep, 500
    Send, {Enter}
    Sleep, 1000
    WinClose, ahk_exe mspaint.exe
    Sleep, 1000
}

Log("Launching SQLDbx")
Run, C:\Path\To\SQLDbx.exe  ; <-- Replace with actual SQLDbx path
WinWait, SQLDbx
CaptureScreenshot("01_SQLDbxOpened")

Log("Filling login fields")
ControlSend, ComboBox1, ASQ, SQLDbx
Sleep, 500

ControlClick, Button1, SQLDbx  ; Click server [...]
Sleep, 60000
ControlSend, Edit1, Absc123, SQLDbx

ControlSend, Edit2, 123456, SQLDbx
ControlSend, Edit3, 27473839, SQLDbx
CaptureScreenshot("02_FilledLogin")

ControlClick, Button4, SQLDbx ; Click OK
Sleep, 3000
CaptureScreenshot("03_AfterLogin")

WinWait, SQLDbx - Main
ControlClick, ComboBox2, SQLDbx
ControlSend, ComboBox2, web_enable, SQLDbx
CaptureScreenshot("04_SelectedWebEnable")

Log("Entering SQL query")
ControlSend, Edit1, SELECT * FROM your_table LIMIT 10;, SQLDbx
ControlClick, Button5, SQLDbx ; Execute button
Sleep, 5000
CaptureScreenshot("05_ExecutedQuery")

Log("Exporting result to CSV")
Send, ^s
Sleep, 1000
Send, C:\SQLDbxLogs\result.csv
Sleep, 500
Send, {Enter}
Sleep, 1000
CaptureScreenshot("06_SavedCSV")

Log("Automation completed successfully")
ExitApp