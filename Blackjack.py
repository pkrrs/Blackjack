import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card(deck , no_of_cards):
  for n in range(no_of_cards):
    deck.append(cards[random.randint(0,len(cards)-1)])
  return deck

def calculate_score(deck):
  """Caluclating scores for deck and returning optimal calculations"""
  score = sum(deck)
  if score == 21:
    return 0    
  elif score > 21:
    for card in deck:
      if card == 11:
        deck.remove(card)
        deck.append(1)
        score = sum(deck)
      return score
  else:
    return score

def compare(user_sum , computer_sum):
  """Comparing The Sums of cards and Deciding the winner"""
  if user_sum > 21 and computer_sum > 21:
      print("you went over. you lose.")

  if user_sum == computer_sum:
    print("Its a draw.")
    return False
  elif user_sum == 0:
    print("User has won by blackjack")
    return False
  elif user_sum > 21:
    print("Dealer Won")
    return False  
  elif computer_sum == 0:
    print("Dealer has won by blackjack")
    return False
  elif computer_sum > 21:
    print("User Won")
    return False 
  else:
    if user_sum > computer_sum:
      print("User win")
    else: 
      print("Dealer wins")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
should_continue = True
user_cards = []
computer_cards = []

#starting 
print(logo)
#dealing first cards
deal_card(user_cards, 2)
deal_card(computer_cards, 2)
#calculating sum
user_sum = calculate_score(user_cards)
computer_sum = calculate_score(computer_cards)

print(f"  Your cards: {user_cards}, Current score: {user_sum}")
print(f"  Dealer's First card: {computer_cards[0]}")

while should_continue:
  if user_sum == 0 or computer_sum == 0 or user_sum > 21:
    print(f"  Your final hand: {user_cards}. Your Final Score: {user_sum}")
    print(f"  Dealer's final hand: {computer_cards}. Dealer's Final Score: {computer_sum}")
    compare(user_sum , computer_sum)
    should_continue = False
  else:  
    choice = input("Do you wish to draw another card? Type 'yes' to draw or 'no' to pass. ").lower()
  if choice == "yes":
    deal_card(user_cards, 1)
    user_sum = calculate_score(user_cards)
    print(f"Your cards: {user_cards}, Current score: {user_sum}")
    print(f"Dealer's First card: {computer_cards[0]}")
  elif choice == "no":
    while computer_sum <= 17 and computer_sum != 0:
      deal_card(computer_cards , 1)
      computer_sum = calculate_score(computer_cards)
    print(f"  Your final hand: {user_cards}. Your Final Score: {user_sum}")
    print(f"  Dealer's final hand: {computer_cards}. Dealer's Final Score: {computer_sum}")

    compare(user_sum , computer_sum)

    restart = input("Do you wish to play A new Game? Type 'yes or 'no'. ")
    if restart == "yes":
      #clears screen and print logo
      print("restarting")
    elif restart == "no":
      #clear screen
      print("Thank you for playing. Goodbye.")
    should_continue = False

# another way to code this game.  
# import random

# def deal_card():
#   """Returns a random card from the deck."""
#   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#   card = random.choice(cards)
#   return card

# def calculate_score(cards):
#   """Take a list of cards and return the score calculated from the cards"""
#   if sum(cards) == 21 and len(cards) == 2:
#     return 0
#   if 11 in cards and sum(cards) > 21:
#     cards.remove(11)
#     cards.append(1)
#   return sum(cards)

# def compare(user_score, computer_score):
#   #Bug fix. If you and the computer are both over, you lose.
#   if user_score > 21 and computer_score > 21:
#     return "You went over. You lose 😤"

#   if user_score == computer_score:
#     return "Draw 🙃"
#   elif computer_score == 0:
#     return "Lose, opponent has Blackjack 😱"
#   elif user_score == 0:
#     return "Win with a Blackjack 😎"
#   elif user_score > 21:
#     return "You went over. You lose 😭"
#   elif computer_score > 21:
#     return "Opponent went over. You win 😁"
#   elif user_score > computer_score:
#     return "You win 😃"
#   else:
#     return "You lose 😤"

# def play_game():

#   print(logo)
#   user_cards = []
#   computer_cards = []
#   is_game_over = False

#   for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())

#   while not is_game_over:
    
#     user_score = calculate_score(user_cards)
#     computer_score = calculate_score(computer_cards)
#     print(f"   Your cards: {user_cards}, current score: {user_score}")
#     print(f"   Computer's first card: {computer_cards[0]}")

#     if user_score == 0 or computer_score == 0 or user_score > 21:
#       is_game_over = True
#     else:
#       user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#       if user_should_deal == "y":
#         user_cards.append(deal_card())
#       else:
#         is_game_over = True

#   while computer_score != 0 and computer_score < 17:
#     computer_cards.append(deal_card())
#     computer_score = calculate_score(computer_cards)

#   print(f"   Your final hand: {user_cards}, final score: {user_score}")
#   print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
#   print(compare(user_score, computer_score))

# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#   play_game()
 






