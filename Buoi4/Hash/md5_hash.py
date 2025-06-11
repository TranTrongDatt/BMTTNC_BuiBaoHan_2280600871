def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

# Hàm xử lý tin nhắn
def md5(message):
    # Khởi tạo các biến ban đầu
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    # Tiền xử lý chuỗi với biến
    original_length = len(message)
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += original_length.to_bytes(8, 'little')

    # Chia chuỗi thành các khối 512-bit và xử lý từng khối
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]

        # Lưu giá trị ban đầu để cộng sau
        a0, b0, c0, d0 = a, b, c, d

        # Vòng lặp xử lý từng từ trong khối của thuật toán MD5
        for j in range(64):
            if j < 16:
                f = (b & c) | ((~b) & d)
                g = j
                constant = 0xD76AA478  # Hằng số vòng 1
            elif j < 32:
                f = (d & b) | ((~d) & c)
                g = (5*j + 1) % 16
                constant = 0xE8C7B756  # Hằng số vòng 2
            elif j < 48:
                f = b ^ c ^ d
                g = (3*j + 5) % 16
                constant = 0x242070DB  # Hằng số vòng 3
            else:
                f = c ^ (b | (~d))
                g = (7*j) % 16
                constant = 0xC1BDCEEE  # Hằng số vòng 4

            # Cập nhật giá trị với shift đúng
            f = (a + f + constant + words[g]) & 0xFFFFFFFF
            temp = d
            d = c
            c = b
            b = b + left_rotate(f, [7, 12, 17, 22][j % 4])  # Sử dụng mảng shift
            a = temp

        # Cập nhật giá trị cuối cùng sau mỗi khối
        a = (a + a0) & 0xFFFFFFFF
        b = (b + b0) & 0xFFFFFFFF
        c = (c + c0) & 0xFFFFFFFF
        d = (d + d0) & 0xFFFFFFFF

    return '{:08x}{:08x}{:08x}{:08x}'.format(a, b, c, d)

# Nhập chuỗi từ người dùng và tính MD5
input_string = input("Nhập chuỗi cần băm: ")
md5_hash = md5(input_string.encode('utf-8'))
print("Mã băm MD5 của chuỗi '{}' là: {}".format(input_string, md5_hash))