import random

#declaring 2 example sequences
sequence1 = "ATCATGCGAT"
sequence2 = "GATCGATCGATCGA"

#n,m are the number of nucleotides on each sequence
n = len(sequence1)
m = len(sequence2)

#creating the dynamic programming table
dp_table = [[[] for _ in range(m)] for _ in range(n)]

#keep?
n_index = n - 1
m_index = m - 1

#initiallizing the dynamic programming table
#e.g. of a table 10x10
'''
   0 1 2 3 4 5 6 7 8 9 10
0  L W W W W W W W W W W
1  W W L L L L L L L L L
2  W L W L L L L L L L L
3  W L L W L L L L L L L
4  W L L L W L L L L L L
5  W L L L L W L L L L L
6  W L L L L L W L L L L
7  W L L L L L L W L L L
8  W L L L L L L L W L L
9  W L L L L L L L L W L
10 W L L L L L L L L L W
'''

for i in range(n):
    for j in range(m):
        if i == j:
            if i == 0 or j == 0:
                dp_table[i][j] = "L"
            else:
                dp_table[i][j] = "W"
        else:
            if i == 0 or j == 0:
                dp_table[i][j] = "W"
            else:
                dp_table[i][j] = "L"

#random int to decide which player is going to play first
turn = random.randint(1,2)

#loop ends when both sequences are empty (n == 0 and m == 0)
while ((n != 0) or (m!=0)):
    if (turn == 1): #if it is player1's turn...
        dice = random.randint(1, max(n, m)) #roll the dice (values from 1 to the max length of sequence1, sequence2)
        print("player 1 plays...")
        print("dice is" , dice)
        if (n < dice): #if sequence1 length < dice then we can only subtract nucleotides from sequence2
            turn+=1 #turn becomes 2
            m = m - dice
            m_index = m_index - dice
            print(dice , "nucleotides subtracted from sequence 2")
            print("number of nucleotides on sequence 1 :" , n)
            print("number of nucleotides on sequence 2 :" , m)
        elif (m < dice): #if sequence2 length < dice then we can only subtract nucleotides from sequence1
            turn+=1
            n = n - dice
            n_index = n_index - dice
            print(dice , "nucleotides subtracted from sequence 1")
            print("number of nucleotides on sequence 1 :" , n)
            print("number of nucleotides on sequence 2 :" , m)
        else: #if both sequences have length larger than the dice then decide on the movement based on the winning strategy
            if (dp_table[n_index-dice][m_index] == "L"): #checking horizontally
                turn+=1
                n = n - dice
                n_index = n_index - dice
                print(dice , "nucleotides subtracted from sequence 1")
                print("number of nucleotides on sequence 1 :" , n)
                print("number of nucleotides on sequence 2 :" , m)
            elif (dp_table[n_index][m_index-dice] == "L"): #checking vertically
                turn+=1
                m = m - dice
                m_index = m_index - dice
                print(dice , "nucleotides subtracted from sequence 2")
                print("number of nucleotides on sequence 1 :" , n)
                print("number of nucleotides on sequence 2 :" , m)
            elif (dp_table[n_index-dice][m_index-dice] == "L"): #checking diagonally
                turn+=1
                n = n - dice
                n_index = n_index - dice
                m = m - dice
                m_index = m_index - dice
                print(dice , "nucleotides subtracted from sequence 1")
                print(dice , "nucleotides subtracted from sequence 2")
                print("number of nucleotides on sequence 1 :" , n)
                print("number of nucleotides on sequence 2 :" , m)
            else: #if all the cells have the value "W"
                turn+=1
                n = n - dice #then by default subtract nucleotides from sequence1
                n_index = n_index - dice 
                print(dice , "nucleotides subtracted from sequence 1")
                print("number of nucleotides on sequence 1 :" , n)
                print("number of nucleotides on sequence 2 :" , m)
    else: #if it is player2's turn...
        dice = random.randint(1, max(n, m))
        print("player 2 plays...")
        print("dice is" , dice)
        if (n < dice): #if sequence1 length < dice then we can only subtract nucleotides from sequence2
            turn-=1 #turn becomes 1
            m = m - dice
            m_index = m_index - dice
            print(dice , "nucleotides subtracted from sequence 2")
            print("number of nucleotides on sequence 1 :" , n)
            print("number of nucleotides on sequence 2 :" , m)
        elif (m < dice): #if sequence2 length < dice then we can only subtract nucleotides from sequence1
            turn-=1
            n = n - dice
            n_index = n_index - dice
            print(dice , "nucleotides subtracted from sequence 1")
            print("number of nucleotides on sequence 1 :" , n)
            print("number of nucleotides on sequence 2 :" , m)
        else: #if both sequences have length larger than the dice then decide on the movement with a random int
            movement = random.randint(1, 3) # 1 => horizontally, 2 => vertically, 3 => diagonally
            if (movement == 1):   
                turn-=1
                n = n - dice
                n_index = n_index - dice
                print(dice , "nucleotides subtracted from sequence 1")
                print("number of nucleotides on sequence 1 :" , n)
                print("number of nucleotides on sequence 2 :" , m)
            elif (movement == 2):
                turn-=1
                m = m - dice
                m_index = m_index - dice 
                print(dice , "nucleotides subtracted from sequence 2")
                print("number of nucleotides on sequence 1 :" , n)
                print("number of nucleotides on sequence 2 :" , m)
            else:
                turn-=1
                n = n - dice
                n_index = n_index - dice
                m = m - dice
                m_index = m_index - dice
                print(dice , "nucleotides subtracted from sequence 1")
                print(dice , "nucleotides subtracted from sequence 2")
                print("number of nucleotides on sequence 1 :" , n)
                print("number of nucleotides on sequence 2 :" , m)

'''
because after each movement we change the value of turn
we can't say that when the turn is 1 player1 has one
it is the exact opposite
if turn == 2 then player1 won
elif turn == 1 then player2 won
we also have to check that both the values of n,m are 0 
because only then the game is finished
'''
    if (turn == 2 and n == 0 and m == 0): 
        print("player 1 wins!")
    elif(turn == 1 and n == 0 and m == 0):
        print("player 2 wins!")
            

