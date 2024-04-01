from enum import Enum

Wordle_word = "force"


class state(Enum):
    wrong = '\033[0m'
    yellow = '\033[93m'
    right = '\033[92m'


class Character:
    def __init__(self,c,index):
        self.c = c
        self.index = index
        self.state = state.wrong
    
class Game:
    def __init__(self,Wordle_word) -> None:
        self.Wordle_word = Wordle_word
        
    def inputword(self,word):
        if not self.CheckForAnswer(word):
            return []    

        characters = []
        for i in range(5):
            c = word[i]
            character = Character(c,i)

            if(c == self.Wordle_word[i]):
                character.state = state.right
            elif c in self.Wordle_word:
                character.state = state.yellow
            characters.append(character)
        return characters

    def tostring(characters):
        return ''.join([char.state.value + char.c for char in characters])


    def CheckForAnswer(self,word: str):
        if len(word) != 5:
            return False
        word = word.lower()
        with open("Answers/wordle-La.txt", mode="r") as f:
            return word in f.read()



    