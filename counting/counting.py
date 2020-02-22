import sys

# Precalculus
count = [0] * 1001
count[0] = 1,
count[1] = 2
count[2] = 5
count[3] = 13
for idx in range(4, 1001):
    count[idx] = count[idx - 1] + count[idx - 2] + count[idx - 3] + count[
        idx - 1]


if __name__ == '__main__':
    
    while True:
        try:
            line = None
            line = input()
        except:
            pass
        
        if line is None: break
        
        line = line.strip()
        if len(line) == 0: break
        
        n = int(line)
        fn = count[n]
        print(fn)