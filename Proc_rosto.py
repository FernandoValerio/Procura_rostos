import os
from tkinter import filedialog
import cv2
from retinaface import RetinaFace
import matplotlib.pyplot as plt

def lista_pastas(path):
    return os.listdir(path)

def arquivos(path):
    folder = lista_pastas(path)
    ext=[]
    i=0
    arquivo = []
    while i<len(folder):
        ext.append(folder[i][int(len(folder[i])-4):len(folder[i])])
        if (ext[i]=='.jpg' or ext[i]=='.jpeg' or ext[i]=='.png' or ext[i]=='.JPG' or ext[i]=='.PNG'):
            arquivo.append(path+"\\"+folder[i])
        i=i+1
    return (arquivo)

def cria_imagem (imagem,path,executa=True):
    if executa:
        try:
            cv2.imwrite(path, imagem)
        except:
            print("erro")


def procura_rostos(path, nome ,salva, path_salva="", alinha=True):
    faces = RetinaFace.extract_faces(path, align=alinha)
    if salva:
        i=0
        for face in faces:
            i=i+1
           # plt.imshow(face)
            plt.imsave(path_salva+"\\face_"+str(i)+"_"+nome,face)
        plt.show()



path_video= filedialog.askopenfilename()
path_img = filedialog.askdirectory()
taxa = input("Quantos segundos por captura?")

#if procura:
#    for path_quest in path_busca:
#        print(path_quest)
#        procura_rostos(path_quest,True,path+"\\faces",False)


# inicia o vídeo
cap = cv2.VideoCapture(path_video)

# verifica a razão de frames
fps = cap.get(cv2.CAP_PROP_FPS)
fim_vd, frame = cap.read()
i=0
imagecount = 0
e
while fim_vd:

#    cria_imagem(path_img, frame)
    if (i%(int(int(fps)*int(taxa)))==0):
        nome="Capture_"+str(imagecount+1)+".png"
        arquivo = path_img+'/'+nome
        imagecount=imagecount+1
        cria_imagem(frame,arquivo) #problema no tamanho do path
        procura_rostos(arquivo,nome, True, path_img, False)
    i=i+1

    cv2.imshow("Frame", frame)
    cv2.waitKey(2)
    fim_vd, frame = cap.read()

cap.release()
cv2.destroyAllWindows()