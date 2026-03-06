from os import name
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


User = "standard_user"
Password = "secret_sauce"

def main():
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    #option.add_argument("--headless")
    option.add_argument("--window-size=1920,1080")
    driver = Chrome(service=service, options=option)
    driver.get("https://www.mercadolibre.com.mx/ofertas#nav-header")
    time.sleep(5) # Esperar a que carguen los productos

    # Se usa CSS_SELECTOR porque CLASS_NAME no permite múltiples clases (espacios)
    products = driver.find_elements(By.CSS_SELECTOR, ".andes-card.poly-card.poly-card--grid-card")
    product_data = []
    for product in products:
        try:
            name = product.find_element(By.CLASS_NAME, "poly-component__title-wrapper").text
            price = product.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text
           # print(f"Nombre: {name}, Precio: {price}")
            product_data.append([name, price])
        except Exception:
            # Si no encuentra el precio en algún elemento, saltamos al siguiente
            continue

    #cuadro con datos bonita
    import pandas as pd
    df = pd.DataFrame(product_data, columns=["Nombre", "Precio"])
    print(df)

    #guardar en excel
    df.to_excel("productos.xlsx", index=False)
    



if __name__ == '__main__':
    main()