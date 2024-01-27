from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from telegram_send import send


# Функция для отправки уведомлений в Telegram
def send_telegram_notification(message):
    send(message, parse_mode='markdown')

# Функция для входа в WhatsApp Web и получения количества непрочитанных сообщений
def check_whatsapp_unread_messages():
    # Путь к драйверу Chrome, укажите свой путь
    chrome_driver_path = '/путь/к/драйверу/chromedriver'

    # Запуск драйвера Chrome
    service = Service(chrome_driver_path)
    service.start()
    options = Options()
    options.add_argument("--headless")  # Запуск в безголовом режиме (без отображения браузера)
    driver = webdriver.Chrome(service=service, options=options)

    # Открываем WhatsApp Web
    driver.get("https://web.whatsapp.com/")

    # Ждем, пока пользователь войдет в WhatsApp
    input("Пожалуйста, войдите в WhatsApp Web и нажмите Enter")

    # Получаем количество непрочитанных сообщений
    unread_count = len(driver.find_elements(By.XPATH, "//span[contains(@class, 'P6z4j')]"))

    # Закрываем браузер
    driver.quit()

    return unread_count

# Основная функция скрипта
def main():
    unread_messages = check_whatsapp_unread_messages()

    if unread_messages > 0:
        message = f"У вас {unread_messages} непрочитанных сообщений в WhatsApp."
        send_telegram_notification(message)
    else:
        print("Нет непрочитанных сообщений в WhatsApp.")

if __name__ == "__main__":
    main()
