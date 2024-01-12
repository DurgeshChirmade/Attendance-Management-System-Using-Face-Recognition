import os
from tkinter import *  # for GUI purpose
from tkinter import ttk  # stylish toolkit
from PIL import Image, ImageTk  # for image editing
from tkinter import messagebox
import cv2                                # ML algorithum
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # window size geometry(width,height,x-axis,y-axis)
        self.root.title("Face Recognition System")

        # Title
        title_lb1 = Label(self.root, text="Train data set", font=("times new roman", 35, "bold"), bg="white", fg="red") # Title
        title_lb1.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open("Images/studentdetails.jpg")  # Set Image Path
        img_top = img_top.resize((1530, 325))  # width , height  and ANTIALIAS used to convert high to low level image
        self.photoimg_top = ImageTk.PhotoImage(img_top)  # set image

        lb_img = Label(self.root, image=self.photoimg_top)
        lb_img.place(x=0, y=55, width=1530, height=325)  # image show on window place(x_axis,y_axis)

        # Button
        reset_button = Button(self.root, text="Train data", command=self.train_classifier, width=18, font=("times new roman", 18, "bold"), bg="red",fg="white")
        reset_button.place(x=0, y=380, width=1530, height=60)

        img_bottom = Image.open("Images/studentdetails.jpg")  # Set Image Path
        img_bottom = img_bottom.resize((1530, 325))  # width , height  and ANTIALIAS used to convert high to low level image
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)  # set image

        lb_img = Label(self.root, image=self.photoimg_bottom)
        lb_img.place(x=0, y=440, width=1530, height=325)  # image show on window place(x_axis,y_axis)

    def train_classifier(self):
        data_dir = ("Data")  # images data
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)] # taking all images

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') # Gray scale image
            imageNp = np.array(img,'uint8') # data type
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13           # when click enter window close
        ids = np.array(ids)                # perormance better

        # ====== Train the Classifier And save ====== #
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()