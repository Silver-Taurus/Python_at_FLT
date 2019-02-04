''' Project Sipher '''

def Reverse_Cipher(message):
    pass

def Caesar_Cipher(message):
    pass

def Transposition_Cipher(message):
    pass

def Affine_Cipher(message):
    pass

def Vigenere_Cipher(message):
    pass

def OTP_Cipher(message):
    pass

def RSA_Cipher(message):
    pass


def Encode_sub_routine():
    ''' Encode-Routine for Encoding the plaintext into ciphertext '''

    plain_text = input('Enter the Text to encrypt : ')

    ciphers = {'Reverse Cipher': Reverse_Cipher(plain_text), 'Caesar Cipher': Caesar_Cipher(plain_text), \
                'Transposition Cipher': Transposition_Cipher(plain_text), 'Affine Cipher': Affine_Cipher(plain_text), \
                'One Time Pad Cipher': OTP_Cipher(plain_text), 'Vigenere Cipher': Vigenere_Cipher(plain_text), \
                'RSA Cipher': RSA_Cipher(plain_text)}
    
    cipher_keys = {}
    print('\nMain Menu:')
    for num, val in enumerate(ciphers.keys(), 1):
        print(f'{num}. {val}')
        cipher_keys[f'{num}'] = f'{val}'

    ciphers[cipher_keys[input('\nEnter Your Choice: ')]]


def Decode_sub_routine():
    ''' Decode-Routine for Decoding the ciphertext into plaintext '''

    cipher_text = input('Enter the Text to decrypt : ')

    ciphers = {'Reverse Cipher': Reverse_Cipher(cipher_text), 'Caesar Cipher': Caesar_Cipher(cipher_text), \
                'Transposition Cipher': Transposition_Cipher(cipher_text), 'Affine Cipher': Affine_Cipher(cipher_text), \
                'One Time Pad Cipher': OTP_Cipher(cipher_text), 'Vigenere Cipher': Vigenere_Cipher(cipher_text), \
                'RSA Cipher': RSA_Cipher(cipher_text)}
    
    cipher_keys = {}
    print('\nMain Menu:')
    for num, val in enumerate(ciphers.keys(), 1):
        print(f'{num}. {val}')
        cipher_keys[f'{num}'] = f'{val}'

    ciphers[cipher_keys[input('\nEnter Your Choice: ')]]

    pass

def Hack_sub_routine():
    pass

def main():
    ''' Main Driver Program '''
    while(True):
        choice = input(''' Main Menu:
            1. Encode into ciphertext
            2. Decode into plaintext
            3. Hack the ciphertext
            4. Exit
            ''')

        if choice == '1':
            Encode_sub_routine()
        elif choice == '2':
            Decode_sub_routine()
        elif choice == '3':
            Hack_sub_routine()
        else:
            break

if __name__ == '__main__':
    main()