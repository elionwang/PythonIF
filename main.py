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

  spelerInput = input('Kies steen[0], papier[1] of schaar[2]: ')

  time.sleep(3)

  spelerActie = int(spelerInput)

  if spelerActie == 0:
    spelerActieNaam = 'steen'
  elif spelerActie == 1:
    spelerActieNaam = 'papier'
  elif spelerActie == 2:
    spelerActieNaam = 'schaar'

  if spelerActie == computerActie:
    spelerScore = spelerScore + 1
    computerScore += 1
    print(f'Jij koos: {spelerActieNaam} \n Computer koos: {computerActieNaam} \n Het is gelijkspel! \n Jouw score: {spelerScore} | Computer score: {computerScore}')
  elif spelerActie == 0:
    if computerActie == 1:
      computerScore += 1
      print(f'Jij koos: {spelerActieNaam} \n Computer koos: {computerActieNaam} \n Computer wint! \n Jouw score: {spelerScore} | Computer score: {computerScore}')
    elif computerActie == 2:
      spelerScore += 1
      print(f'Jij koos: {spelerActieNaam} \n Computer koos: {computerActieNaam} \n Jij wint! \n Jouw score: {spelerScore} | Computer score: {computerScore}')
  elif spelerActie == 1:
    if computerActie == 0:
      spelerScore += 1
      print(f'Jij koos: {spelerActieNaam} \n Computer koos: {computerActieNaam} \n Jij wint! \n Jouw score: {spelerScore} | Computer score: {computerScore}')
    elif computerActie == 2:
      computerScore += 1
      print(f'Jij koos: {spelerActieNaam} \n Computer koos: {computerActieNaam} \n Computer wint! \n Jouw score: {spelerScore} | Computer score: {computerScore}')
  elif spelerActie == 2:
    if computerActie == 0:
      computerScore += 1
      print(f'Jij koos: {spelerActieNaam} \n Computer koos: {computerActieNaam} \n Computer wint! \n Jouw score: {spelerScore} | Computer score: {computerScore}')
    elif computerActie == 1:
      spelerScore += 1
      print(f'Jij koos: {spelerActieNaam} \n Computer koos: {computerActieNaam} \n Jij wint! \n Jouw score: {spelerScore} | Computer score: {computerScore}')

  i += 1