from itertools import count
import os #to clear screen
import random 
#Message of the game - Welcome
def head ():
    head="""
                    Bienvenido al juego del Ahorcado
     _   _                                           _____                      
    | | | |                                         |  __ \                     
    | |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __   | |  \/ __ _ _ __ ___   ___ 
    |  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  | | __ / _` | '_ ` _ \ / _ \\
    | | | | (_| | | | | (_| | | | | | | (_| | | | | | |_\ \ (_| | | | | | |  __/
    \_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  \____/\__,_|_| |_| |_|\___|
                        __/ |                                                   
                        |___/                                                   
    """

    print(head)

#Normalize the word
def normalize(sentence): # It removes the accents of a string
    new_sentence = sentence.maketrans('áéíóú', 'aeiou')
    n_sentence = sentence.translate(new_sentence)
    n_sentence = n_sentence.upper() #Convert the word to upper
    n_sentence = n_sentence.strip() #Remove the spaces
    n_sentence = n_sentence.replace(" ", "") #Remove the spaces
    # print(n_sentence) #Test. This is the new word 
    return n_sentence

#Open the file and read it (Words the game) ------------- Working with files:
# IMPORTANT: The word DATA_PATH is remplaced by the file path of the file 'data'
data_path = './archivos/data.txt'
def read_file():
    data=[]
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            for line in f:
                    data.append(line.strip())
            word=random.choice(data)
        return word
    except (TypeError, NameError, SyntaxError, FileNotFoundError):
        print("Can't find the file named 'data', we are restoring the file, but please, don't modify or delete that file...")
        quit()

#Hide the word to show the user
def hide_word (newword):
    hide_word=[]
    for letter in newword:
        hide_word.append('_')
    print("".join(hide_word))
    return hide_word

def draw_hangman (count):
    #dic draw_hangman
    draw_hangman = {
        0: """
            +---+
            |   |
                |
                |
                |
                |
            ========= 
        """,
        1: """
            +---+
            |   |
            O   |
                |
                |
                |
            ========= 
        """,
        2: """
            +---+
            |   |
            O   |
            |   |
                |
                |
            ========= 
        """,
        3: """ 
            +---+
            |   |
            O   |
           /|   |
                |
                |
            =========
        """,
        4: """ 
            +---+
            |   |
            O   |
           /|\  |
                |
                |
            =========
        """,
        5: """
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
            =========""",
        6: """
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
            =========""",
        7: """
            +---+
            |   |
           \O/  |
            |   |
           / \  |
                |
            =========""",
        8: """
            +---+
            |   |            
            |   |
            O   |
           /|\ =====
           / \  """,
        
    }
    print(draw_hangman[count])


def play (newword, word_hide,word):
    
    cont = 0
    while cont <= 8:
        letter=input("Ingrese una letra: ")
        try:
            letter=letter.upper()
            if letter in newword:
                print("Correcto")
                for i in range (len(newword)):
                    if newword[i]==letter:
                        os.system('cls')
                        word_hide[i]=letter
                print("".join(word_hide))
                if "_" in word_hide:
                    draw_hangman(cont)
                    print("Continua")
                if "_" not in word_hide:
                    print("Ganaste!")
                    draw_hangman(cont)
                    print("".join(word_hide),"La palabra era: ", word)
                    cont = 0
                    break
            else:
                os.system('cls')
                print("".join(word_hide))
                print("Incorrecto")
                cont += 1
                draw_hangman(cont)
                if cont == 8:
                    os.system('cls')
                    print("Perdiste!")
                    draw_hangman(cont)
                    print("".join(word_hide),"La palabra era: ", word)
                    break
        except ValueError:
            print("Debe ingresar una letra")


def run ():
    os.system('cls')
    head()
    word=read_file() #Read the file and get a random word
    newword=normalize(word) #Normalize the word
    word_hide=hide_word(newword) #Hide the word
    play(newword, word_hide,word) #Play the game

if __name__=='__main__':
    run()