def validateTime(timeStr): # 11:30 Valid 15:70, 25:11 not valid
    colon = timeStr.find(':')
    if colon == -1:
        raise Exception('Invalid format')
    h, m = timeStr.split(':')
    if not h.isdigit() or not 0<=int(h)<24:
        raise Exception('Invalid hour')
    if not m.isdigit() or not 0<=int(m)<60:
        raise Exception('Invalid minute')
    return True

if __name__ == "__main__":

    try:
        print('Valid' if validateTime("11:98") else 'Invalid')
    except Exception as e:
        print(e)