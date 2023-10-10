import random
def hangman():
    word_list=["chips","kurkure","burger","colddrink"]
    word=random.choice(word_list)
    turns=10
    guessmade=''
    valid_entry=set('abcdefghijklmnopqrstuvwxyz')

    while turns>=0:
        main_word = ""
        print("guess the word:")
        guess = input()

        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print("enter a valid character ")
            guess=input()


        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_"

        if main_word==word:
            print(main_word)
            print("you won!")
            break


        if guess not in word:
            turns=turns-1

            if turns==9:
                print("9 turns left!!")
                print("---------------")
            if turns==8:
                print("8 turns left!!")
                print("---------------")
                print("      o        ")
            if turns==7:
                print("7 turns left!!")
                print("---------------")
                print("      o        ")
                print("      |        ")
            if turns==6:
                print("6 turns left!!")
                print("---------------")
                print("      o        ")
                print("      |        ")
                print("     /         ")
            if turns==5:
                print("5 turns left!!")
                print("---------------")
                print("      o        ")
                print("      |        ")
                print("     / \       ")
            if turns==4:
                print("4 turns left!!")
                print("---------------")
                print("     \o        ")
                print("      |        ")
                print("     / \       ")
            if turns==3:
                print("3 turns left!!")
                print("---------------")
                print("     \o/        ")
                print("      |        ")
                print("     / \       ")
            if turns==2:
                print("2 turns left!!")
                print("---------------")
                print("     \o/ |      ")
                print("      |        ")
                print("     / \       ")

            if turns == 1:
                print("1 turns left!!")
                print("---------------")
                print("      o_|      ")
                print("     /|\       ")
                print("     / \       ")
            if turns==0:
                print("you loose")
                print("hangman died")
                break

name = input("Enter your name:")
print("Welcome",name,"!")
print("----------------------")
print("try to guess the word in less than 10 seconds")
hangman()