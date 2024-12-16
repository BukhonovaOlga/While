my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7 , -6, 5]

my_list_index = 0

while my_list[my_list_index] >= 0 and my_list_index < len(my_list):
    if my_list[my_list_index] > 0:
        print(my_list[my_list_index])
    my_list_index = my_list_index + 1