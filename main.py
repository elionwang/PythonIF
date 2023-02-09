import time # import time module, voor sleep functie
import random # import random module, voor randint functie


matches = int(input('Hoeveel potjes wil je spelen? ')) # vraag hoeveel matches user wil spelen, sla het antwoord op in var 'matches'

i = 1 # var i een waarde van 1 geven. (identifier) 

spelerScore = 0 # geef var spelerScore een waarde van 0
computerScore = 0 # geef var computerScore een waarde van 0

aantalSteenSpeler = 0
aantalPapierSpeler = 0
aantalSchaarSpeler = 0

aantalSteenComputer = 0
aantalPapierComputer = 0
aantalSchaarComputer = 0

while i <= matches: # maak while loop, voer uit als i kleiner of gelijk is aan variabele 'matches'

  computerActie = random.randint(0, 2) # gebruik functie randint om willekeurige integer te krijgen tussen 0 en 2

  if computerActie == 0: # geef in het geval dat computer een output geeft van 0 de actie 'steen' als naam 
    aantalSteenComputer += 1
    computerActieNaam = 'steen'
  elif computerActie == 1: # geef in het geval dat computer een output geeft van 1 de actie 'papier' als naam
    aantalPapierComputer += 1
    computerActieNaam = 'papier'
  elif computerActie == 2: # geef in het geval dat computer een output geeft van 2 de actie 'schaar' als naam
    aantalSchaarComputer += 1
    computerActieNaam = 'schaar'

  print('-------------------------------------') # print een lijn met streepjes voor overzichtelijkheid
  spelerInput = int(input('Kies steen[0], papier[1] of schaar[2]: ')) # vraag of user steen, papier of schaar wil kiezen d.m.v. getal, maak hier een integer van en sla op in variabele 'spelerInput'

  if spelerInput < 0 or spelerInput > 2: # voer code uit als variabele spelerInput kleiner dan 0 of groter dan 2 is
    print(f'\x1b[1;30;41m{spelerInput} is geen geldige input idioot. Kies steen[0], papier[1] of schaar[2].',"\033[0m") # print error message en beledig user, gebruik ANSI escape code voor rode achtergrond van tekst en op het einde zodat tekst daarna wit blijft
    
  time.sleep(3) # wacht drie seconden voordat rest van de code wordt uitgevoerd d.m.v. sleep functie van time library

  spelerActie = int(spelerInput) # maak een integer van spelerInput en sla deze op in de variabele 'userAction' 

  if spelerActie == 0: # geef in het geval dat spelerInput 0 is, de actie 'steen' als naam 
    aantalSteenSpeler += 1
    spelerActieNaam = 'steen'
  elif spelerActie == 1: # geef in het geval dat spelerInput 1 is, de actie 'papier' als naam
    aantalPapierSpeler += 1
    spelerActieNaam = 'papier'
  elif spelerActie == 2: # geef in het geval dat spelerInput 2 is, de actie 'schaar' als naam
    aantalSchaarSpeler += 1
    spelerActieNaam = 'schaar'

  if spelerActie == computerActie: # check of spelerActie hetzelfde is als computerActie en voer code uit als dit klopt
    spelerScore += 1 # voeg 1 toe aan variabele spelerScore
    computerScore += 1 # voeg 1 toe aan variabele computerScore
    print(f'\x1b[1;34;40mPot {i}:\n\033[0mJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;40m",'Het is gelijkspel!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}\033[0m |',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console, gebruik ANSI escape code voor alle kleuren
  elif spelerActie == 0: # anders als spelerActie 0 is, voer code uit
    if computerActie == 1: # check of computerActie gelijk staat tot 1, en voer code uit als dit klopt
      computerScore += 1 # voeg 1 toe aan variabele computerScore
      print(f'\x1b[1;34;40mPot {i}:\n\033[0mJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;40m",'Computer wint!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}\033[0m |',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console, gebruik ANSI escape code voor alle kleuren
    elif computerActie == 2: # anders als computerActie 2 is, voer code uit
      spelerScore += 1 # voeg 1 toe aan variabele spelerScore
      print(f'\x1b[1;34;40mPot {i}:\n\033[0mJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;40m",'Jij wint!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}',"\033[0m",'|',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console, gebruik ANSI escape code voor alle kleuren
  elif spelerActie == 1: # check of spelerActie gelijk staat tot 1 en voer code uit als dit klopt
    if computerActie == 0: # check of computerActie gelijk staat tot 0, en voer code uit als dit klopt
      spelerScore += 1 # voeg 1 toe aan variabele spelerScore
      print(f'\x1b[1;34;40mPot {i}:\n\033[0mJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;40m",'Jij wint!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}',"\033[0m",'|',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console, gebruik ANSI escape code voor alle kleuren
    elif computerActie == 2: # anders als computerActie 2 is, voer code uit
      computerScore += 1 # voeg 1 toe aan variabele computerScore
      print(f'\x1b[1;34;40mPot {i}:\n\033[0mJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;40m",'Computer wint!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}',"\033[0m",'|',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console, gebruik ANSI escape code voor alle kleuren
  elif spelerActie == 2: # check of spelerActie gelijk staat tot 2, en voer code uit als dit klopt
    if computerActie == 0: # check of computerActie gelijk staat tot 0, en voer code uit als dit klopt
      computerScore += 1 # voeg 1 toe aan variabele computerScore
      print(f'\x1b[1;34;40mPot {i}:\n\033[0mJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;40m",'Computer wint!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}',"\033[0m",'|',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console, gebruik ANSI escape code voor alle kleuren
    elif computerActie == 1: # anders als computerActie 1 is, voer code uit
      spelerScore += 1 # voeg 1 toe aan variabele spelerScore
      print(f'\x1b[1;34;40mPot {i}:\n\033[0mJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;40m",'Jij wint!',"\n\x1b[1;30;42m",f'Jouw score: {spelerScore}',"\033[0m",'|',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console, gebruik ANSI escape code voor alle kleuren

  if i == matches:
    print('-------------------------------------') # print een lijn met streepjes voor overzichtelijkheid
    print(f'\x1b[1;34;40mOverzicht:\n\x1b[1;30;42mJouw score: {spelerScore}',"\033[0m",'|',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef score van speler en computer d.m.v. variabelen spelerScore en computerScore en print naar console, gebruik ANSI escape code voor alle kleuren
    if spelerScore == computerScore: # voer code uit in het geval dat spelerScore gelijk staat aan computerScore
      print(f'\n\x1b[1;30;40mHet is gelijkspel geworden!\033[0m') # print uitslag (gelijkspel) naar console
    elif spelerScore > computerScore: # voer code uit in het geval dat spelerScore groter is dan computerScore
      print(f'\n\x1b[1;32;40mGefeliciteerd! Jij hebt gewonnen!\033[0m') # print uitslag (winst) naar console
    elif computerScore > spelerScore: # voer code uit in het geval dat computerScore groter is dan spelerScore
      print(f'\n\x1b[1;31;40mHelaas! Computer heeft gewonnen!\033[0m') # print uitslag (nederlaag) naar console
    print('\n\x1b[1;32;40mKeuzes (Speler):\n\x1b[1;30;40mSteen:',f'{aantalSteenSpeler / matches * 100}% ({aantalSteenSpeler}/{matches})\n\x1b[1;37;40mPapier:',f'{aantalPapierSpeler / matches * 100}% ({aantalPapierSpeler}/{matches})\n\x1b[1;31;40mSchaar:',f'{aantalSchaarSpeler / matches * 100}% ({aantalSchaarSpeler}/{matches})\033[0m\n') # print de keuzes die de speler heeft gemaakt over alle potjes naar de console d.m.v. de variabelen aantalSteenSpeler, aantalPapierSpeler en aantalSchaarSpeler en bereken hiervan de percentages met formatted strings
    print('\x1b[1;32;40mKeuzes (Computer):\n\x1b[1;30;40mSteen:',f'{aantalSteenComputer / matches * 100}% ({aantalSteenComputer}/{matches})\n\x1b[1;37;40mPapier:',f'{aantalPapierComputer / matches * 100}% ({aantalPapierComputer}/{matches})\n\x1b[1;31;40mSchaar:',f'{aantalSchaarComputer / matches * 100}% ({aantalSchaarComputer}/{matches})\033[0m') # print de keuzes die de computer heeft gemaakt over alle potjes naar de console d.m.v. de variabelen aantalSteenComputer, aantalPapierComputer en aantalSchaarComputer en bereken hiervan de percentages met formatted strings

  i += 1 # voeg 1 toe aan i, zodat while loop stopt na variabele 'matches' aantal aan potjes