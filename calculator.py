def addition ():
    print("Addition")
    n = float(input("Enter the number: "))
    count = 0 
    ans = 0
    while n != 0:
        ans = ans + n
        count += 1
        n = float(input("Enter another number (0 to stop): "))
    return [ans,count]

def subtraction ():
    print("Subtraction");
    n = float(input("Enter the number: "))
    count = 0 
    ans = n*2
    while n != 0:
        ans = ans - n
        count += 1
        n = float(input("Enter another number (0 to stop): "))
    return [ans,count]

def multiplication ():
    print("Multiplication")
    n = float(input("Enter the number: "))
    count = 0 
    ans = 1
    while n != 0:
        ans = ans * n
        count += 1
        n = float(input("Enter another number (0 to stop): "))
    return [ans,count]

def average():
    an = []
    an = addition()
    count = an[1]
    a = an[0]
    ans = a / count
    return [ans,count]

while True:
    list = []
    
    print("**********************Python Calculator**********************")
    print(" Enter 'a' for addition")
    print(" Enter 's' for subtraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'v' for average")
    print(" Enter 'q' for quit")
    print("*************************************************************")
    c = input("Enter Your Choice: ")
    if c != 'q':
        if c == 'a':
            list = addition()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 's':
            list = subtraction()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 'm':
            list = multiplication()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 'v':
            list = average()
            print("Ans = ", list[0], " total inputs ",list[1])
        else:
            print ("Sorry, invalid character")
            print("Enter again")
    else:
        break
