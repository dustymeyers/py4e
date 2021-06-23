fh = open('mbox-short.txt')
# print(fh)

for lx in fh:
    # rstrip() method removes the line ending characters to make the doc more readable
    ly = lx.rstrip()
    # .upp() method changes all text to uppercase, .lower() does opposite
    print(ly.upper())

