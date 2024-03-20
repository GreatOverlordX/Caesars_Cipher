txt = 'mrttaqrhknsw ih pugrandomziergrur'
custom_key = 'Codingisfun'

# vigenere
def vgn(msg, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_msg = ''
    for char in msg.lower():
        # Append any non-letter character to the message (:
        if not char.isalpha():
            final_msg += char
        else:
            # Find the right key character to enc/decode
            key_char = key[key_index % len(key)]
            key_index += 1
            # Ensure key character is lowercase for consistency
            key_char = key_char.lower()
			# Define the offset and the enc/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_msg += alphabet[new_index]
    return final_msg

def encrypt(msg, key):
    return vgn(msg, key)

def decrypt(msg, key):
    return vgn(msg, key, -1)

print(f'\nEncrypted text: {txt}')
print(f'Key: {custom_key}')
decryption = decrypt(txt, custom_key)
print(f'\nDecrypted text: {decryption}\n')