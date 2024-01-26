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
            sleep(0.5)
        elif letter == '.':
            led.on()
            sleep(0.1) """1unit"""
            led.off()
            sleep(0.1)   """ interelement space """
        elif letter == '-':
            led.on()
            sleep(0.3) """3unit"""
            led.off()
            sleep(0.1) """interelement space"""

lampeggia(encrypt(stringa))

