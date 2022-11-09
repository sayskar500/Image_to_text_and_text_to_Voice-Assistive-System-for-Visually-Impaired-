import cv2
import os
import glob

# system camera access via which image will be captured
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# image capturing window named "test"
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

    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

    elif k % 256 == 32:
        # SPACE pressed
        img_name = "image_captured{}.jpg".format(img_counter)
        cv2.imwrite(path + '/images/' + img_name, frame)
        print("{} written!".format(img_name))

        # count the number of images captured
        img_counter += 1
 
# the access to system camera is released
cam.release()

# image capturing window named "test"d is detroyed
cv2.destroyAllWindows()

# this line of code automatically runs "Conversion.py" file at the end
os.system('python Conversion.py')