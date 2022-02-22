import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
PROMISED_UP = 30
PROMISED_DOWN = 15
chrome_driver_path = "C:\Coding\chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()
        time.sleep(30)
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                     '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        time.sleep(30)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                       '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div['
                                                       '2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(2)
        sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                            '1]/div[1]/div/div[3]/div[5]/a')
        sign_in_button.click()
        time.sleep(2)
        email_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                         '2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div['
                                                         '2]/div/input')
        email_input.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                         '2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div')
        next_button.click()
        time.sleep(2)
        password_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                            '2]/div/div/div[2]/div[2]/div[1]/div/div['
                                                            '3]/div/label/div/div[2]/div[1]/input')
        password_input.send_keys(TWITTER_PASSWORD)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                          '2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div')
        login_button.click()
        time.sleep(5)
        tweet_field = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                                         '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                         '1]/div/div/div/div[2]/div['
                                                         '1]/div/div/div/div/div/div/div/div/div/label/div['
                                                         '1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_field.send_keys(f"{self.up}, {self.down}")
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                          '1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                          '3]/div/div/div[2]/div[3]/div')
        tweet_button.click()


bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweet_at_provider()
