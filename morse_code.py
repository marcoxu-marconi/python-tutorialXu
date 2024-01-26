from gpiozero import LED
from time import sleep
import sys
file_path = sys.argv[1]  #prende argomento da linea di comando

#print(file_path)

file = open(file_path,'r')  


stringa = file.read()

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', 
}

def encrypt(message):
    cipher = ''
    for letter in message.upper():
        if letter in morse_dict:
            cipher += morse_dict[letter] + ' ' #spazio tra le lettere
        elif letter == ' ':
            cipher += '/' #spazio tra le parole
    return cipher

led=LED(17)

# 1 unit = 0.1 second
def lampeggia(mors):
    for letter in mors:
        if letter == ' ': 
            led.off()
            sleep(0.3) #spazio tra le lettere di Stessa parola
        elif letter == '.': 
            led.on()
            sleep(0.1) #shortmark
            led.off()
            sleep(0.1)  #interelement gap
        elif letter == '-':
            led.on()
            sleep(0.3) #longmark
            led.off()
            sleep(0.1) #interelement gap
        elif letter == '/':
            led.off()
            sleep(0.7) #spazio tra le parole 


print(encrypt(stringa))

lampeggia(encrypt(stringa))



