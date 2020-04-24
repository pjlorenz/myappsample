# things you can do with a file handle
#
# fhand.read()
# fhand.close()
# iterate: for line in fhand:

def test1():
    fhand = open('mbox-short.txt')
    count = 0 
    for line in fhand:
        count = count + 1
    print('Line Count:', count)

def test2():
    fhand = open('mbox-short.txt')
    count = 0
    for line in fhand:
        if line.startswith('b'):
            print(line)

test2()