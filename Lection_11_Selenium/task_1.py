# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
sbis_site = 'https://sbis.ru/'
tensor_site = 'https://tensor.ru/about'

try:
    # Открытие сайта https://sbis.ru/
    driver.get(sbis_site)
    sleep(2)  # жду загрузку страницы

    # Переход в раздел Контакты
    contacts = driver.find_element(By.CSS_SELECTOR, "[href='/contacts']")
    contacts.click(), sleep(2)

    # Клик по баннеру Tensor
    tensor_banner = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    tensor_banner.click()

    # Переход во вкладку с сайтом https://tensor.ru/
    driver.switch_to.window(driver.window_handles[1]), sleep(2)

    # Проверка наличия блока новости "Сила в людях"
    text_news_block = 'Сила в людях'
    news_block = driver.find_element(By.XPATH, "//*[contains(@class, 'tensor_ru-Index__card-title')"
                                               "and contains(text(), 'Сила в людях')]")
    driver.execute_script("return arguments[0].scrollIntoView(true);", news_block)
    assert news_block.text == text_news_block, sleep(2)

    # Переход в "Подробнее" и проверка открытия сайта https://tensor.ru/about
    more = driver.find_element(By.XPATH, "//*[contains(@class, 'tensor_ru-link') and contains(@href, '/about')]")
    more.click(), sleep(2)
    assert driver.current_url == tensor_site

finally:
    driver.quit()
