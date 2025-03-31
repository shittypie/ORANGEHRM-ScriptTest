from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class textfield:
    @staticmethod
    def clear_fields(driver, field_xpaths):
        """
        Checks if all specified fields have a red border (error validation).
        
        :param driver: Selenium WebDriver instance
        :param field_xpaths: List of XPaths for the input fields
        :return: True if all fields show an error, False otherwise
        
        usage:
        from selenium.webdriver.common.keys import Keys
        
        fields = [list of text]
        result = textfield.clear_fields(driver, fields) # or self.driver
        """
        
        for field_xpath in field_xpaths:
            field = driver.find_element(By.XPATH, field_xpath)
            field.send_keys(Keys.CONTROL + "a") 
            field.send_keys(Keys.DELETE)