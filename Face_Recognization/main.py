import tkinter.messagebox
from tkinter import *  # for GUI purpose
from tkinter import ttk  # stylish toolkit
from PIL import Image, ImageTk  # for image editing
from student import Student
from Train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from help import Help
import os                    # Taking photos from Directory

class Face_Recognizaion_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # window size geometry(width,height,x-axis,y-axis)
        self.root.title("Face Recognition System")

        # Image set Big Image
        img = Image.open("Images/bigImage.jpg")  # Set Image Path
        img = img.resize((1530, 790))  # width , height  and ANTIALIAS used to convert high to low level image
        self.photoimg = ImageTk.PhotoImage(img)  # set image

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1530, height=790)  # image show on window place(x_axis,y_axis)

        title_lb1 = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="red") #Title
        title_lb1.place(x=0, y=0, width=1530, height=45)

        # student button
        img1 = Image.open("Images/studentbutton.jpg")  # Set Image Path
        img1 = img1.resize((220, 220))  # width ,height  and ANTIALIAS used to convert high to low level image
        self.photoimg1 = ImageTk.PhotoImage(img1)  # set image

        bt1 = Button(bg_img, image=self.photoimg1, command=self.student_details, cursor="hand2")  #button and cursor chnage to hand
        bt1.place(x=200, y=100, width="220", height="220")

        bt1_1 = Button(bg_img, text="Student Details", command=self.student_details,  cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")  # button, cursor chnage to hand, set text bottom of image
        bt1_1.place(x=200, y=320, width="220", height="40")

        # Detect Face button
        img2 = Image.open("Images/facedetector.png")  # Set Image Path
        img2 = img2.resize((220, 220))  # width ,height  and ANTIALIAS used to convert high to low level image
        self.photoimg2 = ImageTk.PhotoImage(img2)  # set image

        bt2 = Button(bg_img, image=self.photoimg2, cursor="hand2", command=self.face_data)  # button and cursor chnage to hand
        bt2.place(x=500, y=100, width="220", height="220")

        bt2_2 = Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")  # button, cursor chnage to hand, set text bottom of image
        bt2_2.place(x=500, y=320, width="220", height="40")

        # Attendance button
        img3 = Image.open("Images/Attendance.jpg")  # Set Image Path
        img3 = img3.resize((220, 220))  # width ,height  and ANTIALIAS used to convert high to low level image
        self.photoimg3 = ImageTk.PhotoImage(img3)  # set image

        bt2 = Button(bg_img, image=self.photoimg3, cursor="hand2", command=self.attendance_data )  # button and cursor chnage to hand
        bt2.place(x=800, y=100, width="220", height="220")

        bt2_2 = Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")  # button, cursor chnage to hand, set text bottom of image
        bt2_2.place(x=800, y=320, width="220", height="40")

        # Help button
        img4 = Image.open("Images/photo_help.jpg")  # Set Image Path
        img4 = img4.resize((220, 220))  # width ,height  and ANTIALIAS used to convert high to low level image
        self.photoimg4 = ImageTk.PhotoImage(img4)  # set image

        bt2 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.help_data)  # button and cursor change to hand
        bt2.place(x=1100, y=100, width="220", height="220")

        bt2_2 = Button(bg_img, text="Help", cursor="hand2", command=self.help_data, font=("times new roman", 15, "bold"), bg="darkblue",fg="white")  # button, cursor chnage to hand, set text bottom of image
        bt2_2.place(x=1100, y=320, width="220", height="40")

        # Train Data button
        img5 = Image.open("Images/traindata.jpg")  # Set Image Path
        img5 = img5.resize((220, 220))  # width ,height  and ANTIALIAS used to convert high to low level image
        self.photoimg5 = ImageTk.PhotoImage(img5)  # set image

        bt2 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.train_data)  # button and cursor change to hand
        bt2.place(x=200, y=400, width="220", height="220")

        bt2_2 = Button(bg_img, text="Train Data", command=self.train_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue",fg="white")  # button, cursor change to hand, set text bottom of image
        bt2_2.place(x=200, y=620, width="220", height="40")

        # Photos button
        img6 = Image.open("Images/photos.jpg")  # Set Image Path
        img6 = img6.resize((220, 220))  # width ,height  and ANTIALIAS used to convert high to low level image
        self.photoimg6 = ImageTk.PhotoImage(img6)  # set image

        bt2 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.open_img)  # button and cursor chnage to hand
        bt2.place(x=500, y=400, width="220", height="220")

        bt2_2 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue",fg="white")  # button, cursor change to hand, set text bottom of image
        bt2_2.place(x=500, y=620, width="220", height="40")

        # Developer button
        img7 = Image.open("Images/developer.jpeg") #Set Image Path
        img7 = img7.resize((220, 220))  # width ,height  and ANTIALIAS used to convert high to low level image
        self.photoimg7 = ImageTk.PhotoImage(img7)  # set image

        bt2 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.developer_data)  # button and cursor change to hand
        bt2.place(x=800, y=400, width="220", height="220")

        bt2_2 = Button(bg_img, text="Developer", cursor="hand2", command=self.developer_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")  # button, cursor change to hand, set text bottom of image
        bt2_2.place(x=800, y=620, width="220", height="40")

        # Exit button
        img8 = Image.open("Images/Exit.png")  # Set Image Path
        img8 = img8.resize((220, 220))  # width ,height  and ANTIALIAS used to convert high to low level image
        self.photoimg8 = ImageTk.PhotoImage(img8)  # set image

        bt2 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.iExit)  # button and cursor chnage to hand
        bt2.place(x=1100, y=400, width="220", height="220")

        bt2_2 = Button(bg_img, text="Exit", cursor="hand2", command=self.iExit, font=("times new roman", 15, "bold"), bg="darkblue",fg="white")  # button, cursor change to hand, set text bottom of image
        bt2_2.place(x=1100, y=620, width="220", height="40")

    def open_img(self):
        os.startfile("Data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition", "Are you sure exit this project",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

        #=========== Function Button ============
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognizaion_System(root)
    root.mainloop()
