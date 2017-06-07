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
        print(grid[i],end=" ")
        print('(',i,')',end=" ")
    print('\n-------------')
def winCheck(grid):
    '''
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

    (result, X_O)=winCheck(grid)
    #print('Function returned: ',result, X_O)

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
    grid=['_']*9
    #print(grid)

    return grid

def entry(grid,i):
    
    if i%2==0:
        position=input('Enter Position for Player 1:')
        if int(position)>=9 or int(position)<0 :
            print('Warning: Input a position between 0 to 8:')
            position=input('Enter Position for Player 1:')

        if int(position)>=9 or int(position)<0 :
            print('Penalty for wrong input')
            return 0

        grid[int(position)]='X'
        return 1
        
    else:
        position=input('Enter Position for Player 2:')
        if int(position)>=9 or int(position)<0 :
            print('Warning: Input a position between 0 to 8:')
            position=input('Enter Position for Player 2:')

        if int(position)>=9 or int(position)<0 :
            print('Penalty for wrong input')
            return 0
        
        grid[int(position)]='O'
        return 1
    
def main():
    
    grid=initialiser()
    print('Player 1: X and Player 2: O\nEnter Numbers between 0 to 8 designating the entry position')

    i=0
    while declare_result(grid) and i<=9:
        
        showGrid(grid)
        fail=entry(grid,i)
        if fail==0:
            i+=1
            continue
        i+=1
         
main()
