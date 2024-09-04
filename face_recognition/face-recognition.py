import numpy as np
import os
import face_recognition
import cv2 as cv

path="person"
images=[]
classNames=[]
personList=os.listdir(path)

for c1 in personList:
    curPerson=cv.imread(f'{path}/{c1}')
    images.append(curPerson)
    classNames.append(os.path.splitext(c1)[0])
print(classNames)

def findEncodeings(images):
    encodeList=[]
    for img in images:
        img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListisKnow=findEncodeings(images)
print(encodeListisKnow)
print('Encoding complete')

cap=cv.VideoCapture(0)
while True:
        frame,img=cap.read()

        imgs=cv.resize(img,(0,0),None,0.25,0.25)
        imgs=cv.cvtColor(imgs,cv.COLOR_BGR2RGB)
        faceCurentFrame=face_recognition.face_locations(imgs)
        encodeCurentFrame=face_recognition.face_encodings(imgs,faceCurentFrame)
        for encodeface,faceLoc in zip(encodeCurentFrame,faceCurentFrame):
            matches=face_recognition.compare_faces(encodeListisKnow,encodeface)
            faceDis=face_recognition.face_distance(encodeListisKnow,encodeface)
            matchIndex=np.argmin(faceDis)
            if matches[matchIndex]:
                 name=classNames[matchIndex].upper()
                 print(name)
                 y1,x2,y2,x1=faceLoc
                 y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
                 cv.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
                 cv.rectangle(img, (x1, y2-35), (x2, y2), (0, 0, 255), cv.FILLED)
                 cv.putText(img,name, (x1+6, y2-6),cv.FONT_HERSHEY_COMPLEX,1,(255, 255, 255), 2)





        cv.imshow("face recognition",img)
        k=cv.waitKey(1)
        if k == ord("x"):
           break
cap.release()
cv.destroyWindow()
