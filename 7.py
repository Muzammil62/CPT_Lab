def caesar_cipher_encryption(plain_text,shift):
    encrypted_text=""

    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char)- ord('A')+ shift)% 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char)- ord('a')+ shift)% 26 + ord('a'))
                encrypted_char += encrypted_char
        else:
                encrypted_text += char

                return encrypted_text
        
        plain_text = input+("enter the plaintext:")
        shift = int(input("Enter the shift value:"))

        encrypted_text = caesar_cipher_encryption(plain_text, shift)

        print("encrypted text:", encrypted_text) 