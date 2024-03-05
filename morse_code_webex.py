import requests
import json
import time
from gpiozero import LED

led=LED(17)

oneUnit = 0.1

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', 
    'è': '.', 'é': '.', 'à': '.-', 'ù': '..-', 'ì': '..', 'ò': '---',  #filtro per lettere italiane, trattali come quei normali
}


def encrypt(message):
    cipher = ''
    for letter in message.lower():
        if letter in morse_dict:
            cipher += morse_dict[letter] + ' ' #spazio tra le lettere
        elif letter == ' ':
            cipher += '/' #spazio tra le parole
    return cipher

morse_dict = {k.lower(): v for k, v in morse_dict.items()} #trasforma in maiuscolo

def lampeggia(mors):
    for letter in mors:
        if letter == ' ': 
            led.off()
            sleep(3*oneUnit) #spazio tra le lettere di Stessa parola
        elif letter == '.': 
            led.on()
            sleep(oneUnit) #shortmark
            led.off()
            sleep(oneUnit)  #interelement gap
        elif letter == '-':
            led.on()
            sleep(3*oneUnit) #longmark
            led.off()
            sleep(oneUnit) #interelement gap
        elif letter == '/':
            led.off()
            sleep(5*oneUnit) #spazio tra le parole 
    led.off();


# Define a local variable in Python that will hold our Authentication API KEY:
APIAuthorizationKey = 'Bearer MmU4MjgxOGYtMTQ2My00ZGM1LWFjYWMtNDc3ZDM3ZjNhNzM5ZmIwOTliZDktZmVm_PE93_b6f7ca7f-55ce-4df9-855a-8cfebcad253f'

r = requests.get(   "https://api.ciscospark.com/v1/rooms",
                    headers={'Authorization':APIAuthorizationKey}
                )

if(r.status_code != 200):
    print("Something wrong has happened:")
    print("ERROR CODE: {} \nRESPONSE: {}".format(r.status_code, r.text))
    assert()

jsonData = r.json()

print(
    json.dumps(
        jsonData,
        indent=4
    )
)

# rooms = r.json()['items']
# for room in rooms:
#     print ("Room name: '" + room['title'] + "' ID: " + room['id'])

roomNameToSearch = 'Morse Code'

roomIdToMessage = None

rooms = r.json()['items']
for room in rooms:

    if(room['title'].find(roomNameToSearch) != -1):
        print ("Found rooms with the word " + roomNameToSearch)
        print ("Room name: '" + room['title'] + "' ID: " + room['id'])
        roomIdToMessage = room['id']
        roomTitleToMessage = room['title']
        break

if(roomIdToMessage == None):
    exit("No valid room has been found with the name: " + roomNameToSearch)
else:
    print("A valid room has been found and this is the room id: " + roomIdToMessage)

lastMessageId = None

while True:
    # the code should not hammer the API service with too many reqeuests in a short time
    #  to limit the number of requests in the while loop, begin with a short 1 second delay:
    time.sleep(1)
    print("Next iteration is starting ...")
    
    # define the mandatory or optional GET parametrs for the `messages` API endpoint:
    getMessagesUrlParameters = {
                # mandatory parameter - the room ID
                "roomId": roomIdToMessage,
                # optional parameter - number of the last messages to return
                #  only interested in the very last message in the room
                #   thefore max = 1
                "max": 1
    }

    # Using the requests library, creare a new HTTP GET Request against the Webex Teams API Endpoint for Webex Teams Messages:
    #  the local object "r" will hold the returned data:
    r = requests.get(   "https://api.ciscospark.com/v1/messages",
                        params=getMessagesUrlParameters,
                        headers={'Authorization':APIAuthorizationKey}
                    )
    if(r.status_code != 200):
        print("Something wrong has happened:")
        print("ERROR CODE: {} \nRESPONSE: {}".format(r.status_code, r.text))
        assert()
    
    
    # Store the json data from the reply
    jsonData = r.json()
    
    # Get the items (array of messages) from the jsonData.
    messages = jsonData['items']
    # since the request specified max=1, only one message should be returned:
    if(messages):
        message  = messages[0]
    else:
        continue
    # Verify if this is a new message:
    if(lastMessageId == message['id']):
        #this is the same message as before, no new messages
        print("No New Messages.")
    else:
        # this is a new message, its ID is different from the one in the previous iteration
        print("New Message: " + message['text'])
        # save the message id for the next iteration:
        lastMessageId = message['id']
        messageText = message['text'].split(" ",1)
        text = encrypt(messageText[1])
        if(messageText[0] == '/iniziaMorse'):
            print("Sending the morse code to the room")
            lampeggia(text) 
