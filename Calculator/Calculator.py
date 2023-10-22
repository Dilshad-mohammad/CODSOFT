A = float(input("Enter 1st Number"))
B = float(input("Enter 2st Number"))
rule = True
while rule:
    key = int(input("""
    Press 1 For Addition
    Press 2 For Subtraction
    Press 3 For Multiplition
    Press 4 For Division
    Press 0 For EXIT
    """))
    if(key == 1):
        print("Addition of",A, "and",B,"is: ", A+B)
    elif(key == 2):
        print("Subtraction of",A, "and",B,"is: ", A-B)
    elif(key == 3):
        print("Multiplication of",A, "and",B,"is: ", A*B)
    elif(key == 4):
        print("Division of",A, "and",B,"is: ", A/B)
    elif(key > 4 or key < 0):
        print("Please Select Valid Option")
    elif(key == 0):
        rule = False