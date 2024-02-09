file_object = open ("numbers.txt","r")
file_object2 = open("new_numbers.txt","w")
my_list = []
for line in file_object:
    print(line,end="")
    my_list.append(int(line.strip()))
print("")
print(my_list)

def max_min(my_list):
    max_value = my_list[0]
    min_value = my_list[0]
    for i in range (len(my_list)):
        if my_list[i]> max_value:
            max_value = my_list[i]
        elif my_list[i]< min_value:
            min_value = my_list[i]
    file_object2.write("min_value:" +str(min_value) + "max_value:"+ str(max_value))
max_min(my_list)
