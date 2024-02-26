#entrando
# Lno site
import pyautogui
from time import sleep
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
sleep(2)
#automatizando o login
pyautogui.click(x=450, y=349)
pyautogui.press("tab")
pyautogui.write('borzistephany18@outlook.com')
pyautogui.press("tab")
pyautogui.write('123')
pyautogui.press("tab")
pyautogui.press("enter")
sleep(3)

import pandas as pd

tabela = pd.read_csv("produtos.csv")
for linha in tabela.index:
    #codigo

    pyautogui.click(x=714, y=267)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    #preço
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha,"obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    #enviar produto
    pyautogui.press("tab")
    pyautogui.press("enter")  # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)