import subprocess

arg = int(input("Você deseja desligar ou abortar um desligamento?\n 1- Desligar \n 2- Abortar \n"))

if arg == 1:
    h = int(input("Quantas horas? "))
    m = (input("Quantos minutos? "))

    if m == '':
        s = h * 3600
    else:
        s = h * 3600 + int(m) * 60

    shutdown = f'shutdown /s /t {s}'

    subprocess.run(shutdown, shell=True)

else:
    abort = 'shutdown /a'
    subprocess.run(abort, shell=True)
