import random
choices = ["steen", "papier", "schaar"]
computerChoice = random.choice(choices)
playerChoice = input('Kies steen, papier of schaar: ').lower()
outcome = choices.index(playerChoice) - choices.index(computerChoice)
print(f'Speler: {playerChoice}')
print(f'Computer: {computerChoice}')
if outcome == -1 or outcome == 2:
  print('Computer wint!')
elif outcome == 0:
  print('Het is gelijkspel!')
elif outcome == 1 or outcome == -2:
  print('Jij wint!')