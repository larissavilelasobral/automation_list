from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class WhatsBot:
    def __init__(self):
        self.mensagem = " botzao "
        self.grupos = ["Links", "Laiza (Sestra)"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        s = Service('./chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
        # self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        # <span dir="auto" title="Links"
        # <div tabindex="-1" class="p3_M1">
        # <span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element(By.XPATH, f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element(By.CLASS_NAME, "p3_M1")
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element(By.XPATH, "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = WhatsBot()
bot.EnviarMensagens()
