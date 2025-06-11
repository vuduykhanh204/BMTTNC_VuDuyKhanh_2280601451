import struct

# Hàm xoay trái
def left_rotate(x, amount):
    x &= 0xFFFFFFFF
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF

# Hàm MD5 chính
def md5(message: bytes) -> str:
    # Khởi tạo 4 biến A, B, C, D theo chuẩn MD5
    A = 0x67452301
    B = 0xefcdab89
    C = 0x98badcfe
    D = 0x10325476

    # Các giá trị s (số vòng quay trái)
    s = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + \
        [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4

    # Bảng T chứa các hằng số (sin(i))
    K = [int(abs(struct.unpack('<i', struct.pack('<f', abs(__import__('math').sin(i + 1))))[0]) & 0xFFFFFFFF) for i in range(64)]

    # Thêm padding
    original_length = len(message) * 8
    message += b'\x80'
    while (len(message) % 64) != 56:
        message += b'\x00'
    message += struct.pack('<Q', original_length)

    # Xử lý từng khối 512-bit
    for i in range(0, len(message), 64):
        chunk = message[i:i+64]
        M = list(struct.unpack('<16I', chunk))

        a, b, c, d = A, B, C, D

        for i in range(64):
            if 0 <= i <= 15:
                f = (b & c) | (~b & d)
                g = i
            elif 16 <= i <= 31:
                f = (d & b) | (~d & c)
                g = (5 * i + 1) % 16
            elif 32 <= i <= 47:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            elif 48 <= i <= 63:
                f = c ^ (b | ~d)
                g = (7 * i) % 16

            f = (f + a + K[i] + M[g]) & 0xFFFFFFFF
            a = d
            d = c
            c = b
            b = (b + left_rotate(f, s[i])) & 0xFFFFFFFF

        # Cộng dồn kết quả
        A = (A + a) & 0xFFFFFFFF
        B = (B + b) & 0xFFFFFFFF
        C = (C + c) & 0xFFFFFFFF
        D = (D + d) & 0xFFFFFFFF

    # Trả về chuỗi hash
    return '{:08x}{:08x}{:08x}{:08x}'.format(A, B, C, D)

# Dùng thử
if __name__ == "__main__":
    input_string = input("Enter string to hash: ")
    result = md5(input_string.encode('utf-8'))
    print("The MD5 hash of string '{}' is: {}".format(input_string, result))
