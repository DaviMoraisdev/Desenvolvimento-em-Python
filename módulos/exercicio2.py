"""
* Agendamento do Desligamento Pc 
-> Crie duas funções em python para agendar o desligamento do
computador em uma hora e meia 

"""
import os 

# * Desligar o computador 
# os.system("shutdown /s") # Desliga em 60s
# os.system("shutdown /s /t 0") # Desliga imediatamente 

# Cancelar o desligamento 
# os.system("shutdoen /a")

def turn_off_one_hour():
    os.system("shutdown /s /t 3600")

def turn_off_half_an_hour():
    os.system("shutdown /s /t 1800") 

def cancel_shutdown():
    os.system("shutdown /a")

# turn_off_one_hour()
# cancel_shutdown()
# turn_off_half_an_hour()
cancel_shutdown()