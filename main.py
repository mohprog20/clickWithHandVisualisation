import clicker,time
import hand_tracking_base as htb
import cv2
import position_handler as ph

clicker = clicker.Clicker(cooldown=1.0)

pos_handler = ph.PositionHandler()
distance_percentage = 0.0255
click_distance = distance_percentage * (pos_handler.screen_size[0]**2+pos_handler.screen_size[1]**2)**0.5
offset_percentage=0.1


def main():
    last_distance = 0
    new_distance = 0

    ptime=0
    ctime=0
    cap=cv2.VideoCapture(0)
    detector=htb.handDetector(mode=False,maxHands=1,detectionCon=0.5,trackCon=0.5)
    while True:
        success,img=cap.read()
        img=cv2.flip(img,1)
        img=detector.findHands(img)
        lmList=detector.findPosition(img)
        ctime=time.time()
        fps=1/(ctime-ptime)
        ptime=ctime
        cv2.putText(img,f"FPS: {int(fps)}",(10,70),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,255),2)
        cv2.imshow("Image",img)
        cv2.waitKey(1)
        if len(lmList)!=0 and True:
            pos1=pos_handler.get_refernce_position(lmList[4][1:3])
            pos2=pos_handler.get_refernce_position(lmList[8][1:3])
            pos1=pos_handler.position_offset(pos1,offset_percentage)
            pos2=pos_handler.position_offset(pos2,offset_percentage)
            new_distance =(int(pos_handler.get_distance(pos1,pos2)))
            clicker.move_mouse((pos2[0]+pos1[0])/2,(pos2[1]+pos1[1])/2)

            if new_distance<40 and last_distance>=40:
                clicker.click()
            last_distance=new_distance
if __name__ == "__main__":
    main()