import pyautogui # type: ignore
import subprocess
import time

#C:\Users\jefferson.cavalcante\AppData\Local\Microsoft\WindowsApps\python.exe extrairRelatorio.py

login = 'jcavalc'
senha = 'jcavalc2023'
email = 'jefferson.cavalcante@poly-vac.com.br'

#Abrindo o sistema
subprocess.Popen(r'C:\TERMINAL_SGPV\putty.exe -load SGPV')
time.sleep(1)

#Realizando autenticação no sistema
pyautogui.write(login)
time.sleep(1)
pyautogui.press('enter')
pyautogui.write(senha)
time.sleep(1)
pyautogui.press('enter')

#Acessando o menu do sistema responsavel por gerar e enviar o relatório por e-mail
time.sleep(2)
pyautogui.write('09')
time.sleep(2)
pyautogui.write('02')
time.sleep(2)
pyautogui.write('2')
time.sleep(1)
pyautogui.write('N')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.write(email)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
