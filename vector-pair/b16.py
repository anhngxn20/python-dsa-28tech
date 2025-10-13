# Bạn được cung cấp 1 bảng số gồm nhiều dòng, mỗi dòng có thể có số lượng số khác nhau và bạn cần chỉ ra giá trị nằm ở cột y của dòng x trong bảng số.
# Gợi ý : Bài này bạn sử dụng 1 mảng vector vector a[N]; với N là số dòng, hoặc bạn có thể dùng 1 vector các vector để lưu. Mỗi dòng sẽ dùng 1 vector để lưu.

# Đầu vào
# • Dòng 1 là N và Q : Số dòng và số truy vấn
# • N dòng tiếp theo mỗi dòng bao gồm số đầu tiên M là số lượng số của dòng đó, theo sau là M số của dòng này
# • Q dòng tiếp theo mỗi dòng là một truy vấn gồm dòng x và cột y, lưu ý dòng x và cột y được đánh số từ 1

# Giới hạn
# • 1<=N,M<=10^5
# • 1<=Q<=1000
# • x, y đảm bảo dữ liệu hợp lệ

# Đầu ra
# • Đối với mỗi truy vấn in ra phần tử nằm ở dòng x, cột y.


if __name__ == "__main__":
    n, q = map(int, input().split())
    a = []
    for i in range(n):
        arr = list(map(int, input().split()))
        arr.pop(0)
        a.append(arr)
    
    for i in range(q):
        x,y = map(int, input().split())
        print(a[x - 1][y - 1])