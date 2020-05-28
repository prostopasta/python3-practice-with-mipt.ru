def multiply(s, op):
    return s * op


string = input()
operand = int(input())

if operand > 0:
    print(multiply(string, operand))
elif operand == 0:
    print(string)
else:
    sub = string[:int(len(string)/abs(operand))]
    if multiply(sub, abs(operand)) == string:
        print(sub)
    else:
        print('NO SOLUTION')
