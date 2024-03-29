#https://github.com/apitcock-csci/WEEK12-git.git
#Anna Pitcock
#CSCI - 102
#Week12 - Part B

#Function 1
def PrintOutput(string_to_output):
    print("OUTPUT", string_to_output)

#Function 2
def LoadFile(input_string):
    with open(input_string, 'r') as file:
        read_file = file.read().splitlines()
        print("OUTPUT", read_file)
        
#Function 3
#FIX ME
def UpdateString(string_1, new_letter, index_num):
    old_letter = string_1[index_num]
    string_1.replace(old_letter, new_letter)
    print(string_1)

#Funtion 4
def FindWordCount(input_list, input_string):
    occurances = 0
    for i in list:
        if i == input_string:
            occurances += 1
    print("OUTPUT", occurances)

#Function 5
def ScoreFinder(list_player_names, player_scores, player_name):
    yes = 0
    for i in range(len(list_player_names)):
        name = list_player_names[i]
        if name == player_name:
            score = player_scores[i]
            yes += 1
            print(f"OUTPUT {name} got a score of {score}")
    if yes == 0:
        print("OUTPUT player not found")

#Function 6
def Union(list1, list2):
    union_list = list1 + list2
    print("OUTPUT", union_list)

#Function 7
def Intersection(list1, list2):
    occurances = []
    for i in list1:
        for j in list2:
            if i == j:
                occurances.append(i)
    print(f"OUTPUT {occurances}")

#Function 8
def NotIn(list1, list2):
    output_list = []
    for a in list1:
        count = 0
        for b in list2:
            if a == b:
                 count += 1
        if count == 0:
            output_list.append(a)
    print(f"OUTPUT {output_list}")
