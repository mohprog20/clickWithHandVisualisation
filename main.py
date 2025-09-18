import clicker,time
import hand_tracking_base as htb
import cv2


clicker = clicker.Clicker(cooldown=1.0)
def main():
    ptime=0
    ctime=0
    cap=cv2.VideoCapture(0)
    detector=htb.handDetector()
    while True:
        success,img=cap.read()
        img=cv2.flip(img,1)
        img=detector.findHands(img)
        lmList=detector.findPosition(img)
        if len(lmList)!=0:
            print(lmList[4])
        ctime=time.time()
        fps=1/(ctime-ptime)
        ptime=ctime
        cv2.putText(img,f"FPS: {int(fps)}",(10,70),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,255),2)


        cv2.imshow("Image",img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()