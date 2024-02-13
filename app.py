import pyautogui
import webbrowser
from time import sleep


def efetuar_logout():
    pyautogui.click(1218, 290, duration=1)
    sleep(1)
    pyautogui.click(74, 672, duration=1)
    sleep(1)
    pyautogui.click(111, 605, duration=1)
    sleep(7)
    pyautogui.hotkey('ctrl', 'w')


while True:
    # 01 - Navegar até o site https://www.instagram.com/
    webbrowser.open('https://www.instagram.com/')
    sleep(3)
    # 02 - Entrar com meu usuário
    pyautogui.click(864, 321, duration=1)
    sleep(1)
    pyautogui.typewrite('suelen.teste@yahoo.com', interval=0.1)
    sleep(1)
    # 03 - Entrar com a minha senha
    pyautogui.press('tab')
    sleep(1)
    pyautogui.typewrite('pythonista', interval=0.1)
    sleep(1)
    # 04 - Clicar em "Entrar"
    pyautogui.move(-150, 0, duration=1)
    pyautogui.click()
    pyautogui.click(864, 415, duration=1)
    sleep(10)
    # 05 - Clicar em "Agora não" para não salvar navegador
    pyautogui.click(790, 464, duration=1)
    sleep(4)
    # 06 - Clicar em "Agora não" para não ativar as notificações
    pyautogui.click(671, 566, duration=1)
    sleep(4)
    # 07 - Pesquisar pela página
    pyautogui.click(94, 296, duration=1)
    sleep(1)
    pyautogui.click(128, 227, duration=1)
    sleep(1)
    pyautogui.typewrite('nike')
    sleep(3)
    # 08 - Entrar na página
    pyautogui.click(174, 291, duration=1)
    sleep(6)
    # 09 - Clicar na postagem mais recente
    pyautogui.click(490, 684, duration=1)
    sleep(4)
    # 10 - Verificar se já curti ou não aquela postagem
    coracao = None
    try:
        coracao = pyautogui.locateCenterOnScreen('coracao.png')
        sleep(2)
    except:
        pass
    # 11 - Se já tiver curtido, fazer nada e pausar o bot por 24 horas
    if coracao is not None:
        efetuar_logout()  # efetuar logout e fechar aba do navegador
        sleep(86400)
    # 12 - Se não tiver curtido, curtir a foto
    elif coracao == None:
        pyautogui.click(605, 564, duration=1)
        sleep(1)
        # 13 - Se não tiver curtido, comentar na foto
        pyautogui.click(676, 666, duration=1)
        pyautogui.typewrite('Legal!!!', interval=0.1)
        sleep(1)
        pyautogui.click(1037, 671, duration=1)
        sleep(10)
        efetuar_logout()  # efetuar Logout e Fechar Aba do Navedador
        # 14 - Pausar por 24 horas
        sleep(86400)
# 15 - Após 24 horas, rodar tudo de novo (bloco while: True)
