from collections import deque
import sys
n = int(sys.stdin.readline())

temp = int('0o'+str(n),8)

print(bin(temp)[2:])

