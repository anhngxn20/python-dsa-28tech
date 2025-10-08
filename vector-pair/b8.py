# Cho N điểm trong hệ tọa độ Oxyz, bạn hãy dùng vector pair<pair<int, int>, int>> để lưu tọa độ các điểm này.

# Sau đó duyệt vector và in ra tổng của tung độ, hoành độ, cao độ.

# Đầu vào
# Dòng 1 là N : số lượng điểm. N dòng tiếp theo mỗi dòng gồm 3 số là tung độ, hoành độ, cao độ.

# Giới hạn
# 1<=N<=1000
# Tọa độ là số nguyên có trị tuyệt đối không quá 100

# Đầu ra
# In ra đáp án của bài toán

from math import *

n = int(input())
res = []
for i in range(n):
    x, y, z = map(int, input().split())
    s = x + y + z
    res.append(s)

for item in res:
    print(item, end=' ')