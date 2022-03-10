import string

# The alphabet will be used in all the methods
alphabet = string.ascii_lowercase


def count_letters(str):
    global alphabet
    count = 0
    
    for index in range(0, len(str)):
        if str[index] in alphabet:
            count += 1
            
    return count       
            

def encrypt_vigenere_code(str, key):
    global alphabet
    crypted_str = ""
    
    # We compare the number of letters and not the sizes because if the key has less letters then the string but has 
    # a larger size, than we will not repeat the key
    while count_letters(key) < count_letters(str):
        key += key
    
    for index in range(0, len(str)):
        
        # When there is a character that is not in the alphabet in the string, we put this character in the key at
        # the same place and when there is a character that is not in the alphabet in the key, we delete it. We
        # are doing this to make the letters of the string and the key correspond
        if str[index] not in alphabet:
            crypted_str += str[index]
            new_key = key[0:index]
            new_key += str[index]
            new_key += key[index:len(key)]   
            key = new_key

        elif key[index] not in alphabet:
            new_key = key[0:index]
            new_key += key[index+1:len(key)] 
            key = new_key     
        
        # Encryption    
        for alphabet_index in range(0, 26):            
            if(str[index] == alphabet[alphabet_index]):
                letter_position1 = alphabet.find(str[index])
                letter_position2 = alphabet.find(key[index])
                crypted_str += alphabet[(letter_position1 + letter_position2) % 26]       
    
    return crypted_str


def decrypt_vigenere_code(crypted_str, key):
    global alphabet
    decrypted_str = ""
    
    while count_letters(key) < count_letters(crypted_str):
        key += key
        
    for index in range(0, len(crypted_str)):
            
        if crypted_str[index] not in alphabet:
            decrypted_str += crypted_str[index]
            new_key = key[0:index]
            new_key += crypted_str[index]
            new_key += key[index:len(key)]   
            key = new_key
            
        elif key[index] not in alphabet:
            new_key = key[0:index]
            new_key += key[index+1:len(key)] 
            key = new_key     
        
        # Decryption    
        for alphabet_index in range(0, 26):            
            if(crypted_str[index] == alphabet[alphabet_index]):
                letter_position1 = alphabet.find(crypted_str[index])
                letter_position2 = alphabet.find(key[index])
                decrypted_str += alphabet[(letter_position1 - letter_position2) % 26]    
                
    return decrypted_str            


print(encrypt_vigenere_code("il fait beau", "il pleut"))
print( decrypt_vigenere_code( encrypt_vigenere_code("il fait beau", "il pleut") , "il pleut") )