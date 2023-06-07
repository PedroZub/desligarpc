import subprocess

arg = int(input("Você deseja desligar ou abortar um desligamento?\n 1- Desligar \n 2- Abortar \n"))

if arg == 1:
    h = int(input("Quantas horas? "))
    m = int(input("Quantos minutos? "))

    s= (h * 3600) + (m * 60) 

    shutdown = f'shutdown /s /t {s}'

    subprocess.run(shutdown, shell=True)
else:
     abort = f'shutdown /a'

     subprocess.run(abort, shell=True)





          



