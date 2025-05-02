import org.openqa.selenium.*;
import org.openqa.selenium.support.ui.*;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;
import java.time.Duration;


public void selectDRValue(String label, String dateRange) {
    WebDriverWait wait = new WebDriverWait(driver, 10);
    
    // Step 1: Click the date range input to open the calendar
    WebElement dateInput = wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector(".datepicker-base-input input")));
    dateInput.click();

    // Step 2: Parse the date range
    String[] parts = dateRange.split(" to ");
    String start = parts[0].trim();
    String end = parts[1].trim();

    try {
        SimpleDateFormat sdf = new SimpleDateFormat("MM/dd/yyyy", Locale.ENGLISH);
        Date startDate = sdf.parse(start);
        Date endDate = sdf.parse(end);

        // Select start and end date one after another
        selectDateFromCalendar(startDate);
        selectDateFromCalendar(endDate);

    } catch (Exception e) {
        throw new RuntimeException("Failed to parse date range or select calendar dates: " + e.getMessage());
    }
}








private void selectDateFromCalendar(Date date) {
    WebDriverWait wait = new WebDriverWait(driver, 10);
    SimpleDateFormat monthFormat = new SimpleDateFormat("MMMM", Locale.ENGLISH);
    SimpleDateFormat yearFormat = new SimpleDateFormat("yyyy", Locale.ENGLISH);
    SimpleDateFormat dayFormat = new SimpleDateFormat("d", Locale.ENGLISH);

    String targetMonth = monthFormat.format(date);
    String targetYear = yearFormat.format(date);
    String targetDay = dayFormat.format(date);

    // Step 1: Loop until correct month and year are visible
    while (true) {
        WebElement monthYearLabel = wait.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".calendar-title-selector")));
        String visible = monthYearLabel.getText();  // e.g., "May 2025"

        if (visible.contains(targetMonth) && visible.contains(targetYear)) {
            break;
        }

        // Decide whether to go forward or backward
        int currentYear = Integer.parseInt(visible.replaceAll("[^0-9]", ""));
        int targetY = Integer.parseInt(targetYear);

        if (currentYear < targetY) {
            driver.findElement(By.cssSelector(".calendar-next-button")).click();
        } else {
            driver.findElement(By.cssSelector(".calendar-prev-button")).click();
        }
    }

    // Step 2: Click the correct day
    String dayXpath = "//td[normalize-space()='" + targetDay + "']";
    wait.until(ExpectedConditions.elementToBeClickable(By.xpath(dayXpath))).click();
}






