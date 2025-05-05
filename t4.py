@echo off
setlocal enabledelayedexpansion

:: Change directory to JMeter bin
cd /d "C:\Users\practice_project\jmeter\apache-jmeter-5.6.3\bin"

:: List of script names (without extension)
set scripts=interactiveview loginFlow paymentTest searchTest checkoutFlow

:: Loop through each script
for %%s in (%scripts%) do (
    call :runScript %%s
)

goto :eof

:runScript
setlocal
set "scriptName=%~1"

:: Generate timestamp
set "timestamp=%date:~10,4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%"
set "timestamp=%timestamp: =0%"

echo Running %scriptName% at %timestamp%

:: Run JMeter command
jmeter -n -t "C:\Users\practice_project\JMeterMySS\JMeterScripts\%scriptName%.jmx" ^
 -l "C:\Users\practice_project\JMeterMySS\JMeterLogs\%scriptName%_%timestamp%_Report.csv" ^
 -e -o "C:\Users\practice_project\JMeterMySS\JMeterReports\%scriptName%_%timestamp%_Report"

endlocal
exit /b