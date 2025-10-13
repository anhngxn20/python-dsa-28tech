# Cho số N không âm 64 bit, bạn hãy in ra dạng nhị phân của N, lưu ý bạn cần in đủ 64 bit của N

# Đầu vào
# • Dòng 1 là T : số test case

# • T dòng tiếp theo mỗi dòng là số nguyên N

# Giới hạn
# • 1<=T<=1000

# • 0<=N<=10^18

# Đầu ra
# • Đối với mỗi test in ra dạng nhị phân của N

def decToBin(n):
    res = [0] * 64
    cnt = 1
    while n:
        res[64 - cnt] = n % 2
        n //= 2
        cnt += 1
    return res

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        res = decToBin(n)
        for digit in res:
            print(digit, end='')
        print()