
def printPattern(symbol, row=2, col=2):
    for n in range(row):
        print(symbol * col)

# print(__name__)

if __name__ == "__main__":
    printPattern('*') 
    print("--")
    printPattern('&', 3, 2)
    print("--")
    printPattern('&', col=2, row=3)