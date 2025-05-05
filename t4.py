@echo off
C:
cd C:\Users\practice_project\jmeter\apache-jmeter-5.6.3\bin

set scriptNames=interactiveview script2 another_test final_script yet_another

for %%scriptName in (%scriptNames%) do (
    echo Running script: %%scriptName%%.jmx
    set timestamp=%date:~10,4%_%date:~4,2%_%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%
    set logFile=C:\Users\practice_project\JMeterMySS\JMeterLogs\%%scriptName%%_%timestamp%_Report.csv
    set reportFolder=C:\Users\practice_project\JMeterMySS\JMeterReports\%%scriptName%%_%timestamp%_Report

    jmeter -n -t "C:\Users\practice_project\JMeterMySS\JMeterScripts\%%scriptName%%.jmx" -l "%logFile%" -e -o "%reportFolder%"
    echo Report and log saved for %%scriptName%%.jmx
    echo.
)

echo All scripts have been executed.
pause
