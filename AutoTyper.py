from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace this with your actual Firefox profile path
firefox_profile_path = r"C:\Users\YourUserPcUsername\AppData\Roaming\Mozilla\Firefox\Profiles\-------.default"

# Replace this with the URL of the typing lesson you want to complete (ONLY WORKS WITH PARAGRAPHS!!)
lesson = "https://www.typing.com/student/lesson/"

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument(f"-profile")
firefox_options.add_argument(firefox_profile_path)
driver = webdriver.Firefox(options=firefox_options)


driver.get(lesson)

try:
    typing_area = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "screenBasic-advanced"))
    )

    text_elements = typing_area.find_elements(By.CLASS_NAME, "screenBasic-word")
    text_to_type = ""
    for word_element in text_elements:
        letter_elements = word_element.find_elements(By.CLASS_NAME, "letter")
        for letter in letter_elements:
            text_to_type += letter.text

    # Clean up extra spaces and the prompt " ⇉  "
    text_to_type = text_to_type.replace('\xa0', ' ').strip()
    text_to_type = text_to_type.replace(' ⇉  ', '')

    print("The letters that the code found:", text_to_type)

    # Locate the input field
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))
    )

    for char in text_to_type:
        input_field.send_keys(char)
        time.sleep(0.1)  # Wait for 0.1 seconds after each character

except:
    print("Error!!! idk man your own now cuh")