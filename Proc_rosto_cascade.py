from tkinter import filedialog
import cv2
from retinaface import RetinaFace
import matplotlib.pyplot as plt

def cria_imagem (imagem,path,executa=True):
    if executa:
        try:
            cv2.imwrite(path, imagem)
        except:
            print("erro")


def detectFaces(path, nome ,salva, path_salva="", cascPath=''):

    faceCascade = cv2.CascadeClassifier(cascPath)
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=3,
        minSize=(10, 10),
        flags=cv2.CASCADE_SCALE_IMAGE)
    if len(faces) == 0:
        return()
    else:
        if salva:
            i=0
            for (x, y, w, h) in faces:
                # draw the face bounding box on the image
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                rosto = image[y:y+h,x:x+w]
                plt.imsave(path_salva + "\\face_" + str(i) + "_" + nome, rosto)
                i=i+1
                cv2.imwrite(path,image)

path_video= filedialog.askopenfilename()
path_img = filedialog.askdirectory()
cascPath = filedialog.askopenfilename()
taxa = input("Quantos segundos por captura?")


# inicia o vídeo
cap = cv2.VideoCapture(path_video)

# verifica a razão de frames
fps = cap.get(cv2.CAP_PROP_FPS)
fim_vd, frame = cap.read()
i=0
imagecount = 0

while fim_vd:

    if (i%(int(int(fps)*int(taxa)))==0):
        nome="Capture_"+str(imagecount+1)+".png"
        arquivo = path_img+'/'+nome
        imagecount=imagecount+1
        cria_imagem(frame,arquivo) #problema no tamanho do path
        detectFaces(arquivo,nome, True, path_img, cascPath)
    i=i+1

    cv2.imshow("Frame", frame)
    cv2.waitKey(2)
    fim_vd, frame = cap.read()

cap.release()
cv2.destroyAllWindows()