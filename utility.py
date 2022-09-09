#optional parameters

def printPattern(symbol, row=1, col=1):
    for n in range(row) :
        print( symbol*col )


# if __name__ == '__main__':
#     printPattern('*', 2, 3)
#     printPattern('#') #default is row 1, col 1
#     printPattern('$', 3) # row =3 , default col = 1
#     printPattern('%', col=2) #use default row=1, specify col = 2
#     printPattern(symbol='&', row=1, col=2)

print( __name__ ) #__main__