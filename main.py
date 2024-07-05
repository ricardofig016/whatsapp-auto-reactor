from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

group_name = input("Type the name of the chat: ")

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")


# Wait for the user to scan the QR code
print("Please scan the QR code to log in.")
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, "//canvas[@aria-label='Scan me!']"))
)
WebDriverWait(driver, 600).until(
    EC.presence_of_element_located(
        (By.XPATH, "//div[@aria-label='Search input textbox']")
    )
)

# Search for the group chat
search_box = driver.find_element(By.XPATH, "//div[@aria-label='Search input textbox']")
search_box.click()
search_box.send_keys(group_name)
search_box.send_keys(Keys.ENTER)

# Wait for the group chat to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//div[@class='x3psx0u xwib8y2 xkhd6sd xrmvbpv']")
    )
)


# Function to react to the latest message with the "🙏" emoji
def react_to_latest_message():
    try:
        # Find the latest message
        messages = driver.find_elements(
            By.XPATH, "//div[contains(@class, 'message-in')]"
        )
        latest_message = messages[-1]

        # Check if the message is already reacted
        try:
            latest_message.find_element(By.XPATH, ".//img[@alt='🙏']")

        except:
            # Click on the message to open the reaction menu
            action = webdriver.common.action_chains.ActionChains(driver)
            action.move_to_element(latest_message).perform()

            # Click the emoji reaction button
            reaction_button = latest_message.find_element(
                By.XPATH, ".//span[@class='x1odib58']"
            )
            reaction_button.click()
            print("The latest message has been reacted")

            time.sleep(0.5)

            # Select the "🙏" emoji from the reaction menu
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//img[@alt='🙏']"))
            )
            emoji_reaction = driver.find_element(By.XPATH, "//img[@alt='🙏']")
            emoji_reaction.click()

    except Exception as e:
        print(f"An error occurred: {e}")


# Monitor for new messages and react
try:
    while True:
        react_to_latest_message()
        time.sleep(0.5)  # Check for new messages every 0.5 seconds
except KeyboardInterrupt:
    print("Exiting...")
finally:
    driver.quit()
