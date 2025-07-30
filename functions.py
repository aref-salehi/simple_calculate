def add(num1 , num2 ) :
    return num1+num2

def subtract(num1 , num2 ) :
    return num1-num2

def multiply(num1 , num2 ) :
    return num1*num2

def divide(num1 , num2 ) :
    answer = num1 / num2 
    if num2 == 0 :
        return ("Undefined")
    else:
        return answer

def integer_division(num1 , num2 ) :
    return num1/num2

def modulo(num1 , num2 ) :
    return num1%num2

def power(num1 , num2 ) :
    return num1**num2

def square_root(num1 , num2 ) :
    num2 = 1 / num2
    if num1 >= 0 :
        return num1**0.5
    
def factorial(num1 ) :
    if num1 == 0 or num1 == 1 :
        return 1
    return num1*factorial(num1 - 1) 



