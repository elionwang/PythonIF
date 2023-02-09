import time
import random

matches = int(input('Hoeveel potjes wil je spelen? '))

i = 1

spelerScore = 0
computerScore = 0

while i <= matches:

  computerActie = random.randint(0, 2)

  if computerActie == 0:
    computerActieNaam = 'steen'
  elif computerActie == 1:
    computerActieNaam = 'papier'
  elif computerActie == 2:
    computerActieNaam = 'schaar'

  print('-------------------------------------')
  spelerInput = int(input('Kies steen[0], papier[1] of schaar[2]: '))

  if spelerInput < 0 or spelerInput > 2:
    i -= 1
    print(f'\x1b[4;30;41m{spelerInput} is geen geldige input idioot. Kies steen[0], papier[1] of schaar[2].',"\033[0m")

  time.sleep(3)

  spelerActie = int(spelerInput)

  if spelerActie == 0:
    spelerActieNaam = 'steen'
  elif spelerActie == 1:
    spelerActieNaam = 'papier'
  elif spelerActie == 2:
    spelerActieNaam = 'schaar'

  if spelerActie == computerActie:
    spelerScore += 1
    computerScore += 1
    print('Jij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;40m",'Het is gelijkspel!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}' "\033[0m",'|', "\x1b[1;30;41m",f'Computer score: {computerScore}',"\033[0m")
  elif spelerActie == 0:
    if computerActie == 1:
      computerScore += 1
      print('Jij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;41m",'Computer wint!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}' "\033[0m",'|', "\x1b[1;30;41m",f'Computer score: {computerScore}',"\033[0m")
    elif computerActie == 2:
      spelerScore += 1
      print('Jij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;42m",'Jij wint!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}' "\033[0m",'|', "\x1b[1;30;41m",f'Computer score: {computerScore}',"\033[0m")
  elif spelerActie == 1:
    if computerActie == 0:
      spelerScore += 1
      print('Jij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;42m",'Jij wint!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}' "\033[0m",'|', "\x1b[1;30;41m",f'Computer score: {computerScore}',"\033[0m")
    elif computerActie == 2:
      computerScore += 1
      print('Jij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;41m",'Computer wint!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}' "\033[0m",'|', "\x1b[1;30;41m",f'Computer score: {computerScore}',"\033[0m")
  elif spelerActie == 2:
    if computerActie == 0:
      computerScore += 1
      print('Jij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;41m",'Computer wint!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}' "\033[0m",'|', "\x1b[1;30;41m",f'Computer score: {computerScore}',"\033[0m")
    elif computerActie == 1:
      spelerScore += 1
      print('Jij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;42m",'Jij wint!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}' "\033[0m",'|', "\x1b[1;30;41m",f'Computer score: {computerScore}',"\033[0m")

  i += 1