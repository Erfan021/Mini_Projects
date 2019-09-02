import re

print("\t======================\n"
      "\txx-BASIC CALCULATOR-xx\n"
      "\t======================\n")
print("Type 'quit' to Exit\n")

previous = 0 #to hold the previous result
run = True

def performMath():
    global run
    global previous

    equation= ""
    if previous is 0:
        equation = input('Enter equation: ')
    else:
        equation = input(str(previous))
    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[a-zA-Z.,:;(){}" "]','',equation)
        if previous is 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    performMath()