""" import RPi.GPIO as GPIO
import time 
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
GPIO.setup(17, GPIO.out)

def lampeggia(mors):
    for letter in mors:
        if letter == ' ':
        

            GPIO.output(17, GPIO.LOW)
            sleep(1000)
        elif letter == '.':
            

            GPIO.output(17, GPIO.HIGH)
            sleep(200)
            GPIO.output(17, GPIO.LOW)
        elif letter == '-':
           
            
            GPIO.output(17, GPIO.HIGH)
            sleep(600)
            GPIO.output(17, GPIO.LOW)

lampeggia(encrypt(stringa)) """



from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
