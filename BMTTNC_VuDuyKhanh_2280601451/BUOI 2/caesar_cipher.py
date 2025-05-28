from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET
        
    def encrypt_text(self , text : str ,key : int ) -> str:
        alphabet_len = len(self.alphabet)
        text = text .upper()
        encrypted_text = []
        for letter in text:
            letter_index = self.alphabet.index(letter)
            letter_index = (letter_index + key ) % alphabet_len
            output_index = self.alphabet[output_index]
        return "" .join(encrypted_text)
    def decrypt_text(self ,text : str , key : int) ->str:
        alphabet_len = len(self.alphabet)
        text = text .upper()
        decrypt_text = []
        for letter in text : 
            letter_index = self .alphabet.index(letter)
            output_index = (letter_index- key) % alphabet_len
            output_index = self.alphabet[output_index]
            decrypt_text.append [output_index]
        return "".join(decrypt_text)   