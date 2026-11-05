

import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.hotkey("win","s")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=833, y=456)
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=1037, y=461)
pyautogui.write("beatriz@gmail.com")
pyautogui.press("tab")
pyautogui.write("megezone")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(4)


import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)

#index é o número da linha
#pra localizar um tabela usar o loc[]

for linha in tabela.index:
    pyautogui.click(x=1166, y=327)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    preco_unitario = (str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
     pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")   
    pyautogui.scroll(5000)   







