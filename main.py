import random
import tkinter
from tkinter.font import BOLD



def choose_game():
    game_choice = input("Which game would you like to play tic-tac-toe, Hangman or BlackJack? ")
    if game_choice.lower() == "tic-tac-toe":
        tic_tac_toe()
    elif game_choice.lower() == "hangman":
        hangman()
    elif game_choice.lower() == "BlackJack":
        BlackJack()    



def tic_tac_toe():
    board = ["-", "-", "-", 
             "-", "-", "-", 
             "-", "-", "-"]
    player = "X"
    game_over = False
    def print_board():
        print(board[0] + " | " + board[1] + " | " + board[2])
        print(board[3] + " | " + board[4] + " | " + board[5])
        print(board[6] + " | " + board[7] + " | " + board[8])

    def play_game():
        nonlocal game_over, player
        print_board()

        while not game_over:
            if player == "X":
                move = int(input("Enter a position (1-9): ")) - 1
                if board[move] == "-":
                    board[move] = "X"
                    player = "O"
                else:
                    print("That position is already taken. Try again.")
            else:
                print("Computer's turn.")
                move = simple_ai()
                board[move] = "O"
                player = "X"
            print_board()
            check_game_over()

    def check_game_over():
        nonlocal game_over
        if check_win():
            game_over = True
            print(player + " won!")
        elif check_tie():
            game_over = True
            print("It's a tie!")

    def check_win():
        nonlocal player
        if board[0] == player and board[1] == player and board[2] == player:
            return True
        elif board[3] == player and board[4] == player and board[5] == player:
            return True
        elif board[6] == player and board[7] == player and board[8] == player:
            return True
        elif board[0] == player and board[3] == player and board[6] == player:
            return True
        elif board[1] == player and board[4] == player and board[7] == player:
            return True
        elif board[2] == player and board[5] == player and board[8] == player:
            return True
        elif board[0] == player and board[4] == player and board[8] == player:
            return True
        elif board[2] == player and board[4] == player and board[6] == player:
            return True
        else:
            return False

    def check_tie():
        if "-" not in board:
            return True
        else:
            return False

    def simple_ai():
        possible_moves = []
        for i in range(len(board)):
            if board[i] == "-":
                possible_moves.append(i)
        return random.choice(possible_moves)

    play_game()

def hangman():
    words = ["python", "java", "javascript", "ruby", "php"]
    word = random.choice(words)
    guessed_letters = []
    tries = 5
    game_over = False
    stage = 0
    
    def print_word():
        for letter in word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()

    def play_game():
        nonlocal game_over, tries, stage
        print("Welcome to Hangman!")
        print_word()

        while not game_over:
            if len(guessed_letters) == len(set(word)):
                game_over = True
                print("Congratulations, you won!")
                break

            guess = input("Guess a letter: ").lower()
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word:
                guessed_letters.append(guess)
                print_word()
            else:
                print("Wrong letter!")
                stage +=1
                draw_hangman()
                tries -= 1
                print(f"You have {tries} tries left.")
                if tries == 0:
                    game_over = True
                    print(f"Game over! The word was {word}.")
                    break

            print("AI's turn...")
            ai_guess = simple_ai()
            if ai_guess in guessed_letters:
                print("AI already guessed that letter. Try again.")
            elif ai_guess in word:
                guessed_letters.append(ai_guess)
                print(f"AI guessed {ai_guess}.")
                print_word()
            else:
                print(f"AI guessed {ai_guess}. Wrong letter!")
                stage += 1
                draw_hangman()
                tries -= 1
                print(f"You have {tries} tries left.")
                if tries == 0:
                    game_over = True
                    print(f"Game over! The word was {word}.")
                    break

    def simple_ai():
        possible_letters = []
        for letter in "abcdefghijklmnopqrstuvwxyz":
            if letter not in guessed_letters:
                possible_letters.append(letter)
        return random.choice(possible_letters)
        
    def draw_hangman():

        if stage == 1:
            firststage()
        elif stage == 2:
            secondstage()
        elif stage == 3:
            thirdstage()
        elif stage == 4:
            fourthstage()
        elif stage == 5:
            fifthstage()

    def firststage():
        print("  +---+\n")
        print("      |\n")
        print("      |\n")
        print("      |\n")
        print("      |\n")
        print("      |\n")
        print("=====\n")

    def secondstage():
        print("  +---+\n")
        print("  O   |\n")
        print("      |\n")
        print("      |\n")
        print("      |\n")
        print("      |\n")
        print("=====\n")

    def thirdstage():
        print("   +---+\n")
        print("   O   |\n")
        print("   |   |\n")
        print("       |\n")
        print("       |\n")
        print("       |\n")
        print("=====\n")

    def fourthstage():
        print("   +---+\n")
        print("   O   |\n")
        print("  -|-  |\n")
        print("       |\n")
        print("       |\n")
        print("       |\n")
        print("=====\n")

    def fifthstage():
        print("   +---+\n")
        print("   O   |\n")
        print("  -|-  |\n")
        print("  / \  |\n")
        print("       |\n")
        print("       |\n")
        print("=====\n")

    play_game()          

def blackjack():
    gameWindow = tkinter.Tk()
    # Set up the screen and frames for the dealer and player
    gameWindow.title("DataFlair Black Jack")
    gameWindow.geometry("640x480")

    tkinter.Label(gameWindow, text='DataFlair Black Jack',
          fg='black', font=('Courier', 20,BOLD)).place(x=150, y=10)
    winner=tkinter.StringVar()
    result = tkinter.Label(gameWindow, textvariable=winner,fg='black',font=('Courier', 15))
    result.place(x=250,y=50)
    dealerScore = tkinter.IntVar()
    tkinter.Label(gameWindow, text="Dealer Score:", fg="black",bg="white").place(x=10,y=80)
    tkinter.Label(gameWindow, textvariable=dealerScore, fg="black",bg="white").place(x=10,y=100)
    # embedded frame to hold the card images
    dealer_cardFrame = tkinter.Frame(gameWindow, bg="black")
    dealer_cardFrame.place(x=100,y=80)
    playerScore = tkinter.IntVar()
    tkinter.Label(gameWindow, text="Player Score:", fg="black",bg="white").place(x=10,y=200)
    tkinter.Label(gameWindow, textvariable=playerScore,fg="black",bg="white").place(x=10,y=220)
    # embedded frame to hold the card images
    player_card_frame = tkinter.Frame(gameWindow, bg="black")
    player_card_frame.place(x=100,y=200)
    player_button = tkinter.Button(gameWindow, text="Hit", command=hitting, padx=8)
    player_button.place(x=50,y=350)
    dealer_button = tkinter.Button(gameWindow, text="Stay", command=staying, padx=5)
    dealer_button.place(x=150,y=350)
    reset_button = tkinter.Button(gameWindow, text="New Game", command=new_game)
    reset_button.place(x=250,y=350)
    shuffle_button = tkinter.Button(gameWindow, text="Shuffle", command=shuffle, padx=2)
    shuffle_button.place(x=380,y=350)

    # function for retrieving the images of the cards from device
def getCardImages(card_images):
       suits = ['heart', 'club', 'diamond', 'spade']
       faceCards = ['jack', 'queen', 'king']
       ext= 'png'
        for suit in suits:
           # adding the number cards 1 to 10
           for card in range(1, 11):
               path= 'C:/Users/DELL/Downloads/cards/{}_{}.{}'.format(str(card), suit, ext)
               image = tkinter.PhotoImage(file=path)
               card_images.append((card, image, ))
            # adding the face cards
           for card in faceCards:
                path= 'C:/Users/DELL/Downloads/cards/{}_{}.{}'.format(str(card), suit, ext)
                image = tkinter.PhotoImage(file=path)
                card_images.append((10, image, ))

def getCard(frame):
        # pop the card on the top of the deck
        next_card = deck.pop(0)
       # and add it to the deck at the end
       deck.append(next_card)
       # show the image to a label
       tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
       # return the card
       return next_card

# Function to calculate the total score of all cards in the list
def calcScore(hand):
       score = 0
       ace = False
        for next_card in hand:
            card_value = next_card[0]
            # Ace is considered as 11 only once and rest of the time it is taken as 1
            if card_value == 1 and not ace:
               ace = True
               card_value = 11
        score += card_value
        # if its a bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score

#Show the winner when the player stays
def staying():
    dealer_score = calcScore(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(getCard(dealer_cardFrame))
        dealer_score = calcScore(dealer_hand)
        dealerScore.set(dealer_score)
    player_score = calcScore(player_hand)
    if player_score > 21 or dealer_score > player_score:
        winner.set("Dealer wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        winner.set("Player wins!")
    else:
        winner.set("Draw!")
#Show the winner when the player hits
def hitting():
    player_hand.append(getCard(player_card_frame))
    player_score = calcScore(player_hand)
    playerScore.set(player_score)
    if player_score > 21:
        winner.set("Dealer Wins!")
        
def initial_deal():
    hitting()
    dealer_hand.append(getCard(dealer_cardFrame))
    dealerScore.set(calcScore(dealer_hand))
    hitting()
def new_game():
    global dealer_cardFrame
    global player_card_frame
    global dealer_hand
    global player_hand
    # embedded frame to hold the card images
    dealer_cardFrame.destroy()
    dealer_cardFrame = tkinter.Frame(gameWindow, bg="black")
    dealer_cardFrame.place(x=100,y=80)
   
    # embedded frame to hold the card images
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(gameWindow, bg="black")
    player_card_frame.place(x=100,y=200)
    winner.set("")
    # Create the list to store the dealer's and player's hands
    dealer_hand = []
    player_hand = []
    initial_deal()
def shuffle():
    random.shuffle(deck)
    
    # load cards
    cards = []
    deck = list(cards) + list(cards) + list(cards)
    shuffle()
     # Create the list to store the dealer's and player's hands
     dealer_hand = []
     player_hand = []
     getCardImages(cards)
     initial_deal()
     gameWindow.mainloop()    

choose_game()
