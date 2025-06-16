Actions action = new Actions(driver);

// First click
action.click(objField).perform();
Log.info("Mouse clicked on the " + strName + " field");

// Wait for UI to render search box
waitForSeconds(3);

// Define search box XPath
String searchBoxXpath = "//div[@class='k-list-container k-popup k-group k-reset k-state-border']";

// Check if search box exists
List<WebElement> searchBoxElements = driver.findElements(By.xpath(searchBoxXpath));

if (searchBoxElements.isEmpty()) {
    Log.info("Search box not found after first click. Clicking again on " + strName + " field.");
    action.click(objField).perform();
    Log.info("Clicked again on " + strName + " field to trigger search box.");
} else {
    WebElement searchBox = searchBoxElements.get(0);
    if (searchBox.isDisplayed()) {
        Log.info("Search box appeared after first click. You can continue.");
    } else {
        Log.info("Search box found but not visible. Clicking again on " + strName + " field.");
        action.click(objField).perform();
        Log.info("Clicked again as search box was not visible.");
    }
}