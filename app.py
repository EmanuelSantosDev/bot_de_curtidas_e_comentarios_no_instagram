import pyautogui
import pyperclip
import webbrowser
from time import sleep


# -31:20


# ================================================================================

# 1. Solicitar dados de login ao usuário

email = pyautogui.prompt(
    text='Digite seu e-mail:',
    title='Nome de Usuário',
)

senha = pyautogui.password(
    text='Digite sua senha:',
    title='Senha do Usuário',
    mask='*'
)

sleep(1)

# ================================================================================

# 1. Acessar o site do Instagram

webbrowser.open('https://www.instagram.com/')
sleep(5)

# ================================================================================

# 1. Se aparecer "Continuar como fulano de tal" clicar em "Trocar de conta"
try:
    coordenadas = pyautogui.locateCenterOnScreen(
        'img\\trocar_de_conta.png', confidence=0.7)
    pyautogui.moveTo(coordenadas[0], coordenadas[1], duration=1)
    pyautogui.click()
except pyautogui.ImageNotFoundException as erro:
    pass

# ================================================================================

# 1. Se o usuário estiver logado, "deslogar da conta"

try:
    coordenadas = pyautogui.locateCenterOnScreen(
        'img\\mudar.png', confidence=0.7)
    pyautogui.moveTo(coordenadas[0], coordenadas[1], duration=2)
    pyautogui.click()
    sleep(1)
    coordenadas = pyautogui.locateCenterOnScreen(
        'img\\entrar_em_conta_existente.png')
    pyautogui.moveTo(coordenadas[0], coordenadas[1], duration=2)
    pyautogui.click()
    sleep(2)
except pyautogui.ImageNotFoundException as erro:
    pass

# ================================================================================

# 1. Inserir usuário na tela de login

coordenadas = pyautogui.locateCenterOnScreen(
    'img\\nome_de_usuario.png', confidence=0.7)
pyautogui.moveTo(coordenadas[0], coordenadas[1], duration=1)
pyautogui.click()
pyautogui.typewrite(email, interval=0.1)
sleep(1)

# ================================================================================

# 1. Inserir a senha na tela de login

pyautogui.press('tab')
pyautogui.typewrite(senha, interval=0.1)
sleep(2)

# ================================================================================

# 1. Ocultar menu suspenso de autopreenchimento do aplicativo LastPass

pyautogui.move(-200, 0, duration=1)
pyautogui.click()
sleep(1)

# ================================================================================

# 1. Clicar em "Entrar"

coordenadas = pyautogui.locateCenterOnScreen('img\\entrar.png', confidence=0.7)
pyautogui.moveTo(coordenadas[0], coordenadas[1], duration=1)
pyautogui.click()
sleep(2)

# ================================================================================

# 1. Clicar em "Agora não" para não salvar informações de login

try:
    coordenadas = pyautogui.locateCenterOnScreen(
        'img\\agora_nao.png', confidence=0.7)
    pyautogui.moveTo(coordenadas[0], coordenadas[1], duration=1)
    pyautogui.click()
    sleep(1)
except:
    print('deu erro aqui no AGORA NÃO')

# ================================================================================

# 1. Clicar em "Agora não" para não ativar as notificações

# ================================================================================

# 1. Pesquisar o perfil alvo

coordenadas = pyautogui.locateCenterOnScreen(
    'img\\pesquisa.png', confidence=0.7)
pyautogui.moveTo(coordenadas[0], coordenadas[1], duration=1)
pyautogui.click()
sleep(1)

coordenadas = pyautogui.locateCenterOnScreen(
    'img\\campo_pesquisa.png', confidence=0.7)
pyautogui.moveTo(coordenadas[0], coordenadas[1], duration=0.5)
pyautogui.move(-50, 0, duration=0.5)
pyautogui.click()
sleep(1)

pyautogui.typewrite('nike', interval=0.1)
sleep(1)

# ================================================================================

# 1. Acessar o perfil alvo

coordenadas = pyautogui.locateCenterOnScreen('img\\nike.png', confidence=0.7)
pyautogui.moveTo(coordenadas[0], coordenadas[1], duration=1)
pyautogui.click()
sleep(1)

# ================================================================================

# 1. Acessar a postagem mais recente
# 1. Verificar se meu bot já curtiu ou não aquela postagem
# 1. Se já tiver curtido, não fazer nada e pausar o bot por 24 horas
# 1. Se não tiver curtido, curtir a postagem
# 1. Se não tiver curtido, comentar a postagem
# 1. Pausar o bot por 24 horas
# 1. Após 24 horas rodar tudo de novo
