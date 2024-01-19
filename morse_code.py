from gpiozero import LED
from time import sleep

file = open('./input.txt','r')

stringa = file.read()

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def encrypt(message):
    cipher = ''
    for letter in message.upper():
        if letter in morse_dict:
            cipher += morse_dict[letter] + ' '
        else:
            cipher += ' '
    return cipher

led=LED(17)

def lampeggia(mors):
    for letter in mors:
        if letter == ' ':
        

            led.off()
            sleep(1000)
        elif letter == '.':
            

            led.on()
            sleep(200)
            led.off()
        elif letter == '-':
           
            
            led.on()
            sleep(600)
            led.off()

lampeggia(encrypt(stringa))

