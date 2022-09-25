from string import ascii_lowercase as alphabets
def print_rangoli(size):
    for i in range(1,2*size):
        k = alphabets[abs(size-i):size]
        k = k[-1:0:-1] + k
        print('-'.join(k).center(4*size-3,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)