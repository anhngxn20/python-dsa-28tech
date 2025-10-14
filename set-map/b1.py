# Cho dãy số A[] gồm có N phần tử, bạn hãy đếm xem trong mảng có bao nhiêu phần tử phân biệt? Chú ý giải bài này với 3 cách : Sử dụng set, map, sắp xếp.

# Đầu vào
# Dòng đầu tiên là số nguyên N. Dòng tiếp theo gồm N số nguyên A[i]

# Giới hạn
# 1≤ N ≤ 10^5
# -10^9 ≤ A[i] ≤ 10^9

# Đầu ra
# In ra số lượng phần tử khác nhau trong mảng.

if __name__ == '__main__':
    n = int(input())
    t = list(map(int, input().split()))
    print(len(set(t)))