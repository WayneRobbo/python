# try:
#     Your code
# finally:
#     run this code no matter
try:
    fn = open('testfile', 'w')
    try:
        fn.write('This is my test file')
    finally:
        print('Cant open or find a file with that name, going too close')
        fn.close()
except IOError:
    print('That file doesnt exist!')
