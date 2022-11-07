import sys
import cv2
from time import sleep
from PIL import Image 
import shadow

def main_app(name,face_id,emaild):
        try:
            cascadePath = r"ShadowGui\FaceRecognition\haarcascade_frontalface_default.xml"
            face_cascade = cv2.CascadeClassifier(cascadePath)
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            recognizer.read(f'ShadowGui/FaceRecognition/trainer/{name}_{emaild}_trainer.yml')
            cap = cv2.VideoCapture(0)
            pred = 0
            i = 0
        except Exception as e :
            print(e)
            sys.exit()
        while True:
            ret, frame = cap.read()
            #default_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,1.3,5)

            for (x,y,w,h) in faces:


                roi_gray = gray[y:y+h,x:x+w]

                id,confidence = recognizer.predict(roi_gray)
                confidence = 100 - int(confidence)
                pred = 0
                if confidence > 50:
                    #if u want to print confidence level
                            confidence = 100 - int(confidence)
                            pred += +1
                            text = name.upper()
                            font = cv2.FONT_HERSHEY_PLAIN
                            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            frame = cv2.putText(frame, text, (x, y-4), font, 1, (0, 255, 0), 1, cv2.LINE_AA)

                            ########################################################
                            # ShadowGui\FaceRecognition\samples\{str(count)}.{str(face_id)}.{str(emaild)}.{str(emaild)}.jpg
                            if pred > 0 : 
                                i+=1
                                # print('h',i)
                                if i >5 :
                                    dim =(124,124)
                                    img = cv2.imread(f"ShadowGui\FaceRecognition\samples\\{pred}.{face_id}.{emaild}.{name}.jpg", cv2.IMREAD_UNCHANGED)
                                    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                                    cv2.imwrite(f"ShadowGui\FaceRecognition\samples\\50.{face_id}.{emaild}.{name}.jpg", resized)
                                    Image1 = Image.open(r"ShadowGui\FaceRecognition\2.png") 
                                    
                                    # make a copy the image so that the  
                                    # original image does not get affected 
                                    Image1copy = Image1.copy() 
                                    Image2 = Image.open(f"ShadowGui\FaceRecognition\samples\\25.{face_id}.{emaild}.{name}.jpg") 
                                    Image2copy = Image2.copy() 
                                    
                                    # paste image giving dimensions 
                                    Image1copy.paste(Image2copy, (195, 114)) 
                                    
                                    # save the image  
                                    Image1copy.save("ShadowGui\FaceRecognition\end.png") 
                                    shadow.speak("verification successful")
                                    frame = cv2.imread("ShadowGui\FaceRecognition\end.png", 1)

                                    cv2.imshow(f"Valid User {name}",frame)
                                    cv2.waitKey(5000)
                                    cap.release()
                                    cv2.destroyAllWindows()
                                    return "done"
                                    # shadow.startex(name.capitalize())
                                                         
                else:   
                            pred += -1
                            text = "UnknownFace"
                            font = cv2.FONT_HERSHEY_PLAIN
                            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                            frame = cv2.putText(frame, text, (x, y-4), font, 1, (0, 0,255), 1, cv2.LINE_AA)

            cv2.imshow("image", frame)


            if cv2.waitKey(20) & 0xFF == ord('q'):
                #if not match then press q to exit
                cv2.waitKey(5000)
                cap.release()
                cv2.destroyAllWindows()
                return 'None'


def namedetect():
    # userEmail = input('Enter your Email :').lower() # for login button take name on interface
    # namelist,nameid,nameEmail = [],[],[]
    # with open(r"ShadowGui\FaceRecognition\namelist.txt") as f :
    #     for i in f:
    #         namelist.append(i.split('\n')[0].split('-')[0])
    #         nameid.append(i.split('\n')[0].split('-')[1])
    #         nameEmail.append(i.split('\n')[0].split('-')[2])
    # if userEmail in nameEmail:
    #     index = nameEmail.index(userEmail)
    #     face_id = nameid[index]
    #     username = namelist[index]
    # else:
    #     print('You Email Not Matching In Ourdata. Try again With Correct Email\n')
    #     sys.exit()
    # main_app(username,face_id,userEmail)
    pass


if __name__ =="__main__":
    # namedetect()
    # main_app(username,face_id)
    pass