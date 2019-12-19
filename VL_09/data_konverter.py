
lastreadchar = ''

with open("data.txt",mode='r') as i, open('out.txt','w') as o:
    while True:
        x = i.read(1)

        if x == '': # end of file has been reached
            break 
        elif x==' ':
            pass
        elif x==']':
            pass
        elif x=='[':
            if lastreadchar == '[': 
                # at the beginning of the file, don't do anything
                pass
            elif lastreadchar == '\n': # a new line
                pass   
            elif lastreadchar == ',': # a new line
                pass
        elif x==',':
            if lastreadchar == ']': # at the beginning of the file
                print('\n')
                o.write('\n')
            else:
                print(x, end='')
                o.write(x)
        else:
            print(x, end = '')            
            o.write(x)

        lastreadchar = x