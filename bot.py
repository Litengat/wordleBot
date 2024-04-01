from game import *
import random

from collections import Counter
ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"


pwords = []
with open("Answers/wordle-La.txt", "r") as f:
        for line in f:
            pwords.append(line[:-1])


def start(game,start_word):
    out = test_word(game,start_word,pwords,0,[])
    return out
    #print(str(out[0]) + " | " + str(out[1]))


    

def test_word(game: Game,word: str,possible_words: str,counter: int,guesses: list):
    guesses.append(word)
    #print("Word: " + word)
    if(len(possible_words) == 1):
        return [possible_words[0],counter + 1 ,guesses]

    chars = game.inputword(word)
    x = 0
    for i in chars:
        if i.state == state.right:
            x = x + 1
    if (x == 5):
        return [word,counter + 1 ,guesses]

    
    right_chars = getCharsWithState(chars,state.right)
    yellow_chars = getCharsWithState(chars,state.yellow)
    wrong_chars = getCharsWithState(chars,state.wrong)
    out = []
    for word in possible_words:
        if testpossible_word(word,right_chars,yellow_chars,wrong_chars):
            out.append(word)
    #print(out)
    best_word = GetLetterFrequency(out,chars, guesses)

    return test_word(game,best_word,out,counter + 1,guesses)






def testpossible_word(word,right_chars,yellow_chars,wrong_chars):
    for char in right_chars:
        if(word[char.index] != char.c):
            return False

    for char in yellow_chars:
        if not char.c in word:
            return False
        if(word[char.index] == char.c):
            return False

    for char in wrong_chars:
        if char.c in word:
             return False
    
    return True


def getCharsWithState(chars,state):
    out = []
    for char in chars:
        if(char.state == state):
            out.append(char)
    return out

    

def GetLetterFrequency(words: list,chars, guesses):
    a = ''.join(words)
    CharsValues = dict(sorted([(i.upper(),Counter(a)[i]) for i in ascii_lowercase], key=lambda x:x[1], reverse=True))

    for Char in getCharsWithState(chars,state.right):
        CharsValues[Char.c.upper()] = 0
        
    wordValues = []
    chances = []
    for word in words:
        if word in guesses:
            pass
        else:
            values = []
            for l in range(len(word)):
                if word.count(word[l]) > 1:
                    values.append(-100) 
                chance = ChanceOfCharAtPos(words,word[l], l)[0]
                chances.append(chance)  
                values.append(CharsValues[word[l].upper()] * (chance-0.04))
        
        word_index = sum(values)
        wordValues.append([word,word_index])


    

    out = sorted(wordValues, key=lambda x:x[1], reverse=True)
    # if( Average(chances) > 0.7 and Average(chances) < 0.9):
    #     out.insert(0, [findDifferences(words)[0], 0])

    return out[0][0] if out[0][0] not in guesses else out[1][0]

def ChanceOfCharAtPos(words_left ,char, index):
    total = 0
    words = []
    for word in words_left:
        if word[index] == char:
            total += 1
            words.append(word)
    return [total/len(words_left), words]

def findDifferences(words):
    a = ""
    for word in words:
        a += ''.join(sorted(set(word), key=word.index))
    CharsValues = dict(sorted([(i.upper(),Counter(a)[i]) for i in ascii_lowercase], key=lambda x:x[1], reverse=True))
    CharsValues = { k:v for k, v in CharsValues.items() if v == 1 or v == 2 if len(words) > 2}
    lst = list(CharsValues.keys())
    
    points = []
    for word in pwords:
        point = 0
        for c in lst:
            if c.lower() in word:
                point = point + 1
        points.append([word,point])
    sortedpoints = sorted(points,key=lambda x:x[1],reverse=True)
    return sortedpoints[0]
                
def Average(lst):
    return sum(lst) / len(lst)

        
if __name__ == "__main__":
    game = Game("wound")
    out = start(game,"crane")
    print(str(out[0]) + " | " + str(out[1]))
    print(findDifferences(['found', 'hound', 'mound', 'pound', 'wound']))
