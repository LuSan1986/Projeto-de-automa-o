# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

    #Resolover o problema "Reactivating terminals...Source: Python". Precionar a tecla ctrl+shift+p, digitar Python: Select Interpreter. selecionar o recomendado. 

import pyautogui
import time



# abrir o navelucianosantana48@gmail.comgador (chrome)
time.sleep(5)
pyautogui.press("win")
pyautogui.write("google chrome")
time.sleep(5)   
pyautogui.press("enter")

time.sleep(3)
pyautogui.click(x=258, y=63)


# entrar no link 
time.sleep(5)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write (link)
pyautogui.press("enter")

# Passo 2: Fazer login
# selecionar o campo de email

# escrever o seu email
time.sleep(5)
pyautogui.click(x=464, y=317)
pyautogui.write("lucianosantana48@gmail.com")
pyautogui.click(x=468, y=393)
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")

    
# Passo 3: Importar a base de produtos pra cadastrar
import pandas

tabela = pandas.read_csv("produtos.csv")

print (tabela)

time.sleep(4)

# Passo 4. Cadastrar 1 produto



for linha in tabela.index: # Para cada linha da minha tabela.
    pyautogui.click(x=461, y=227)

    #codigo
    time.sleep(1)
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo)) # o str - (String) é para transformar o numero em texto.
    pyautogui.press("tab")

    #marca
    time.sleep(1)
    marca = tabela.loc[linha,"marca"]
    pyautogui.write (str(marca))
    pyautogui.press("tab")

    #tipo
    time.sleep(1)
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write (str(tipo))
    pyautogui.press("tab")

    #Categoria
    time.sleep(1)
    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write (str(categoria)) # Nesse caso o str transforma o 1 em texto
    pyautogui.press("tab")

    #Preço
    time.sleep(1)
    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #Custo
    time.sleep(1)
    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #Obs
    time.sleep(1)
    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan": # != diferente de nan (Nan é vazio)
        pyautogui.write(str(obs))
        
    pyautogui.press("tab")


    # Apertar o botão de enviar.
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.scroll(1000)
    time.sleep(3)


 # Automação.
