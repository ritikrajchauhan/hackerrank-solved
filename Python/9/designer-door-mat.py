# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    N,M = map(int, input().split())
    
    if N>5 and N<101 and M>15 and M<303 and N%2==1 and M==(3*N):
        for i in range(N//2):
            print(str.center(((2*i)+1)*('.|.'),M,'-'))
        
        print(str.center('WELCOME',M,'-'))
        
        for i in range((N//2)-1,-1,-1):
            print(str.center(((2*i)+1)*('.|.'),M,'-'))
