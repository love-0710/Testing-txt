
echo Current path: %cd%
echo Trying to run: src\test\resources\sendMail.vbs
pause



@echo off
cd /d "%~dp0"
cscript //nologo "src\test\resources\sendMail.vbs"




@echo off
setlocal

:: Set the full path to the VBScript file relative to the batch file
set "SCRIPT_PATH=%~dp0src\test\resources\sendMail.vbs"

:: Run the VBScript with cscript
cscript //nologo "%SCRIPT_PATH%"

endlocal








public void verifyErrorMessageFormat() {
    try {
        // XPath to locate element starting with "Error Messages (Showing:"
        String xpath = "//*[contains(@class, 'tableTitleBar')]//*[starts-with(text(),'Error Messages (Showing:')]";

        WebElement label = driver.findElement(By.xpath(xpath));
        String text = label.getText().trim();

        // Validate format using regex: "Error Messages (Showing: <num> of <num>)"
        if (text.matches("^Error Messages \\(Showing: \\d+ of \\d+\\)$")) {
            System.out.println("✅ Format is correct: " + text);
        } else {
            System.err.println("❌ Text found but format incorrect: " + text);
            Assert.fail("Text format does not match expected pattern.");
        }

    } catch (NoSuchElementException e) {
        System.err.println("❌ Error message label not found.");
        Assert.fail("Error Messages label not found.");
    }
}















public static void verifyRibbonBtn(String buttonName) {
    try {
        // Generalized XPath for ribbon buttons
        String ribbonBtnXpath = "//*[@class='btnLeft']//*[text()='" + buttonName + "']";
        WebElement ribbonBtn = driver.findElement(By.xpath(ribbonBtnXpath));

        if (ribbonBtn.isDisplayed()) {
            Log.info("✅ Ribbon button '" + buttonName + "' is visible on the page.");
        } else {
            Log.error("❌ Ribbon button '" + buttonName + "' is not visible on the page.");
            Assert.fail("Ribbon button '" + buttonName + "' is not visible.");
        }
    } catch (NoSuchElementException e) {
        Log.error("❌ Ribbon button '" + buttonName + "' not found in DOM. Exception: " + e.getMessage());
        Assert.fail("Ribbon button '" + buttonName + "' not found.");
    } catch (Exception e) {
        Log.error("❌ Unexpected error while verifying Ribbon button '" + buttonName + "': " + e.getMessage());
        throw new RuntimeException(e);
    }
}














// Proceed to verify based on the resolved options
    List<WebElement> menuItems = driver.findElements(By.cssSelector(".dropdownMenuListBox .MenuItem"));

    // Map text -> element
    Map<String, WebElement> menuMap = new HashMap<>();
    for (WebElement item : menuItems) {
        String text = item.getText().trim();
        menuMap.put(text, item);
    }

    // ✅ Validate enabled items
    for (String label : expectedEnabled) {
        WebElement el = menuMap.get(label);
        Assert.assertNotNull("Expected enabled item not found: " + label, el);
        boolean isDisabled = el.getAttribute("class").contains("disabledItem");
        Assert.assertFalse("Expected '" + label + "' to be enabled, but it is disabled", isDisabled);
    }

    // ✅ Validate disabled items
    for (String label : expectedDisabled) {
        WebElement el = menuMap.get(label);
        if (el == null) {
            System.out.println("Disabled item '" + label + "' not found in DOM. Treated as disabled.");
            continue;
        }
        boolean isDisabled = el.getAttribute("class").contains("disabledItem");
        Assert.assertTrue("Expected '" + label + "' to be disabled, but it is enabled", isDisabled);
    }












Then verify dropdown options based on first row document status

@Then("verify dropdown options based on first row document status")
public void verifyMenuForUndeleted() {
    dmsAttributesPage.verifyDropdownForUndeletedUsingFirstRowStatus();
}

public void verifyDropdownForUndeletedUsingFirstRowStatus() {
    // Step 1: Get the document status from the first row (2nd column of grid)
    WebElement statusElement = driver.findElement(By.xpath("(//div[@class='dataGridCustomcell gridAnchor'])[2]"));
    String docStatus = statusElement.getText().trim().toLowerCase(); // e.g. "upload", "duplicate", "deleted"
    System.out.println("Status from first row: " + docStatus);

    // Step 2: Define expected enabled and disabled items for each status
    List<String> expectedEnabled;
    List<String> expectedDisabled;

    switch (docStatus) {
        case "upload":
            expectedEnabled = Arrays.asList("Upload Document", "Attributes", "View Document", "Delete");
            expectedDisabled = Arrays.asList("Unpublish", "Duplicate");
            break;

        case "duplicate":
            expectedEnabled = Arrays.asList("Attributes", "View Document", "Delete", "Duplicate");
            expectedDisabled = Arrays.asList("Upload Document", "Unpublish");
            break;

        case "deleted":
            expectedEnabled = Arrays.asList("View Document", "UnDelete");
            expectedDisabled = Arrays.asList("Attributes", "Upload Document", "Duplicate", "Unpublish");
            break;

        default:
            throw new IllegalStateException("Unknown or unsupported status: " + docStatus);
    }

    // Step 3: Click on the Action button to show the dropdown menu
    WebElement actionButton = driver.findElement(By.xpath("//button[text()='Action']"));
    actionButton.click();

    // Step 4: Call the existing reusable menu verification method
    verifyDropdownMenuOptions(expectedEnabled, expectedDisabled);
}
















public void verifyDropdownMenuOptions(List<String> expectedEnabled, List<String> expectedDisabled) {
    List<WebElement> menuItems = driver.findElements(By.cssSelector(".dropdownMenuListBox .MenuItem"));

    // Map menu text -> WebElement
    Map<String, WebElement> menuMap = new HashMap<>();
    for (WebElement item : menuItems) {
        String text = item.getText().trim();
        menuMap.put(text, item);
    }

    // ✅ Check enabled options (must exist and must not be disabled)
    for (String label : expectedEnabled) {
        WebElement el = menuMap.get(label);
        Assert.assertNotNull("Expected enabled item not found: " + label, el);
        boolean isDisabled = el.getAttribute("class").contains("disabledItem");
        Assert.assertFalse("Expected '" + label + "' to be enabled, but it is disabled", isDisabled);
    }

    // ✅ Check disabled options (can be missing OR present with disabledItem class)
    for (String label : expectedDisabled) {
        WebElement el = menuMap.get(label);
        if (el == null) {
            System.out.println("Disabled item '" + label + "' is not in DOM. Treated as disabled.");
            continue; // Consider not shown == not clickable
        }
        boolean isDisabled = el.getAttribute("class").contains("disabledItem");
        Assert.assertTrue("Expected '" + label + "' to be disabled, but it is enabled", isDisabled);
    }
}















import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;

import org.junit.Assert; // Or use TestNG: import org.testng.Assert;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;





public void verifyDropdownMenuOptions(List<String> expectedEnabled, List<String> expectedDisabled) {
    List<WebElement> menuItems = driver.findElements(By.cssSelector(".dropdownMenuListBox .MenuItem"));

    // Create a map of menu text -> WebElement
    Map<String, WebElement> menuMap = new HashMap<>();
    for (WebElement item : menuItems) {
        String text = item.getText().trim();
        menuMap.put(text, item);
    }

    // Check enabled options
    for (String label : expectedEnabled) {
        WebElement el = menuMap.get(label);
        Assert.assertNotNull("Expected menu item not found: " + label, el);
        boolean isDisabled = el.getAttribute("class").contains("disabledItem");
        Assert.assertFalse("Expected '" + label + "' to be enabled, but it is disabled", isDisabled);
    }

    // Check disabled options
    for (String label : expectedDisabled) {
        WebElement el = menuMap.get(label);
        Assert.assertNotNull("Expected menu item not found: " + label, el);
        boolean isDisabled = el.getAttribute("class").contains("disabledItem");
        Assert.assertTrue("Expected '" + label + "' to be disabled, but it is enabled", isDisabled);
    }
}












@Then("for menu status, options {string} are enabled and {string} are disabled")
public void verifyMenuItemsStatus(String enabledList, String disabledList) {
    List<String> enabledOptions = Arrays.asList(enabledList.split(","));
    List<String> disabledOptions = Arrays.asList(disabledList.split(","));

    verifyDropdownMenuOptions(enabledOptions, disabledOptions);
}





Scenario: Verify dropdown menu items for 'Upload' status
  When the menu is opened
  Then for menu status, options "Upload Document,Attributes,View Document" are enabled and "Unpublish" are disabled



