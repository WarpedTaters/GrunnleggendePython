import cv2
import socket
import numpy as np

ip = "100.125.37.104"


port = 40464
buffer = 65536

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))

print(f"listening for stream")

while True:
    try:
        packet, addr = sock.recvfrom(buffer) #tar opp dataen fra serveren
        #print(f"Received {len(packet)} bytes from {addr}") feilsøkings kode
        
        np_data = np.frombuffer(packet, dtype=np.uint8) 
        #gjør om dataen til en numpy array | jeg kjønner ikke helt hvordan denne delen funker (pga. KI), men jeg kjønner konseptet
        
        # Decode the JPEG buffer back into a frame
        frame = cv2.imdecode(np_data, cv2.IMREAD_COLOR) #dekrypterer framen tilbake til jpeg for visning

        if frame is not None:
            cv2.imshow('Receiver (Incoming Stream)', frame) #viser framen
            
        if cv2.waitKey(1) & 0xFF == ord('q'): #lar deg slutte ved å trykke Q
            break
            
    except Exception as e:
        print(f"Error: {e}") #printer ut error hvis noe går galt
        break

cv2.destroyAllWindows() 
sock.close() #lukker alt og slutter tilkoblingen