var getDateTimePublished = WDS.browser.findElement(org.openqa.selenium.By.xpath("(//div[@class])")).getText().trim();
WDS.log.info("Date and Time Published - " + getDateTimePublished);

if (getDateTimePublished != null && getDateTimePublished.length() > 0) {

    var format1 = new java.text.SimpleDateFormat("MM/dd/yyyy hh:mm a");
    var format2 = new java.text.SimpleDateFormat("yyyy-MM-dd hh:mm:ss a");
    var format3 = new java.text.SimpleDateFormat("yyyy-MM-dd hh:mm a");

    var parsedActual = null;

    try {
        parsedActual = format1.parse(getDateTimePublished);
    } catch(e1) {
        try {
            parsedActual = format2.parse(getDateTimePublished);
        } catch(e2) {
            try {
                parsedActual = format3.parse(getDateTimePublished);
            } catch(e3) {
                parsedActual = null;
            }
        }
    }

    if (parsedActual != null) {
        var now = new Date();
        var diffMillis = Math.abs(now.getTime() - parsedActual.getTime());

        // Convert diffMillis to hours, minutes, and seconds
        var diffSecs = Math.floor(diffMillis / 1000); // Total seconds
        var hours = Math.floor(diffSecs / 3600); // Extract hours
        var minutes = Math.floor((diffSecs % 3600) / 60); // Extract minutes
        var seconds = diffSecs % 60; // Extract seconds

        // Format the time difference as HH:mm:ss
        var formattedTimeDiff = String.format("%02d:%02d:%02d", hours, minutes, seconds);
        WDS.log.info("Time difference (formatted): " + formattedTimeDiff);

        // Check if the difference is within 3 minutes (180 seconds)
        if (diffMillis <= 3 * 60 * 1000) {
            WDS.sampleResult.successful = true;
            WDS.sampleResult.responseMessage = "Results returned";
            WDS.log.info("Pass - Results returned: " + getDateTimePublished);
        } else {
            WDS.sampleResult.successful = false;
            WDS.sampleResult.responseMessage = "Time difference too large";
            WDS.log.info("Fail - Time mismatch (difference > 3 min): " + getDateTimePublished);
        }
    } else {
        WDS.sampleResult.successful = false;
        WDS.sampleResult.responseMessage = "Unable to parse date-time";
        WDS.log.info("Fail - Invalid time format: " + getDateTimePublished);
    }

} else {
    WDS.sampleResult.successful = false;
    WDS.sampleResult.responseMessage = "There were no results returned";
    WDS.log.info("Fail - There were no results returned: " + getDateTimePublished);
}

java.lang.Thread.sleep(3000);