# Cho số N không âm 64 bit, bạn hãy in ra dạng thập lục phân của N.

# Đầu vào
# • Dòng 1 là T : số test case
# • T dòng tiếp theo mỗi dòng là số nguyên N

# Giới hạn
# • 1<=T<=1000
# • 0<=N<=10^18

# Đầu ra
# • Đối với mỗi test in ra dạng thập lục phân của N

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        x = int(input())
        x = hex(x)
        print(x[2:])