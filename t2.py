public void clickOkIfVisible() {
    try {
        By okButtonLocator = By.xpath("//div[@class='fis-primary-block']//*[text()='Ok']");

        List<WebElement> okButtons = driver.findElements(okButtonLocator);

        if (!okButtons.isEmpty() && okButtons.get(0).isDisplayed()) {
            okButtons.get(0).click();
            System.out.println("✅ 'Ok' button clicked.");
        } else {
            System.out.println("ℹ️ 'Ok' button not visible. Skipping click.");
        }

    } catch (Exception e) {
        throw new RuntimeException("🚨 Error while checking/clicking 'Ok' button: " + e.getMessage(), e);
    }
}














public void handleMyRecentlyViewedDropdown() {
    try {
        // XPath for the dropdown "My Recently Viewed"
        By dropdownLocator = By.xpath("//div[@class='investran-ui-panel-commands-dropdown']//*[text()='My Recently Viewed']");

        // Check if the dropdown exists
        List<WebElement> dropdowns = driver.findElements(dropdownLocator);

        if (!dropdowns.isEmpty()) {
            System.out.println("🔽 'My Recently Viewed' dropdown found. Proceeding to click...");

            // Click the dropdown
            dropdowns.get(0).click();
            Thread.sleep(1000); // Optional wait for dropdown to expand

            // Click the "All" option
            WebElement allOption = driver.findElement(By.xpath("//span[@class='investran-ui-panel-command-title ng-binding' and text()='All']"));
            allOption.click();
            System.out.println("✅ Clicked on 'All' option.");

            // Wait and click the "Yes" button on confirmation dialog
            WebElement yesButton = driver.findElement(By.xpath("//div[@class='fis-primary-block']//button[@fis-unique-id='dialog button ok' and text()='Yes']"));
            yesButton.click();
            System.out.println("✅ Clicked 'Yes' button to confirm.");

        } else {
            System.out.println("⚠️ 'My Recently Viewed' dropdown not found. Skipping dropdown handling.");
        }

    } catch (Exception e) {
        throw new RuntimeException("🚨 Error handling 'My Recently Viewed' dropdown: " + e.getMessage(), e);
    }
}
















import org.openqa.selenium.By
import java.time.Duration
import org.openqa.selenium.support.ui.WebDriverWait
import org.openqa.selenium.support.ui.ExpectedConditions

// Your 14 values
def inputValues = [
    "value1", "value2", "value3", "value4", "value5",
    "value6", "value7", "value8", "value9", "value10",
    "value11", "value12", "value13", "value14"
]

// XPaths to verify after input (update with your actual XPaths)
def xpathsToCheck = [
    "//*[@id='elementOption1']",
    "//*[@id='elementOption2']",
    "//*[@id='elementOption3']",
    "//*[@id='elementOption4']"
]

// Switch to iframe
def iframe = WDS.browser.findElement(By.xpath("//iframe[contains(@class, 'viewer')]"))
WDS.browser.switchTo().frame(iframe)

def wait = new WebDriverWait(WDS.browser, Duration.ofSeconds(10))

// Loop through values
for (int i = 0; i < inputValues.size(); i++) {
    WDS.log.info("Iteration ${i + 1}: Processing value '${inputValues[i]}'")

    // Click to clear
    def field = WDS.browser.findElement(By.xpath("//*[@id='ReportViewerControl_ctl05_ctl100_Next_ctl100_ctl00']"))
    field.click()
    java.lang.Thread.sleep(2000)

    // Send value
    field.sendKeys(inputValues[i])
    java.lang.Thread.sleep(2000)

    // Check visibility of any one of the 4 elements
    def found = false
    for (xpath in xpathsToCheck) {
        try {
            wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath(xpath)))
            WDS.log.info("Element found for XPath: ${xpath}")
            found = true
            break
        } catch (Exception e) {
            // Do nothing; try next
        }
    }

    if (!found) {
        WDS.log.warn("No matching element found for value '${inputValues[i]}'")
    }

    java.lang.Thread.sleep(4000) // Wait before next iteration
}

// Optionally switch back to default
// WDS.browser.switchTo().defaultContent()






import java.nio.file.*
import java.io.*

def raw = prev.getResponseDataAsString()

if (!raw || !raw.contains("email_subjct")) {
    log.error("Response is empty or 'email_subjct' column not found.")
    return
}

def lines = raw.split('\n')

// Find column index
def headers = lines[0].split('\t')
def colIndex = headers.findIndexOf { it.trim().equalsIgnoreCase("email_subjct") }

if (colIndex == -1) {
    log.error("'email_subjct' column not found in headers.")
    return
}

// Write to CSV
def file = new File("email_subjects.csv")
def writer = new BufferedWriter(new FileWriter(file))
writer.write("email_subjct\n")

lines.drop(1).each { line ->
    def cols = line.split('\t')
    if (cols.size() > colIndex) {
        writer.write((cols[colIndex] ?: "") + "\n")
    }
}

writer.close()
log.info("Saved 'email_subjct' column to email_subjects.csv")