System.out.println("Raw Date Range Input: [" + dateRange + "]");

// Normalize all spaces to regular space
dateRange = dateRange.replaceAll("\\u00A0", " ");  // Replace non-breaking space
dateRange = dateRange.replaceAll("\\s+", " ").trim();  // Normalize whitespace

String[] parts = dateRange.split("\\s*(?i)to\\s*");

if (parts.length != 2) {
    throw new RuntimeException("Failed to parse date range: Expected format 'MM/dd/yyyy to MM/dd/yyyy'. Got: " + dateRange);
}







public void selectDRValue(String label, String dateRange) {
    try {
        // Use the user-provided XPath to open the calendar
        new WebDriverWait(driver, Duration.ofSeconds(10)).until(
            webDriver -> Objects.equals(
                ((JavascriptExecutor) webDriver).executeScript("return document.readyState"), "complete"
            )
        );

        // Click the Date Range input field to open calendar
        WebElement dateInput = new WebDriverWait(driver, Duration.ofSeconds(10)).until(
            ExpectedConditions.elementToBeClickable(By.xpath("//*[@class='datepicker-base-input']"))
        );
        dateInput.click();
        System.out.println("The 'Date Range Field' has been clicked");

        // Split and parse the date range
        String[] parts = dateRange.split("\\s+to\\s+");
if (parts.length != 2) {
    throw new RuntimeException("Invalid date range format. Expected 'MM/dd/yyyy to MM/dd/yyyy' but got: " + dateRange);
}

String start = parts[0].trim();
String end = parts[1].trim();

        SimpleDateFormat sdf = new SimpleDateFormat("MM/dd/yyyy", Locale.ENGLISH);
        Date startDate = sdf.parse(start);
        Date endDate = sdf.parse(end);

        // Select both start and end dates
        selectDateFromCalendar(startDate);
        selectDateFromCalendar(endDate);

    } catch (Exception e) {
        throw new RuntimeException("Failed to select date range: " + e.getMessage());
    }
}







private void selectDateFromCalendar(Date date) {
    WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

    SimpleDateFormat monthFormat = new SimpleDateFormat("MMMM", Locale.ENGLISH);  // e.g., April
    SimpleDateFormat yearFormat = new SimpleDateFormat("yyyy", Locale.ENGLISH);   // e.g., 2025
    SimpleDateFormat dayFormat = new SimpleDateFormat("d", Locale.ENGLISH);       // e.g., 12

    String targetMonth = monthFormat.format(date);
    int targetYear = Integer.parseInt(yearFormat.format(date));
    String targetDay = dayFormat.format(date);

    // Loop to navigate calendar until date appears on either panel
    while (true) {
        // Get left panel month/year
        String leftHeader = wait.until(ExpectedConditions.visibilityOfElementLocated(
            By.xpath("//*[@class='design2-customCalendar-range-part design2-customCalendar-range-left']//div[contains(@class,'design2-customCalendar-header')]")
        )).getText().trim();

        // Get right panel month/year
        String rightHeader = wait.until(ExpectedConditions.visibilityOfElementLocated(
            By.xpath("//*[@class='design2-customCalendar-range-part design2-customCalendar-range-right']//div[contains(@class,'design2-customCalendar-header')]")
        )).getText().trim();

        // Parse month/year from headers
        String[] leftParts = leftHeader.split(" ");
        String[] rightParts = rightHeader.split(" ");
        String leftMonth = leftParts[0];
        int leftYear = Integer.parseInt(leftParts[1]);
        String rightMonth = rightParts[0];
        int rightYear = Integer.parseInt(rightParts[1]);

        // Click if match found in either panel
        if (leftMonth.equalsIgnoreCase(targetMonth) && leftYear == targetYear) {
            String xpathDay = "//*[@class='design2-customCalendar-range-part design2-customCalendar-range-left']//td[normalize-space()='" + targetDay + "']";
            wait.until(ExpectedConditions.elementToBeClickable(By.xpath(xpathDay))).click();
            return;
        } else if (rightMonth.equalsIgnoreCase(targetMonth) && rightYear == targetYear) {
            String xpathDay = "//*[@class='design2-customCalendar-range-part design2-customCalendar-range-right']//td[normalize-space()='" + targetDay + "']";
            wait.until(ExpectedConditions.elementToBeClickable(By.xpath(xpathDay))).click();
            return;
        }

        // Navigate based on target year/month
        if (leftYear > targetYear || (leftYear == targetYear && isTargetMonthBefore(leftMonth, targetMonth))) {
            driver.findElement(By.xpath("//*[@class='design2-customCalendar-prev-month-btn']")).click();
        } else {
            driver.findElement(By.xpath("//*[@class='design2-customCalendar-next-month-btn']")).click();
        }
    }
}

// Helper to compare month positions
private boolean isTargetMonthBefore(String currentMonth, String targetMonth) {
    List<String> months = Arrays.asList(
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    );
    return months.indexOf(targetMonth) < months.indexOf(currentMonth);
}