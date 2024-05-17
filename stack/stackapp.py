from stackcls import Stack

msg_1 = int(input("How many components do you want in your array: "))
string_array = Stack(100)    
msg_2 = input("Write your string: ")
for str in msg_2:
    string_array.push(str)

print(string_array)

while not string_array.isEmpty():
    print(string_array.pop(), end="")

