import random

class blackJack:

    def __init__(self):
        self.deck = []

    def create_deck(self):
        suits = ['heart', 'diamond', 'spade', 'club']
        card_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        for number in card_numbers:
            for suit in suits:
                card = f'{number} of {suit}'
                self.deck.append(card)

    def calculate_hand_value(self, hand):
        value = 0
        for card in hand:
            parts = card.split()
            if len(parts) == 3:
                card_number = parts[0]
            else:
                card_number = 10 
            if card_number.isdigit():
                card_number = int(card_number)
            else:
                card_number = 10  # Handle face cards (King, Queen, Jack)
            value += card_number
        return value

    def deal(self):
        your_hand = random.sample(self.deck, 2)
        dealers_hand = random.sample(self.deck, 2)

        while True:
            your_hand_value = self.calculate_hand_value(your_hand)
            dealers_hand_value = self.calculate_hand_value(dealers_hand)

            print(f"Your hand: {your_hand}")
            next_move = input("What would you like to do next? (Hit/Stand/Blackjack)").lower()

            if next_move == "hit":
                your_hand.append(random.choice(self.deck))
                print(f"Your hand: {your_hand}")
            elif next_move == "stand":
                print(f"Your hand: {your_hand} \nDealer's hand: {dealers_hand}")
                if your_hand_value > 21:
                    print("Bust! The sum of your cards is over 21. The dealer wins this one.")
                else:
                    while dealers_hand_value < 17:
                        dealers_hand.append(random.choice(self.deck))
                        dealers_hand_value = self.calculate_hand_value(dealers_hand)
                    print(f"Dealer's hand: {dealers_hand}")

                    if dealers_hand_value > 21:
                        print("Dealer busts! You win.")
                    elif dealers_hand_value >= your_hand_value:
                        print("Dealer wins.")
                    else:
                        print("You win!")

                break
            elif next_move == "blackjack" and your_hand_value == 21:
                print("Well done. You win!")
                break

run = blackJack()
run.create_deck()
run.deal()

