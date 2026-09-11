import cv2
import matplotlib.pyplot as plt


pathway="C:/Users/roygr/OneDrive - Buskerud fylkeskommune/VG2/Program fag/uke 37 python/programer/oppg 8/oppg8.png"

image= cv2.imread(pathway)
grayed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #gjør bilde svart-hvot for å kjøre raskere


face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
) #brukt for å finne front-seende fjes i bilder



face= face_classifier.detectMultiScale(
    grayed, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40) 
    #passer på at den ikke finner mange ting som ikke er fjes, og at den faktisk finner fjesene
)

for (x, y, w, h) in face:


    face_area = image[y:y+h, x:x+w]
    blurred_face = cv2.GaussianBlur(face_area, (751, 751), 0)
    image[y:y+h, x:x+w] = blurred_face #disse 3: tar målingene fra fjeset, blurrer fjeset og setter blurren tilbake hvor den skal



img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #gjør om til RGB 

plt.imshow(img_rgb) 
plt.axis('off') 
plt.show() #disse tre: viser bilde i farge og skrur av axis linjene

