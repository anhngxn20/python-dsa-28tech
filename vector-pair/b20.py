# Cho 1 dãy các cặp gồm 1 kí tự in thường đi kèm với 1 số tương ứng, nhiệm vụ của bạn là hãy liệt kê các cặp có kí tự đi kèm là nguyên âm, nguyên âm gồm 5 chữ cái o, a, i, e, u. Bạn cần liệt kê theo thứ tự ngược từ cuối về, trong trường hợp không có cặp nào có kí tự là nguyên âm thì in ra 28tech.

# Đầu vào
# Dòng 1 là N : số cặp
# N dòng tiếp theo mỗi dòng là 1 ký tự và số đi kèm

# Giới hạn
# 1<=N<=20000
# Các chữ cái trong cặp số là chữ in thường, số là số nguyên 32 bit

# Đầu ra
# In ra các cặp thỏa mãn theo thứ tự ngược với thứ tự xuất hiện hoặc in ra 28tech nếu không có cặp thỏa mãn

def main():
    n = int(input())
    a = []
    nguyenAm = ['o', 'a', 'i', 'e', 'u']
    for i in range(n):
        c, x = input().split()
        if c in nguyenAm:
            a.append([c, x])
    if len(a) > 0:
        a = a[::-1] 
        for pair in a:
            print(pair[0], pair[1])
    else:
        print("28tech")
    return
if __name__ == "__main__":
    main()