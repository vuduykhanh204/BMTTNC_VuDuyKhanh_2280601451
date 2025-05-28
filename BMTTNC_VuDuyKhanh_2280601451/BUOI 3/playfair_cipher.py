class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        # Thay 'J' thành 'I' và viết hoa key
        key = key.replace("J", "I").upper()
        key_set = set()
        matrix = []

        # Thêm các ký tự của key vào matrix nếu chưa có
        for char in key:
            if char not in key_set and char.isalpha():
                key_set.add(char)
                matrix.append(char)

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Chữ I và J gộp chung thành I
        for letter in alphabet:
            if letter not in key_set:
                matrix.append(letter)
            if len(matrix) == 25:
                break

        # Chia matrix thành 5 hàng, mỗi hàng 5 ký tự
        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return None  # Nếu không tìm thấy (phòng trường hợp)

    def playfair_encrypt(self, plain_text, matrix):
        # Thay 'J' thành 'I' và viết hoa văn bản
        plain_text = plain_text.replace("J", "I").upper()

        # Xử lý cặp ký tự (theo quy tắc Playfair)
        encrypted_text = ""
        i = 0
        while i < len(plain_text):
            pair = plain_text[i:i+2]
            if len(pair) == 1:
                pair += "X"  # nếu lẻ thêm 'X'
            elif pair[0] == pair[1]:
                # Nếu 2 ký tự giống nhau thì chèn 'X' sau ký tự đầu tiên
                pair = pair[0] + "X"
                i -= 1  # để ký tự thứ 2 sẽ được xử lý ở lần tiếp theo

            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                # cùng hàng, lấy ký tự bên phải (mod 5)
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                # cùng cột, lấy ký tự bên dưới (mod 5)
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:
                # khác hàng khác cột, hoán vị cột
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]

            i += 2

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        i = 0

        while i < len(cipher_text):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                # cùng hàng, lấy ký tự bên trái (mod 5)
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                # cùng cột, lấy ký tự bên trên (mod 5)
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:
                # khác hàng khác cột, hoán vị cột
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]

            i += 2

        # Loại bỏ ký tự 'X' được thêm vào (nếu có)
        # Giả sử nếu 'X' nằm giữa hai ký tự giống nhau thì loại bỏ nó
        clean_text = ""
        i = 0
        while i < len(decrypted_text):
            if (i+2 < len(decrypted_text) and
                decrypted_text[i] == decrypted_text[i+2] and
                decrypted_text[i+1] == 'X'):
                clean_text += decrypted_text[i]
                i += 2  # bỏ qua 'X'
            else:
                clean_text += decrypted_text[i]
                i += 1

        # Nếu ký tự cuối cùng là 'X', có thể là ký tự thêm vào, bỏ đi
        if clean_text.endswith('X'):
            clean_text = clean_text[:-1]

        return clean_text
