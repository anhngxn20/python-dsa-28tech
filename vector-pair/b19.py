# Cho 1 dãy số có không quá 10k số nguyên, bạn hãy lọc ra các số nguyên tố trong dãy và in theo thứ tự xuất hiện từ cuối về, và các số không nguyên tố thì bạn in theo thứ tự xuất hiện.
# Ví dụ : dãy số : 1 3 2 7 8 10 2 thì bạn cần in các số nguyên tố theo thứ tự ngược là 2 7 2 3, các số không nguyên tố là 1 8 10

# Đầu vào
# Gồm nhiều dòng, mỗi dòng gồm nhiều số

# Giới hạn
# Có không quá 10k số, các số xuất hiện trong dãy là số int

# Đầu ra
# Dòng 1 in ra các số nguyên tố theo thứ tự xuất hiện ngược từ cuối về
# Dòng 2 in ra các số không phải là số nguyên tố theo thứ tự xuất hiện

from sys import stdin
from math import *

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x) + 1), 1):
        if x % i == 0:
            return False
    return True

if __name__ == "__main__":
    a = []
    for s in stdin:
        a += list(map(int, s.split()))
    primeNum = [x for x in a if isPrime(x) == True][::-1]
    basicNum = [x for x in a if isPrime(x) == False]
    for i in primeNum:
        print(i, end=' ')
    print()
    for i in basicNum:
        print(i, end=' ')