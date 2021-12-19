import random
import textwrap


class Deck:
    def __init__(self):
        suit_cards = [i for i in range(1, 13 + 1)]
        self.cards = suit_cards * 4

    def remove(self, card):
        try:
            self.cards.remove(int(card))
            return True
        except:
            print(f"error removing card {card}")
            return False


class Game:
    def __init__(self):
        self.deck = Deck()

    def remove_pair(self, pair):
        for card in pair:
            self.deck.remove(card)

    def possible_product(self):
        a, b = random.sample(self.deck.cards, 2)
        return a * b

    def run(self):
        while self.deck:
            prompt = textwrap.dedent(
                """            
            Choose an option:
            1: New target
            2: Remove pair
            8: Print deck
            9: Exit
            > """
            )

            choice = input(prompt)

            if choice == "1":
                print(self.possible_product())
            elif choice == "2":
                pair = input(
                    "Enter the values of the pair to remove seperated with whitespace.\n> "
                )
                try:
                    stripped_pair = pair.strip()
                    separated_pair = stripped_pair.split()
                except:
                    print("input error. No changes made to deck. Try again.")
                    continue
                if self.remove_pair(separated_pair):
                    print(f"Removed {stripped_pair}")
            elif choice == "8":
                print(
                    sorted([card for card in self.deck.cards])
                )  # todo - probably should format in a nicer manner. maybe a __str__ or __repr__ for the class.
            elif choice == "9":
                print("bye!")
                return
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    Game().run()
