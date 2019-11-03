import hashlib
import time
start_time = time.time()

geheimer_text = hashlib.md5('98765432'.encode()).hexdigest()

def find_password(maxzahl):
    for i in range(maxzahl):
        m = hashlib.md5(str(i).encode())
        if m.hexdigest() == geheimer_text:
            print(i , 'ist das Passwort')
            break

find_password(100000000)

print("--- %s seconds ---" % (time.time() - start_time))

# --- approx. 122 seconds on Xeon E5-2687W
