
for i in range(1,101):
    
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
        
for i in range(1,101):
    ergebnis=''
    if i%3==0:
        ergebnis=ergebnis+"Fizz" 
    if i%5==0:
        ergebnis=ergebnis+"Buzz"
    else:
        ergebnis = str(i)
    print(ergebnis)
        
        