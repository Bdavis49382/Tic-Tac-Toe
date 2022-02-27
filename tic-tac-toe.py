def main():

    x_turn = True

    response  = input('Welcome to Tic-Tac-Toe! Would you like to view the rules?(y or n)')

    if response == 'y':
        with open('CSE 210\\rules.txt') as source:
            for line in source.readlines():
                print(line)

    grid =create_grid()
    draw_grid(grid)
    while True:
        player_letter = 'X' if x_turn else 'O'
        move = input(f'Player {player_letter}, which space would you like to mark?(1-9)')
        if(move=='stop'):
            break
        grid[int(move)-1] = player_letter
        
        draw_grid(grid)

        if check_for_win(grid,player_letter):
            print(f'Player {player_letter} has won!')
            break

        

        x_turn= not x_turn
    

def create_grid():
    out = []
    for i in range(9):
        out.append(str(i+1))
    return out

def draw_grid(list):
    exit_string = ''
    for index in range(len(list)):
        if index%3==0:
            exit_string += '\n' + list[index]
        else:
            exit_string += '|' + list[index]
    print(exit_string)

def check_for_win(list,letter):
    condition=False
    #check for columns/rows
    for i in range(3):          
        if list[i]==letter and list[i+3]==letter and list[i+6]==letter:
            condition=True
        if list[i*3]==letter and list[(i*3)+1]==letter and list[(i*3)+2]==letter:
            condition=True
    
    #check for diagonals
    if list[0]==letter and list[4]==letter and list[8]==letter:
        condition=True

    if list[6]==letter and list[4]==letter and list[2]==letter:
        condition=True
    return condition

        
    

if __name__=='__main__':
    main()