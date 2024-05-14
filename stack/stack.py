# Class Stack 
# 파이썬 클래스로 스택 자료형 구현
class Stack:
    def __init__(self,cap:int=1):
        try:
            if isinstance(cap, int) and cap >= 1:
                self.array = [None]*cap
                self.cap = cap
                self.__top = -1
            else :
                raise TypeError("The first arugment must be an integer greater than or equal to 1.")

        except TypeError as Error_1:
            print(f"{Error_1}")
    
    def __str__(self):
        return str(self.array)

    def isEmpty(self):
        if self.__top == -1:
            return True
        else:
            return False

    def isFull(self):
        return self.__top == (self.cap -1)
    
    def push(self,comp):
        if not self.isFull():
            self.__top += 1
            self.array[self.__top] = comp
        else :
            print("stack overflow")
            exit()
    
    def pop(self):
        if not self.isEmpty():
            self.__pop_value = self.array[self.__top]
            self.array[self.__top] = None
            self.__top -= 1
            return self.__pop_value            
            
        else:
            print("stack underflow")
            exit()
     
    def peek(self):
        if not self.isEmpty():
            return self.array[self.__top]
        else : pass
   
