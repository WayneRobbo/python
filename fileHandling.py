import os

dir = os.getcwd()
print(dir)

#os.chdir('C:\\Users\\wayne\\Desktop')    Move file to desktop.
#os.mkdir('Folder1')     Make folder in current path.
#os.mkdir('C:\\Users\\wayne\\Desktop\\Folder1')    Make folder with current path.
#print(os.path.abspath('C:\\Users\\wayne\\Desktop'))


# file = open('ourfile.txt')
# file.close()
# fn = open('ourfile.txt', 'r')
# fn.read()
# fn.close()
#
# string = ' hello world'
# fn = open('ourfile.txt', 'w')
# fn.write(string)
# fn.close()
#
# string = ' to exisitng file'
# fn = open('ourfile.txt', 'a')
# fn.write(string)
# fn.close()
#
# fn = open('ourfile.txt', 'r')
# print(fn.read())


filename = 'ourfile.txt'
fn = open(filename, 'r')

for line in fn.readlines():
    print(line)

filename = 'ourfile.txt'
fn = open(filename, 'r')

for line in fn.readlines():
    line = line.strip('\n')
    print(line)
