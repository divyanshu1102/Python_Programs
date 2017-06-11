import random

class Player:
    
    def __init__(self,name):
        self.name=name
        self.player_cards=[]
        self.score=0
        self.bet=0
        print(self.name+" has joined the game!")
        
    def __str__(self):
        return self.name

    def showScore(self):
        return self.score

    def getCards(self, card):
        self.player_cards.append(card)

    def getScore(self,score):
        self.score+=score
            
    def showCards(self):
        return self.player_cards

    def placeBet(self,bet):
        self.bet=bet

    def showBet(self):
        return self.bet
    
    def blackJack(self):
        if self.score==21:  # if score==21, blackjack 
            return 999
        
        elif self.score>21: # if score>21, dead=1 and player is dead
            return False
        
        elif self.score<21: # if score<21, continue game
            return True
    
class Dealer(Player):
    masterCards={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'K':10,'Q':10,'J':10}
    # A1: ace as 1, A11: ace as 11

    #availableCards=list(masterCards)*4
    score=0
    player_cards=[]
    bet=0
    
    def __init__(self,name='Dealer'):   
        Player.__init__(self,name)
        
    def __str__(self):
        return self.name

    def getMasterCards(self):
        return self.masterCards
    
    
dealer=Dealer()
availableCards=list(dealer.getMasterCards())*4*6

def gotAce():
    '''
    Function asks the user how to interpret an ACE
    Returns: Returns 1 or 11, according to user choice
    '''
    aceScore=0
    try:
        while True:
            aceScore=int(input('You got an Ace, count it as 1 or 11? (1 or 11): '))
            if aceScore==1 or aceScore==11:
                break
          
    except:
        print('Wrong Input!')
        while True:
            aceScore=int(input('You got an Ace, count it as 1 or 11? (1 or 11): '))
            if aceScore==1 or aceScore==11:
                break
            
    return aceScore 

def giveCard():
    '''
    Return: Returns a randomly selected Card String 
    '''
    sys_ran1= random.SystemRandom()
    card=sys_ran1.choice(availableCards)
    availableCards.remove(card)

    return card

def takeBet():
    try:
        bet=-2
        while True:
            bet=int(input('How much do you bet?: '))
            if bet>0:
                break
            
    except:
        print('Please Input an amount greater than 0')
        bet=-2
        while True:
            bet=int(input('How much do you bet?: '))
            if bet>0:
                break
    return bet

def startGame(countPlayers,players):
    '''
    Begins the game by giving 2 cards to the dealer and each player
    If any player or dealer achieves a score of 21, a Blackjack is declared and the game stops
    '''
    allBids=0
    
    card1=giveCard()
    card2=giveCard()
    
    dealer.getCards(card1)
    dealer.getCards(card2)

    print("\n")
    print(dealer,end=" ")
    money=takeBet()
    dealer.placeBet(money)
    allBids+=money


    print(dealer,'your cards are: ',dealer.showCards()) # comment this out
    print("One of Dealer's Cards is: ",card1)
    
#-------------
    #dealer = aceConditions(dealer,dealer)
    
    if card1=='A' and card2=='A':

        dealer.getScore(gotAce()+1) # no one will choose 11+11

    elif card1=='A' and card2!='A':
        
        dealer.getScore(gotAce()+dealer.getMasterCards()[str(card2)])

    elif card2=='A' and card1!='A':
        
        dealer.getScore(dealer.getMasterCards()[str(card1)]+ gotAce())

    else:
        dealer.getScore(dealer.getMasterCards()[str(card1)]+dealer.getMasterCards()[str(card2)])
    
#------------


    for i in range(countPlayers):
        card1=giveCard()
        card2=giveCard()

        print("\n")
        print(players[i],end=" ")

        money=takeBet()
        allBids+=money
        players[i].placeBet(money)
        
        players[i].getCards(card1)
        players[i].getCards(card2)

        print('Player:',players[i],'your cards are: ',players[i].showCards())

#-------------
        #players[i]= aceConditions(players[i],dealer)
        
        if card1=='A' and card2=='A':

            players[i].getScore(gotAce()+1) # no one would choose 11+11, obvious choice is 11+1

        elif card1=='A' and card2!='A':
    
            players[i].getScore(gotAce()+dealer.getMasterCards()[str(card2)])

        elif card1!='A' and card2=='A':
        
            players[i].getScore(dealer.getMasterCards()[str(card1)]+gotAce())
        
        else:
            players[i].getScore(dealer.getMasterCards()[str(card1)] + dealer.getMasterCards()[str(card2)])
        
#--------------

        print(players[i],"'s score: ",players[i].showScore())

    if dealer.blackJack()==999:
        print("Dealer's BlackJack!, Dealer keeps",allBids)
        return 1

    for i in range(countPlayers):
        if players[i].blackJack()==999:
            print(players[i],"won",allBids)
            return 1

    return allBids

def Driver():
    '''
    Main Driver of the Game. Initialises all Players Objects and takes in Players' informations
    Then all the players get 'hits' with new cards till they want.
    Followed by the dealer getting all the 'hits' that the dealer wants
    If any participant gets an Ace, the player is asked how to interpret it: 1 or 11.
    If the score of any participant = 21, a blackjack is declared
    If the score of any participant > 21, the player is declared Busted and can't win
    If no one gets a BlackJack, the player whose score is closest to 21, but smaller than 21 wins.
    If no one wins, a draw is declared
    
    '''
    players=[]

    try:
        players.append(Player(input("Player's Name: ")))
    except:
        print("Wrong Input. Please enter the player's name")
        players.append(Player(input("Player's Name: ")))

    
    try:
        more='K'
        while True:
            more=input('Add another Player?(Y/N): ')
            if more=='Y' or more=='N':
                break
        
    except:
        print('Please Input Y for Yes and N for No')
        more='K'
        while True:
            more=input('Add another Player?(Y/N): ')
            if more=='Y' or more=='N':
                break
        
    while more=='Y':
        
        players.append(Player(input("Player's Name: ")))  

        try:
            more='K'
            while True:
                more=input('Add another Player?(Y/N): ')
                if more=='Y' or more=='N':
                    break
            
        except:
            print('Please Input Y for Yes and N for No')
            more='K'
            while True:
                more=input('Add another Player?(Y/N): ')
                if more=='Y' or more=='N':
                    break

#---------------------------------
# game starts with each player and dealer getting 2 cards each

    allBids=startGame(len(players),players) 
    if allBids==1:
        return

    allScores=[None]*len(players)
    
#----------------------------------
# All Players get hits
    print("\n")
    for i in range(len(players)):
        print('Player:',players[i],end=" ")
        
        try:
            hit='K'
            while True:
                hit=input('Hit? (Y/N):')
                if hit=='Y' or hit=='N':
                    break
            
        except:
            print('Please Input Y for Yes and N for No')
            hit='K'
            while True:
                hit=input('Hit? (Y/N):')
                if hit=='Y' or hit=='N':
                    break
            
        while (hit=='Y' or hit=='y' ):

            card=giveCard()
            players[i].getCards(card)
            print('Player:',players[i],'your cards are: ',players[i].showCards())


            # 1. Check if Ace is in the player's deck
            # 2. make player's score=0, ask player how to interpret the first Ace
            # 3. Recalculate the player's score

            if 'A' in players[i].showCards():
                players[i].getScore(-players[i].showScore())

                for j in players[i].showCards():
                    if j=='A':
                        continue
                    else:
                        players[i].getScore(dealer.getMasterCards()[j])

                if players[i].showScore()+1>21:
                     print('Busted!')
                     break
                else:
                        #may need to add condition for multiple A here
                     players[i].getScore(gotAce())


            else:
                players[i].getScore(dealer.getMasterCards()[str(card)])

            print(players[i],"'s score: ",players[i].showScore())
            
            if players[i].blackJack()==0:
                print('Busted!')
                break
            
            if players[i].blackJack()==999:
                print(players[i],"'s BlackJack!")
                return
            
            try:
                hit='K'
                while True:
                    hit=input('Hit? (Y/N):')
                    if hit=='Y' or hit=='N':
                        break
                
            except:
                print('Please Input Y for Yes and N for No')
                hit='K'
                while True:
                    hit=input('Hit? (Y/N):')
                    if hit=='Y' or hit=='N':
                        break

        allScores[i]=players[i].showScore()
        #allBids+=players[i].showBet()
#------------------------------------------
#Dealer gets hits

    print('Time for Dealer to get hits!')
    try:
        hit='K'
        while True:
                hit=input('Hit? (Y/N):')
                if hit=='Y' or hit=='N':
                    break
        
    except:
        print('Please Input Y for Yes and N for No')
        hit='K'
        while True:
                hit=input('Hit? (Y/N):')
                if hit=='Y' or hit=='N':
                    break
        
    while hit=='Y' or hit=='y' :

        card=giveCard()
        dealer.getCards(card)
        print(dealer,'your cards are: ',dealer.showCards())
            
        if 'A' in dealer.showCards():
                dealer.getScore(-dealer.showScore())

                for j in dealer.showCards():
                    if j=='A':
                        continue
                    else:
                        dealer.getScore(dealer.getMasterCards()[j])

                if dealer.showScore()+1>21:
                     print('Busted!')
                     break
                else:
                        #may need to add condition for multiple A here
                     dealer.getScore(gotAce())
        else:
            dealer.getScore(dealer.getMasterCards()[str(card)])

        print(dealer,"'s score: ",dealer.showScore())
        
        if dealer.blackJack()==0:
            print('Busted!')
            break
        
        if dealer.blackJack()==999:
            print(dealer,"'s BlackJack!")
            return
        
        try:
            hit='K'
            while True:
                hit=input('Hit? (Y/N):')
                if hit=='Y' or hit=='N':
                    break
            
        except:
            print('Please Input Y for Yes and N for No')
            hit='K'
            while True:
                hit=input('Hit? (Y/N):')
                if hit=='Y' or hit=='N':
                    break

#-----------------------------------------
# All Cards are put on the Table

    print('Time to show all Cards...')    

    for i in range(len(players)):
        print(players[i],': ',allScores[i])

#-----------------------------------------
# Searching for the player whose score is closest to 21 and less than 21

    largest=-21
    result=-1

    for i in range(len(allScores)):     
        
        if allScores[i]-21>0:
            continue
        else:
            if largest<allScores[i]:
                largest=allScores[i]
                result=i
                
#----------------------------------------
# The winner is being determined

    if result==-1:
        if dealer.blackJack()==True:
            print("Dealer Won!",allBids)
        else:
            print("It's a Draw!")
    else:
        if allScores.count(players[result].showScore())>=2:
            if dealer.blackJack()==True and dealer.showScore()> players[result].showScore():
                print("Dealer Won!",allBids)

            else:
                print("It's a Draw!")
        else:
            print(players[result],'won',allBids)

Driver()

