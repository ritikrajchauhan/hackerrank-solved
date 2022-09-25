import textwrap

def wrap(string, max_width):
    result = ""
    
    if (len(string) and max_width)>0 and len(string)<1000 and max_width<len(string):
        for i in range(max_width,len(string)+max_width,max_width+1):
            string = string[:i] + '\n' + string[i:]

    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)