import pyDes    # Library containing DES implementation
import base64   # Library needed to convert binary data into
                # printable character
import italian_dictionary

cipher_text = base64.b64decode("dpi4c+NIZxM=")
print('Stampo il testo cifrato:')
print(cipher_text) # Text coded in base64

#Dal testo cifrato devo fare in modo di trovare la chiave

def is_plaintext(stringa):
    try:
        key = pyDes.des(bytes(stringa, encoding='utf-8'))
        parola = key.decrypt(cipher_text)
        definizione = italian_dictionary.get_only_definition(parola)
    except (ValueError, TypeError):
            return False      
    try:
        for elemento in definizione:
            print('Significato: ' )
            print(elemento)
            return True
        return False
    except:
        return False
        
        
stringa = range(200068247,18446744073709551616)
for count in stringa:
    print(count)
    if is_plaintext(count):
        break