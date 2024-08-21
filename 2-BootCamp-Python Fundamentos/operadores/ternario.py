lockdown = False
grana = 30

status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuu'

print(f'Status é: {status}')