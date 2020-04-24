# Default imports
import os
import sys
import random


class Hangman(object):

    def __init__(self):
        self.topics = {'fruits': ['banana', 'appricot', 'apple'],
                       'objects': ['knife', 'kitchen', 'whiteboard']}
        self.right = []
        self.wrong = []
        self.word = str
        self.logo = r""" _                                              
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __   
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  
| | | | (_| | | | | (_| | | | | | | (_| | | | | 
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                   |___/                        """

    def clear_sc(self):
        os.system('cls')

    def choose_topic(self):
        while True:
            self.clear_sc()
            print(self.logo, end='\n\n')
            print('\n Here are the genres of words you can pick!\n')

            for topic in self.topics:
                print(f' Type {topic} to choose {topic} like words')

            output = input('\n select: ')

            if output in self.topics.keys():
                self.word = random.choice(self.topics[output])  # Get a random value from out selected topic, if we
                # choose  fruits we have ['banana', 'appricot', 'apple'] and simply choose a random value from the list
                break

    def word_game(self):
        while True:
            count = 2
            # Set to 2 because there are 2 visible letters
            # one at the start and one at the end of the word
            for index, letter in enumerate(self.word):
                if letter in self.right:
                    # If its not the first letter or the last and is revealed add 1 to count
                    if index != 0 and index != self.word.rfind(self.word[-1]):
                        count += 1

            if count == len(self.word):  # We got all the letters!
                break

            self.clear_sc()
            print(self.logo, end='\n\n')
            print(f'Right: {self.right}   Wrong: {self.wrong}')
            print('\n Secret word! ', end='')

            for index, letter in enumerate(self.word, 1):
                if index == 1 or index == len(self.word):  # if its the first or last letter in self.word
                    print(letter, end='')
                else:
                    if letter in self.right:  # if we got the letter right print it
                        print(letter, end='')
                    else:  # otherwise print an underscore
                        print(' _', end='')

            letter = input('\n Type a letter: ')

            if letter in self.word and letter:
                self.right.append(letter)
            elif letter:
                self.wrong.append(letter)

    def success(self):
        self.clear_sc()
        print(self.logo, end='\n\n')  # Python has as default one \n (new line) after each print, we need 2 here
        print(f'\n You got it! The secret word was {self.word}')
        print('\n Type yes to keep playing or no to exit the script')
        option = input(' > ')

        if option == 'no':
            sys.exit()


if __name__ == '__main__':
    while True:
        game = Hangman()  # The variable game contains the copy of our Hangman class
        game.choose_topic()  # game._function-name does this game --> hangman --> choose_topic()
        game.word_game()
        game.success()