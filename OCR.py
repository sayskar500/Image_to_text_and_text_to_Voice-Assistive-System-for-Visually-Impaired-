import cv2
import os
import glob


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
 
cv2.namedWindow("test")
 
img_counter = 0

path = os.getcwd()
fileSystem = glob.glob(path + '/images/*')

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)
 
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.jpg".format(img_counter)
        cv2.imwrite(path + '/images/' + img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
 
cam.release()
 
cv2.destroyAllWindows()

# this line of code automatically runs Conversion file at the end
os.system('python Conversion.py')