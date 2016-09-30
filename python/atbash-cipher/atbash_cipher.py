#create an atbash cipher
# defined by inverting the alphabet:

#plain text:  a b c d e f g h i j k l m n o p q r s t u v w x y z
#cipher text: z y x w v u t s r q p o n m l k j i h g f e d c b a

import re

mapping =   {'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n',
             'n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a'}

def process_input(input_string):
    return ''.join(re.split('\W|\_',input_string)).lower()

def get_mapping(char):
    if char.isdigit():
        return char
    else:
        return mapping[char]

def encode(input_string):
    ciphertext = ''.join(get_mapping(char) for char in process_input(input_string))
    return ''.join(chunk+' ' for chunk in re.findall('.{,5}',ciphertext)).rstrip()

def decode(input_string):
    return ''.join(get_mapping(char) for char in process_input(input_string))
