import re

def minion_game(string):
    cs_count = 0
    vs_count = 0
    
    for iter in re.finditer('[AEIOU]', string):
        vs_count += (len(string) - iter.start())
        
    for iter in re.finditer('[^AEIOU]', string):
        cs_count += (len(string) - iter.start())
        
    if vs_count == cs_count:
        print("Draw")
    elif vs_count > cs_count:
        print("Kevin", vs_count)
    else:
        print("Stuart", cs_count)

if __name__ == '__main__':
    s = input()
    minion_game(s)