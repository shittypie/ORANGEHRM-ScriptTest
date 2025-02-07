import os

def take_screenshot(driver, folder_path = "screenshots", file_name="secret"):
    """
    Captures a screenshot of the current page.
    
    :param driver: The Selenium WebDriver instance.
    :param file_name: The file name (or path) to save the screenshot. Default is 'screenshot.png'.
    """
    driver.save_screenshot(file_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Create the full file path
    file_path = os.path.join(folder_path, file_name)
    
    # Save the screenshot
    driver.save_screenshot(file_path)

    return file_path  # Return the path to the saved screenshot