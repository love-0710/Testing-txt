#NoEnv
SendMode Input
SetWorkingDir %A_Desktop%
SetTitleMatchMode, 2

; Step 1: Open Paint and draw
Run, mspaint.exe
WinWaitActive, ahk_class MSPaintApp
Sleep, 1000
MouseMove, 300, 300
MouseDown("left")
MouseMove, 400, 300, 10
MouseMove, 400, 400, 10
MouseMove, 300, 400, 10
MouseMove, 300, 300, 10
MouseUp("left")
Sleep, 1000
Send, ^s
Sleep, 1000
Send, DemoDrawing.png{Enter}
Sleep, 1000
Send, !{F4} ; Close Paint

; Step 2: Open Notepad and write text
Run, notepad.exe
WinWaitActive, ahk_class Notepad
Sleep, 1000
Send, Hello, this is AutoHotkey demo script!
Sleep, 1000
Send, ^s
Sleep, 500
Send, DemoNote.txt{Enter}
Sleep, 1000
Send, !{F4}

; Step 3: Open Microsoft Teams (simulate if not installed)
Run, %ProgramFiles%\Microsoft\Teams\current\Teams.exe
Sleep, 5000
; If Teams is not installed, skip safely

; Step 4: Open a folder and create subfolder
Run, explorer.exe %A_Desktop%
WinWaitActive, ahk_class CabinetWClass
Sleep, 1000
Send, ^n
Sleep, 500
Send, Demo_Folder{Enter}
Sleep, 500
Send, {Enter} ; open the new folder
Sleep, 1000
Send, ^n ; new file inside folder
Sleep, 500
Send, demo.txt{Enter}









C:\Program Files\AutoHotkey\AutoHotkey.exe
