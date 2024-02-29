# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()
fix_sbis = 'https://fix-online.sbis.ru/'

try:
    # Авторизация
    driver.get(fix_sbis), sleep(2)
    login, password = '1ctest', 'Fix5051'
    field_login = driver.find_element(By.CSS_SELECTOR, '.controls-InputBase__nativeField_caretFilled_theme_default')
    field_login.send_keys(login, Keys.ENTER)
    field_password = driver.find_element(By.CSS_SELECTOR, '[type=password]')
    field_password.send_keys(password, Keys.ENTER)
    sleep(5)  # жду загрузку страницы

    # Переход в меню Контакты
    menu_contacts = driver.find_element(By.CSS_SELECTOR, "[data-qa='Контакты']")
    menu_contacts.click(), sleep(3)
    sub_menu_contacts = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    sub_menu_contacts.click(), sleep(5)

    # Отправка сообщения
    new_massage = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    new_massage.click(), sleep(3)
    find = driver.find_element(By.CSS_SELECTOR, '.controls-InputBase__nativeField')
    contact = 'Наливайко Руслан'
    find.send_keys(contact, Keys.ENTER), sleep(2)
    person_contact = driver.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__secondLine"]')
    person_contact.click(), sleep(3)
    massage = 'Hello World!'
    entry_field = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    entry_field.send_keys(massage, Keys.ENTER)
    send_button = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    send_button.click(), sleep(5)

    # Проверка сообщения в реестре
    display_message = driver.find_element(By.CSS_SELECTOR, '.msg-entity-text')
    assert display_message.is_displayed()

    # Удаление сообщения
    ActionChains(driver).move_to_element(display_message).pause(3).perform()
    delete = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    ActionChains(driver).click(delete).pause(3).perform()

    # Проверка отсутствия сообщения в реестре
    try:
        display_message.is_displayed()
    except:
        print('Сообщение удалено')

finally:
    driver.quit()
