from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

USER = "standard_user"
PASSWORD = "secret_sauce"

def main():
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    #option.add_argument("--headless")
    option.add_argument("--window-size=1920,1080")
    driver = Chrome(service=service, options=option)
    driver.get("https://www.saucedemo.com/")
    user_input = driver.find_element(By.ID, "user-name")
    user_input.send_keys(USER)
    pass_input = driver.find_element(By.ID, "password")
    pass_input.send_keys(PASSWORD)
    button = driver.find_element(By.ID, "login-button")
    button.click()
    time.sleep(5)

    # Se usa CSS_SELECTOR porque CLASS_NAME no permite múltiples clases (espacios)
    # Agregamos el punto (.) para que sea un selector de clase válido
    products = driver.find_elements(By.CSS_SELECTOR, ".inventory_item")
    product_data = []
    for product in products:
        try:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
           # print(f"Nombre: {name}, Precio: {price}")
            product_data.append([name, price])
        except Exception:
            # Si no encuentra el precio en algún elemento, saltamos al siguiente
            continue

    driver.quit()

    #cuadro con datos bonita
    import pandas as pd
    df = pd.DataFrame(product_data, columns=["Nombre", "Precio"])
    print(df)


if __name__ == "__main__":
    main()