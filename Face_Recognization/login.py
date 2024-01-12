from tkinter import *  # for GUI purpose
from tkinter import ttk  # stylish toolkit
from PIL import Image, ImageTk  # for image editing
from tkinter import messagebox
from pymongo.mongo_client import MongoClient
import cv2                                # ML algorithum
from main import Face_Recognizaion_System
from register import Register
def main():
    win = Tk()
    app = Login(win)
    win.mainloop()

class Login:
    teacher_email = ""
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # window size geometry(width,height,x-axis,y-axis)
        self.root.title("Face Recognition System Login")

        # Image set Big Image
        img = Image.open("Images/login_bgm.jpg")  # Set Image Path
        img = img.resize((1530, 790))  # width , height  and ANTIALIAS used to convert high to low level image
        self.photoimg = ImageTk.PhotoImage(img)  # set image

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1530, height=790)  # image show on window place(x_axis,y_axis)

        main_frame = Frame(bg_img, bd=2, bg="black")
        main_frame.place(x=610, y=170, width=340, height=450)

        # login Image
        img1 = Image.open("Images/login_images.png")  # Set Image Path
        img1 = img1.resize((120, 100))  # width ,height  and ANTIALIAS used to convert high to low level image
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimg1, bg="black", borderwidth=0)
        lblimg1.place(x=680, y=175, width=200, height=100)

        # get started label
        get_str = Label(main_frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # username label
        username = Label(main_frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        # username input
        self.txtuser = ttk.Entry(main_frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        # password label
        password = Label(main_frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        # password input
        self.txtpassword = ttk.Entry(main_frame, show="*", font=("times new roman", 15, "bold"))
        self.txtpassword.place(x=40, y=250, width=270)

        # check button
        self.check_button = Checkbutton(main_frame, font=("times new roman", 12, "bold"), command=self.show_password, text="show password", activebackground="white", foreground="black")
        self.check_button.place(x=40, y=285)

        ####### Icon Images #########
        # user icon
        img2 = Image.open("Images/login_images.png")  # Set Image Path
        img2 = img2.resize((25, 25))  # width ,height  and ANTIALIAS used to convert high to low level image
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimg2, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=325, width=25, height=25)

        # password icon
        img3 = Image.open("Images/lock.png")  # Set Image Path
        img3 = img3.resize((32, 27))  # width ,height  and ANTIALIAS used to convert high to low level image
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimg3, bg="black", borderwidth=0)
        lblimg3.place(x=650, y=396, width=32, height=27)

        # login Button
        loginbtn = Button(main_frame, text="Login", font=("times new roman", 15, "bold"), command=self.login, bd=3, relief=RIDGE, fg="white", bg="purple", activeforeground="white", activebackground="purple")
        loginbtn.place(x=110, y=320, width=120, height=35)

        # register Button
        regibtn = Button(main_frame, text="New User Register", command=self.register_window, font=("times new roman", 14, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        regibtn.place(x=16, y=360, width=160)

        # forgot Button
        forgonbtn = Button(main_frame, text="ForgetPassword", command=self.forgot_password, font=("times new roman", 14, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgonbtn.place(x=9, y=400, width=160)

    # ========= Open register window on the login page
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    # ====== Show Password =======
    def show_password(self):
        if self.txtpassword.cget('show') == '*':
            self.txtpassword.config(show= '')
        else:
            self.txtpassword.config(show='*')

    def login(self):
        if self.txtuser.get()=="" or self.txtpassword.get()=="":
            messagebox.showerror("Error", "All field required")
        else:
            client = MongoClient("mongodb://localhost:27017/")
            db = client["FaceRecognization"]
            collection = db["Register"]

            if collection.find_one({'$and': [{"email": self.txtuser.get()}, {"pass": self.txtpassword.get()}]}) is not None:
                open_main = messagebox.askyesno("YesNo", "Access only Authority Person")
                if open_main > 0:
                    teacher_email = self.txtuser.get()
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognizaion_System(self.new_window)
                else:
                    if not open_main:
                        return
            else:
                messagebox.showerror("Error", "please enter valid username and password")
            client.close()

    # ============ Reset Password =============
    def reset_pass(self):
        if self.combo_security_Q.get()== "Select":
            messagebox.showerror("Error", "Select security Quetion", parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please Enter The answer", parent=self.root2)
        elif self.newpassword.get() == "":
            messagebox.showerror("Error", "Please Enter the new password", parent=self.root2)
        else:
            client = MongoClient("mongodb://localhost:27017/")
            db = client["FaceRecognization"]
            collection = db["Register"]
            if collection.find_one({'$and': [{"email": self.txtuser.get()}, {"securityQ": self.combo_security_Q.get()}, {"securityA": self.txt_security.get()}]}) is not None:
                collection.update_one({'$and': [{"email": self.txtuser.get()}, {"securityQ": self.combo_security_Q.get()}, {"securityA": self.txt_security.get()}]}, {'$set': {"pass": self.newpassword.get()}})
                messagebox.showinfo("successful", "Password Updated successfully", parent=self.root2)
                self.root2.destroy()
                client.close()
            else:
                messagebox.showerror("Error", "Please Enter correct Answer", parent=self.root2)


    # ============ Forget password button ===============
    def forgot_password(self):
        if self.txtuser.get()== "":
            messagebox.showerror("Error", "Please Enter the Email address to reset the password", parent=self.root)
        else:
            client = MongoClient("mongodb://localhost:27017/")
            db = client["FaceRecognization"]
            collection = db["Register"]

            if collection.find_one({"email": self.txtuser.get()}) is not None:
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")            #width, height, x, y
                forgot_label = Label(self.root2, text="Forget Password", font=("times new roman", 15, "bold"), fg="red", bg="white")
                forgot_label.place(x=0, y=10, relwidth=1)

                # security quetion
                security_Q = Label(self.root2, text="Select Security", font=("times new roman", 20, "bold"), bg="white")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your favorite Movie")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                # security Answer
                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 20, "bold"), bg="white")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2,  font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                # new password
                new_password = Label(self.root2, text="New Password", font=("times new roman", 20, "bold"), bg="white")
                new_password.place(x=50, y=220)

                self.newpassword = ttk.Entry(self.root2, font=("times new roman", 15))
                self.newpassword.place(x=50, y=250, width=250)

                # Reset Password Button
                btn = Button(self.root2, text="Reset", command=self.reset_pass, font=("times new roman", 20, "bold"), bg="green", fg="white")
                btn.place(x=100, y=290)
            else:
                messagebox.showerror("Error", "Please enter the valid user name", parent=self.root2)
            client.close()


if __name__ == "__main__":
    main()