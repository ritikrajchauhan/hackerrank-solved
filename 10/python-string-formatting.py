def print_formatted(number):
    if number >= 1 and number <= 99:
        #checking final length of binary number
        width = len(bin(number)[2:])
        
        for i in range(1,number+1):
            #printing Decimals            
            print(str.rjust(str(i),width,' '), end=' ')
        
            #printing Octals
            print(str.rjust(str(oct(i)[2:]),width,' '), end=' ')
        
            #printing Hexadecimals
            print(str.rjust(str(hex(i)[2:]),width,' ').upper(), end=' ')
        
            #printing Binaries
            print(str.rjust(str(bin(i)[2:]),width,' '), end=' ')
            print('')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)