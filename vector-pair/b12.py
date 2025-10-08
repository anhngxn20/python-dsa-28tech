# Bạn hãy tự code hàm lật ngược 1 vector theo khuôn mẫu hàm main như sau :

# Đầu vào
# • Dòng 1 là N : số lượng phần tử trong vector
# • Dòng 2 là N số trong vector

# Giới hạn
# • 1<=N<=1000
# • Các số trong vector là số nguyên int

# Đầu ra
# • In ra vector sau khi lật ngược

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    a.reverse()
    for i in a:
        print(i, end=' ')