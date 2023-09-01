import random

#declaring 2 example sequences
sequence2 = "ATCATGCAT"
sequence1 = "GATCGATCGACGA"

#n,m are the number of nucleotides on each sequence
n = len(sequence1)
m = len(sequence2)
#creating the dynamic programming table
dp_table = [[[] for _ in range(m)] for _ in range(n)]


#initiallizing the dynamic programming table
#e.g. of a table 8x7
'''
  0 1 2 3 4 5 6 7 
0 W W W W W W W W 
2 W W L L L L L L 
3 W L L L W W W W 
4 W L L W W W W W 
5 W L W W W L L L 
6 W L W W L L L W 
7 W L W W L L W W 
8 W L W W L W W W 
'''
for i in range(n):
    for j in range(m):
        dp_table[i][j] = "W"

for i in range(n):
    for j in range(m):
        if ((i == 1) or (j == 1)) and (i!= j):
            dp_table[i][j] = "L"

i = 1
j = 1

def apply_procedure(dp_table, i, j):
    for repeats in range (4):
        if repeats == 1:
            dp_table[i + 1][j] = "L"
            dp_table[i + 2][j] = "L"
            dp_table[i + 3][j] = "L"
        elif repeats == 2:
            dp_table[i][j + 1] = "L"
            dp_table[i + 1][j + 1] = "L"
            dp_table[i + 2][j + 1] = "L"
        elif repeats == 3:
            dp_table[i][j + 2] = "L"
            dp_table[i + 1][j + 2] = "L"
        elif repeats == 4:
            dp_table[i][j + 3] = "L"

while (i < (max(n,m) - 3)):
    if (n < m):
        if ((i - n) < 3):
            for repeats in range (4):
                if repeats == 1:
                    dp_table[i + 1][j] = "L"
                elif repeats == 2:
                    dp_table[i][j + 1] = "L"
                    dp_table[i + 1][j + 1] = "L"
                elif repeats == 3:
                    dp_table[i][j + 2] = "L"
                    dp_table[i + 1][j + 2] = "L"
                elif repeats == 4:
                    dp_table[i][j + 3] = "L"
        else:
            apply_procedure(dp_table, i, j)
    
    elif (m < n):
        if((j - m) < 3):
            for repeats in range (2):
                if repeats == 1:
                    dp_table[i + 1][j] = "L"
                    dp_table[i + 2][j] = "L"
                    dp_table[i + 3][j] = "L"
                elif repeats == 2:
                    dp_table[i][j + 1] = "L"
                    dp_table[i + 1][j + 1] = "L"
                    dp_table[i + 2][j + 1] = "L"
        else:
            apply_procedure(dp_table, i, j)
    else:
        for repeats in range (4):
            if repeats == 1:
                dp_table[i + 1][j] = "L"
                dp_table[i + 2][j] = "L"
                dp_table[i + 3][j] = "L"
            elif repeats == 2:
                dp_table[i][j + 1] = "L"
                dp_table[i + 1][j + 1] = "L"
                dp_table[i + 2][j + 1] = "L"
            elif repeats == 3:
                dp_table[i][j + 2] = "L"
                dp_table[i + 1][j + 2] = "L"
            elif repeats == 4:
                dp_table[i][j + 3] = "L"
    
    i += 3
    j += 3

#intiallizing end_game var
end_game = 0

#random int to decide which player is going to play first
turn = random.randint(1,2)

#loop ends when end_game becomes 1
while (end_game == 0):
    if (turn == 1): #if it is player1's turn...
        print("player 1 plays...")

        if (n < 2  and m < 2) or ( n == 0) or (m == 0): #if both sequences have length less than 2 OR one of the sequences is empty
            turn += 1 #turn becomes 2
            end_game = 1 #the are are no other movements available and the game ends
        elif (n < 2): #if sequence1 length < 2 then we can only subtract 2 nucleotides from sequence2 and 1 from sequence1
            turn+=1 
            n = n - 1
            m = m - 2
            print(" 1 nucleotides subtracted from sequence 1")
            print(" 2 nucleotides subtracted from sequence 2")
            print("number of nucleotides on sequence 1 :" , n)
            print("number of nucleotides on sequence 2 :" , m)
        elif (m < 2): #if sequence2 length < 2 then we can only subtract 2 nucleotides from sequence1 and 1 from sequence2
            turn+=1
            n = n - 2
            m = m - 1
            print(" 2 nucleotides subtracted from sequence 1")
            print(" 1 nucleotides subtracted from sequence 2")
            print("number of nucleotides on sequence 1 :" , n)
            print("number of nucleotides on sequence 2 :" , m)  
        else: #if both sequences are larger than 2 then decide on the movement based on the winning strategy
            if (dp_table[n - 2][m - 1] == "L"): #checking vertically
                turn+=1
                n = n - 2
                m = m - 1
                print(" 2 nucleotides subtracted from sequence 1")
                print(" 1 nucleotides subtracted from sequence 2")
                print("number of nucleotides on sequence 1 :" , n)
                print("number of nucleotides on sequence 2 :" , m)
            elif (dp_table[n - 1][m - 2] == "L"): #checking horizontally
                turn+=1
                n = n - 1
                m = m - 2
                print(" 1 nucleotides subtracted from sequence 1")
                print(" 2 nucleotides subtracted from sequence 2")
                print("number of nucleotides on sequence 1 :" , n)
                print("number of nucleotides on sequence 2 :" , m)
            else: #if all the cells have the value "W"
                turn+=1
                n = n - 2 #then by default subtract  2 nucleotides from sequence1
                m = m - 1 #and  1 nucleotide from sequence2
                print(" 2 nucleotides subtracted from sequence 1")
                print(" 1 nucleotides subtracted from sequence 2")
                print("number of nucleotides on sequence 1 :" , n)
                print("number of nucleotides on sequence 2 :" , m)
    else: #if it is player2's turn...
        print("player 2 plays...")

        if ((n < 2  and m < 2) or ( n == 0) or (m == 0)): #if both sequences have length less than 2 OR one of the sequences is empty
            turn -= 1 #turn becomes 1
            end_game = 1
        elif (n < 2): #if sequence1 length < 2 then we can only subtract 2 nucleotides from sequence2 and 1 from sequence1
            turn-=1
            n = n - 1
            m = m - 2
            print(" 1 nucleotides subtracted from sequence 1")
            print(" 2 nucleotides subtracted from sequence 2")
            print("number of nucleotides on sequence 1 :" , n)
            print("number of nucleotides on sequence 2 :" , m)
        elif (m < 2): #if sequence2 length < 2 then we can only subtract 2 nucleotides from sequence1 and 1 from sequence2
            turn-=1
            n = n - 2
            m = m - 1
            print(" 2 nucleotides subtracted from sequence 1")
            print(" 1 nucleotides subtracted from sequence 2")
            print("number of nucleotides on sequence 1 :" , n)
            print("number of nucleotides on sequence 2 :" , m)  
        else: #if both sequences are larger than 2 then decide on the movement randomly
            movement = random.randint(1, 2) # 1 => horizontally, 2 => vertically
            if (movement == 1):   
                turn-=1
                n = n - 2
                m = m - 1
                print(" 2 nucleotides subtracted from sequence 1")
                print(" 1 nucleotides subtracted from sequence 2")
                print("number of nucleotides on sequence 1 :" , n)
                print("number of nucleotides on sequence 2 :" , m)
            elif (movement == 2):
                turn-=1
                n = n - 1
                m = m - 2
                print(" 1 nucleotides subtracted from sequence 1")
                print(" 2 nucleotides subtracted from sequence 2")
                print("number of nucleotides on sequence 1 :" , n)
                print("number of nucleotides on sequence 2 :" , m)

'''
again
if turn == 2 then player1 won
elif turn == 1 then player2 won
'''
if (turn == 2):
    print("player 1 wins!")
elif(turn == 1):
    print("player 2 wins!")
