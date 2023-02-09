import time # import time module, voor sleep functie
import random # import random module, voor randint functie


matches = int(input('Hoeveel potjes wil je spelen? ')) # vraag hoeveel matches user wil spelen, sla het antwoord op in var 'matches'

i = 1 # var i een waarde van 1 geven. (identifier) 

spelerScore = 0 # geef var spelerScore een waarde van 0
computerScore = 0 # geef var computerScore een waarde van 0

while i <= matches: # maak while loop, voer uit als i kleiner of gelijk is aan variabele 'matches'

  computerActie = random.randint(0, 2) # gebruik functie randint om willekeurige integer te krijgen tussen 0 en 2

  if computerActie == 0: # geef in het geval dat computer een output geeft van 0 de actie 'steen' als naam 
    computerActieNaam = 'steen'
  elif computerActie == 1: # geef in het geval dat computer een output geeft van 1 de actie 'papier' als naam
    computerActieNaam = 'papier'
  elif computerActie == 2: # geef in het geval dat computer een output geeft van 2 de actie 'schaar' als naam
    computerActieNaam = 'schaar'

  print('-------------------------------------') # print een lijn met streepjes voor overzichtelijkheid
  spelerInput = int(input('Kies steen[0], papier[1] of schaar[2]: ')) # vraag of user steen, papier of schaar wil kiezen d.m.v. getal en sla input op in variabele 'spelerInput'

  if spelerInput < 0 or spelerInput > 2: # voer code uit als spelerInput kleiner dan 0 of groter dan 2 is
    i -= 1 # verminder i met 1 zodat het gewenste aantal potjes wordt gespeeld.
    print(f'\x1b[4;30;41m{spelerInput} is geen geldige input idioot. Kies steen[0], papier[1] of schaar[2].',"\033[0m") # print error message en beledig user

  time.sleep(3) # wacht drie seconden voordat rest van de code wordt uitgevoerd

  spelerActie = int(spelerInput) # maak een integer van spelerInput en sla deze op in variabele 'userAction' 

  if spelerActie == 0: # geef in het geval dat spelerInput 0 is de actie 'steen' als naam 
    spelerActieNaam = 'steen'
  elif spelerActie == 1: # geef in het geval dat spelerInput 1 is de actie 'papier' als naam
    spelerActieNaam = 'papier'
  elif spelerActie == 2: # geef in het geval dat spelerInput 2 is de actie 'schaar' als naam
    spelerActieNaam = 'schaar'

  if spelerActie == computerActie: # check of spelerActie hetzelfde is als computerActie en voer code uit als dit klopt
    spelerScore += 1 # voeg 1 toe aan variabele spelerScore
    computerScore += 1 # voeg 1 toe aan variabele computerScore
    print(f'Pot {i}:\nJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;40m",'Het is gelijkspel!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}\033[0m |',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console
  elif spelerActie == 0: # anders als spelerActie 0 is, voer code uit
    if computerActie == 1: # check of computerActie gelijk staat tot 1, en voer code uit als dit klopt
      computerScore += 1 # voeg 1 toe aan variabele computerScore
      print(f'Pot {i}:\nJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;40m",'Computer wint!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}\033[0m |',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console
    elif computerActie == 2: # anders als computerActie 2 is, voer code uit
      spelerScore += 1 # voeg 1 toe aan variabele spelerScore
      print(f'Pot {i}:\nJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;40m",'Jij wint!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}',"\033[0m",'|',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console
  elif spelerActie == 1: # check of spelerActie gelijk staat tot 1 en voer code uit als dit klopt
    if computerActie == 0: # check of computerActie gelijk staat tot 0, en voer code uit als dit klopt
      spelerScore += 1 # voeg 1 toe aan variabele spelerScore
      print(f'Pot {i}:\nJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;40m",'Jij wint!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}',"\033[0m",'|',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console
    elif computerActie == 2: # anders als computerActie 2 is, voer code uit
      computerScore += 1 # voeg 1 toe aan variabele computerScore
      print(f'Pot {i}:\nJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;40m",'Computer wint!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}',"\033[0m",'|',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console
  elif spelerActie == 2: # check of spelerActie gelijk staat tot 2, en voer code uit als dit klopt
    if computerActie == 0: # check of computerActie gelijk staat tot 0, en voer code uit als dit klopt
      computerScore += 1 # voeg 1 toe aan variabele computerScore
      print(f'Pot {i}:\nJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;40m",'Computer wint!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}',"\033[0m",'|',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console
    elif computerActie == 1: # anders als computerActie 1 is, voer code uit
      spelerScore += 1 # voeg 1 toe aan variabele spelerScore
      print(f'Pot {i}:\nJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;40m",'Jij wint!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}',"\033[0m",'|',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console

  i += 1 # voeg 1 toe aan i, zodat while loop stopt na variabele 'matches' aantal aan potjes