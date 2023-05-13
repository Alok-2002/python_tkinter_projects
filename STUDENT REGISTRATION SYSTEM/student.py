from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT REGISTRATION SYSTEM")

        #variables
        self.var_enrollment=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_department=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_section=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phone=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar() 

       #1st image 
        img=Image.open(r'./college_images/mits.jpg')
        img=img.resize((1550,170),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        self.button1=Button(self.root,image=self.photoimg,cursor="hand2")
        self.button1.place(x=0,y=0,width=1550,height=170)

        #background image
        img_4=Image.open(r'./college_images/university.png')
        img_4=img_4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        bg_label=Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_label.place(x=0,y=160,width=1530,height=650)

        label_title=Label(bg_label,text="STUDENT REGISTRATION SYSTEM",font=("Comic Sans MS",37,"bold"),fg="blue",bg="white")
        label_title.place(x=0,y=0,width=1530,height=50)

        #manage frames
        manage_frame=Frame(bg_label,bd=2,relief=RIDGE,bg="white")
        manage_frame.place(x=15,y=55,width=1500,height=560)

        #left data frame
        left_frame=LabelFrame(manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("Comic Sans MS",12,"bold"),fg="red",bg="white")
        left_frame.place(x=10,y=10,width=660,height=540)

        img_5=Image.open(r'./college_images/3.jpg')
        img_5=img_5.resize((650,120),Image.ANTIALIAS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        my_labl=Label(left_frame,image=self.photoimg_5,bd=2,relief=RIDGE)
        my_labl.place(x=0,y=0,width=650,height=120)

        #current course
        student_info_frame=LabelFrame(manage_frame,bd=4,relief=RIDGE,padx=2,text="Current Course Information",font=("Comic Sans MS",12,"bold"),fg="red",bg="white")
        student_info_frame.place(x=0,y=120,width=667,height=115)

        course_label=Label(student_info_frame,text="Course",font=("Comic Sans MS",12,"bold"),bg="white")
        course_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        course_combo=ttk.Combobox(student_info_frame,textvariable=self.var_course,font=("Arial",12,"bold"),width=17,state="readonly")
        course_combo["value"]=("Select Courses","B.E/B.Tech","Ph.D","MBA","MCA","M.E","M.Tech")
        course_combo.current(0)
        course_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #department drop box
        department_label=Label(student_info_frame,text="Department",font=("Comic Sans MS",12,"bold"),bg="white")
        department_label.grid(row=0,column=2,padx=2,sticky=W)

        department_combo=ttk.Combobox(student_info_frame,textvariable=self.var_department,font=("Arial",12,"bold"),width=17,state="readonly")
        department_combo["value"]=("Select Department","Computer Science And Engineering","Computer Science And Design","Information Technology","Artificial Intelligence And Machine Learning","Artificial Intelligence And Data Science","Artificial Intelligence And Robotics","Electrical Engineering","Internet Of Things Offered By Electrical Engineering Department","Internet Of Things Offered By Information Technology","Mathematics And Computing","Autombile Engineering","Electronics And TeleCommunication","Chemical Engineering","Architecture","Electronics Engineering","Civil Engineering Department","Mechanical Engineering")
        department_combo.current(0)
        department_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        current_year=Label(student_info_frame,text="Year:",font=("Comic Sans MS",12,"bold"),bg="white")
        current_year.grid(row=1,column=0,padx=2,sticky=W)

        current_year_combo=ttk.Combobox(student_info_frame,textvariable=self.var_year,font=("Arial",12,"bold"),width=17,state="readonly")
        current_year_combo["value"]=("Select Your Current Year","1st Year","2nd Year","3rd Year","4th Year")
        current_year_combo.current(0)
        current_year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #current semester
        current_semester=Label(student_info_frame,text="Semester:",font=("Comic Sans MS",12,"bold"),bg="white")
        current_semester.grid(row=1,column=2,padx=2,pady=10,sticky=W)

        current_semester_combo=ttk.Combobox(student_info_frame,textvariable=self.var_semester,font=("Arial",12,"bold"),width=17,state="readonly")
        current_semester_combo["value"]=("Select Your Current Semester","1st Semester","2nd Semester","3rd Semester","4th Semester","5th Semester","6th Semester","7th Semester","8th Semester")
        current_semester_combo.current(0)
        current_semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #student class information
        student_class=LabelFrame(left_frame,bd=4,relief=RIDGE,padx=2,text="Student Class Information",font=("Comic Sans MS",12,"bold"),fg="red",bg="white")
        student_class.place(x=0,y=195,width=650,height=235)

        #student name
        student_name=Label(student_class,text="Student Name: ",font=("Comic Sans MS",12,"bold"),bg="white")
        student_name.grid(row=0,column=0,padx=2,pady=7,sticky=W)

        name_entry=ttk.Entry(student_class,textvariable=self.var_name,font=("Comic Sans MS",12,"bold"),width=15)
        name_entry.grid(row=0,column=1,sticky=W,padx=2,pady=7)
       
        #student id
        student_id=Label(student_class,text="Enrollment",font=("Comic Sans MS",12,"bold"),bg="white")
        student_id.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        id_entry=ttk.Entry(student_class,textvariable=self.var_enrollment,font=("Comic Sans MS",12,"bold"),width=15)
        id_entry.grid(row=0,column=3,sticky=W,padx=2,pady=7)

        #sections
        class_section=Label(student_class,text="Section: ",font=("Comic Sans MS",12,"bold"),bg="white")
        class_section.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        section_entry=ttk.Combobox(student_class,textvariable=self.var_section,state="readonly",font=("Arial",10,"bold"),width=18)
        section_entry["values"]=("Select Your Branch Section","A","B","C")
        section_entry.current(0)
        section_entry.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        #gender
        student_gender=Label(student_class,text="Gender:",font=("Comic Sans MS",10,"bold"),bg="white")
        student_gender.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        gender_combo=ttk.Combobox(student_class,textvariable=self.var_gender,state="readonly",font=("Arial",10,"bold"),width=19)
        gender_combo["values"]=("Select Your Gender","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        #dob
        student_dob=Label(student_class,text="DOB:",font=("Comic Sans MS",12,"bold"),bg="white")
        student_dob.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        dob_entry=ttk.Entry(student_class,textvariable=self.var_dob,font=("Arial",12,"bold"),width=15)
        dob_entry.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        #mobilenumber
        student_mobile=Label(student_class,text="Phone",font=("Comic Sans MS",12,"bold"),bg="white")
        student_mobile.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        num_entry=ttk.Entry(student_class,textvariable=self.var_phone,font=("Arial",12,"bold"),width=16)
        num_entry.grid(row=2,column=3,sticky=W,padx=2,pady=7)

        #mail
        student_email=Label(student_class,text="Email I'D:",font=("Comic Sans MS",12,"bold"),bg="white")
        student_email.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        email_entry=ttk.Entry(student_class,textvariable=self.var_email,font=("calbri",12,"bold"),width=15)
        email_entry.grid(row=3,column=1,sticky=W,padx=2,pady=7)

        #address
        student_address=Label(student_class,text="Address:",font=("Comic Sans MS",12,"bold"),bg="white")
        student_address.grid(row=3,column=2,padx=2,pady=7,sticky=W)

        address_entry=ttk.Entry(student_class,textvariable=self.var_address,font=("Comic Sans MS",12,"bold"),width=15)
        address_entry.grid(row=3,column=3,sticky=W,padx=2,pady=7)

        #button
        button_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=435,width=650,height=45)

        button_add=Button(button_frame,text="Save",command=self.add_data,font=("arial",14,"bold"),width=13,bg="blue",fg="white")
        button_add.grid(row=0,column=0,padx=1)

        button_update=Button(button_frame,text="Update",command=self.update_data,font=("arial",14,"bold"),width=13,bg="blue",fg="white")
        button_update.grid(row=0,column=1,padx=1)
        
        button_del=Button(button_frame,text="Delete",command=self.delete_data,font=("arial",14,"bold"),width=13,bg="blue",fg="white")
        button_del.grid(row=0,column=2,padx=1)

        button_reset=Button(button_frame,text="Reset",command=self.reset_data,font=("arial",14,"bold"),width=12,bg="blue",fg="white")
        button_reset.grid(row=0,column=3,padx=1)
       

        #right frame
        right_frame=LabelFrame(manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Details",font=("Comic Sans MS",12,"bold"),fg="red",bg="white")
        right_frame.place(x=680,y=10,width=810,height=540)
        
        #img 1
        img_7=Image.open(r'./college_images/5th.jpg')
        img_7=img_7.resize((798,200),Image.ANTIALIAS)
        self.photoimg_7=ImageTk.PhotoImage(img_7)

        right_img=Label(right_frame,image=self.photoimg_7,bd=2,relief=RIDGE)
        right_img.place(x=0,y=0,width=798,height=200)
        
        #search frame
        search_frame=LabelFrame(right_frame,bd=4,relief=RIDGE,padx=2,text="Search Student Information",font=("Comic Sans MS",12,"bold"),fg="red",bg="white")
        search_frame.place(x=0,y=200,width=798,height=70)

        search_label=Label(search_frame,font=("arial",14,"bold"),text="Search By: ",width=12,bg="grey",fg="Black")
        search_label.grid(row=0,column=0,padx=5,sticky=W)

        #Search 
        self.var_combo_search=StringVar()

        search_combo=ttk.Combobox(search_frame,textvariable=self.var_combo_search,state="readonly",font=("Arial",10,"bold"),width=19)
        search_combo["values"]=("Select Option","Enrollment","Phone","Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()

        search_entry=ttk.Entry(search_frame,textvariable=self.var_search,font=("Comic Sans MS",12,"bold"),width=15)
        search_entry.grid(row=0,column=2,sticky=W,padx=5)
       
        button_search=Button(search_frame,text="Search",command=self.search_data,font=("arial",14,"bold"),width=11,bg="blue",fg="white")
        button_search.grid(row=0,column=3,padx=5)

        button_ShowAll=Button(search_frame,command=self.fetch_data,text="Show All",font=("arial",14,"bold"),width=10,bg="blue",fg="white")
        button_ShowAll.grid(row=0,column=4,padx=5)

        #=======Student Table And Scroll Bar========
        table_frame=Frame(right_frame,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=272,width=797,height=240)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("Enrollment","Name","Course","Department","Year","Semester","Section","Gender","Dob","Phone","Email","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("Enrollment",text="Enrollment")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Section",text="Section")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Dob",text="DOB")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Address",text="Address")

        self.student_table["show"]="headings"

        self.student_table.column("Enrollment",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Department",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Section",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Dob",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Address",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

    def add_data(self):
        if (self.var_enrollment.get()=="" or self.var_name.get()=="" or self.var_course.get()==""):
            messagebox.showerror("Error","All Fields Are Required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="2030",database="student_management_system")
                my_cursur=conn.cursor()
                my_cursur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_enrollment.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_department.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_section.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_address.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Registration Successfull","Student Has Been Successfully Registered...",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="2030",database="student_management_system")
        my_cursur=conn.cursor()
        my_cursur.execute("select * from student order by Enrollment")
        data=my_cursur.fetchall()
        if len(data)!=0: 
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END,values=i)
            conn.commit()
        conn.close()

    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]

        self.var_enrollment.set(data[0])
        self.var_name.set(data[1])
        self.var_course.set(data[2])
        self.var_department.set(data[3])
        self.var_year.set(data[4])
        self.var_semester.set(data[5])
        self.var_section.set(data[6])
        self.var_gender.set(data[7])
        self.var_dob.set(data[8])
        self.var_phone.set(data[9])
        self.var_email.set(data[10])
        self.var_address.set(data[11])
    
#update in database
    def update_data(self):
        if (self.var_enrollment.get()=="" or self.var_name.get()=="" or self.var_course.get()==""):
            messagebox.showerror("Error","All Fields Are Required")
        else:
            try:
                update=messagebox.askyesno("Update","Are You Sure To Update This Student Information ?",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="2030",database="student_management_system")
                    my_cursur=conn.cursor()
                    my_cursur.execute("update student set Name=%s,Course=%s,Department=%s,Year=%s,Semester=%s,Section=%s,Gender=%s,DOB=%s,Phone=%s,Email=%s,Address=%s where Enrollment=%s",(                                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                        self.var_department.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                        self.var_section.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_enrollment.get()
                                                                                                                                                                                                        ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Succesfull","Student Information Updated Successfull.....",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   

    #Delete Button
    def delete_data(self):
        if self.var_enrollment.get()=="":
            messagebox.showerror("Error","All Fields Are Required")
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are You Sure Want To Delete This Student ?")
                if Delete > 0 :
                    conn=mysql.connector.connect(host="localhost",username="root",password="2030",database="student_management_system")
                    my_cursur=conn.cursor()
                    sql="delete from student where Enrollment=%s"
                    value=(self.var_enrollment.get(),)
                    my_cursur.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Your Studen Information Has Been Deleted...",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
    #Reset
    def reset_data(self):
        self.var_enrollment.set("")
        self.var_name.set("")
        self.var_course.set("Select Course")
        self.var_department.set("Select Department")
        self.var_year.set("Select Your Current Year")
        self.var_semester.set("Select Your Current Semester")
        self.var_section.set("Select Your Branch Section")
        self.var_gender.set("Select Your Gender")
        self.var_dob.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_address.set("")
    
    #search
    def search_data(self):
        if self.var_combo_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please Select Option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="2030",database="student_management_system")
                my_cursur=conn.cursor()
                my_cursur.execute("Select * From Student where " +str(self.var_combo_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursur.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i  in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close() 
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                  

#main function
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()