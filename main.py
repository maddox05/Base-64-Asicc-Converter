import base64
import time


def encode():
    userinput = input("Encode Here: ")
    message_bytes = userinput.encode('ascii')
    based_bytes = base64.b64encode(message_bytes)
    encodeduuidmessage = based_bytes.decode('ascii')
    print(encodeduuidmessage)
    start()


def decode():
    userinput = input("Decode Here: ")
    decodedmessage = base64.b64decode(userinput)
    newmessage = str(decodedmessage)
    newermsg = newmessage.replace('b', '')
    newestmsg = newermsg[1:len(newermsg) - 1]
    print(newestmsg)
    start()


def start():
    time.sleep(.1)
    userinput = input("Encode = E or Decode = D: ").upper()
    if userinput == "E":
        encode()
    elif userinput == "D":
        decode()
    else:
        print("Not E or D")


if __name__ == "__main__":
    start()
