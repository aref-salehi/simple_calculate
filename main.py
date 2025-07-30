from functions import add 
from functions import subtract
from functions import multiply
from functions import divide
from functions import modulo
from functions import power
from functions import square_root
from functions import factorial

num1 = int (input ())
math_operations = input ()
num2 = int (input ())




if math_operations == ("+"):
    print (add(num1 , num2))
    
elif math_operations == ("-"):
    print (subtract(num1 , num2 ))
    
elif math_operations == ("*"):
    print (multiply(num1 , num2 ))
    
elif math_operations == ("/"):
    print (divide(num1 , num2 ))
    
elif math_operations == ("%"):
    print (modulo(num1 , num2 ))
    
elif math_operations == ("**"):
    print (power(num1 , num2 ))
    
elif math_operations == ("~"):
    print (square_root(num1 , num2 ))
    
elif math_operations ==("!"):
    print (factorial(num1 ))
    