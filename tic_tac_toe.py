'''
Player 1: X
Player 2: O
'''

def showGrid(grid):
    '''
    Input: grid, a list of players' inputs
    Output: prints the inputs in a 3x3 matrix
    Return: void
    '''
    for i in range(len(grid)):
        if i%3==0 and i!=0:
            print()
        print(grid[i],end="|")
        print(i,end=" ")
    print('\n-------------')
    
def winCheck(grid):
    '''
    Input: grid, list of user's entries
    Checks for a 'win' situation
    Return:(True, character that won) if there is a win situation
           (False,character that won) if there is no win situation
    '''
    
    if grid[0]!='_' and (grid[0]==grid[1]==grid[2] or grid[0]==grid[4]==grid[8] or grid[0]==grid[3]==grid[6]):
        return (True, grid[0])

    elif grid[1]!='_'  and (grid[1]==grid[4]==grid[7]):
        return (True,grid[1])

    elif grid[2]!='_' and (grid[2]==grid[4]==grid[6] or grid[2]==grid[5]==grid[8]):
        return (True, grid[2])

    elif grid[3]!='_'  and (grid[3]==grid[4]==grid[5]):
        return (True, grid[3])
    
    elif grid[6]!='_' and (grid[6]==grid[7]==grid[8]):
        return (True, grid[6])

    else:
        return (False, None)

def declare_result(grid):

    '''
    Input: grid, list of user's entries
    Checks whether input loop should continue or not
    Return: False, if the input loop should stop
            True, if input loops should continue
    '''
    
    (result, X_O)=winCheck(grid)

    if result:
        if X_O=='X':
            showGrid(grid)
            print('\nPlayer 1 won')
            return False
        
        elif X_O=='O':
            showGrid(grid)
            print('\nPlayer 2 won')
            return False
        
    elif '_' not in grid:
        showGrid(grid)
        print('\nDraw!')
        return False

    elif not result and ('_' in grid):
        #print('\nNo results yet')
        return True
    
def initialiser():
    '''
    Initialises a list of 9 elements
    Returns: grid, a list of 9 elements
    '''
    grid=['_']*9

    return grid

def entry(grid,i):
    '''
    Input: grid, list of user's entries
           i, number of input
    Return: 0, if user enters wrong input after warning
            1, if there was a correct input
    '''

    try:
        
        if i%2==0:
            position=int(input('Enter Position for Player 1:'))

            if 0<=position<=8 :
                if grid[position]=='_':
                    grid[position]='X'
                    return 1
                else:
                    print('Penalty for wrong input, Enter numbers between 0-8')
                    return 0
            else:
                 print('Penalty for wrong input, Enter numbers between 0-8')
                 return 0
        else:
            position=int(input('Enter Position for Player 2:'))

            if 0<=position<=8 :
                if grid[int(position)]=='_':
                    grid[position]='O'
                    return 1
                else:
                    print('Penalty for wrong input, Enter numbers between 0-8')
                    return 0
            else:
                 print('Penalty for wrong input, Enter numbers between 0-8')
                 return 0

        
    except ValueError:
            print("Penalty for wrong input, Enter numbers between 0-8")
            return 0

    return 0

    
def main():
    '''
    Main Driver loop for the game
    '''
    grid=initialiser()
    print('Player 1: X and Player 2: O\nEnter Numbers between 0 to 8 designating the entry position')

    i=0
    while declare_result(grid) and i<=9:
        
        showGrid(grid)
        fail=entry(grid,i)
        if fail==0:
            continue
        i+=1
         
main()
