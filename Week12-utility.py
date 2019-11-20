#https://github.com/apitcock-csci/WEEK12-git.git
#Anna Pitcock
#CSCI - 102
#Week12 - Part B

#Function 1
def PrintOutput(string_to_output):
    print(string_to_output)

def LoadFile(input_string):
    with open(input_string, 'r') as file:
        read_file = file.readlines()
        print(read_file)
