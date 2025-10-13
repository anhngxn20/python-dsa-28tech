# Cho input gồm nhiều dòng, mỗi dòng gồm nhiều ký tự viết cách nhau 1 dấu cách. Bạn hãy tiến hành lưu các ký tự này vào vector, sau đó những ký tự là in hoa thì đổi thành in thường, in thường thì đổi thành in hoa, chữ số thì giữ nguyên và in ra màn hình.
# Bạn phải triển khai mã nguồn theo khuôn mẫu sau :

# Đầu vào
# • Gồm nhiều dòng, mỗi dòng có nhiều ký tự nhưng không quá 1 triệu kí tự, các ký tự là chữ in hoa in thường hoặc chữ số.

# Giới hạn
# Các ký tự là chứ cái hoặc chữ số

# Đầu ra
# • In ra đáp án của bài toán

from sys import stdin

def nhap(arr):
    for s in stdin:
        arr += list(s.split())
    return arr

def thaydoi(arr):
    for i in range(len(arr)):
        arr[i] = arr[i].swapcase()
    return arr

def xuat(arr):
    for c in arr:
        print(c, end=' ')

if __name__ == "__main__":
    arr = []
    arr = nhap(arr)
    arr = thaydoi(arr)
    xuat(arr)