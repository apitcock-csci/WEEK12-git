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
