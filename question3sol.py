num_list=""
for number in range(1500,2701):
    if number%7==0 and number%5==0:
        num_list=num_list+" "+str(number)
print(num_list)