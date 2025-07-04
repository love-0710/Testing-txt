












try {
    comMethods.waitForSeconds(5);

    String strLocator = "//*[contains(@class, '-fund-diagram-cell') and @style='border-color: rgb(75, 205, 62); ']";
    List<WebElement> elements = driver.findElements(By.xpath(strLocator));

    boolean isAnyDisplayed = false;
    for (WebElement el : elements) {
        if (el.isDisplayed()) {
            isAnyDisplayed = true;
            break;
        }
    }

    if (isAnyDisplayed) {
        log.info("Green Border lines for the Legal Entities were displayed");
    } else {
        log.error("Green Border lines for the Legal Entities were not displayed");
        Assert.fail("Green Border lines for the Legal Entities were not displayed");
    }

} catch (Exception e) {
    throw new RuntimeException(e);
}

















private void clickDateInPanel(@NotNull WebElement panel, int day) {
    String xpath = ".//div[@class='design2-customCalendar-date']/span[text()='" + day + "']";
    List<WebElement> elements = panel.findElements(By.xpath(xpath));
    if (!elements.isEmpty()) {
        elements.get(0).click();
    } else {
        throw new NoSuchElementException("Date " + day + " not found in panel.");
    }
}


Public void selectDateFromCalendar(String dateStr) throws Exception {
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM/dd/yyyy");
    LocalDate targetDate = LocalDate.parse(dateStr, formatter);

    while (true) {
        // Fetch current panels
        WebElement leftPanel = driver.findElement(By.xpath("//*[@class='design2-customCalendar-range-part design2-customCalendar-range-left']"));
        WebElement rightPanel = driver.findElement(By.xpath("//*[@class='design2-customCalendar-range-part design2-customCalendar-range-right']"));

        String leftMonthYear = getMonthYearFromPanel(leftPanel);
        String rightMonthYear = getMonthYearFromPanel(rightPanel);

        // Correctly format the target month and year for comparison
        DateTimeFormatter monthYearFormatter = DateTimeFormatter.ofPattern("MMMM yyyy", Locale.ENGLISH);
        String targetMonthYear = targetDate.format(monthYearFormatter).toUpperCase(); // Ensure case-insensitive comparison

        String leftMonthYearUpper = leftMonthYear.toUpperCase();
        String rightMonthYearUpper = rightMonthYear.toUpperCase();

        // Check left panel
        if (leftMonthYearUpper.equals(targetMonthYear)) {
            clickDateInPanel(leftPanel, targetDate.getDayOfMonth());
            return;
        }

        // Check right panel
        if (rightMonthYearUpper.equals(targetMonthYear)) {
            clickDateInPanel(rightPanel, targetDate.getDayOfMonth());
            return;
        }

        // Navigate to correct month
        if (targetDate.isBefore(parseMonthYear(leftMonthYear))) {
            driver.findElement(By.xpath("//*[@class='design2-customCalendar-prev-month-btn']")).click(); // Go backward
        } else {
            driver.findElement(By.xpath("//*[@class='design2-customCalendar-next-month-btn']")).click(); // Go forward
        }

        Thread.sleep(300); // Optional short wait to allow calendar update
    }
}

















private LocalDate parseMonthYear(String rawText) {
    // Ensure space between month and year
    String fixedText = rawText.replaceAll("(?i)(January|February|March|April|May|June|July|August|September|October|November|December)(\\d{4})", "$1 $2");

    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MMMM yyyy", Locale.ENGLISH);
    try {
        return LocalDate.parse("01 " + fixedText, formatter);
    } catch (DateTimeParseException e) {
        System.err.println("Error parsing month and year: " + rawText);
        throw e; // Re-throw the exception for better error reporting
    }
}



Public void selectDateFromCalendar(String dateStr) throws Exception {
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM/dd/yyyy");
    LocalDate targetDate = LocalDate.parse(dateStr, formatter);

    while (true) {
        // Fetch current panels
        WebElement leftPanel = driver.findElement(By.xpath("//*[@class='design2-customCalendar-range-part design2-customCalendar-range-left']"));
        WebElement rightPanel = driver.findElement(By.xpath("//*[@class='design2-customCalendar-range-part design2-customCalendar-range-right']"));

        String leftMonthYear = getMonthYearFromPanel(leftPanel);
        String rightMonthYear = getMonthYearFromPanel(rightPanel);

        // Correctly format the target month and year for comparison
        DateTimeFormatter monthYearFormatter = DateTimeFormatter.ofPattern("MMMM yyyy", Locale.ENGLISH);
        String targetMonthYear = targetDate.format(monthYearFormatter).toUpperCase(); // Ensure case-insensitive comparison

        String leftMonthYearUpper = leftMonthYear.toUpperCase();
        String rightMonthYearUpper = rightMonthYear.toUpperCase();

        // Check left panel
        if (leftMonthYearUpper.equals(targetMonthYear)) {
            clickDateInPanel(leftPanel, targetDate.getDayOfMonth());
            return;
        }

        // Check right panel
        if (rightMonthYearUpper.equals(targetMonthYear)) {
            clickDateInPanel(rightPanel, targetDate.getDayOfMonth());
            return;
        }

        // Navigate to correct month
        // ... (rest of the navigation logic remains the same)
    }
}



private void clickDateInPanel(WebElement panel, int day) {
    String xpath = ".//div[@class='design2-customCalendar-date']/span[text()='" + day + "']";
    List<WebElement> elements = panel.findElements(By.xpath(xpath));
    if (!elements.isEmpty()) {
        elements.get(0).click();
    } else {
        throw new NoSuchElementException("Date " + day + " not found in panel.");
    }
}








































private LocalDate parseMonthYear(String rawText) {
    // Ensure space between month and year
    String fixedText = rawText.replaceAll("(?i)(January|February|March|April|May|June|July|August|September|October|November|December)(\\d{4})", "$1 $2");

    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MMMM yyyy", Locale.ENGLISH);
    try {
        return LocalDate.parse("01 " + fixedText, DateTimeFormatter.ofPattern("dd MMMM yyyy", Locale.ENGLISH));
    } catch (DateTimeParseException e) {
        System.err.println("Error parsing month and year: " + rawText);
        throw e; // Re-throw the exception for better error reporting
    }
}








String xpath = "(//div[@class='design2-customCalendar-body'])[1]//div[@class='design2-customCalendar-date']/span[text()='" + day + "']";





public void selectDRValue(String label, String startDate, String endDate) {
    try {
        System.out.println("Raw Date Range Input: [" + startDate + " to " + endDate + "]");

        // Step 1: Click the date picker field
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(15));
        WebElement dateInput = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[@class='datepicker-base-input']")));
        dateInput.click();
        System.out.println("The 'Date Range Field' has been clicked");

        // Step 2: Select Start Date
        selectDateFromCalendar(startDate);

        // Step 3: Select End Date
        selectDateFromCalendar(endDate);

    } catch (Exception e) {
        throw new RuntimeException("Failed to select date range: " + e.getMessage(), e);
    }
}





public void selectDateFromCalendar(String dateStr) throws Exception {
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM/dd/yyyy");
    LocalDate targetDate = LocalDate.parse(dateStr, formatter);

    while (true) {
        // Fetch current panels
        WebElement leftPanel = driver.findElement(By.xpath("//*[@class='design2-customCalendar-range-part design2-customCalendar-range-left']"));
        WebElement rightPanel = driver.findElement(By.xpath("//*[@class='design2-customCalendar-range-part design2-customCalendar-range-right']"));

        String leftMonthYear = getMonthYearFromPanel(leftPanel);
        String rightMonthYear = getMonthYearFromPanel(rightPanel);

        String targetMonthYear = targetDate.getMonth().name().substring(0, 1) + targetDate.getMonth().name().substring(1).toLowerCase() + " " + targetDate.getYear();

        // Check left panel
        if (leftMonthYear.equalsIgnoreCase(targetMonthYear)) {
            clickDateInPanel(leftPanel, targetDate.getDayOfMonth());
            return;
        }

        // Check right panel
        if (rightMonthYear.equalsIgnoreCase(targetMonthYear)) {
            clickDateInPanel(rightPanel, targetDate.getDayOfMonth());
            return;
        }

        // Navigate to correct month
        if (targetDate.isBefore(parseMonthYear(leftMonthYear))) {
            driver.findElement(By.xpath("//*[@class='design2-customCalendar-prev-month-btn']")).click(); // Go backward
        } else {
            driver.findElement(By.xpath("//*[@class='design2-customCalendar-next-month-btn']")).click(); // Go forward
        }

        Thread.sleep(300); // Optional short wait to allow calendar update
    }
}








private String getMonthYearFromPanel(WebElement panel) {
    String leftMonthYearXpath = "(//div[@class='design2-customCalendar-header'])[1]";  // Left panel
    String rightMonthYearXpath = "(//div[@class='design2-customCalendar-header'])[2]"; // Right panel

    try {
        // Try to find the month-year from both panels
        WebElement monthYearElement = panel.findElement(By.xpath(".//div[contains(@class,'design2-customCalendar-header')]"));
        return monthYearElement.getText().trim();
    } catch (NoSuchElementException e) {
        // If the specific panel is not found, throw exception
        throw new NoSuchElementException("Unable to extract month-year from panel.");
    }
}






private LocalDate parseMonthYear(String rawText) {
    // Ensure space between month and year
    String fixedText = rawText.replaceAll("(?i)(January|February|March|April|May|June|July|August|September|October|November|December)(\\d{4})", "$1 $2");

    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MMMM yyyy", Locale.ENGLISH);
    return LocalDate.parse("01 " + fixedText, DateTimeFormatter.ofPattern("dd MMMM yyyy", Locale.ENGLISH));
}



private void clickDateInPanel(WebElement panel, int day) {
    // Update XPath to click the correct date from the panel
    String xpath = "(//div[@class='design2-customCalendar-body'])[1]//div[@class='design2-customCalendar-date']/span[text()='" + day + "']";
    List<WebElement> elements = panel.findElements(By.xpath(xpath));
    if (!elements.isEmpty()) {
        elements.get(0).click();
    } else {
        throw new NoSuchElementException("Date " + day + " not found in panel.");
    }
}







































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