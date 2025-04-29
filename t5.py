Set WshShell = CreateObject("WScript.Shell")

' Start by opening SQLDBX (adjust the path to your executable)
WshShell.Run "C:\path\to\sqldbx.exe"
WScript.Sleep 2000 ' Wait for the application to open

' Assuming focus is on the DBMS Type field
' Continuously send "S" until "Sybase ASE" is found in the dropdown
Dim foundMatch
foundMatch = False

Do While Not foundMatch
    ' Send the "S" key to scroll the dropdown
    WshShell.SendKeys "s"
    WScript.Sleep 500 ' Wait for dropdown to update

    ' Capture the dropdown area (using external tool like AutoHotKey or Snipping Tool)
    ' Assume the screenshot is saved as "dropdown.png"

    ' Run Tesseract OCR to read the text from the image
    WshShell.Run "C:\path\to\tesseract.exe C:\path\to\dropdown.png C:\path\to\output.txt"
    WScript.Sleep 3000 ' Wait for Tesseract to process the image (adjust time as needed)

    ' Read the OCR output from the text file
    Set objFSO = CreateObject("Scripting.FileSystemObject")
    Set objFile = objFSO.OpenTextFile("C:\path\to\output.txt", 1)

    ' Read the file contents
    strText = objFile.ReadAll
    objFile.Close

    ' Check if the OCR result contains "Sybase ASE"
    If InStr(strText, "Sybase ASE") > 0 Then
        ' If "Sybase ASE" is found in the OCR result, select it
        foundMatch = True
        WshShell.SendKeys "{ENTER}"
    End If

    ' Optional: Add a timeout or max iterations to avoid infinite loop
    If Timer > 60 Then ' 60 seconds timeout
        WshShell.SendKeys "{ESC}" ' If no match found in timeout, exit
        Exit Do
    End If
Loop

' End script
WScript.Quit