print("------------ Welcome to Our Calculator ------------")
print("=========Pick an Operation! =========")
print("1. Addition")
print("2. Difference")
print("3. Product")
print("4. Division")
print("5. Quit")
print("-------------------------------------")

def Calculator() :
    
    
    while True:
        operation = int(input("What operation you want? >> "))
        if operation == 5:
            return
        
        num1 = int(input("Write your first number>> "))
        num2 = int(input("Write your second number>> "))
        result = None
        match operation:
                case 1:
                    result =  num1 + num2
                case 2:
                    result = num1 - num2
                case 3:
                    result = num1 * num2
                case 4:
                    if num2 == 0:
                        print("You can't devide by Zer0!")
                        continue
                    else : result = num1 / num2
                    
        print(str(result))

Calculator()