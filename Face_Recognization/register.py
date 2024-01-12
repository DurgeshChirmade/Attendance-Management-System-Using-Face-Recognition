from tkinter import *  # for GUI purpose
from tkinter import ttk  # stylish toolkit
from PIL import Image, ImageTk  # for image editing
from tkinter import messagebox
from pymongo.mongo_client import MongoClient

class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # window size geometry(width,height,x-axis,y-axis)
        self.root.title("Face Recognition System Register")

        # ============= Variables =============
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_check = IntVar()

        # Image set Big Image
        img = Image.open("Images/register_bgm.jpeg")  # Set Image Path
        img = img.resize((1530, 790))  # width , height  and ANTIALIAS used to convert high to low level image
        self.photoimg = ImageTk.PhotoImage(img)  # set image

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1530, height=790)  # image show on window place(x_axis,y_axis)

        # Main frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=450, y=130, width=670, height=600)

        # Label
        register_lb1 = Label(main_frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="darkgreen")
        register_lb1.place(x=20, y=20)

        # first name label
        fname = Label(main_frame, text="First Name", font=("times new roman", 20, "bold"), bg="white")
        fname.place(x=50, y=100)

        # first name input
        fname_entry = ttk.Entry(main_frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=140, width=250)

        # last name label
        last_name = Label(main_frame, text="Last Name", font=("times new roman", 20, "bold"), bg="white")
        last_name.place(x=370, y=100)

        # last name input
        self.last_name_entry = ttk.Entry(main_frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.last_name_entry.place(x=370, y=140, width=250)

        # contact label
        contact = Label(main_frame, text="Contact No", font=("times new roman", 20, "bold"), bg="white")
        contact.place(x=50, y=190)

        # contact input
        self.contact_entry = ttk.Entry(main_frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.contact_entry.place(x=50, y=230, width=250)

        # email label
        email = Label(main_frame, text="Email", font=("times new roman", 20, "bold"), bg="white")
        email.place(x=370, y=190)

        # email input
        self.email_entry = ttk.Entry(main_frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.email_entry.place(x=370, y=230, width=250)

        # security quetion
        security_Q = Label(main_frame, text="Select Security", font=("times new roman", 20, "bold"), bg="white")
        security_Q.place(x=50, y=280)

        self.combo_security_Q = ttk.Combobox(main_frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your favorite Movie")
        self.combo_security_Q.place(x=50, y=320, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(main_frame, text="Security Answer", font=("times new roman", 20, "bold"), bg="white")
        security_A.place(x=370, y=280)

        self.txt_security = ttk.Entry(main_frame,textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=320, width=250)

        # password Label
        passw = Label(main_frame, text="Password ", font=("times new roman", 20, "bold"), bg="white")
        passw.place(x=50, y=370)

        # password input
        self.txt_psw = ttk.Entry(main_frame, show="*", textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_psw.place(x=50, y=410)

        # confirm password label
        confirm_password = Label(main_frame, text="Confirm Password", font=("times new roman", 20, "bold"), bg="white")
        confirm_password.place(x=370, y=370) #30

        # confirm password input
        self.txt_confirmpsw = ttk.Entry(main_frame, show="*", textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_confirmpsw.place(x=370, y=410, width=250)

        # check button
        self.check_button_password = Checkbutton(main_frame, command=self.show_password, text="Show password", font=("times new roman", 12), bg="white")
        self.check_button_password.place(x=50, y=460)

        # =============  Check Button Condition ===================
        self.checkbtn = Checkbutton(main_frame, variable=self.var_check, text="I Agree The Terms and Conditions", font=("times new roman", 12), bg="white", onvalue=1, offvalue=0)
        self.checkbtn.place(x=50, y=490)

        # ============ Register Now Button ============================
        regibtn = Button(main_frame, text="Register Now", command=self.register_data, font=("times new roman", 14, "bold"), borderwidth=0,fg="white", bg="black", activeforeground="white", activebackground="black")
        regibtn.place(x=10, y=530, width=160)

        # ============ Login Button ============================
        loginbtn = Button(main_frame, text="Login", command=self.return_login, font=("times new roman", 14, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        loginbtn.place(x=210, y=530, width=160)

        # ====== Show Password =======

    def show_password(self):
        if self.txt_psw.cget('show') == '*':
            self.txt_psw.config(show='')
            self.txt_confirmpsw.config(show='')
        else:
            self.txt_psw.config(show='*')
            self.txt_confirmpsw.config(show='*')

    # =================== Reset Entry Fill ==============
    def reset_data(self):
        self.var_fname.set("")
        self.var_lname.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_securityQ.set("Select")
        self.var_securityA.set("")
        self.var_pass.set("")
        self.var_confpass.set("")
        self.var_check.set(0)

    # ========= Function Declaration =============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="" or self.var_securityA.get()=="" or self.var_pass.get()=="" or self.var_confpass.get()=="" or self.var_check.get()=="":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password and Confirm password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree our terms and condition")
        else:
            client = MongoClient("mongodb://localhost:27017/")
            db = client["FaceRecognization"]
            collection = db["Register"]

            if collection.find_one({"email": self.var_email.get()}, {"_id": 0, "email": 1}) is not None:
                  messagebox.showerror("Error", "User already exist, please try another email")
            else:
                data = {
                        "fname": self.var_fname.get(),
                        "lname": self.var_lname.get(),
                        "contact": self.var_contact.get(),
                        "email": self.var_email.get(),
                        "securityQ": self.var_securityQ.get(),
                        "securityA": self.var_securityA.get(),
                        "pass": self.var_pass.get()
                }
                collection.insert_one(data)
                messagebox.showinfo("successful", "Register details has been added Successfully", parent=self.root)
                self.reset_data()
                client.close()

    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()