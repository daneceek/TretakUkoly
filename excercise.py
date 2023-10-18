list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

for letter in sub_list:
    
    list1[2][1][2].append(letter)
print(list1)

list2 = [5, 10, 15, 20, 25, 50, 20]

for index, i  in enumerate(list2):
        if i == 20:
            
            list2[index] = 200
            break
        
print(list2)

            