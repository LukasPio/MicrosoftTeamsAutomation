import pyautogui
import webbrowser
import time

# Substitua o link para a o da reunião que deseja entrar
meeting_link = "https://teams.microsoft.com/l/meetup-join/19%3ameeting_OGUxZDA2MzQtM2UxZi00ZjdkLTkyNzgtNGUyMWVjZWEyNDg0%40thread.v2/0?context=%7b%22Tid%22%3a%222882be50-2012-4d88-ac86-544124e120c8%22%2c%22Oid%22%3a%223bf9da2e-7415-4ac9-8ff4-aee1087fd560%22%7d"

# Substitua pelo tempo que falta para sua reunião começar (segundos), caso não saiba, acesse o calcularTempo.java
time.sleep(9940)

webbrowser.open(meeting_link)

time.sleep(10)

# Ativar o modo tela cheia do teams
pyautogui.click('telacheia.PNG')

time.sleep(10)

# Substituir pelas coordenadas do botão de mutar o microfone, depois que o teams estiver em tela cheia
x = 1116
y = 567

# Clicando no botão de mutar o microfone
pyautogui.click(x, y)

time.sleep(10)

# Substituir as coordenadas pelas do botão de mutar o microfone depois que o teams estiver em tela cheia
x = 1502
y = 856

# Clicando no botão de ingressar na reunião
pyautogui.click(x, y)

time.sleep(20)

# Clicando no chat para enviar uma mensagem
pyautogui.click('foto.PNG')

time.sleep(15)

pyautogui.press('backspace', presses=10)

time.sleep(1)

# Substitua essa mensgem pela que você deseja enviar
texto = 'Bom dia! boa reuniao para todos'

for char in texto:
    pyautogui.write(char)
    time.sleep(0.2)  

pyautogui.press('enter')

# Substitua pelo tempo de duração da sua reunião (considerando que ela só acabe nessa duração, caso contrário, retire 15 minutos para margem de erro)
# Caso não saiba a duração em segundos, acesse o arquivo calcularTempo.java para descobrir
time.sleep(2550)

# Saindo da reunião
pyautogui.click('sair.PNG')


