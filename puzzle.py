import math
import random
word_Bank = ["string","intiger", "runtime error", "min", "max","else", "for", "range", "break", "import", "Array", "random", "functions", "while", "list", "boolean", "variable", "def", "camalCasing"]

question_bank = [
#string:
"its a statement or a number wrapped in double quotations",
#intiger:
"Its a whole number not a fraction",
#runtime error:
"It occurs in the program and stops it where the error in placed:",
#min:
"it returns the item with the lowest value",
#max:
"it returns the item with the highest value",
#else:
"its combined with an if statement and it runs if nothing else works",
#for:
"its used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)",
#range:
"It is used when a user needs to perform an action for a specific number of times",
#break:
"statement can be used in both while and for loops.stops the execution of the innermost loop and start executing the next line of code after the block",
#import:
"it brings in 1000 of diffrent operations",
#array
"its diffrent from lists, it can only contain values correspondingto the same data type",
#random:
"it generates random floats",
#while:
"it put a progran in a loop",
#list:
"its diffrent from arrays, it contains many diffrent values and they dont have to be the same",
#boolean:
"its data type used to represent logic values True and False",
#variable:
"it holds information or values in it",
#def:
"it helps create a defintion the is a block of code",
#return:
"it gives back the results",
#camalCasing:
"it is the stile that is used in coding"]

randnum_Picked = []

puzzle = """TGNISACLAMACGFBAQPBIUXUFQTEOHGZEJFHEWTTOELTLECTEULWYPSSRBMCMTZGNIRTSLBUAJNILWLCJQDEDRXILETMYHTROPMIYARRANOSZINTIGEREAPHUDMMOLEUSIGDVBHRNIMNTEVRHRAYPBYANOSKIAENAELOOBRDIAFNKRQEFEDZTHLELGSMRCAWENCJJRVEOOJOTTRULLEBJUOOFYRFPIEPBI
"""
Rows = 15
Cols = 15






def display_puzzel(puzzle):
     minIndex = 0
     person_Maxindex = int(input(" How long is the first row "))
     maxIndex = person_Maxindex -1
     if " " in puzzle:
          pass
          
     for i in range(15):
          print(puzzle[minIndex : maxIndex].replace("", " "))
          minIndex += 15
          maxIndex += 15

def randome_Question(question_bank,puzzle):
     randNum = random.randrange(0,20,1)
     if randNum in randnum_Picked:
          print("it passed")
     else:
          randnum_Picked.append(randNum)
          print(question_bank[randNum])

pairedFunctions = []
def question_answer(question_bank, puzzle, word_Bank):

     while word_Bank:
          pairedFunctions.append(word_Bank)
          return word_Bank


picked = []
def random_question(word_Bank,question_bank,picked):
    """gets a random Question"""
    import random
    while word_Bank:
        choice = random.randint(0,len(word_Bank)-1)
        if choice not in picked:
            question = question_bank[choice]
            answer = word_Bank[choice]
            picked.append(question)
            picked.append(answer)
            return question, answer
            print(picked)

          
#display_puzzel(puzzle)
#randome_Question(question_bank,puzzle)
#question_answer(question_bank, puzzle, word_Bank)
#question_answer(question_bank, puzzle, word_Bank)
random_question(word_Bank,question_bank,picked)
