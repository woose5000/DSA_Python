from stack import Stack

string_array = Stack(100)    
msg = input("Write your string")
for str in msg:
    string_array.push(str)