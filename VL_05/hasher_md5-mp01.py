# nicht klausurrelevant!

import hashlib
import time
from multiprocessing import Pool

start_time = time.time()

geheimer_text = hashlib.md5('98765432'.encode()).hexdigest()

def find_password(zahl):
        m = hashlib.md5(str(zahl).encode())
        return m.hexdigest()

result = []

if __name__ == '__main__':
    with Pool(8) as p:
        result = p.map(find_password, range(100000000))
    
    print(result.index(geheimer_text))

print("--- %s seconds ---" % (time.time() - start_time))

# --- Pool(8): approx. 60 seconds on Xeon E5-2687W
# --- Pool(4): approx. 80 seconds on Xeon E5-2687W
# --- Pool(2): approx. 130 seconds on Xeon E5-2687W

# --- Pool(8): approx. 60 seconds on i7 4770
# --- Pool(4): approx. 80 seconds on i7 4770
# --- Pool(2): approx. 130 seconds on i7 4770

# --- Pool(8): approx. 45 seconds on Xeon E3-1230 v2
# --- Pool(4): approx. 53 seconds on Xeon E3-1230 v2
# --- Pool(2): approx. 84 seconds on Xeon E3-1230 v2

# --- Pool(8): approx. 93 seconds on i7 4800MQ