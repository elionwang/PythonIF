import time
import random


computerActie = random.randint(0, 2)

if computerActie == 0:
  computerActieNaam = 'steen'
elif computerActie == 1:
  computerActieNaam = 'papier'
elif computerActie == 2:
  computerActieNaam = 'schaar'

spelerInput = input('Kies steen[0], papier[1] of schaar[2]: ')

spelerActie = int(spelerInput)

if spelerActie == 0:
  spelerActieNaam = 'steen'
elif spelerActie == 1:
  spelerActieNaam = 'papier'
elif spelerActie == 2:
  spelerActieNaam = 'schaar'

if spelerActie == computerActie:
  print(f'Jij koos: {spelerActieNaam} \n Computer koos: {computerActieNaam} \n Het is gelijkspel!')
elif spelerActie == 0:
  if computerActie == 1:
    print(f'Jij koos: {spelerActieNaam} \n Computer koos: {computerActieNaam} \n Computer wint!')
  elif computerActie == 2:
    print(f'Jij koos: {spelerActieNaam} \n Computer koos: {computerActieNaam} \n Jij wint!')
elif spelerActie == 1:
  if computerActie == 0:
    print(f'Jij koos: {spelerActieNaam} \n Computer koos: {computerActieNaam} \n Jij wint!')
  elif computerActie == 2:
    print(f'Jij koos: {spelerActieNaam} \n Computer koos: {computerActieNaam} \n Computer wint!')
elif spelerActie == 2:
  if computerActie == 0:
    print(f'Jij koos: {spelerActieNaam} \n Computer koos: {computerActieNaam} \n Computer wint!')
  elif computerActie == 1:
    print(f'Jij koos: {spelerActieNaam} \n Computer koos: {computerActieNaam} \n Jij wint!')