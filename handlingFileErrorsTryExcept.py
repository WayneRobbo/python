#ZeroDivsionError: dividing by zero

# try:
#     do Some task
# except Exception1:
#     do somthing else
# else:
#     if there is no error it will excute this

print("please enter two numbers for division")
firstnumber = int(input("enter first number: "))
secondnumber = int(input("enter first number: "))

try:
    answer = firstnumber/secondnumber
    print(answer)

except ZeroDivisionError:
    print('Sorry! Cant divid by zero.')


try:
    fn = open('ourtestfile')
    fn.write('This is a test file')

except IOError:
    print('Cant open file, it doesnt exist!')

else:
    print('Everything works ok!')
