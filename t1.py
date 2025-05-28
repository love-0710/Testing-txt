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



