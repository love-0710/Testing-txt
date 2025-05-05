@echo off
setlocal enabledelayedexpansion

:: Change directory to JMeter bin
cd "C:\Users\practice_project\jmeter\apache-jmeter-5.6.3\bin"

:: List of script names (without extension)
set scripts=interactiveview loginFlow paymentTest searchTest checkoutFlow

:: Loop through each script
for %%s in (%scripts%) do (
    set scriptName=%%s
    set timestamp=%date:~10,4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%
    set timestamp=!timestamp: =0!

    jmeter -n -t "C:\Users\practice_project\JMeterMySS\JMeterScripts\!scriptName!.jmx" ^
    -l "C:\Users\practice_project\JMeterMySS\JMeterLogs\!scriptName!_!timestamp!_Report.csv" ^
    -e -o "C:\Users\practice_project\JMeterMySS\JMeterReports\!scriptName!_!timestamp!_Report"
)

endlocal
pause















@echo off
setlocal enabledelayedexpansion

:: Change to JMeter bin directory
cd "C:\Users\practice_project\jmeter\apache-jmeter-5.6.3\bin"

:: List your test scripts
set scripts=interactiveview loginFlow paymentTest searchTest checkoutFlow

:: Loop through all script names
for %%s in (%scripts%) do (
    set scriptName=%%s
    set attempts=1

    :retry
    set timestamp=%date:~10,4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%
    set timestamp=!timestamp: =0!
    set logFile="C:\Users\practice_project\JMeterMySS\JMeterLogs\!scriptName!_!timestamp!_Report.csv"
    set reportDir="C:\Users\practice_project\JMeterMySS\JMeterReports\!scriptName!_!timestamp!_Report"

    echo Running script !scriptName! (Attempt !attempts!)...

    jmeter -n -t "C:\Users\practice_project\JMeterMySS\JMeterScripts\!scriptName!.jmx" ^
        -l !logFile! -e -o !reportDir!

    :: Count total and failed samples
    set total=0
    set failed=0
    for /f "tokens=1,3 delims=," %%a in ('findstr /r /c:"^[0-9]" !logFile!') do (
        set /a total+=1
        if "%%b" NEQ "true" set /a failed+=1
    )

    if !failed! GTR 0 (
        echo Failed Samples: !failed! of !total!
        if !attempts! LSS 3 (
            set /a attempts+=1
            echo Retrying script !scriptName!... (Attempt !attempts!)
            goto retry
        ) else (
            echo Script !scriptName! failed after 3 attempts.
        )
    ) else (
        echo Script !scriptName! passed successfully with 100%% success.
    )
)

endlocal
pause