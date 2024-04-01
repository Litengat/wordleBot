import game
import bot
import random
import time
start_word = "crane"
possible_words = []
start_words = ["champ","lucky","adieu","stare","ratio"]

def main():
    print("Welcome to Wordle!")
    print("You have 6 Guesses to Guess the Word")
    i = 0
    while i < 6:
        currentgame = game.Game("force")
        a = input("Enter your Guess... ")
        b = currentgame.inputword(a)
        try:
            print(game.tostring(b)+ '\033[0m')
            AllCorrect = True
            for i in range(5):
                if b[i].state == game.state.wrong:
                    AllCorrect = False
            if AllCorrect:
                print("You won! The Word was", game.tostring(b))
                break
            i += 1
        except IndexError:
            print("Your word needs to be 5 Letters long.")

def botTest():
    # guesses_start = []
    # for start_word in start_words:
    wordsAverage = []
    guesses = []
    for word in possible_words:
        newgame = game.Game(word)
        out = bot.start(newgame,start_word)
        wordsAverage.append(out)
        guesses.append(out[1])
        print(str(out[0]) + " | " + str(out[1]) + " | " + str(round(Average(guesses),3)))
    with open("Average.txt","w") as f:
        f.writelines([str(i[0]) + " | " + str(i[1]) + " | "+ ' -> '.join(i[2])+ "\n" for i in wordsAverage] )
    print(Average(guesses))


    #print("Average: " + str(Average(guesses)) + " | "+ start_word)
    # guesses_start.append(Average(guesses))
    # print(guesses_start)
    


def Average(lst):
    return sum(lst) / len(lst)

if __name__ == "__main__":
    with open("Answers/wordle-La.txt", "r") as f:
        for line in f:
            possible_words.append(line[:-1])
    botTest()