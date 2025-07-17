from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

isOpen = False

def iniciar_driver_e_logar():

    USUARIO = "toteminternacao"
    SENHA = "tasy@2025" 
    
    options = webdriver.ChromeOptions()
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    options.add_argument(r"--user-data-dir=C:\selenium\ChromeProfile")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--incognito")
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    actions = ActionChains(driver)


    driver.get("https://tasyhomol.unimedpc.coop.br/#/")
    driver.maximize_window()
    driver.fullscreen_window()
    time.sleep(8)  

    driver.find_element(By.ID, "loginUsername").send_keys(USUARIO + Keys.TAB)
    time.sleep(2)
    actions.send_keys(SENHA + Keys.TAB)
    actions.send_keys(Keys.ENTER).perform()

    time.sleep(15)
    try:
        btn = driver.find_element(By.XPATH, "//button[normalize-space()='Cancelar']")
        print("ENCONTROU")
        btn.click()
        time.sleep(2)
        actions.send_keys(Keys.ENTER).perform()
    except NoSuchElementException:
        print("NAO ENCONTROU")

    # tenta fechar pop-up “Cancelar”
    try:
        btn = driver.find_element(By.XPATH, "//button[normalize-space()='Cancelar']")
        btn.click()
        time.sleep(2)
        actions.send_keys(Keys.ENTER).perform()
    except NoSuchElementException:
        pass  # se não existir esse botão, prossegue normalmente
        main = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "wgrid-include-container"))
        )
        main = driver.find_element(By.CLASS_NAME, "wgrid-include-container")
        actions.context_click(main).perform()
        time.sleep(2)
        actions.send_keys(Keys.ENTER).perform()

        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Monitor')]"))
        )
        dropdown.click()
        time.sleep(1)

        auto_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='Autoatendimento']"))
        )
        auto_option.click()
        time.sleep(1)

        container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "m-container-autoatendimento"))
        )
        actions.context_click(container).perform()
        time.sleep(1)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(10)

    return driver, actions

options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
options.add_argument(r"--user-data-dir=C:\selenium\ChromeProfile")
options.add_argument(r"--remote-debugging-port=9222")
options.debugger_address = "127.0.0.1:9222"

driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)

driver = webdriver.Chrome(options=options)
time.sleep(2)  # caso a aba ainda esteja carregando

try:
    driver.find_element(By.CLASS_NAME, "m-container-autoatendimento")
    try:
        # Segunda verificação: se também existe o elemento com classe w-header
        driver.find_element(By.CSS_SELECTOR, "w-footer.philips-footer")
        print("TELA DESBLOQUEADA. BLOQUEANDO")
    except NoSuchElementException:
        container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "m-container-autoatendimento"))
        )
        actions.context_click(container).perform()
        time.sleep(1)
        actions.send_keys(Keys.ENTER).perform()
    print("✅ Elemento encontrado. Nada a fazer.")
except NoSuchElementException:
    print("❌ Elemento não encontrado. Carregando a URL base...")
    driver.close()     # fecha a aba atual
    driver.quit()      # encerra a sessão WebDriver
    driver, actions = iniciar_driver_e_logar()
