#primero vamos a importar los modulos desde la liberia cvzone la cual depende a su vez de tensorflow, mediapipe, cv2, keras, numpy, serial
"""
The cvzone library is a Python library that provides computer vision and machine learning functionality. 
It depends on several other libraries, including TensorFlow, Mediapipe, OpenCV (cv2), Keras, and NumPy. 
The library provides a range of tools for image and video processing, including object detection, face recognition, 
and pose estimation. It also includes pre-trained models for various tasks, such as facial landmark detection and hand tracking.
"""
import cvzone.HandTrackingModule
import cv2
import cvzone.SerialModule
#cap es para la captura de video si es la camara por defecto deberia de ser la 0, en caso de ser externa 1
cap = cv2.VideoCapture(0)
#definimos los parametros para la detecion de la mano
detector = cvzone.HandTrackingModule.HandDetector(maxHands = 1, detectionCon = 1)
#definimos la configuracion del puerto serial
mySerial = cvzone.SerialModule.SerialObject("COM3", 9600, 1)
#loop infinito
while True:
    #realizamos la captura de imagen
    successs, img = cap.read()
    #de la imagen detectamos la o las manos
    img = detector.findHands(img)
    #detectamos la posicion de la o las mismas
    lmList, bbox = detector.findPosition(img)
    #en caso de que obtengamos un valor True ejecutamos:
    if lmList:
        #detecion de los dedos arriba
        fingers = detector.fingersUp()
        print(fingers)
        #Mandamos la informacion de los dedos a traves del puerto serial
        mySerial.sendData(fingers)
    #abrimos una ventana para mostrar la imagen de la cual se realiza la extraccion de datos
    cv2.imshow("Image",img)
    cv2.waitKey(1)