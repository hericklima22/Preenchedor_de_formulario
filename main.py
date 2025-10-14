from os.path import exists

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time
import os
import requests
import zipfile
import shutil
import random

def get_edge_version():
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge Dev\Application"
    versions = [d for d in os.listdir(edge_path) if os.path.isdir(os.path.join(edge_path, d))]
    return versions[0] if versions else None


# Função para baixar o EdgeDriver
def download_edgedriver(version):
    url = f"https://msedgedriver.microsoft.com/{version}/edgedriver_win64.zip"
    driver_zip_path = os.path.join(os.getcwd(), "edgedriver_win64.zip")

    print(os.path.join(os.getcwd(), "edgedriver_win64.zip"))

    print(f"Baixando EdgeDriver versão {version}...")

    os.makedirs(os.path.join(os.getcwd(), 'edge_driver'), exist_ok=True)

    # Baixa o arquivo ZIP do EdgeDriver
    response = requests.get(url)
    with open(driver_zip_path, "wb") as file:
        file.write(response.content)

    # Descompacta o arquivo ZIP
    with zipfile.ZipFile(driver_zip_path, 'r') as zip_ref:
        zip_ref.extractall(os.getcwd())

    # Remove o arquivo ZIP após a extração
    os.remove(driver_zip_path)

    print("EdgeDriver baixado e descompactado com sucesso.")


# Função principal
def update_edgedriver():
    # Obtém a versão do Edge Dev
    edge_version = get_edge_version()
    if not edge_version:
        print("Não foi possível encontrar a versão do Microsoft Edge Dev.")
        return

    # Baixa e atualiza o EdgeDriver
    download_edgedriver(edge_version)

    # Copia o EdgeDriver para o local apropriado (por exemplo, onde o Selenium espera)
    driver_src = os.path.join(os.getcwd(), "msedgedriver.exe")
    driver_dst = os.path.join(os.getcwd(), "edge_driver")

    if os.path.exists(driver_src):
        if 'msedgedriver.exe' in os.listdir(driver_dst):
            os.remove(os.path.join(driver_dst, 'msedgedriver.exe'))
            os.rmdir(os.path.join(driver_dst, 'Driver_Notes'))
        shutil.move(driver_src, driver_dst)
        print(f"EdgeDriver movido para {driver_dst}.")


def fill_form_1(driver: webdriver.Edge):
    link_1 = 'https://www.selenium.dev/selenium/web/web-form.html'

    driver.get(link_1)

    time.sleep(1)

    text_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'my-text-id')))

    if text_input:
        text_input = driver.find_element(By.ID, 'my-text-id')

        text_input.send_keys('user')

    time.sleep(1)

    password_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/main/div/form/div/div[1]/label[2]/input')))

    if password_input:
        password_input = driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[1]/label[2]/input')

        password_input.send_keys('password01')

    time.sleep(1)

    text_area = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/main/div/form/div/div[1]/label[3]/textarea')))

    if text_area:
        text_area = driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[1]/label[3]/textarea')

        text_area.send_keys('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sagittis.')

    time.sleep(1)

    disabled_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/main/div/form/div/div[1]/label[4]/input')))

    if disabled_input:
        disabled_input = driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[1]/label[4]/input')

        # time.sleep(2)
        driver.execute_script("arguments[0].removeAttribute('disabled')", disabled_input)

        disabled_input.send_keys('não está mais desabilitado')

        driver.execute_script("arguments[0].setAttribute('disabled', true)", disabled_input)
    time.sleep(1)
    readonly_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/main/div/form/div/div[1]/label[5]/input')))

    if readonly_input:
        readonly_input = driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[1]/label[5]/input')

        # time.sleep(2)
        driver.execute_script("arguments[0].removeAttribute('readonly')", readonly_input)

        readonly_input.send_keys('não está mais em readonly')

        driver.execute_script("arguments[0].setAttribute('readonly', true)", readonly_input)
    time.sleep(1)
    select_box = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/main/div/form/div/div[2]/label[1]/select')))

    if select_box:

        select_box = driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[2]/label[1]/select')

        select = Select(select_box)

        select.select_by_index(random.randint(1, 3))
    time.sleep(1)
    file_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.NAME, 'my-file')))

    if file_input:
        file_input = driver.find_element(By.NAME, 'my-file')

        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'dog.jpeg'))

        file_input.send_keys(file_path)
    time.sleep(1)
    check1 = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, 'my-check-1')))

    if check1:
        check1 = driver.find_element(By.ID, 'my-check-1')

        check1.click()
    time.sleep(1)
    check2 = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, 'my-check-2')))

    if check2:
        check2 = driver.find_element(By.ID, 'my-check-2')

        check2.click()
    time.sleep(1)
    radio = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, 'my-radio-2')))

    if radio:
        radio = driver.find_element(By.ID, 'my-radio-2')

        radio.click()
    time.sleep(1)
    color = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.NAME, 'my-colors')))

    if color:
        color = driver.find_element(By.NAME, 'my-colors')
        r, g, b = str(hex(random.randint(0, 255))).replace('0x', '').zfill(2), str(hex(random.randint(0, 255))).replace('0x', '').zfill(2), str(hex(random.randint(0, 255))).replace('0x', '').zfill(2)

        c = '#' + r + g + b

        driver.execute_script(f"arguments[0].value = '{c}';", color)
    time.sleep(1)
    date_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.NAME, 'my-date')))

    if date_input:
        date_input = driver.find_element(By.NAME, 'my-date')

        from datetime import datetime

        date = datetime.today().strftime('mm/dd/yyyy')

        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)
        date_input.send_keys(Keys.ESCAPE)
    time.sleep(1)
    range_field = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.NAME, 'my-range')))

    if range_field:
        range_field = driver.find_element(By.NAME, 'my-range')

        min_range = range_field.get_attribute('min')
        max_range = range_field.get_attribute('max')
        step = range_field.get_attribute('step')

        actions = ActionChains(driver)
        actions.click_and_hold(range_field).move_by_offset(-100, 100).release().perform()

    time.sleep(5)

    form = driver.find_element(By.TAG_NAME, "form")

    form.submit()

    # driver.quit()

def verificar_driver(loc):
    # update_edgedriver()

    if not os.path.isfile(loc):
        print('Não foi possível baixar o driver :(')
        return False

    return True

def main():
    driver_loc = 'edge_driver/msedgedriver.exe'

    if not verificar_driver(driver_loc):
        return

    service = Service(executable_path=driver_loc)
    options = Options()
    options.binary_location = 'C:/Program Files (x86)/Microsoft/Edge Dev/Application/msedge.exe'

    driver = webdriver.Edge()

    fill_form_1(driver)



if __name__ == '__main__':
    main()