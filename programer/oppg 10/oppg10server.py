#DETTE ER EN KOPI AV KODEN FOR SERVEREN PÅ UBUNTU, DET ER NOEN SMÅ FORSKJELLIER, MEN INGENTING VIKTIG

import socket
import cv2

ip="100.125.37.104" #tailscale IP for windows maskin

port = 40464

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cap=cv2.VideoCapture(0) #tar opp video streamen

while cap.isOpened():
    ret, frame = cap.read() #leser streamen
    if not ret: #passer på at streamen er lesbar
        print("gah")
        break

    encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 89]) #tar framen og krypterer den slik at den er enkel å sende, og kan dekrypteres som jpg

    data = buffer.tobytes() #dataen som skal bli sendt

    if len(data) > 65507: #passer på at dataen ikke er for stor for å sendes
        print("uh oh too big")

    socket_server.sendto(data, (ip, port)) #sender dataen til den andre maskinen

    cv2.imshow('Webcam Stream', frame) #viser streamen lokalt også
    if cv2.waitKey(1) & 0xFF == ord('q'): #gjør at man kan slutte ved å trykke Q
        break


cap.release()
cv2.destroyAllWindows()
socket_server.close() #lukker alt som på clienten, men også stopper å ta opp video streamen