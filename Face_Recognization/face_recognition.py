from tkinter import *  # for GUI purpose
from PIL import Image, ImageTk  # for image editing
from datetime import datetime
import cv2                                # ML algorithum
from pymongo.mongo_client import MongoClient
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Face_recognition:
    sender_email = 'padolekiran2001@gmail.com'
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # window size geometry(width,height,x-axis,y-axis)
        self.root.title("Face Recognition System")

        # Title
        title_lb1 = Label(self.root, text="Face Recognization", font=("times new roman", 30, "bold"), bg="white", fg="green")  # Title
        title_lb1.place(x=0, y=0, width=1530, height=45)

        img_full = Image.open("Images/facial_recognition_system_identification_digital.jpeg")  # Set Image Path
        img_full = img_full.resize((1530, 760))  # width , height  and ANTIALIAS used to convert high to low level image
        self.photoimg_full = ImageTk.PhotoImage(img_full)  # set image

        lb_img = Label(self.root, image=self.photoimg_full)
        lb_img.place(x=0, y=55, width=1530, height=760)  # image show on window place(x_axis,y_axis)

        # Button
        reset_button = Button(lb_img, text="Face Recognization", command=self.face_recog, width=18, font=("times new roman", 18, "bold"), bg="darkgreen", fg="white")
        reset_button.place(x=640, y=670, width=250, height=40)

########### Attendance ########################
    def mark_attedance(self, name, roll, dep, div, email):
        with open("Attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list=[]
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if (name not in name_list) and (roll not in name_list) and (dep not in name_list) and (div not in name_list) and (email not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"{name},{roll},{dep},{div},{email},{d1},{dtString},Present\n")

############ Email Sending ####################
    def mail_send_m(self, email, name):

        email = email
        name = name

        body_mail = name + " is absent for today's lecture"

        # Set up the email details
        receiver_email = email
        subject = "Presenty of your child"  # subject for mail
        body = body_mail  # "this is about message"    #this is body part of mail

        # Create a multipart message and set the headers
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        # Create SMTP session for sending the email
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with your SMTP server and port
        smtp_server.starttls()  # Secure the connection
        smtp_server.login(self.sender_email,
                          'dllyqedtdurwlamp')  # Use your app-specific password instead of your Google account password
        smtp_server.sendmail(self.sender_email, receiver_email, message.as_string())
        smtp_server.quit()
        print("mail is send!!")

############# Face Recognization ###############
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)      # convert Image into Gray scale
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)
            coord = []
            for(x, y, w, h) in features: # making rectangle
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))  #check same image or not

                client = MongoClient("mongodb://localhost:27017/")
                db = client["FaceRecognization"]
                collection = db["Student"]

                name = collection.find_one({"studentId": str(id)}, {"_id": 0, "name": 1})

                roll = collection.find_one({"studentId": str(id)}, {"_id": 0, "roll": 1})

                dept = collection.find_one({"studentId": str(id)}, {"_id": 0, "dep": 1})

                email = collection.find_one({"studentId": str(id)}, {"_id": 0, "Email": 1})

                div = collection.find_one({"studentId": str(id)}, {"_id": 0, "division": 1})

                if name is not None:
                    name = name['name']
                    roll = str(roll['roll'])
                    dept = dept['dep']
                    div = div['division']
                    email =email['Email']

                if confidence > 77:
                    cv2.putText(img, f"Roll No: {roll}", (x, y-70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 248, 220), 3)
                    cv2.putText(img, f"Name: {name}", (x, y - 45), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 248, 220), 3)
                    cv2.putText(img, f"Department: {dept}", (x, y-15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 248, 220), 3)
                    self.mark_attedance(name, roll, dept, div, email)
                else:    #Unknown Face
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord=[x, y, w, y]
                client.close()
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(0) # laptop camera 0 other 1

        with open("Attendance.csv", "r+") as f:
            f.truncate()

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        now = datetime.now()
        d1 = now.strftime("%d_%m_%y")
        dtString = now.strftime("%H_%M_%S")
        file_name = "D_M_Y " + d1 + " H_M_S " + dtString + ".csv"

        f = open("Attendance.csv", 'r+')
        first_line = f.readline()
        temp = first_line.split(",")
        client = MongoClient("mongodb://localhost:27017/")
        db = client["FaceRecognization"]
        collection = db["Student"]
        my_cursors = collection.find({"dep": temp[2], "division": temp[3]})
        f.close()
        # copy data from Attendence.csv file
        with open("Attendance.csv", "r+") as f:
            with open("Attendance/"+file_name, "a+") as new_file:
                new_file.writelines(f.readline())

        # Final attendance file
        with open("Attendance.csv", "r+") as f:
            new_file = open("Attendance/"+file_name, "a+")
            content = f.read()
            for i in my_cursors:
                if i['roll'] in content and i['Email'] in content and i['name'] in content:
                    continue
                else:
                    new_file.writelines(f"{i['name']},{i['roll']},{i['dep']},{i['division']},{i['Email']},{'-'},{'-'},Absent"+"\n")
            new_file.close()

            # Give read permissions
            os.chmod("Attendance/"+file_name, 0o600)
            client.close()
        with open("Attendance/"+file_name, "r") as sending_file:
            content = sending_file.readlines()
            for i in content:
                if "Absent" in i:
                    temp= i.split(",")
                    self.mail_send_m(temp[4], temp[0])




if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()