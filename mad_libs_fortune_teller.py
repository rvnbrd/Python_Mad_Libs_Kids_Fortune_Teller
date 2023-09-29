import sys
import time

#Originally from MadLibs.com Printable Resources: Mad Libs Fortune Teller. Code modified from Bennorth's python_text_fortune_teller on GitHub by Raven Hoffman.

outside_colours = ['RED', 'GREEN', 'BLUE', 'PURPLE']
yes_no = ['YES', 'NO']

def player_choice(name, choices):
  player_has_chosen_ok = False

  while not player_has_chosen_ok:
    print('\nChoose a ' + name + ':')
    for i in range(0, len(choices)):
      print(choices[i])

    choice = input('   I choose: ').casefold()

    player_has_chosen_ok = choice in map(str.casefold, choices)

    if not player_has_chosen_ok:
      print('please choose something on the list')
      
  return choice
  

def start_over(choices):
  player_has_chosen_ok = False

  while not player_has_chosen_ok:
    print('\n\n\nWould you like another fortune?')
    for i in range(0, len(choices)):
      print(choices[i])

    choice = input('   I think: ').casefold()

    player_has_chosen_ok = choice in map(str.casefold, choices)

    if not player_has_chosen_ok:
      print('please choose something on the list')

  return choice

print('Welcome to the Mad Libs fortune teller.')
input('\nTo get started, pose a yes or no question: ')

while True:
  colour_choice = player_choice('colour', outside_colours)
  if colour_choice in ["red"]:
    print ("\nR", "\nE", "\nD!", sep="...")
  elif colour_choice in ["green"]:
    print ("\nG", "\nR", "\nE", "\nE", "\nN!", sep="...")
  elif colour_choice in ["blue"]:
    print ("\nB", "\nL", "\nU", "\nE!", sep="...")
  else:
    print ("\nP", "\nU", "\nR", "\nP", "\nL", "\nE!", sep="...")

  n_letters_in_colour = len(colour_choice)
  if n_letters_in_colour in [3, 5]:
    first_number_choices = ['1', '2', '5', '6']
  else:
    first_number_choices = ['3', '4', '7', '8']

  time.sleep(1)
  first_number_chosen = player_choice('number', first_number_choices)

  if first_number_chosen in ["1"]:
    print("\n...1!")
  elif first_number_chosen in ["2"]:
    print("\n...1", "2!", sep="...")
  elif first_number_chosen in ["3"]:
    print("\n...1", "2", "3!", sep="...")
  elif first_number_chosen in ["4"]:
    print("\n...1", "2", "3", "4!", sep="...")
  elif first_number_chosen in ["5"]:
    print("\n...1", "2", "3", "4", "5!", sep="...")
  elif first_number_chosen in ["6"]:
    print("\n...1", "2", "3", "4", "5", "6!", sep="...")
  elif first_number_chosen in ["7"]:
    print("\n...1", "2", "3", "4", "5", "6", "7!", sep="...")
  else:
    print("\n...1", "2", "3", "4", "5", "6", "7", "8!", sep="...")

  if n_letters_in_colour in [3, 5]:
    if first_number_chosen in ['1', '5']:
        second_number_choices = ['3', '4', '7', '8']
    else:
        second_number_choices = ['1', '2', '5', '6']
  else:
    if first_number_chosen in ['3', '7']:
        second_number_choices = ['1', '2', '5', '6']
    else:
        second_number_choices = ['3', '4', '7', '8']
      
  time.sleep(1)
  second_number_chosen = player_choice('second number', second_number_choices)

  if second_number_chosen in ['1', '2', '5', '8']:
    adjective = input('\nChoose an adjective: ')
    if second_number_chosen in ['1']:
      print('\nAnswer: Signs point to a/an ' + adjective + ' yes.')
    elif second_number_chosen in ['2']:
      print('\nAnswer: Signs point to a very ' + adjective + ' no.')
    elif second_number_chosen in ['8']:
      print('\nAnswer: The skies are ' + adjective + '.' + 'The future is uncertain.')
    else:
      singular_noun = input('Choose a singular noun: ')
      print('\nAnswer: Picture a/an ' + adjective + ' ' + singular_noun + "That is your answer.")
  elif second_number_chosen in ['3']:
    person = input("\nChoose a person in the room: ")
    print("\nAnswer: Don't believe anything " + person + " says.")
  elif second_number_chosen in ['4']:
    body_part = input("\nChoose a part of the body: ")
    print("\nAnswer: What does your " + body_part + " tell you?")
  elif second_number_chosen in ['6']:
    article_clothing = input("\nChoose an article of clothing that you are wearing: ")
    print("\nAnswer: You will find the answer in your " + article_clothing + ".")
  else:
    positive_number = input('\nChoose a number greater than one: ')
    plural_noun = input('Choose a plural noun: ')
    print('\nAnswer: I see ' + positive_number + ' big ' + plural_noun + ' in your future.')

  time.sleep(2)
  start_over_choice = start_over(yes_no)
  if start_over_choice in ['yes']:
    input("\nGreat! Pose another yes or no question: ")
    continue
  else:
    print("Okay, thank you for playing! Good bye.")
    time.sleep(3)
    sys.exit()