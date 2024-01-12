from tkinter import *  # for GUI purpose
from tkinter import ttk  # stylish toolkit
from PIL import Image, ImageTk  # for image editing
from tkinter import messagebox
from pymongo.mongo_client import MongoClient
import cv2                                # ML algorithum

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # window size geometry(width,height,x-axis,y-axis)
        self.root.title("Face Recognition System")

        # variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_search = StringVar()
        self.var_search_txt = StringVar()

        # Image set Big Image
        img = Image.open("Images/bigImage.jpg")  # Set Image Path
        img = img.resize((1530, 790))  # width , height  and ANTIALIAS used to convert high to low level image
        self.photoimg = ImageTk.PhotoImage(img)  # set image

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1530, height=790)  # image show on window place(x_axis,y_axis)

        title_lb1 = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")  # Title
        title_lb1.place(x=0, y=0, width=1530, height=45)

        # frame
        main_frame=Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=60, width=1500, height=700)

        # left side frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=760, height=670)

        left_img = Image.open("Images/studentdetails.jpg")  # Set Image Path
        left_img = left_img.resize((660, 300))  # width , height  and ANTIALIAS used to convert high to low level image
        self.photoimg_left = ImageTk.PhotoImage(left_img)  # set image

        lb_img = Label(left_frame, image=self.photoimg_left)
        lb_img.place(x=7, y=0, width=740, height=140)  # image show on window place(x_axis,y_axis)

        # current course Information
        current_course = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information",font=("times new roman", 12, "bold"))
        current_course.place(x=5, y=145, width=740, height=150)

        # Department
        dep_label = Label(current_course, text="Department", font=("times new roman", 13, "bold"),bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course, textvariable=self.var_dep, font=("times new roman", 13, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department", "Computer Science", "Computer Application")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course, text="Course", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course, textvariable=self.var_course, font=("times new roman", 13, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course", "First Year", "Second Year", "Third year", "Part 1", "Part 2")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course, text="Year", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course, textvariable=self.var_year, font=("times new roman", 13, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Select Year", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course, textvariable=self.var_semester, font=("times new roman", 13, "bold"), state="readonly", width=20)
        semester_combo["values"] = ("Select Semester", "Sem-1", "Sem-2", "Sem-3", "Sem-4", "Sem-5", "Sem-6")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class student Information
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Class student Information",font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=300, width=740, height=330)

        # student id
        studentId_label = Label(class_student_frame, text="Student Id:", font=("times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=("times new roman", 13, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # student Name
        studentName_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 13, "bold"),bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5,sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # class didvision
        classdiv_label = Label(class_student_frame, text="Class Division:", font=("times new roman", 13, "bold"),bg="white")
        classdiv_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        classdiv_entry = ttk.Entry(class_student_frame, textvariable=self.var_div, width=20, font=("times new roman", 13, "bold"))
        classdiv_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        RollNo_label = Label(class_student_frame, text="Roll No:", font=("times new roman", 13, "bold"),bg="white")
        RollNo_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        RollNo_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=("times new roman", 13, "bold"))
        RollNo_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 13, "bold"),state="readonly", width=13)
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB
        dob_label = Label(class_student_frame, text="DOB:", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email:", font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email, width=20, font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone no
        phoneno_label = Label(class_student_frame, text="Phone no:", font=("times new roman", 13, "bold"), bg="white")
        phoneno_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phoneno_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("times new roman", 13, "bold"))
        phoneno_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_student_frame, text="Address:", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher name
        address_label = Label(class_student_frame, text="Teacher name:", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio Buttons
        self.var_radio1 = StringVar()
        radionbt1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radionbt1.grid(row=6, column=0)

        radionbt2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radionbt2.grid(row=6, column=1)


        # Buttons frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=735, height=35)

        # save button
        save_button = Button(btn_frame, text="Save", command=self.add_data, width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_button.grid(row=0, column=0)

        # update button
        update_button = Button(btn_frame, text="Update", command=self.update_data, width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_button.grid(row=0, column=1)

        # Delete button
        delete_button = Button(btn_frame, text="Delete", command=self.delete_data, width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_button.grid(row=0, column=2)

        # Reset button
        reset_button = Button(btn_frame, text="Reset", command=self.reset_data, width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_button.grid(row=0, column=3)

        #Photo frame
        photo_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        photo_frame.place(x=200, y=250, width=260, height=35)

        # Take photo button
        takephoto_button = Button(photo_frame, text="Take photo", command=self.generate_dataset, width=25, font=("times new roman", 13, "bold"),bg="blue", fg="white")
        takephoto_button.grid(row=0, column=0)

        # right side frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",font=("times new roman", 12, "bold"))
        right_frame.place(x=780, y=10, width=660, height=670)

        right_img = Image.open("Images/studentdetails.jpg")  # Set Image Path
        right_img = right_img.resize((660, 300))  # width , height  and ANTIALIAS used to convert high to low level image
        self.photoimg_right = ImageTk.PhotoImage(right_img)  # set image

        lb_img = Label(right_frame, image=self.photoimg_right)
        lb_img.place(x=5, y=0, width=650, height=140)  # image show on window place(x_axis,y_axis)


        # =========== Search System ================
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=150, width=640, height=64)

        # search label
        search_label = Label(search_frame, text="Search By", font=("times new roman", 13, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        # search combo
        search_combo = ttk.Combobox(search_frame, font=("times new roman", 13, "bold"), textvariable=self.var_search_txt, state="readonly", width=10)
        search_combo["values"] = ("Select", "Roll No", "Division", "Course", "Year", "Semester")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Enter search data
        search_entry = ttk.Entry(search_frame, width=10, textvariable=self.var_search, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        # Search button
        search_button = Button(search_frame, text="Search", command=self.search_data, width=15, font=("times new roman", 12, "bold"), bg="blue",fg="white")
        search_button.grid(row=0, column=3, padx=4)

        # Show All button
        show_button = Button(search_frame, text="Show All", width=15, command=self.fetch_data, font=("times new roman", 12, "bold"), bg="blue",fg="white")
        show_button.grid(row=0, column=4, padx=4)

        # ============== Table Frame ===================
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=220, width=640, height=300)

        # Scroll bar for x
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=("roll","dept", "course", "year", "sem", "id", "name", "div", "dob", "email","gender", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("roll", text="Roll_no")
        self.student_table.heading("dept", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Div")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo")
        self.student_table["show"] = "headings"

        # set size for column
        self.student_table.column("roll", width=100)
        self.student_table.column("dept", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor) # data show when click
        self.fetch_data()

# ========== Function Declaration =============
    def add_data(self):
       if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
         messagebox.showerror("Error", "All Fields are Required", parent=self.root)
       else:
          # Create a new client and connect to the server
          client = MongoClient("mongodb://localhost:27017/")
          # Send a ping to confirm a successful connection
          try:
              db = client["FaceRecognization"]
              collection = db["Student"]
              data = {
                  "roll": self.var_roll.get(),
                  "dep": self.var_dep.get(),
                  "course": self.var_course.get(),
                  "year": self.var_year.get(),
                  "semester": self.var_semester.get(),
                  "studentId": self.var_std_id.get(),
                  "name": self.var_std_name.get(),
                  "division": self.var_div.get(),
                  "DOB": self.var_dob.get(),
                  "Email": self.var_email.get(),
                  "gender": self.var_gender.get(),
                  "phone": self.var_phone.get(),
                  "address": self.var_address.get(),
                  "teacher": self.var_teacher.get(),
                  "photosample": self.var_radio1.get(),
              }
              collection.insert_one(data)
              self.fetch_data()
              messagebox.showinfo("successful", "Student details has been added Successfully", parent=self.root)
              client.close()
          except Exception as e:
              messagebox.showerror("Error", "All Fields are Required", parent=self.root)


    # ============= Fetch Data ===========
    def fetch_data(self):
        client = MongoClient("mongodb://localhost:27017/")
        db = client["FaceRecognization"]
        collection = db["Student"]
        my_cursor = collection.find({}, {"_id": 0})

        self.student_table.delete(*self.student_table.get_children())   # delete first existing data
        for i in my_cursor:
            self.student_table.insert('', 'end', values=(i['roll'], i['dep'], i['course'], i['year'], i['semester'], i['studentId'], i['name'], i['division'], i['DOB'], i['Email'], i['gender'],i['phone'], i['address'], i['teacher'], i['photosample']))
        client.close()

    # =========== Get Cursor =============
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        if data is not None:
            self.var_roll.set(data[0]),
            self.var_dep.set(data[1]),
            self.var_course.set(data[2]),
            self.var_year.set(data[3]),
            self.var_semester.set(data[4]),
            self.var_std_id.set(data[5]),
            self.var_std_name.set(data[6]),
            self.var_div.set(data[7]),
            self.var_dob.set(data[8]),
            self.var_email.set(data[9]),
            self.var_gender.set(data[10]),
            self.var_phone.set(data[11]),
            self.var_address.set(data[12]),
            self.var_teacher.set(data[13]),
            self.var_radio1.set(data[14])

    # ========= Update Data ==========
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update > 0:
                    client = MongoClient("mongodb://localhost:27017/")
                    db = client["FaceRecognization"]
                    collection = db["Student"]
                    collection.update({'$and': [{"roll": self.var_roll.get()}, {"studentId": self.var_std_id.get()}, {"Email": self.var_email.get()}]}, {"$set": {"roll": self.var_roll.get(),
                                                  "dep": self.var_dep.get(),
                                                  "course": self.var_course.get(),
                                                  "year": self.var_year.get(),
                                                  "semester": self.var_semester.get(),
                                                  "studentId": self.var_std_id.get(),
                                                  "name": self.var_std_name.get(),
                                                  "division": self.var_div.get(),
                                                  "DOB": self.var_dob.get(),
                                                  "Email": self.var_email.get(),
                                                  "gender": self.var_gender.get(),
                                                  "phone": self.var_phone.get(),
                                                  "address": self.var_address.get(),
                                                  "teacher": self.var_teacher.get(),
                                                  "photosample": self.var_radio1.get()}})
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details successfully update completed", parent=self.root)
                self.fetch_data()
                client.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # =================== Search Data =============
    def search_data(self):
        if self.var_search.get() == "" or self.var_search_txt.get() == "":
            messagebox.showerror("Error", "Select Combo option and enter entry box", parent=self.root)
        else:
            client = MongoClient("mongodb://localhost:27017/")
            db = client["FaceRecognization"]
            collection = db["Student"]

            # Roll number wise Searching
            if self.var_search_txt.get() == "Roll No":
                my_cursor = collection.find({"roll": self.var_search.get()}, {"_id": 0})
                self.student_table.delete(*self.student_table.get_children())  # delete first existing data
                for i in my_cursor:
                    self.student_table.insert('', 'end', values=(i['roll'], i['dep'], i['course'], i['year'], i['semester'], i['studentId'], i['name'], i['division'], i['DOB'], i['Email'], i['gender'], i['phone'], i['address'], i['teacher'],i['photosample']))

            # Division wise Searching
            if self.var_search_txt.get() == "Division":
                my_cursor = collection.find({"division": self.var_search.get()}, {"_id": 0})
                self.student_table.delete(*self.student_table.get_children())  # delete first existing data
                for i in my_cursor:
                    self.student_table.insert('', 'end', values=(i['roll'], i['dep'], i['course'], i['year'], i['semester'], i['studentId'], i['name'], i['division'], i['DOB'], i['Email'], i['gender'], i['phone'], i['address'], i['teacher'], i['photosample']))

            # Course wise Searching
            if self.var_search_txt.get() == "Course":
                my_cursor = collection.find({"course": self.var_search.get()}, {"_id": 0})
                self.student_table.delete(*self.student_table.get_children())  # delete first existing data
                for i in my_cursor:
                    self.student_table.insert('', 'end', values=(i['roll'], i['dep'], i['course'], i['year'], i['semester'], i['studentId'], i['name'], i['division'], i['DOB'], i['Email'], i['gender'], i['phone'], i['address'], i['teacher'], i['photosample']))

            # Year wise Searching
            if self.var_search_txt.get() == "Year":
                my_cursor = collection.find({"year": self.var_search.get()}, {"_id": 0})
                self.student_table.delete(*self.student_table.get_children())  # delete first existing data
                for i in my_cursor:
                    self.student_table.insert('', 'end', values=(i['roll'], i['dep'], i['course'], i['year'], i['semester'], i['studentId'], i['name'], i['division'], i['DOB'], i['Email'], i['gender'], i['phone'], i['address'], i['teacher'], i['photosample']))

            # Semester wise Searching
            if self.var_search_txt.get() == "Semester":
                my_cursor = collection.find({"semester": self.var_search.get()}, {"_id": 0})
                self.student_table.delete(*self.student_table.get_children())  # delete first existing data
                for i in my_cursor:
                    self.student_table.insert('', 'end', values=(i['roll'], i['dep'], i['course'], i['year'], i['semester'], i['studentId'], i['name'], i['division'], i['DOB'], i['Email'], i['gender'], i['phone'], i['address'], i['teacher'], i['photosample']))
            client.close()


    # =================== Delete Data =============
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Data required ", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student", parent=self.root)
                if delete > 0:
                    client = MongoClient("mongodb://localhost:27017/")
                    db = client["FaceRecognization"]
                    collection = db["Student"]
                    collection.delete_one({"roll": self.var_roll.get()})
                    client.close()
                else:
                    if not delete:
                        return
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
                self.fetch_data()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # =========== Reset ==============
    def reset_data(self):
        self.var_dep.set("Selected Department")
        self.var_roll.set("")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("No")

    # ================== Generate data set or take photo samples ======================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "": # All fields are required
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                client = MongoClient("mongodb://localhost:27017/")
                db = client["FaceRecognization"]
                collection = db["Student"]
                collection.find({}, {"_id": 0}) # get all data
                id = self.var_std_id.get()
                collection.update({'$and': [{"roll": self.var_roll.get()}, {"studentId": self.var_std_id.get()}, {"Email": self.var_email.get()}]}, {"$set": {"roll": self.var_roll.get(),
                                                "dep": self.var_dep.get(),
                                                "course": self.var_course.get(),
                                                "year": self.var_year.get(),
                                                "semester": self.var_semester.get(),
                                                "student_Id": self.var_std_id.get(),
                                                "name": self.var_std_name.get(),
                                                "division": self.var_div.get(),
                                                "DOB": self.var_dob.get(),
                                                "Email": self.var_email.get(),
                                                "gender": self.var_gender.get(),
                                                "phone": self.var_phone.get(),
                                                "address": self.var_address.get(),
                                                "teacher": self.var_teacher.get(),
                                                "photosample": self.var_radio1.get()}})
                self.fetch_data()
                self.reset_data()
                client.close()

                # ===== Load predifiend data on face , recognize eye and object
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # convert image into gray scale
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)  # Scaling factor = 1.3,  Minimum Neighbor=5
                    for(x, y, w, h) in faces:  # Rectangle shape on face
                        face_cropped = img[y:y+h, x:x+w]     # set image size
                        return face_cropped

                cap = cv2.VideoCapture(0)  # camera open
                img_id = 0                 # 100 sample
                while True: # infinite loop
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None: # if data preset then increment id
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450)) # croped photo
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)  # convert image into gray scale
                        file_name_path = "Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)
                        cv2.imshow("Croopped Face", face)
                    if cv2.waitKey(1) == 13 or int(img_id) == 100: # 100n image sample
                        break
                cap.release() # close camera
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
