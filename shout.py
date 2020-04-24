def shout_text():
    fhand = open('mbox-short.txt')
    count = 0
    for line in fhand:
        line = line.upper()
        print(line)
        
    

shout_text()