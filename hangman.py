import os
import sys
import random
from colorama import Fore, Style


class Hangman(object):

    def __init__(self):
        self.topics = {'fruits': ['banana', 'appricot', 'apple'],
                       'objects': ['knife', 'kitchen', 'whiteboard']}
        self.right = [] # Change dtype to avoid repetition
        self.wrong = []
        self.word = None
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
            print(f"{Fore.GREEN}{self.logo}{Style.RESET_ALL}", end='\n\n')
            print('\n Here are the genres of words you can pick!\n')

            for topic in self.topics:
                print(f' Type {topic} to choose {topic} like words')

            output = input('\n select: ')

            if output in self.topics.keys():
                self.choose_random(output)
                self.word_game()
                break

    def choose_random(self, genre):
        self.word = random.choice(self.topics[genre])

    def word_game(self):
        while True:
            count = 2
            for index, letter in enumerate(self.word):
                if letter in self.right:
                    if index != 0 and index != self.word.rfind(self.word[-1]):
                        count += 1

            if count == len(self.word):
                self.success()
                break

            self.clear_sc()

            print(f"{Fore.GREEN}{self.logo}{Style.RESET_ALL}", end='\n\n')
            print(f'Right: {self.right}   Wrong: {self.wrong}')
            print('\n Secret word! ', end='')

            for index, letter in enumerate(self.word, 1):
                if index == 1 or index == len(self.word):
                    print(letter, end='')
                else:
                    if letter in self.right:
                        print(letter, end='')
                    else:
                        print(' _', end='')

            letter = input('\n Type a letter: ')

            if letter in self.word and letter:
                self.right.append(letter)
            else:
                if letter:
                    self.wrong.append(letter)

    def success(self):
        while True:
            self.clear_sc()
            print(f"{Fore.GREEN}{self.logo}{Style.RESET_ALL}", end='\n\n')
            print(f'\n You got it! The secret word was {self.word}')
            print('\n Type yes to keep playing or no to exit the script')
            option = input(' > ')

            if option == 'no':
                sys.exit()
            break


if __name__ == '__main__':
    while True:
        game = Hangman()
        game.choose_topic()