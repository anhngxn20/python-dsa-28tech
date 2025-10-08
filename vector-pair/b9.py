# Sử dụng vector và pair để giải quyết bài toán sau. Cho mảng A[] gồm N phần tử, bạn hãy đếm xem mỗi phần tử trong mảng A[] xuất hiện bao nhiêu lần và in ra theo thứ tự xuất hiện trong mảng A[].
# Hướng dẫn : Các bạn sử dụng 1 vector rỗng lưu pair<int, int> trong đó first của pair lưu giá trị và second lưu tần suất, mỗi khi gặp 1 phần tử trong mảng A[] bạn hãy duyệt vector đã có và kiểm tra xem giá trị này đã xuất hiện chưa, nếu đã xuất hiện bạn tăng second của nó lên còn nếu chưa xuất hiện thì bạn push_back 1 cặp pair mới vào vector, pair này sẽ lưu giá trị bạn đang xét và tần suất là 1.

# Đầu vào
# Dòng 1 : N
# Dòng 2 là các phần tử trong mảng A[] viết cách nhau một dấu cách

# Giới hạn
# 1<=N<=10^4
# -1000<=A[i]<=1000

# Đầu ra
# In ra các giá trị xuất hiện trong mảng và tần suất tương ứng.

from math import *

n = int(input())
lst = list(map(int, input().split()))
mp = {}

for i in lst:
    if mp.get(i) == None:
        mp[i] = 1
    else:
        mp[i] += 1

for key, value in mp.items():
    print(key, value)