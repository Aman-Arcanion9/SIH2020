import cv2
import os

class ImageCap():
    for i in range(3):
        videoCaptureObject = cv2.VideoCapture(0)
        result = True
        f_name = "pic"
        temp_name = "pic"
        cnt = 1
        loc_path = os.getcwd()
        while os.path.exists(str(loc_path) + "/" + f_name + ".jpg"):
        	f_name = temp_name + "({})".format(cnt)
        	cnt += 1
        f_name += ".jpg"
        while(result):
            ret,frame = videoCaptureObject.read()
            cv2.imwrite(f_name,frame)
            result = False
        videoCaptureObject.release()
        cv2.destroyAllWindows()

ImageCap().run()
