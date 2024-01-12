from tkinter import *  # for GUI purpose
from tkinter import ttk  # stylish toolkit
from PIL import Image, ImageTk  # for image editing
import os
import csv
from tkinter import filedialog
from tkinter import messagebox
from pymongo.mongo_client import MongoClient
import cv2                                # ML algorithum

mydata=[] #Fetch data from csv

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # window size geometry(width,height,x-axis,y-axis)
        self.root.title("Face Recognition System")

        ####### Variables ###############
        self.var_atte_name = StringVar()
        self.var_atte_roll = StringVar()
        self.var_atte_division = StringVar()
        self.var_atte_department = StringVar()
        self.var_atte_date = StringVar()
        self.var_atte_time = StringVar()
        self.var_atte_email = StringVar()
        self.var_atte_status = StringVar()


        # Top Image
        img = Image.open("Images/class_photo_detections.jpg")  # Set Image Path
        img = img.resize((1530, 200))  # width , height  and ANTIALIAS used to convert high to low level image
        self.photoimg = ImageTk.PhotoImage(img)  # set image

        top_img = Label(self.root, image=self.photoimg)
        top_img.place(x=0, y=0, width=1530, height=200)

        # Big Image
        img2 = Image.open("Images/bigImage.jpg")  # Set Image Path
        img2 = img2.resize((1530, 710))  # width , height  and ANTIALIAS used to convert high to low level image
        self.photoimg2 = ImageTk.PhotoImage(img2)  # set image

        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lb1 = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white",fg="darkgreen")  # Title
        title_lb1.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=60, width=1500, height=500)

        # left side frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=760, height=480)

        left_img = Image.open("Images/studentdetails.jpg")  # Set Image Path
        left_img = left_img.resize((660, 300))  # width , height  and ANTIALIAS used to convert high to low level image
        self.photoimg_left = ImageTk.PhotoImage(left_img)  # set image

        lb_img = Label(left_frame, image=self.photoimg_left)
        lb_img.place(x=7, y=0, width=740, height=140)  # image show on window place(x_axis,y_axis)

        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=145, width=750, height=250)

        # attendance name
        name_label = Label(left_inside_frame, text="Name:", font=("comicsansns 11 bold", 13, "bold"), bg="white")
        name_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        name_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atte_name, font=("comicsansns 11 bold", 13, "bold"))
        name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # attendance roll no
        roll_label = Label(left_inside_frame, text="Roll No:", font=("comicsansns 11 bold", 13, "bold"),bg="white")
        roll_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        roll_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atte_roll, font=("comicsansns 11 bold", 13, "bold"))
        roll_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # attendance division
        division_label = Label(left_inside_frame, text="Division:", font=("comicsansns 11 bold", 13, "bold"), bg="white")
        division_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        division_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atte_division, font=("comicsansns 11 bold", 13, "bold"))
        division_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # attendance department
        dept_label = Label(left_inside_frame, text="Department", font=("comicsansns 11 bold", 13, "bold"), bg="white")
        dept_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        dept_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atte_department, font=("comicsansns 11 bold", 13, "bold"))
        dept_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # attendance time
        time_label = Label(left_inside_frame, text="Time:", font=("comicsansns 11 bold", 13, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        time_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atte_time, font=("comicsansns 11 bold", 13, "bold"))
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # attendance date
        date_label = Label(left_inside_frame, text="Date:", font=("comicsansns 11 bold", 13, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        date_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atte_date, font=("comicsansns 11 bold", 13, "bold"))
        date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # attendance email
        email_label = Label(left_inside_frame, text="Email:", font=("comicsansns 11 bold", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atte_email, font=("comicsansns 11 bold", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # attendance status
        attendancelabel = Label(left_inside_frame, text="Attendance Status:", font=("comicsansns 11 bold", 13, "bold"), bg="white")
        attendancelabel.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        self.atten_status = ttk.Combobox(left_inside_frame, width=20, textvariable=self.var_atte_status, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"]=("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        self.atten_status.current(0)

        # Buttons frame
        btn_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=80, y=300, width=573, height=35)

        # Import csv button
        import_button = Button(btn_frame, text="Import csv", command=self.importCsv, width=18,font=("times new roman", 13, "bold"), bg="blue", fg="white")
        import_button.grid(row=0, column=0)

        # Export csv button
        export_button = Button(btn_frame, text="Export csv", width=18, command=self.exportCsv, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        export_button.grid(row=0, column=1)

        # Reset button
        reset_button = Button(btn_frame, text="Reset", width=18, command=self.reset_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_button.grid(row=0, column=2)

        # right side frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details",font=("times new roman", 12, "bold"))
        right_frame.place(x=780, y=10, width=700, height=480)

        # Table frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=680, height=445)

        ############# Scroll bar table ############
        scroll_x =ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("Name", "Roll", "Department", "Division", "Email", "Date", "Time", "Status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("Name", text="Name")
        self.AttendanceReportTable.heading("Roll", text="Roll")
        self.AttendanceReportTable.heading("Department", text="Department")
        self.AttendanceReportTable.heading("Division", text="Division")
        self.AttendanceReportTable.heading("Email", text="Email")
        self.AttendanceReportTable.heading("Date", text="Date")
        self.AttendanceReportTable.heading("Time", text="Time")
        self.AttendanceReportTable.heading("Status", text="Status")
        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("Name", width=100)
        self.AttendanceReportTable.column("Roll", width=100)
        self.AttendanceReportTable.column("Department", width=100)
        self.AttendanceReportTable.column("Division", width=100)
        self.AttendanceReportTable.column("Email", width=100)
        self.AttendanceReportTable.column("Date", width=100)
        self.AttendanceReportTable.column("Time", width=100)
        self.AttendanceReportTable.column("Status", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)



 ################# Fetch Data ################
    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children()) # First data delete
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

########### Import CSV #####################
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

################# Export CSV ##########
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data", "No data Found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data is exported to"+os.path.basename(fln)+"Successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()    # focus cursor data store
        content = self.AttendanceReportTable.item(cursor_row) # store data
        rows = content["values"]
        if rows is not None:
            self.var_atte_name.set(rows[0])
            self.var_atte_roll.set(rows[1])
            self.var_atte_department.set(rows[2])
            self.var_atte_division.set(rows[3])
            self.var_atte_email.set(rows[4])
            self.var_atte_date.set(rows[5])
            self.var_atte_time.set(rows[6])
            self.var_atte_status.set(rows[7])

    def reset_data(self):
        self.var_atte_name.set("")
        self.var_atte_roll.set("")
        self.var_atte_department.set("")
        self.var_atte_division.set("")
        self.var_atte_email.set("")
        self.var_atte_date.set("")
        self.var_atte_time.set("")
        self.var_atte_status.set("")




if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()