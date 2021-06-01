import re


def regex_check(file_name):
    if re.search("[.<>:\"/|?*\\\\\040]", file_name):
        return "Invalid file name - illegal character(s)(. < > : \" / \\ | ? * )"
    if file_name == "":
        return "Invalid file name - can't be blank"
    return "No Error"

loop = ""
while loop == "":
    user_input = input("enter a filename without a extension: ")
    output = regex_check(user_input)
    print(output)