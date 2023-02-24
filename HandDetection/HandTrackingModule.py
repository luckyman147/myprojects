import mediapipe as mp 
import cv2
import time

class handDetector():
    def __init__(self,mode=False,maxHands=2,detectionCon=0.5,trackConf=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectCon=detectionCon
        self.trackConf=trackConf

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        
        self.mpDraw=mp.solutions.drawing_utils
    def findHands(self,img,draw=True):

    
        imgRGB = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        self.results = self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
               if draw:
                    self.mpDraw.draw_landmarks(img,handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img
          
    def FindPosition(self,img,HandNo=0,draw=True):
        lmlist=[]
        if self.results.multi_hand_landmarks:
            myhand= self.results.multi_hand_landmarks[HandNo]
            for id,lm in enumerate(myhand.landmark):
                    #  print(id,lm)
                    h,w,c=img.shape
                    cx,cy=int(lm.x*w),int(lm.y*h)
                    #print(id, cx,cy)
                    lmlist.append([id,cx,cy])
                    if draw:
                        cv2.circle(img,(cx,cy),15,(155,46,37),cv2.FILLED)
        return lmlist              
def main():
    ctime=0
    ptime=0
    cap = cv2.VideoCapture(0)
    detector=handDetector()
    while True:
        success, img = cap.read()
        img=detector.findHands(img)
        lmlist=detector.FindPosition(img)
        if len(lmlist)!=0:
            print(lmlist[4])
        ctime=time.time()
        fps=1/(ctime-ptime)
        ptime=ctime
        cv2.putText(img,"fps"+str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,
                    3,(255,0,255),2)
        cv2.imshow('Image', img)
        if cv2.waitKey(1) == ord('q'):
            break

    
if   __name__=='__main__':
    main()