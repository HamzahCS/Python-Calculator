
def calculate():
    value1=int(input("Enter a Number: "))
    value2=int(input("Enter Second Number: "))
    operator=int(input("1)Addition  \n2)Subtract   \n3)Multiply    \n4)Divide \n5)Modulus  \n6)Power  \n7)Exit\n"))
    calculates={"Value 1":value1,"Value 2":value2, "Operator":operator}
    return calculates

def solution(number1,number2,operator):
        if operator == 4 and number2 == 0:
         print("Cannot divide by zero.")
         return
        elif operator==1:
            result=number1+number2
        elif operator==2:          
         result=number1-number2
        elif operator==3:          
         result=number1*number2
        elif operator==4:          
         result=number1/number2
        elif operator==5:          
         result=number1%number2
        elif operator==6:          
         result=number1**number2
        elif operator==7:   
          print("Good Bye!")
          return 

        
        return result
        
     

calculates=calculate()
result=solution(calculates["Value 1"],calculates["Value 2"],calculates["Operator"])
print(f"Result= {result}")



