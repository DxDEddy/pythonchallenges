#INPUTS
#Integer - N - between 1 and 50 - this is the number of matches on the floor                                            int_numberofmatches
#Integer - W - between 1 and 100 - this is the width of the box                                                         int_widthofbox
#Integer - H - between 1 and 100 - this is the height of the box                                                        int_heightofbox
#Integer - W - between - this is the integer that is used to
#Integer - X - between 1 and 1000 - this is the length of match N and there must be N values                            arr_matchlength
#Integer - Y - between 0 and N - this is the incrementor that will go through and check if it will fit                  int_incrementor
#Integer - Z - between 0 and N - this is the incrementor that will check if the max amount of values has been met yey   int_inputincrementor


#A match can fit in the box if it's entire length can lay down in the bottom of the box
#For each match, in the order they were given, output whether they can fir or not
#Take the first value and keep comparing the length of an array to it
#append each of the matches to an array where they will be in order and they can be incremented through
#Output with a newline that shows whether it will fit or not


int_numberofmatches = 1
int_widthofbox = 1
int_heightofbox = 1
arr_matchlength = ()
int_incrementor = 0
int_inputincrementor = 0

###

print("Enter: Num of matches, width of box and height of box")
int_numberofmatches, int_widthofbox, int_heightofbox = input().split()

int_numberofmatches = int(int_numberofmatches)
int_widthofbox = int(int_widthofbox)
int_heightofbox = int(int_heightofbox)
arr_matchlength = list(arr_matchlength)
int_inputincrementor = int(int_inputincrementor)
int_incrementor = int_incrementor

print("this is num of matches: %s" % int_numberofmatches)
print("this is the width of box: %s" % int_widthofbox)
print("this is the height of the box: %s" % int_heightofbox)

### prep for match value gathering



###
while int_inputincrementor<int_numberofmatches: #This works and gets me loops equal to int_numberofmatches
    print("Please enter %i values that represent the length of a match: " % int_numberofmatches)
    int_transferinc = input()
    int_transferinc = int(int_transferinc)
    arr_matchlength.append(int_transferinc)
    print("Transferinc has been changed to: %i" % int_transferinc)
    print(arr_matchlength[int_inputincrementor])
    int_inputincrementor = int_inputincrementor + 1
    print("This is the list now: %s" % arr_matchlength)