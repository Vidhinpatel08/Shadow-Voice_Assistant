import sys
# import Model_Trainer
from FaceRecognition import Model_Trainer
import loginShadow
import cv2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #create a video capture object which is helpful to capture videos through webcam
cam.set(3, 640) # set video FrameWidth
cam.set(4, 480) # set video FrameHeight


detector = cv2.CascadeClassifier(r'ShadowGui\FaceRecognition\haarcascade_frontalface_default.xml')
#Haar Cascade classifier is an effective object detection approach

############### for Registtion Take id & name by user ####################


face_id = input("Enter a Numeric user ID  here:  ") 
#Use integer ID for every new face (0,1,2,3,4,5,6,7,8,9........)

name = input("Enter a Name of user  here:  ")
#Use integer ID for every new face (0,1,2,3,4,5,6,7,8,9........)

# namelist file management 

f = open(r'ShadowGui\FaceRecognition\namelist.txt')
value = f.read(1)
f.close()
if value  == '':
    with open(r'ShadowGui\FaceRecognition\namelist.txt','a') as f :
        nameadd = name +"-"+ face_id+'\n'
        f.write(nameadd)
else:
    with open(r'ShadowGui\FaceRecognition\namelist.txt') as f :
        namelist,nameid = [],[]
        for i in f:
                namelist.append(i.split('\n')[0].split('-')[0])
                nameid.append(i.split('\n')[0].split('-')[1])
        # print(namelist)
        # print(nameid)
        if name in namelist:
            print('You Name Already In Ourdata. Try again With Other name')
            sys.exit()
        elif face_id in nameid:
            print('You FAce ID Number Already In Ourdata. Try again With Other ID')
            sys.exit()
        else:
            with open(r'ShadowGui\FaceRecognition\namelist.txt','a') as f :
                nameadd = name +"-"+ face_id+'\n'
                f.write(nameadd)

print("\nTaking samples, look at camera ....... ")
count = 0 # Initializing sampling face count

while True:

    ret, img = cam.read() #read the frames using the above created object
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #The function converts an input image from one color space to another
    faces = detector.detectMultiScale(converted_image, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2) #used to draw a rectangle on any image
        count += 1

        
        cv2.imwrite(f"ShadowGui\FaceRecognition\samples\{str(count)}.{str(face_id)}.{str(name)}.jpg", converted_image[y:y+h,x:x+w])
        # To capture & Save images into the datasets folder

        cv2.imshow('image', img) #Used to display an image in a window

    k = cv2.waitKey(100) & 0xff # Waits for a pressed key
    if k == 27: # Press 'ESC' to stop
        break
    elif count >= 100 : # Take 100 sample (More sample --> More accuracy)
         break

print("Samples taken now closing the program....\n\n")
cam.release()
cv2.destroyAllWindows()


# tranier Model 
Model_Trainer.starttrainer(name)

print('For login Continue....')

# login shadow
loginShadow.namedetect()

