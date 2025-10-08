# Cho 1 bảng số có N dòng và M cột, bạn hãy lưu bảng số này vào một vector các vector dạng vector> trong đó mỗi hàng của bảng số bạn lưu vào 1 vector. Hãy lật ngược từng dòng của bảng số sau đó in ra màn hình.
# Bạn phải cài đặt theo khuôn mẫu sau


# Đầu vào
# • Dòng 1 là N và M
# • N dòng tiếp theo mỗi dòng là M số

# Giới hạn
# • 1<=N,M<=100
# • Các số trong bảng số là số int

# Đầu ra
# In ra bảng số sau khi lật ngược từng dòng

if __name__ == "__main__":
    n,m = map(int, input().split())
    