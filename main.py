import time # import time module, voor sleep functie, line 52
import random # import random module, voor randint functie, line 40

# gebruikte ANSI escape codes:
# \033[0m = wit
# \x1b[1;30;41m = rode achtergrond op grijze tekst
# \x1b[3;37;40m = schuingedrukte witte tekst (zwarte achtergrond)
# \x1b[1;34;40m = dikgedrukte blauwe tekst (zwarte achtergrond)
# \x1b[1;30;40m = schuingedrukte grijze tekst (zwarte achtergrond)
# \x1b[1;30;42m = groene achtergrond op grijze tekst
# \x1b[1;32;40m = dikgedrukte groene tekst (zwarte achtergrond)
# \x1b[1;31;40m = dikgedrukte rode tekst (zwarte achtergrond)
# \x1b[1;37;40m = dikgedrukte witte tekst (zwarte achtergrond)


matches = int(input('Hoeveel potjes wil je spelen? ')) # vraag hoeveel matches user wil spelen, maak er een integer van en sla het antwoord op in de variabele 'matches'

i = 1 # geef var i een waarde van 1 (identifier), gebruik later in while loop, om aan te geven hoeveelste keer de loop draait

spelerScore = 0 # creëer variabele spelerScore en geef een waarde van 0
computerScore = 0 # creëer variabele computerScore en geef een waarde van 0

aantalSteenSpeler = 0 # creëer variabele aantalSteenSpeler en geef een waarde van 0, voor aantal gekozen keren van de actie 'steen' van de speler
aantalPapierSpeler = 0 # creëer variabele aantalPapierSpeler en geef een waarde van 0, voor aantal gekozen keren van de actie 'papier' van de speler
aantalSchaarSpeler = 0 # creëer variabele aantalSchaarSpeler en geef een waarde van 0, voor aantal gekozen keren van de actie 'schaar' van de speler

aantalSteenComputer = 0 # creëer variabele aantalSteenComputer en geef een waarde van 0, voor aantal gekozen keren van de actie 'steen' van de computer
aantalPapierComputer = 0 # creëer variabele aantalPapierComputer en geef een waarde van 0, voor aantal gekozen keren van de actie 'papier' van de computer
aantalSchaarComputer = 0 # creëer variabele aantalSchaarComputer en geef een waarde van 0, voor aantal gekozen keren van de actie 'schaar' van de computer

while i <= matches: # maak while loop, voer code uit als i kleiner of gelijk is aan waarde van variabele 'matches'

  print('-------------------------------------') # print een lijn met streepjes naar de console voor overzichtelijkheid 
  spelerInput = int(input('Kies steen[0], papier[1] of schaar[2]: ')) # vraag of user steen, papier of schaar wil kiezen d.m.v. getal, maak hier een integer van en sla deze waarde op in de variabele 'spelerInput'

  if spelerInput < 0 or spelerInput > 2: # voer code uit als variabele spelerInput kleiner dan 0 of groter dan 2 is
    print(f'\x1b[1;30;41m{spelerInput} is geen geldige input idioot. Kies steen[0], papier[1] of schaar[2].',"\033[0m") # print error message en beledig user, gebruik ANSI escape code voor rode achtergrond van tekst en op het einde zodat tekst daarna wit blijft
    continue # ga terug naar begin van de while loop, niet 1 toevoegen aan de waarde van i
    
  computerActie = random.randint(0, 2) # gebruik functie randint uit 'random' library om willekeurige integer te krijgen tussen 0 en 2

  if computerActie == 0: # geef in het geval dat computer een output geeft van 0 in random.randint(0,2), de actie 'steen' als naam 
    aantalSteenComputer += 1 # voeg 1 toe aan de waarde van de variabele aantalSteenComputer
    computerActieNaam = 'steen'
  elif computerActie == 1: # geef in het geval dat computer een output geeft van 1 in random.randint(0,2), de actie 'papier' als naam
    aantalPapierComputer += 1 # voeg 1 toe aan de waarde van de variabele aantalPapierComputer
    computerActieNaam = 'papier'
  elif computerActie == 2: # geef in het geval dat computer een output geeft van 2 in random.randint(0,2), de actie 'schaar' als naam
    aantalSchaarComputer += 1
    computerActieNaam = 'schaar'
  
  time.sleep(3) # wacht drie seconden voordat rest van de code wordt uitgevoerd d.m.v. sleep functie van time library

  print('-------------------------------------') # print een lijn met streepjes naar de console voor overzichtelijkheid 

  spelerActie = int(spelerInput) # maak een integer van de variabele spelerInput en sla deze op in de variabele 'spelerActie' 

  if spelerActie == 0: # geef in het geval dat spelerActie een waarde van 0 heeft, de actie 'steen' als naam 
    aantalSteenSpeler += 1 # voeg 1 toe aan de waarde van de variabele aantalSteenSpeler
    spelerActieNaam = 'steen'
  elif spelerActie == 1: # geef in het geval dat spelerActie een waarde van 1 heeft, de actie 'papier' als naam
    aantalPapierSpeler += 1 # voeg 1 toe aan de waarde van de variabele aantalPapierSpeler
    spelerActieNaam = 'papier'
  elif spelerActie == 2: # geef in het geval dat spelerActie een waarde van 2 heeft, de actie 'schaar' als naam
    aantalSchaarSpeler += 1 # voeg 1 toe aan de waarde van de variabele aantalSchaarSpeler
    spelerActieNaam = 'schaar'

  if spelerActie == computerActie: # check of spelerActie hetzelfde is als computerActie en voer code uit als dit klopt
    spelerScore += 1 # voeg 1 toe aan de  variabele spelerScore
    computerScore += 1 # voeg 1 toe aan de  variabele computerScore
    print(f'\x1b[1;34;40mPot {i}:\n\033[0mJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',"\n\x1b[1;30;40mHet is gelijkspel!",f'\n\x1b[1;30;42mJouw score: {spelerScore}\033[0m |',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console, gebruik ANSI escape codes voor alle kleuren
  elif spelerActie == 0: # anders als spelerActie een waarde van 0 heeft, voer code uit
    if computerActie == 1: # check of computerActie gelijk staat tot 1, en voer code uit als dit klopt
      computerScore += 1 # voeg 1 toe aan de waarde van de variabele computerScore
      print(f'\x1b[1;34;40mPot {i}:\n\033[0mJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',f'\n\x1b[1;30;40mComputer wint!\n\x1b[1;30;42mJouw score: {spelerScore}\033[0m |',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console, gebruik ANSI escape codes voor alle kleuren
    elif computerActie == 2: # anders als computerActie een waarde heeft van 2, voer code uit
      spelerScore += 1 # voeg 1 toe aan de waarde van de variabele spelerScore
      print(f'\x1b[1;34;40mPot {i}:\n\033[0mJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',f'\n\x1b[1;30;40mJij wint!\n\x1b[1;30;42mJouw score: {spelerScore}\033[0m |',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console, gebruik ANSI escape codes voor alle kleuren
  elif spelerActie == 1: # check of spelerActie gelijk staat tot 1 en voer code uit als dit klopt
    if computerActie == 0: # check of computerActie gelijk staat tot 0, en voer code uit als dit klopt
      spelerScore += 1 # voeg 1 toe aan de waarde van de variabele spelerScore
      print(f'\x1b[1;34;40mPot {i}:\n\033[0mJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',f'\n\x1b[1;30;40mJij wint!\n\x1b[1;30;42mJouw score: {spelerScore}\033[0m |',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console, gebruik ANSI escape codes voor alle kleuren
    elif computerActie == 2: # anders als computerActie een waarde heeft van 2, voer code uit
      computerScore += 1 # voeg 1 toe aan de waarde van de variabele computerScore
      print(f'\x1b[1;34;40mPot {i}:\n\033[0mJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',f'\n\x1b[1;30;40mComputer wint!\n\x1b[1;30;42mJouw score: {spelerScore}\033[0m |',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console, gebruik ANSI escape codes voor alle kleuren
  elif spelerActie == 2: # check of spelerActie gelijk staat tot 2, en voer code uit als dit klopt
    if computerActie == 0: # check of computerActie gelijk staat tot 0, en voer code uit als dit klopt
      computerScore += 1 # voeg 1 toe aan de waarde van de variabele computerScore
      print(f'\x1b[1;34;40mPot {i}:\n\033[0mJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',f'\n\x1b[1;30;40mComputer wint!\n\x1b[1;30;42mJouw score: {spelerScore}\033[0m |',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console, gebruik ANSI escape codes voor alle kleuren
    elif computerActie == 1: # anders als computerActie 1 is, voer code uit
      spelerScore += 1 # voeg 1 toe aan de waarde van de variabele spelerScore
      print(f'\x1b[1;34;40mPot {i}:\n\033[0mJij koos:',"\x1b[3;37;40m",f'{spelerActieNaam}',"\033[0m",'\nComputer koos:',"\x1b[3;37;40m",f'{computerActieNaam}',f'\n\x1b[1;30;40mJij wint!\n\x1b[1;30;42mJouw score: {spelerScore}\033[0m |',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef uitslag en print naar console, gebruik ANSI escape codes voor alle kleuren

  if i == matches: # voer code uit als de variabele i gelijk staat aan variabele 'matches'
    print('-------------------------------------') # print een lijn met streepjes naar de console voor overzichtelijkheid
    print(f'\x1b[1;34;40mOverzicht:\n\x1b[1;30;42mJouw score: {spelerScore}',"\033[0m",'|',"\x1b[1;30;41m",f'Computer score: {computerScore}\033[0m') # geef score van speler en computer d.m.v. variabelen spelerScore en computerScore en print naar console, gebruik ANSI escape codes voor alle kleuren
    if spelerScore == computerScore: # voer code uit in het geval dat spelerScore gelijk staat aan computerScore
      print('\n\x1b[1;30;40mHet is gelijkspel geworden!\033[0m') # print uitslag (gelijkspel) naar console
    elif spelerScore > computerScore: # voer code uit in het geval dat spelerScore groter is dan computerScore
      print('\n\x1b[1;32;40mGefeliciteerd! Jij hebt gewonnen!\033[0m') # print uitslag (winst) naar console
    elif computerScore > spelerScore: # voer code uit in het geval dat computerScore groter is dan spelerScore
      print('\n\x1b[1;31;40mHelaas! Computer heeft gewonnen!\033[0m') # print uitslag (nederlaag) naar console
    print('\n\x1b[1;32;40mKeuzes (Speler):\n\x1b[1;30;40mSteen:',f'{round((aantalSteenSpeler / matches * 100), 1)}% ({aantalSteenSpeler}/{matches})\n\x1b[1;37;40mPapier:',f'{round((aantalPapierSpeler / matches * 100), 1)}% ({aantalPapierSpeler}/{matches})\n\x1b[1;31;40mSchaar:',f'{round((aantalSchaarSpeler / matches * 100), 1)}% ({aantalSchaarSpeler}/{matches})\033[0m\n') # print de keuzes die de speler heeft gemaakt over alle potjes naar de console d.m.v. de variabelen aantalSteenSpeler, aantalPapierSpeler en aantalSchaarSpeler, bereken hiervan de percentages met formatted strings, gebruik round() om af te ronden op 1 decimaal nadat getal wordt vermenigvuldigd met 100 en geef kleur met ANSI escape codes
    print('\x1b[1;32;40mKeuzes (Computer):\n\x1b[1;30;40mSteen:',f'{round((aantalSteenComputer / matches * 100), 1)}% ({aantalSteenComputer}/{matches})\n\x1b[1;37;40mPapier:',f'{round((aantalPapierComputer / matches * 100), 1)}% ({aantalPapierComputer}/{matches})\n\x1b[1;31;40mSchaar:',f'{round((aantalSchaarComputer / matches * 100), 1)}% ({aantalSchaarComputer}/{matches})\033[0m') # print de keuzes die de computer heeft gemaakt over alle potjes naar de console d.m.v. de variabelen aantalSteenComputer, aantalPapierComputer en aantalSchaarComputer, bereken hiervan de percentages met formatted strings, gebruik round() om af te ronden op 1 decimaal nadat getal wordt vermenigvuldigd met 100 en geef kleur met ANSI escape codes

  i += 1 # voeg 1 toe aan i, zodat while loop stopt na variabele 'matches' aantal aan potjes