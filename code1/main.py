# PA.click -> clicar com o mouse
# PA.write -> escrever um texto
# PA.press -> pressionar uma tecla do teclado
# PA.hotkey -> apertar um conjunto de teclas (Ctrl C, Ctrl V, Alt, Tab)

import pyautogui as PA
import time as t
import pandas as pd

PA.PAUSE = 0.8 # cada linha ele vai demorar esse tanto de tempo

# entrar no site
PA.press("win")
PA.write("edge")
PA.press("enter")
PA.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
PA.press("enter")

t.sleep(4)
PA.click(x=480, y=362) #PA.click(x=480, y=362, clicks=4, button='right')
# aqui ele vai levar o mouse ate o destino que voce quer

# fazer login
PA.write('teste@gmail.com')
PA.press("tab")
PA.write('teste234')
PA.press("enter")

t.sleep(3)

# colocar os dados
tabela = pd.read_csv('produtos.csv')

for linha in tabela.index:
    codigo = str(tabela.loc[linha, 'codigo'])
    PA.click(x=655, y=247)
    PA.write(codigo)
    PA.press('tab')
    PA.write(str(tabela.loc[linha, 'marca']))
    PA.press('tab')
    PA.write(str(tabela.loc[linha, 'tipo']))
    PA.press('tab')
    PA.write(str(tabela.loc[linha, 'categoria']))
    PA.press('tab')
    PA.write(str(tabela.loc[linha, 'preco_unitario']))
    PA.press('tab')
    PA.write(str(tabela.loc[linha, 'custo']))
    PA.press('tab')
   
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        PA.write(obs)
    PA.press('tab')
    PA.press('enter')
    PA.scroll(500000)