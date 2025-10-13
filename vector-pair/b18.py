# Cho số N không âm 64 bit, bạn hãy in ra dạng thập lục phân của N.

# Đầu vào
# • Dòng 1 là T : số test case
# • T dòng tiếp theo mỗi dòng là số nguyên N

# Giới hạn
# • 1<=T<=1000
# • 0<=N<=10^18

# Đầu ra
# • Đối với mỗi test in ra dạng thập lục phân của N

# Cach 1
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        x = int(input())
        x = hex(x)
        print(x[2:])

# Cach 2
import sys

dict = [ i for i in range(10)] + [chr(j) for j in range(97, 103)]
def hecxa(n):
    
    res = ''
    while n != 0:
        r = n % 16
        if r < 10:
            res = str(r) + res
        else:
            res = dict[r] + res
        
        n = n // 16
    return res
    
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(hecxa(n))
if __name__=="__main__":
    
    solve()
