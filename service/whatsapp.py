from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class WhatsAppService:
    def __init__(self):
        # Setup Chrome options
        options = webdriver.ChromeOptions()
        options.add_argument("--user-data-dir=./chrome-data")  # Preserve login session

        # Launch WhatsApp Web
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get("https://web.whatsapp.com")

        # input("Scan the QR code and press Enter...")
        print("Logged in!")

        # Wait for WhatsApp Web to load
        time.sleep(5)  

        # Locate and click the channels tab
        channels_button = self.driver.find_element(By.XPATH, '//button[@aria-label="Channels"]')
        channels_button.click()
        time.sleep(3)  # Wait for the channels tab to load

        channel = self.driver.find_element(By.XPATH, "//div[@aria-label='Tech Unplugged Channel']")
        channel.click()

    def send_message(self, message):
        # Locate the message box
        message_box = self.driver.find_element(By.XPATH, "//footer//div[@contenteditable='true']")
        message_box.click()

        # Send a message
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        print("Message sent:", message)
        time.sleep(10)  # Wait for the message to send

    def close(self):
        self.driver.quit()

# Example usage:
# whatsapp_service = WhatsAppService()
# whatsapp_service.send_message("Hello from Python!")
# whatsapp_service.close()
