private LocalDate parseMonthYear(String rawText) {
    System.out.println("Raw text received in parseMonthYear: [" + rawText + "]");
    // Ensure space between month and year
    String fixedText = rawText.replaceAll("(?i)(January|February|March|April|May|June|July|August|September|October|November|December)(\\d{4})", "$1 $2");
    System.out.println("Fixed text after replaceAll: [" + fixedText + "]");

    DateTimeFormatter monthYearFormatter = DateTimeFormatter.ofPattern("MMMM yyyy", Locale.ENGLISH); // Pattern to parse the fixedText
    LocalDate parsedDate = null;
    try {
        parsedDate = LocalDate.parse(fixedText, monthYearFormatter); // Parse fixedText directly
        System.out.println("Successfully parsed to LocalDate for comparison: " + parsedDate);
        return parsedDate;
    } catch (DateTimeParseException e) {
        System.err.println("Error parsing month and year: [" + rawText + "]");
        System.err.println("Attempted to parse: [" + fixedText + "] with pattern: [MMMM yyyy]");
        e.printStackTrace();
        throw e; // Re-throw the exception for better error reporting
    }
}






public void selectDateFromCalendar(String dateStr) throws Exception {
    DateTimeFormatter inputFormatter = DateTimeFormatter.ofPattern("MM/dd/yyyy");
    LocalDate targetDate = LocalDate.parse(dateStr, inputFormatter);
    System.out.println("Target date to select: " + targetDate.format(DateTimeFormatter.ISO_DATE));

    while (true) {
        // Fetch current panels
        WebElement leftPanel = driver.findElement(By.xpath("//*[@class='design2-customCalendar-range-part design2-customCalendar-range-left']"));
        WebElement rightPanel = driver.findElement(By.xpath("//*[@class='design2-customCalendar-range-part design2-customCalendar-range-right']"));

        String leftMonthYear = getMonthYearFromPanel(leftPanel);
        String rightMonthYear = getMonthYearFromPanel(rightPanel);
        System.out.println("Left Panel Month Year: [" + leftMonthYear + "]");
        System.out.println("Right Panel Month Year: [" + rightMonthYear + "]");

        // Correctly format the target month and year for comparison
        DateTimeFormatter monthYearFormatter = DateTimeFormatter.ofPattern("MMMM yyyy", Locale.ENGLISH);
        String targetMonthYear = targetDate.format(monthYearFormatter).toUpperCase();

        String leftMonthYearUpper = leftMonthYear.toUpperCase();
        String rightMonthYearUpper = rightMonthYear.toUpperCase();
        System.out.println("Target Month Year (Upper): [" + targetMonthYear + "]");
        System.out.println("Left Month Year (Upper): [" + leftMonthYearUpper + "]");
        System.out.println("Right Month Year (Upper): [" + rightMonthYearUpper + "]");

        // Check left panel
        if (leftMonthYearUpper.equals(targetMonthYear)) {
            System.out.println("Target month/year found in Left Panel. Clicking date: " + targetDate.getDayOfMonth());
            clickDateInPanel(leftPanel, targetDate.getDayOfMonth());
            return;
        }

        // Check right panel
        if (rightMonthYearUpper.equals(targetMonthYear)) {
            System.out.println("Target month/year found in Right Panel. Clicking date: " + targetDate.getDayOfMonth());
            clickDateInPanel(rightPanel, targetDate.getDayOfMonth());
            return;
        }

        // Navigate to correct month
        if (targetDate.isBefore(parseMonthYear(leftMonthYear))) {
            System.out.println("Target date is before the left panel. Clicking Previous Month.");
            driver.findElement(By.xpath("//*[@class='design2-customCalendar-prev-month-btn']")).click(); // Go backward
        } else {
            System.out.println("Target date is after the left panel. Clicking Next Month.");
            driver.findElement(By.xpath("//*[@class='design2-customCalendar-next-month-btn']")).click(); // Go forward
        }

        Thread.sleep(300); // Optional short wait to allow calendar update
    }
}

