def demo():

    try:
        # x = input("Enter a number ")

        # #y = x + "abc"
        # x = int(x)
        # result = 1 / x
        # print(f'Result is {result}')

        a = 1
        # print('a = ' + a) # TypeError
        # print(length(a)) # NameError
        print(a._x) # AttributeError

    except ValueError as e:
        print(e)
    except ZeroDivisionError as ax:
        print(ax)
    except Exception as f:
        print(f)
    else:
        print(f'There is no error')
    finally:
        print(f'End of Program')

def demo1():

    x = [1, 2, 3]
    try:
        print('begin try')
        index = int(input('Enter index: '))
        x[index] = 4
        print('end try')
        return
    except Exception as e:
        print('except block')
    else:
        print('else block')
    finally:
        print('finally block')
    print('end main') 

if __name__ == "__main__":
    # demo() 
    demo1()