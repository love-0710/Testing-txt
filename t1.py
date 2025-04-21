// Date and Time Published
var getDateTimePublished = WDS.browser.findElement(org.openqa.selenium.By.xpath("(//div[@class])"));
WDS.log.info("Date and Time Published - " + getDateTimePublished);
java.lang.Thread.sleep(2000);

var actualTime = getDateTimePublished.getText().trim();

if(actualTime != null && actualTime.length() > 0){

    var format1 = new java.text.SimpleDateFormat("MM/dd/yyyy hh:mm a");
    var format2 = new java.text.SimpleDateFormat("yyyy-MM-dd hh:mm:ss a");
    var format3 = new java.text.SimpleDateFormat("yyyy-MM-dd hh:mm a");

    var parsedActual = null;

    try {
        parsedActual = format1.parse(actualTime);
    } catch(e1) {
        try {
            parsedActual = format2.parse(actualTime);
        } catch(e2) {
            try {
                parsedActual = format3.parse(actualTime);
            } catch(e3) {
                parsedActual = null;
            }
        }
    }

    if (parsedActual != null) {
        var now = new Date();
        var diffMillis = Math.abs(now.getTime() - parsedActual.getTime());
        var diffMins = diffMillis / (1000 * 60);

        if (diffMins <= 3) {
            WDS.sampleResult.successful = true;
            WDS.sampleResult.responseMessage = "Results returned";
            WDS.log.info("Pass - Results returned :"+ actualTime);
        } else {
            WDS.sampleResult.successful = false;
            WDS.sampleResult.responseMessage = "Time difference too large";
            WDS.log.info("Fail - Time mismatch (difference > 3 min): " + actualTime);
        }
    } else {
        WDS.sampleResult.successful = false;
        WDS.sampleResult.responseMessage = "Unable to parse date-time";
        WDS.log.info("Fail - Invalid time format: " + actualTime);
    }

}else{
    WDS.sampleResult.successful = false;
    WDS.sampleResult.responseMessage = "There were no results returned";
    WDS.log.info("Fail - There were no results returned :"+actualTime);
}

java.lang.Thread.sleep(3000);