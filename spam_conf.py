
def spam():
    fname = input('Enter the file name: ')
    fhand = open(fname)
    xword = 'X-DSPAM-Confidence: '
    our_float = xword.isdecimal()
    count = 0
    total = 0

    for line in fhand:
        if line.startswith(xword):
            count = count + 1
            return count
            
    
    index = xword[19:].isdecimal()
    index = int(index)
    while index > (xword):
        fpoint = index 
        total = fpoint + index
        average = total / count

        return total
        return average
        

    

    print('Average SPAM-Confidence: ' + average)
