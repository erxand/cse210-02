#director.py

import card.py

class Director:
    
    def __init__(self):
        self.running_points = 300
        self.is_playing = True
        self.starting_card = Card.draw_card()
        self.next_card = Card.draw_card()
    

    def get_first_input(self):
        response = input("Higher or lower? [h/l] ")
        return response
    

    def get_second_input(self):
        response = input("Play again? [y/n] ")
        return response
    
    def make_updates(self, response):
        if response == "h":
            if self.starting_card.card_value() < self.next_card.card_value():
                self.running_points += 100
            elif self.starting_card.card_value() > self.next_card.card_value():
                self.running_points -= 75
        elif response == "l":
            if self.starting_card.card_value() > self.next_card.card_value():
                self.running_points += 100
            elif self.starting_card.card_value() < self.next_card.card_value():
                self.running_points -= 75
        

    def do_output(self):
        print("Next card was:", self.next_card.card_value())
        print("Your score is:", self.running_points)
    

    def game_loop(self):
        while self.is_playing == True:
            print("The card is:", self.starting_card.card_value())
            response = self.get_first_input(self)
            self.make_updates(self, response)
            self.do_output(self)

            response = self.get_second_input()
            if response == "n":
                self.is_playing = False            

            self.starting_card = self.next_card
            self.next_card = Card.draw_card()