@echo off
:: Ensure AutoHotkey is installed and the AHK script path is correct
"C:\Program Files\AutoHotkey\AutoHotkey.exe" "C:\Path\To\login_execute_save.ahk"
pause





; Launch SQLDbx
Run, C:\Path\To\SQLDbx.exe
WinWait, SQLDbx - Login
ControlSend, Edit1, 123456, SQLDbx - Login ; Username
ControlSend, Edit2, 27473839, SQLDbx - Login ; Password
ControlClick, Button1, SQLDbx - Login ; Click OK button
Sleep, 1000 ; Wait for login to complete

; Select DBMS Type from dropdown (ASQ)
ControlSend, ComboBox1, ASQ, SQLDbx - Main
ControlSend, Edit1, Absc123, SQLDbx - Main ; Server Name
ControlClick, Button1, SQLDbx - Main ; Click Connect button

; Wait for connection to complete
Sleep, 3000
; Send the SQL query to the query editor
ControlSend, Edit3, SELECT * FROM my_table;, SQLDbx - Main ; Your SQL query here
ControlClick, Button2, SQLDbx - Main ; Click Execute button

; Wait for query to finish executing
Sleep, 3000

; Save results to Excel (Ctrl+S, then save the file)
Send, ^s ; Ctrl+S to save
Sleep, 500
Send, C:\Path\To\Save\Results.xlsx ; Path to save the results
Send, {Enter} ; Confirm save location
Sleep, 500

; Close SQLDbx (optional)
Send, ^w ; Close window