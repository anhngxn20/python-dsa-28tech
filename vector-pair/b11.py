# Vector cũng như một kiểu dữ liệu bình thường, vì thế bạn có thể viết 1 hàm có tham số là vector hay 1 hàm trả về vector. Cho một vector chứa N số nguyên, bạn hãy viết hàm trả về 1 vector chứa các số nguyên tố trong dãy số đó. Bạn phải code tuân theo khuôn mẫu sau

# Đầu vào
# • Dòng 1 là N : số lượng phần tử trong vector

# • Dòng 2 N số trong vector

# Giới hạn
# • 1<=N<=1000

# • Các phần tử trong vector là số int

# Đầu ra
# • In ra các số nguyên tố trong dãy theo thứ tự xuất hiện

from math import *

def isPrime(x):
    if x < 2:
        return 0
    for i in range(2, int(sqrt(x)) + 1, 1):
        if x % i == 0:
            return 0
    return 1

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    lst = []
    for i in a:
        if (isPrime(i) == 1):
            print(i, end=' ')