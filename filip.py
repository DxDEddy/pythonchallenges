query = input()

array = query.split(" ")

int_inp1 = array[0]
int_inp2 = array[1]



int_inp1 = int_inp1[::-1]
int_inp2 = int_inp2[::-1]
if int_inp1 > int_inp2:
    print(int_inp1)
else:
    print(int_inp2)