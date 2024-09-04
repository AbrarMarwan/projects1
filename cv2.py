import cv2
import numpy as np
# Reading image
# im=cv2.imread("C:/Users/victus/Pictures/DSC_0634-1.jpg")
# cv2.imshow("image",im)
# cv2.imwrite("image.png",im)
# cv2.waitKey(0)


# Reading videos
# video=cv2.VideoCapture("C:/Users/victus/Videos/POS.mp4")
# while True:
#     ret,frame=video.read()
#     if ret:
#         cv2.imshow("video",frame)
#         f=cv2.waitKey(1)
#         if f==ord('a'):
#             break
#     else:
#         break
# video.release()

# cap=cv2.VideoCapture(0)
# i=0
# print(cap.isOpened())
# while cap.isOpened():
#     ret,frame=cap.read()
#     if ret:
#         cv2.imshow("photo",frame)
#     k=cv2.waitKey(1)
#     if k==ord("a"):
#         cv2.imwrite(f"abrar{i}.png",frame )
#         i+=1
#     if k == ord("x"):
#         break
# cap.release()

# #Resizing images and video
# im=cv2.imread("C:/Users/victus/Pictures/DSC_0634-1.jpg")
# cv2.imshow("image",im)
# im_resized=cv2.resize(im,(500,600),interpolation=cv2.INTER_CUBIC)
# cv2.imshow("DAD",im_resized)
# cv2.waitKey(0)
# print(im.shape)

#cropping
# im=cv2.imread("C:/Users/victus/Pictures/DSC_0634-1.jpg")
# cv2.imshow("image",im)
# im_cropped=im[500:5000,300:1100]
# cv2.imshow("image_cropped",im_cropped)
# cv2.waitKey(0)

#drawing
# empty = np.zeros((600,600,3),dtype="uint8")
# #cv2.imshow("empty",empty)
# empty[0:200]=0,0,255
# empty[201:400]=255,255,255
# cv2.imshow("colored",empty)
# cv2.waitKey(0)


#line
imag=np.zeros((512,512,3),np.uint8)
#cv2.line(imag,(0,0),(512,512),(22,22,144),10)
#cv2.rectangle(imag,(240,270),(100,100),(151,88,0),20)
#cv2.rectangle(imag,(240,270),(100,100),(151,88,0),-1)
a=cv2.FONT_HERSHEY_PLAIN
cv2.putText(imag,"Abrar^_^",(100,200),a,4,(222,55,11))
cv2.imshow("line",imag)
cv2.waitKey(0)
cv2.destroyAllWindows()  