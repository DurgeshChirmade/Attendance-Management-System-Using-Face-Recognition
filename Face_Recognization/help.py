from tkinter import *  # for GUI purpose
from tkinter import ttk  # stylish toolkit
from PIL import Image, ImageTk  # for image editing
from tkinter import messagebox
from pymongo.mongo_client import MongoClient
import cv2                                # ML algorithum


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # window size geometry(width,height,x-axis,y-axis)
        self.root.title("Face Recognition System")

        # Title
        title_lb1 = Label(self.root, text="Help", font=("times new roman", 35, "bold"), bg="white",fg="blue")  # Title
        title_lb1.place(x=0, y=0, width=1530, height=55)

        img_top = Image.open("Images/computer-303283__480.jpeg")  # Set Image Path
        img_top = img_top.resize((1530, 750))  # width , height  and ANTIALIAS used to convert high to low level image
        self.photoimg_top = ImageTk.PhotoImage(img_top)  # set image

        lb_img = Label(self.root, image=self.photoimg_top)
        lb_img.place(x=0, y=55, width=1530, height=750)  # image show on window place(x_axis,y_axis)

        lbl1 = Label(lb_img, text="Gmail", font=("verdana", 40, "bold"), bg="white")
        lbl1.place(x=700, y=60)

        lbl1 = Label(lb_img, text="padolekiran2001@gmail.com", font=("verdana", 25, "bold"), bg="white")
        lbl1.place(x=500, y=200)

        lbl2 = Label(lb_img, text="chirmadedurgesh@gmail.com", font=("verdana", 25, "bold"), bg="white")
        lbl2.place(x=500, y=300)

        lbl2 = Label(lb_img, text="sahilgurav233@gmail.com", font=("verdana", 25, "bold"), bg="white")
        lbl2.place(x=500, y=400)



if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()