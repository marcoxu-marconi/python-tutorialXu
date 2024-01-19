import RPi.GPIO as GPIO

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

GPIO.setmode(GPIO.BCM)
GPIO.setup(1, GPIO.out)

def lampeggia(mors):
    for letter in mors:
        if letter == ' ':
            """ print(' ', end='') """

            GPIO.output(1, GPIO.LOW)
            sleep(1000)
        elif letter == '.':
            """ print('.', end='') """

            GPIO.output(1, GPIO.HIGH)
            sleep(200)
            GPIO.output(1, GPIO.LOW)
        elif letter == '-':
            """ print('-', end='') """
            
            GPIO.output(1, GPIO.HIGH)
            sleep(600)
            GPIO.output(1, GPIO.LOW)

lampeggia(encrypt(stringa))