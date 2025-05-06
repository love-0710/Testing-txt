public void selectDRValue(String label, String dateRange) {
    try {
        // Wait for the page to fully load
        new WebDriverWait(driver, Duration.ofSeconds(10)).until(webDriver ->
            Objects.equals(
                ((JavascriptExecutor) webDriver).executeScript("return document.readyState"),
                "complete"
            )
        );

        // Click the date range field using your XPath
        WebElement objField = driver.findElement(By.xpath("//*[@class='datepicker-base-input']"));
        comMethods.clickWebElement(objField, "Date Range Field", false);

    // Step 2: Split and parse date range
    String[] parts = dateRange.split(" - ");
    String start = parts[0].trim();
    String end = parts[1].trim();

    try {
        SimpleDateFormat sdf = new SimpleDateFormat("MM/dd/yyyy", Locale.ENGLISH);
        Date startDate = sdf.parse(start);
        Date endDate = sdf.parse(end);

        selectDateFromCalendar(startDate);
        selectDateFromCalendar(endDate);

    } catch (Exception e) {
        throw new RuntimeException("Failed to parse or select dates: " + e.getMessage(), e);
    }
}








private void selectDateFromCalendar(Date targetDate) {
    WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    SimpleDateFormat monthFormat = new SimpleDateFormat("MMMM", Locale.ENGLISH);
    SimpleDateFormat yearFormat = new SimpleDateFormat("yyyy", Locale.ENGLISH);
    SimpleDateFormat dayFormat = new SimpleDateFormat("d", Locale.ENGLISH);

    String targetMonth = monthFormat.format(targetDate);
    String targetYear = yearFormat.format(targetDate);
    String targetDay = dayFormat.format(targetDate);

    while (true) {
        String leftMonthYear = wait.until(ExpectedConditions.visibilityOfElementLocated(
            By.xpath("//*[@class='design2-customCalendar-range-left']//div[contains(@class,'design2-customCalendar-header')]"))).getText();
        String rightMonthYear = wait.until(ExpectedConditions.visibilityOfElementLocated(
            By.xpath("//*[@class='design2-customCalendar-range-right']//div[contains(@class,'design2-customCalendar-header')]"))).getText();

        if (leftMonthYear.contains(targetMonth) && leftMonthYear.contains(targetYear)) {
            clickDayFromPanel("left", targetDay);
            break;
        } else if (rightMonthYear.contains(targetMonth) && rightMonthYear.contains(targetYear)) {
            clickDayFromPanel("right", targetDay);
            break;
        } else {
            int targetY = Integer.parseInt(targetYear);
            int visibleY = extractYear(leftMonthYear);

            if (visibleY < targetY) {
                driver.findElement(By.xpath("//*[@class='design2-customCalendar-next-year-btn']")).click();
            } else if (visibleY > targetY) {
                driver.findElement(By.xpath("//*[@class='design2-customCalendar-prev-year-btn']")).click();
            } else {
                // Same year, use month buttons
                driver.findElement(By.xpath("//*[@class='design2-customCalendar-next-month-btn']")).click();
            }
        }
    }
}









private void clickDayFromPanel(String panel, String day) {
    WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(5));
    String panelXpath = panel.equals("left")
        ? "//*[@class='design2-customCalendar-range-part design2-customCalendar-range-left']"
        : "//*[@class='design2-customCalendar-range-part design2-customCalendar-range-right']";

    String dayXpath = panelXpath + "//td[normalize-space()='" + day + "']";
    WebElement dayEl = wait.until(ExpectedConditions.elementToBeClickable(By.xpath(dayXpath)));
    dayEl.click();
}








private int extractYear(String monthYearText) {
    String digits = monthYearText.replaceAll("[^0-9]", "");
    return Integer.parseInt(digits);
}







