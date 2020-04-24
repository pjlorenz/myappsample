def spam_confidence():

    file_name = input('Enter the file name: ')
    fname = open(file_name)
    xword = 'X-DSPAM-Confidence: 0.0000'
    nums = xword[20::]
    our_nums = float(nums)
    count = 0
    total = 0

    for line in fname:
        if line.startswith('X-DSPAM-Confidence: '):
            xword.replace(nums, line[20:])
            line = float(line[20:])
            count = count + 1
            total = line + total
            average = total / count
    print(average)

spam_confidence()