# Cho N điểm trong hệ tọa độ Oxy, 
# bạn hãy dùng vector<pair<int, int>> để lưu tọa độ các điểm này.
# Sau đó duyệt vector và tính khoảng cách từ các điểm này về gốc tọa độ và lưu vào 1 vector sau đó in ra các phần tử trong vector khoảng cách này lấy 2 số sau dấu phẩy.

# Đầu vào
# Dòng 1 là N : số lượng điểm. N dòng tiếp theo mỗi dòng gồm 2 số là tung độ và hoành độ.

# Giới hạn
# 1<=N<=1000
# Tọa độ là số nguyên có trị tuyệt đối không quá 100;

# Đầu ra
# In ra đáp án của bài toán.



from math import *

if __name__ == "__main__":
    n = int(input())
    lst = []
    for i in range(n):
        x, y = map(int, input().split())
        d = sqrt(x**2 + y**2)
        lst.append(d)

    for kc in lst:
        print("{:.2f}".format(kc), end=' ')