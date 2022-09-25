if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if (a and b) <= pow(10,10) and (a and b) >= 1:
        print(str(a+b) + '\n' + str(a-b) + '\n' + str(a*b))
