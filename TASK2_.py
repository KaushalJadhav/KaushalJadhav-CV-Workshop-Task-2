# PROBLEM STATEMENT: ( in Opencv Python)
# Making a whiteboard using the ball in 
# the user’s hand as a pen pointer to write 
# on air and perform various functions 
# such as deletion and clear screen.
import cv2
import numpy as np 
import math
import statistics as stat

listi=[]
listj=[]
t=0
msg='Press Q to quit.Press C to clear screen.'
msg2='Press D for delete'

cap=cv2.VideoCapture(0)
# Get the video from Webcam
if cap.isOpened()==False:
# Check whether the video has been detected
# without any error
    print('error opening camera')
cv2.namedWindow('whiteboard',cv2.WINDOW_NORMAL)
cv2.namedWindow('original',cv2.WINDOW_NORMAL)
#frame_rate=int(cap.get(cv2.CAP_PROP_FPS))

while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        l=[]
#    Segmentation
        frame2=cv2.inRange(frame,(0,100,0),(100,255,100))
        frame3=np.full((frame2.shape[0],frame2.shape[1]),255,dtype='uint8')
# to initialise frame4 only once
        if t==0:
             frame4=np.copy(frame3)
             t=t+1
        contour,hierarchy=cv2.findContours(frame2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for i in range(len(contour)):
            area=cv2.contourArea(contour[i])
            l.append(int(area)) 
        #print(l)
# get the contour with max area
        if np.array(l).size>0:
         a=max(l)
         ind=0
# find the index
         for i in range(len(l)):
            if l[i]==a:
                ind=i
         cv2.drawContours(frame3,contour,ind,0,thickness=-1)
# get the max area contour drawn
         pts=np.where(frame3==0)
# take mean of all points which are black
         meani=stat.mean(pts[1])
         meanj=stat.mean(pts[0])
# store the points in the list
         listi.append(meani)
         listj.append(meanj)
        #meani2=listi.append()
        if(len(listi)>=2):
         l3=len(listi)-2
         l4=len(listj)-2
# track the ball movement by drawing lines
         frame4=cv2.line(frame4,(frame4.shape[0]-listi[l3],listj[l4]),(frame4.shape[0]-listi[l3+1],listj[l4+1]),0,thickness=10,lineType=-1)
        img=np.copy(frame4)
        img=cv2.putText(img,msg,(0,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)
        img=cv2.putText(img,msg2,(0,48),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)
        cv2.imshow('whiteboard',img)

        p=cv2.waitKey(1)
# exit
        if p== ord('q')or p == ord('Q') :
         break
# clearscreen
        if p== ord('c') or p == ord('C'):
         frame4=np.full((frame3.shape[0],frame3.shape[1]),255,dtype='uint8')
# delete
        if p== ord('d') or p == ord('D'):
            l33=l3
            l44=l4
            while(1):
                k=cv2.waitKey(1) 
                if k==ord('b') or k==ord('B'):
                    break
                if k==ord('j') or k== ord('J'):
                    l33=l33-1
                    l44=l44-1
                if k==ord('d') or k== ord('D'):
                    l33=l33-1
                    l44=l44-1
                    if l44==0 or l33==0:
                        break
                    frame4=cv2.line(frame4,(listi[l33],listj[l44]),(listi[l33+1],listj[l44+1]),255,thickness=10,lineType=-1)
                cv2.imshow('whiteboard',frame4)
        cv2.imshow('whiteboard',frame4)
    else:
        break
cap.release()
cv2.destroyAllWindows