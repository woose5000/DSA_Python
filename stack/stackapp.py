# 문자열 거꾸로 뒤집기, 괄호 검사 프로그램
from stackcls import Stack 
import os

columns, _ = os.get_terminal_size()
divides = "=" * columns
print(divides)
user_input = input(f"원하시는 프로그램 번호를 입력해주세요. : ")
print(divides)

bracket_couple ={"]":"[","}":"{",")":"("}

if user_input in ['1','2']:
    if user_input == '1':
        print("Stack 자료형을 이용해 문자열을 거꾸로 뒤집는 프로그램입니다.")
        msg_1 = int(input("How many components do you want in your array: "))
        string_array = Stack(msg_1)    
        msg_2 = input("Write your string: ")
        for str in msg_2:
            string_array.push(str)

        print(string_array)

        while not string_array.isEmpty():
            print(string_array.pop(), end="")

    elif user_input == '2':
        print("괄호 검사 프로그램입니다.")
        raw_text = input("Text를 입력해주세요.")
        array_bracket = Stack(len(raw_text))
        for k in raw_text:
            if k in ["(","{","["]:
                array_bracket.push(k)
        for k in raw_text:  
            if k in [")","}","]"]:
                if array_bracket.isEmpty(): #오른쪽 괄호는 있는데 왼쪽이 아예 없는 경우 
                    print("오른쪽 괄호는 있으나 왼쪽 괄호가 존재하지 않습니다.")
                    break
                else:       
                    if array_bracket.peek() != bracket_couple[k]: #짝이 맞지 않는 경우 
                        print("오른쪽 괄호와 왼쪽 괄호의 짝이 맞지 않습니다")
                        break
                    else : 
                        array_bracket.pop()

        if not array_bracket.isEmpty(): # 오른쪽 괄호의 개수가 더 많은 경우 
            print("왼쪽 괄호가 닫히지 않았습니다")
            print(array_bracket)
        else :
            print("정상적인 bracket 쌍입니다.")
                            
                
else:
    print("\aWarning:TypeError")


