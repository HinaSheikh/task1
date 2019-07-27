number_list=[1, 2,  0]
if number_list!=[]:
    smallest=number_list[0] 
    for index in range(len(number_list)):
            if(number_list[index]<smallest ):
                smallest=number_list[index]
    print("The smallest number in list is",smallest)           