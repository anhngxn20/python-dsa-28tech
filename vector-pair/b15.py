# Cho vector gồm N số, bạn hãy viết 1 hàm trả về 1 vector có được từ vector đầu vào bằng cách xóa đi các phần tử đứng cạnh mà giống nhau. Lưu ý sau khi xóa 1 phần tử trong vector thì phần tử đứng trước và đứng sau phần tử vừa xóa lại được coi là đứng cạnh nhau.
# Ví dụ : vector = {1, 1, 1, 2, 2, 3, 4, 4, 4, 5} sẽ có kết quả là {1, 2, 3, 4, 5}.

# Đầu vào
# • Dòng 1 là N : số lượng phần tử trong vector
# • Dòng 2 là N số trong vector

# Giới hạn
# • 1<=N<=1000
# • Các phần tử trong vector là số int

# Đầu ra
# • In ra đáp án của bài toán

def unique_arr(a):
    for i in range(len(a) - 1, 0, -1):
        if a[i] == a[i-1]:
            a.pop(i)
    return a    

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a = unique_arr(a)
    
    for x in a:
        print(x, end=' ')