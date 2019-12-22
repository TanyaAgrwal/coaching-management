from tkinter import *
from PIL import ImageTk,Image
def marks_of8():
    marks_page=Toplevel()
    marks_page.geometry("1366x768")
    marks_page.title("Test Marks of 8")
    Label(marks_page,text="**TEST MARKS ENTRY FOR CLASS VIII**",font=("Copperplate Gothic Bold",28,"underline"),fg="midnight blue").grid(row=0,column=1)
    Label(marks_page,text="STUDENTS:-",font=("Candara Light",18,"underline","bold"),fg="maroon").grid(row=1,column=0)
    Label(marks_page,text="TEST ENTRY FOR SCIENCE:-",font=("Candara Light",18,"underline","bold"),fg="maroon").grid(row=1,column=1)
    Label(marks_page,text="TEST ENTRY FOR MATHS:-",font=("Candara Light",18,"underline","bold"),fg="maroon").grid(row=1,column=2)
    global sciencemarks,mathmarks
    sciencemarks=[]
    mathmarks=[]
    import mysql.connector
    sql=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="coaching")
    cur=sql.cursor()
    class8th="SELECT first_name FROM login WHERE current_class='8' "
    cur.execute(class8th)
    var8=cur.fetchall()
    for i in range(0,variable):               
        label1=Label(marks_page,text=var8[i][0],font=("Constantia",15),fg="RoyalBlue4")
        label1.grid(row=2+i,column=0)
        science=IntVar()
        math=IntVar()
        e1=Entry(marks_page,textvariable=science)
        e1.grid(row=2+i,column=1)
        e2=Entry(marks_page,textvariable=math)
        e2.grid(row=2+i,column=2)
        sciencemarks.append(e1)
        mathmarks.append(e2)
    Button(marks_page,text="SUBMIT",command=marks8submit).grid(row=variable+2,column=0)

def marks8submit():
    import mysql.connector
    sql=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="coaching")
    cur=sql.cursor()
    class8th="SELECT first_name FROM login WHERE current_class='8' "
    cur.execute(class8th)
    var8=cur.fetchall()
    for q in range(0,variable):
        var="INSERT INTO test_marks_of8(first_name,current_class,science,maths) VALUES (%s,%s,%s,%s)"
        value=(var8[q][0],8,sciencemarks[q].get(),mathmarks[q].get())
        cur.execute(var,value)
        sql.commit()

def marks_of9():
    marks_page9=Toplevel()
    marks_page9.geometry("1366x768")
    marks_page9.title("Test Marks of 9")
    Label(marks_page9,text="**TEST MARKS ENTRY FOR CLASS IX**",font=("Copperplate Gothic Bold",28,"underline"),fg="midnight blue").grid(row=0,column=2)
    Label(marks_page9,text="STUDENTS:-",font=("Candara Light",18,"underline","bold"),fg="maroon").grid(row=1,column=0)
    Label(marks_page9,text="PHYSICS:-",font=("Candara Light",18,"underline","bold"),fg="maroon").grid(row=1,column=1)
    Label(marks_page9,text="CHEMISTRY:-",font=("Candara Light",18,"underline","bold"),fg="maroon").grid(row=1,column=2)
    Label(marks_page9,text="MATHS:-",font=("Candara Light",18,"underline","bold"),fg="maroon").grid(row=1,column=3)
    global mathsmarks,physicsmarks,chemistrymarks
    physicsmarks=[]
    chemistrymarks=[]
    mathsmarks=[]
    import mysql.connector
    sql=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="coaching")
    cur=sql.cursor()
    class9th="SELECT first_name FROM login WHERE current_class='9' "
    cur.execute(class9th)
    var9=cur.fetchall()
    for i in range(0,variable1):               
        label1=Label(marks_page9,text=var9[i][0],font=("Constantia",15),fg="RoyalBlue4")
        label1.grid(row=2+i,column=0)
        physics=IntVar()
        chemistry=IntVar()
        maths=IntVar()
        e1=Entry(marks_page9,textvariable=physics)
        e1.grid(row=2+i,column=1)
        e2=Entry(marks_page9,textvariable=chemistry)
        e2.grid(row=2+i,column=2)
        e3=Entry(marks_page9,textvariable=maths)
        e3.grid(row=2+i,column=3)

        physicsmarks.append(e1)
        chemistrymarks.append(e2)
        mathsmarks.append(e3)
        
    Button(marks_page9,text="SUBMIT",command=marks9submit).grid(row=variable1+2,column=2)

def marks9submit():
    import mysql.connector
    sql=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="coaching")
    cur=sql.cursor()
    class9th="SELECT first_name FROM login WHERE current_class='9' "
    cur.execute(class9th)
    var9=cur.fetchall()
    for p in range(0,variable1):    
        var="INSERT INTO test_marks_of9(first_name,current_class,physics,chemistry,maths) VALUES (%s,%s,%s,%s,%s)"
        value=(var9[p][0],9,physicsmarks[p].get(),chemistrymarks[p].get(),mathsmarks[p].get())
        cur.execute(var,value)
        sql.commit()

def marks_of10():
    marks_page10=Toplevel()
    marks_page10.geometry("1366x768")
    marks_page10.title("Test Marks of 10")
    Label(marks_page10,text="**TEST MARKS ENTRY FOR CLASS X**",font=("Copperplate Gothic Bold",28,"underline"),fg="midnight blue").grid(row=0,column=2)
    Label(marks_page10,text="STUDENTS:-",font=("Candara Light",18,"underline","bold"),fg="maroon").grid(row=1,column=0)
    Label(marks_page10,text="PHYSICS:-",font=("Candara Light",18,"underline","bold"),fg="maroon").grid(row=1,column=1)
    Label(marks_page10,text="CHEMISTRY:-",font=("Candara Light",18,"underline","bold"),fg="maroon").grid(row=1,column=2)
    Label(marks_page10,text="MATHS:-",font=("Candara Light",18,"underline","bold"),fg="maroon").grid(row=1,column=3)
    global phymarks,chemmarks,mmarks
    phymarks=[]
    chemmarks=[]
    mmarks=[]
    import mysql.connector
    sql=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="coaching")
    cur=sql.cursor()
    class10th="SELECT first_name FROM login WHERE current_class='10' "
    cur.execute(class10th)
    var10=cur.fetchall()
    for i in range(0,variable2):               
        label1=Label(marks_page10,text=var10[i][0],font=("Constantia",15),fg="RoyalBlue4")
        label1.grid(row=2+i,column=0)
        physics=IntVar()
        chemistry=IntVar()
        maths=IntVar()
        e1=Entry(marks_page10,textvariable=physics)
        e1.grid(row=2+i,column=1)
        e2=Entry(marks_page10,textvariable=chemistry)
        e2.grid(row=2+i,column=2)
        e3=Entry(marks_page10,textvariable=maths)
        e3.grid(row=2+i,column=3)
        phymarks.append(e1)
        chemmarks.append(e2)
        mmarks.append(e3)
    Button(marks_page10,text="SUBMIT",command=marks10submit).grid(row=variable1+2,column=2)

def marks10submit():
    import mysql.connector
    sql=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="coaching")
    cur=sql.cursor()
    class10th="SELECT first_name FROM login WHERE current_class='10' "
    cur.execute(class10th)
    var10=cur.fetchall()
    for r in range(0,variable2):    
        var="INSERT INTO test_marks_of10(first_name,current_class,physics,chemistry,maths) VALUES (%s,%s,%s,%s,%s)"
        value=(var10[r][0],9,phymarks[r].get(),chemmarks[r].get(),mmarks[r].get())
        cur.execute(var,value)
        sql.commit()

    
def entries_of10():
    n10=name_of10.get()
    c10=class_of10.get()
    import mysql.connector
    sql=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="coaching")
    cur=sql.cursor()
    comm="SELECT first_name,last_name,gender,father_name,mother_name,current_class,previous_class_marks,mobile_no,address,gmail FROM login WHERE first_name='{}' and current_class='{}' ".format(n10,c10)
    cur.execute(comm)
    store_of10=cur.fetchall()
    for i in store_of10:
        Label(detail_of10,text=i[0],font=("Candara Light",18,"bold"),fg="navy").grid(row=3,column=2)
        Label(detail_of10,text=i[1],font=("Candara Light",18,"bold"),fg="navy").grid(row=4,column=2)
        Label(detail_of10,text=i[2],font=("Candara Light",18,"bold"),fg="navy").grid(row=5,column=2)
        Label(detail_of10,text=i[3],font=("Candara Light",18,"bold"),fg="navy").grid(row=6,column=2)
        Label(detail_of10,text=i[4],font=("Candara Light",18,"bold"),fg="navy").grid(row=7,column=2)
        Label(detail_of10,text=i[5],font=("Candara Light",18,"bold"),fg="navy").grid(row=8,column=2)
        Label(detail_of10,text=i[6],font=("Candara Light",18,"bold"),fg="navy").grid(row=9,column=2)
        Label(detail_of10,text=i[7],font=("Candara Light",18,"bold"),fg="navy").grid(row=10,column=2)
        Label(detail_of10,text=i[8],font=("Candara Light",18,"bold"),fg="navy").grid(row=11,column=2)
        Label(detail_of10,text=i[9],font=("Candara Light",18,"bold"),fg="navy").grid(row=12,column=2)

def entries_of9():
    n9=name_of9.get()
    c9=class_of9.get()
    import mysql.connector
    sql=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="coaching")
    cur=sql.cursor()
    comm="SELECT first_name,last_name,gender,father_name,mother_name,current_class,previous_class_marks,mobile_no,address,gmail FROM login WHERE first_name='{}' and current_class='{}' ".format(n9,c9)
    cur.execute(comm)
    store_of9=cur.fetchall()
    for i in store_of9:
        Label(detail_of9,text=i[0],font=("Candara Light",18,"bold"),fg="navy").grid(row=3,column=2)
        Label(detail_of9,text=i[1],font=("Candara Light",18,"bold"),fg="navy").grid(row=4,column=2)
        Label(detail_of9,text=i[2],font=("Candara Light",18,"bold"),fg="navy").grid(row=5,column=2)
        Label(detail_of9,text=i[3],font=("Candara Light",18,"bold"),fg="navy").grid(row=6,column=2)
        Label(detail_of9,text=i[4],font=("Candara Light",18,"bold"),fg="navy").grid(row=7,column=2)
        Label(detail_of9,text=i[5],font=("Candara Light",18,"bold"),fg="navy").grid(row=8,column=2)
        Label(detail_of9,text=i[6],font=("Candara Light",18,"bold"),fg="navy").grid(row=9,column=2)
        Label(detail_of9,text=i[7],font=("Candara Light",18,"bold"),fg="navy").grid(row=10,column=2)
        Label(detail_of9,text=i[8],font=("Candara Light",18,"bold"),fg="navy").grid(row=11,column=2)
        Label(detail_of9,text=i[9],font=("Candara Light",18,"bold"),fg="navy").grid(row=12,column=2)

def entries_of8():
    n8=name_of8.get()
    c8=class_of8.get()
    import mysql.connector
    sql=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="coaching")
    cur=sql.cursor()
    comm="SELECT first_name,last_name,gender,father_name,mother_name,current_class,previous_class_marks,mobile_no,address,gmail FROM login WHERE first_name='{}' and current_class='{}' ".format(n8,c8)
    cur.execute(comm)
    store_of8=cur.fetchall()
    for i in store_of8:
        Label(detail_of8,text=i[0],font=("Candara Light",18,"bold"),fg="navy").grid(row=3,column=2)
        Label(detail_of8,text=i[1],font=("Candara Light",18,"bold"),fg="navy").grid(row=4,column=2)
        Label(detail_of8,text=i[2],font=("Candara Light",18,"bold"),fg="navy").grid(row=5,column=2)
        Label(detail_of8,text=i[3],font=("Candara Light",18,"bold"),fg="navy").grid(row=6,column=2)
        Label(detail_of8,text=i[4],font=("Candara Light",18,"bold"),fg="navy").grid(row=7,column=2)
        Label(detail_of8,text=i[5],font=("Candara Light",18,"bold"),fg="navy").grid(row=8,column=2)
        Label(detail_of8,text=i[6],font=("Candara Light",18,"bold"),fg="navy").grid(row=9,column=2)
        Label(detail_of8,text=i[7],font=("Candara Light",18,"bold"),fg="navy").grid(row=10,column=2)
        Label(detail_of8,text=i[8],font=("Candara Light",18,"bold"),fg="navy").grid(row=11,column=2)
        Label(detail_of8,text=i[9],font=("Candara Light",18,"bold"),fg="navy").grid(row=12,column=2)
def class8_detail():
    global detail_of8
    detail_of8=Toplevel()
    detail_of8.geometry("1366x768")
    detail_of8.title("CLASS 8th DETAILS")
    global name_of8,class_of8
    name_of8=StringVar()
    class_of8=IntVar()
    Label(detail_of8,text="**DETAILS OF CLASS 8 STUDENT**",font=("Copperplate Gothic Bold",28,"underline"),fg="purple").grid(row=0,column=1)
    Label(detail_of8,text="ENTER STUDENT NAME:",font=("Candara Light",18,"bold")).grid(row=1,column=0)
    Label(detail_of8,text="ENTER STUDENT CLASS:",font=("Candara Light",18,"bold")).grid(row=2,column=0)
    Button(detail_of8,text="ENTER",command=entries_of8).grid(row=2,column=2)
    Entry(detail_of8,textvariable=name_of8).grid(row=1,column=1)
    Entry(detail_of8,textvariable=class_of8).grid(row=2,column=1)
    Label(detail_of8,text="FIRST NAME:",font=("Candara Light",18,"bold"),fg="navy").grid(row=3,column=0)
    Label(detail_of8,text="LAST NAME:",font=("Candara Light",18,"bold"),fg="navy").grid(row=4,column=0)
    Label(detail_of8,text="GENDER:",font=("Candara Light",18,"bold"),fg="navy").grid(row=5,column=0)
    Label(detail_of8,text="FATHER'S NAME:",font=("Candara Light",18,"bold"),fg="navy").grid(row=6,column=0)
    Label(detail_of8,text="MOTHER'S NAME:",font=("Candara Light",18,"bold"),fg="navy").grid(row=7,column=0)
    Label(detail_of8,text="CURRENT STUDYING CLASS:",font=("Candara Light",18,"bold"),fg="navy").grid(row=8,column=0)
    Label(detail_of8,text="PREVIOUS CLASS MARKS:",font=("Candara Light",18,"bold"),fg="navy").grid(row=9,column=0)
    Label(detail_of8,text="MOBILE NUMBER:",font=("Candara Light",18,"bold"),fg="navy").grid(row=10,column=0)
    Label(detail_of8,text="ADDRESS:",font=("Candara Light",18,"bold"),fg="navy").grid(row=11,column=0)
    Label(detail_of8,text="GMAIL ID:",font=("Candara Light",18,"bold"),fg="navy").grid(row=12,column=0)
    
    
def class9_detail():
    global detail_of9
    detail_of9=Toplevel()
    detail_of9.geometry("1366x768")
    detail_of9.title("CLASS 9th DETAILS")
    global name_of9,class_of9
    name_of9=StringVar()
    class_of9=IntVar()
    Label(detail_of9,text="**DETAILS OF CLASS 9 STUDENT**",font=("Copperplate Gothic Bold",28,"underline"),fg="purple").grid(row=0,column=1)
    Label(detail_of9,text="ENTER STUDENT NAME:",font=("Candara Light",18,"bold")).grid(row=1,column=0)
    Label(detail_of9,text="ENTER STUDENT CLASS:",font=("Candara Light",18,"bold")).grid(row=2,column=0)
    Button(detail_of9,text="ENTER",command=entries_of9).grid(row=2,column=2)
    Entry(detail_of9,textvariable=name_of9).grid(row=1,column=1)
    Entry(detail_of9,textvariable=class_of9).grid(row=2,column=1)
    Label(detail_of9,text="FIRST NAME:",font=("Candara Light",18,"bold"),fg="navy").grid(row=3,column=0)
    Label(detail_of9,text="LAST NAME:",font=("Candara Light",18,"bold"),fg="navy").grid(row=4,column=0)
    Label(detail_of9,text="GENDER:",font=("Candara Light",18,"bold"),fg="navy").grid(row=5,column=0)
    Label(detail_of9,text="FATHER'S NAME:",font=("Candara Light",18,"bold"),fg="navy").grid(row=6,column=0)
    Label(detail_of9,text="MOTHER'S NAME:",font=("Candara Light",18,"bold"),fg="navy").grid(row=7,column=0)
    Label(detail_of9,text="CURRENT STUDYING CLASS:",font=("Candara Light",18,"bold"),fg="navy").grid(row=8,column=0)
    Label(detail_of9,text="PREVIOUS CLASS MARKS:",font=("Candara Light",18,"bold"),fg="navy").grid(row=9,column=0)
    Label(detail_of9,text="MOBILE NUMBER:",font=("Candara Light",18,"bold"),fg="navy").grid(row=10,column=0)
    Label(detail_of9,text="ADDRESS:",font=("Candara Light",18,"bold"),fg="navy").grid(row=11,column=0)
    Label(detail_of9,text="GMAIL ID:",font=("Candara Light",18,"bold"),fg="navy").grid(row=12,column=0)

def class10_detail():
    global detail_of10
    detail_of10=Toplevel()
    detail_of10.geometry("1366x768")
    detail_of10.title("CLASS 10th DETAILS")
    global name_of10,class_of10
    name_of10=StringVar()
    class_of10=IntVar()
    Label(detail_of10,text="**DETAILS OF CLASS 10 STUDENT**",font=("Copperplate Gothic Bold",28,"underline"),fg="purple").grid(row=0,column=1)
    Label(detail_of10,text="ENTER STUDENT NAME:",font=("Candara Light",18,"bold")).grid(row=1,column=0)
    Label(detail_of10,text="ENTER STUDENT CLASS:",font=("Candara Light",18,"bold")).grid(row=2,column=0)
    Button(detail_of10,text="ENTER",command=entries_of10).grid(row=2,column=2)
    Entry(detail_of10,textvariable=name_of10).grid(row=1,column=1)
    Entry(detail_of10,textvariable=class_of10).grid(row=2,column=1)
    Label(detail_of10,text="FIRST NAME:",font=("Candara Light",18,"bold"),fg="navy").grid(row=3,column=0)
    Label(detail_of10,text="LAST NAME:",font=("Candara Light",18,"bold"),fg="navy").grid(row=4,column=0)
    Label(detail_of10,text="GENDER:",font=("Candara Light",18,"bold"),fg="navy").grid(row=5,column=0)
    Label(detail_of10,text="FATHER'S NAME:",font=("Candara Light",18,"bold"),fg="navy").grid(row=6,column=0)
    Label(detail_of10,text="MOTHER'S NAME:",font=("Candara Light",18,"bold"),fg="navy").grid(row=7,column=0)
    Label(detail_of10,text="CURRENT STUDYING CLASS:",font=("Candara Light",18,"bold"),fg="navy").grid(row=8,column=0)
    Label(detail_of10,text="PREVIOUS CLASS MARKS:",font=("Candara Light",18,"bold"),fg="navy").grid(row=9,column=0)
    Label(detail_of10,text="MOBILE NUMBER:",font=("Candara Light",18,"bold"),fg="navy").grid(row=10,column=0)
    Label(detail_of10,text="ADDRESS:",font=("Candara Light",18,"bold"),fg="navy").grid(row=11,column=0)
    Label(detail_of10,text="GMAIL ID:",font=("Candara Light",18,"bold"),fg="navy").grid(row=12,column=0)


def signup():
    tea_id=t_id.get()
    teacher_pw=t_password.get()
    import mysql.connector
    obj8=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="coaching")
    c8=obj8.cursor()
    sql8="SELECT teacher_id,teacher_password FROM teacher WHERE teacher_id='{}' and teacher_password='{}' ".format(tea_id,teacher_pw) 
    c8.execute(sql8)
    y8=c8.fetchall()
    for k in y8:
        if(k[0]==tea_id and k[1]==teacher_pw):
            import mysql.connector
            var1=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="coaching")
            ob=var1.cursor()
            var2="SELECT COUNT(current_class) FROM login WHERE current_class='8' "
            var3="SELECT COUNT(current_class) FROM login WHERE current_class='9' "
            var4="SELECT COUNT(current_class) FROM login WHERE current_class='10' "
            class8="SELECT first_name FROM login WHERE current_class='8' "
            class9="SELECT first_name FROM login WHERE current_class='9' "
            class10="SELECT first_name FROM login WHERE current_class='10' "
            ob.execute(var2)
            var5=ob.fetchall()
            ob.execute(class8)
            var8=ob.fetchall()
            ob.execute(var3)
            var6=ob.fetchall()
            ob.execute(class9)
            var9=ob.fetchall()
            ob.execute(var4)
            var7=ob.fetchall()
            ob.execute(class10)
            var10=ob.fetchall()
            pages=Toplevel()
            pages.geometry("1366x768")
            pages.title("STUDENT DETAILS")
            Label(pages,text="**STUDENT DETAILS**",font=("Copperplate Gothic Bold",28,"underline"),fg="midnight blue").grid(row=0,column=1,columnspan=5)
            Button(pages,text="CLASS 8 TEST ENTRY",borderwidth=4,relief="raised",command=marks_of8).grid(row=3,column=6,padx=30,pady=10)
            Button(pages,text="CLASS 9 TEST ENTRY",borderwidth=4,relief="raised",command=marks_of9).grid(row=4,column=6,padx=30,pady=10)
            Button(pages,text="CLASS 10 TEST ENTRY",borderwidth=4,relief="raised",command=marks_of10).grid(row=5,column=6,padx=30,pady=10)
            Label(pages,text="STUDENTS OF CLASS VIII:",font=("Constantia",15,"underline"),fg="maroon").grid(row=1,column=0,pady=15,padx=10)
            Label(pages,text=var5[0][0],font=("Constantia",15,"underline"),fg="maroon").grid(row=1,column=1,pady=15,padx=10)
            Label(pages,text=var6[0][0],font=("Constantia",15,"underline"),fg="maroon").grid(row=1,column=3,pady=15,padx=10)
            Label(pages,text=var7[0][0],font=("Constantia",15,"underline"),fg="maroon").grid(row=1,column=5,pady=15,padx=10)
            Label(pages,text="STUDENTS OF CLASS IX:",font=("Constantia",15,"underline"),fg="maroon").grid(row=1,column=2,pady=15,padx=10)
            Label(pages,text="STUDENTS OF CLASS X:",font=("Constantia",15,"underline"),fg="maroon").grid(row=1,column=4,pady=15,padx=10)
            global variable,variable1,variable2
            variable=var5[0][0]
            variable1=var6[0][0]
            variable2=var7[0][0]
            global i
            for i in range(0,variable):               
                label1=Label(pages,text=var8[i][0],font=("Constantia",15,"underline"),fg="RoyalBlue4")
                label1.grid(row=2+i,column=0)
                label1.bind("<Button-1>",lambda detail1:class8_detail())
            for j in range(0,variable1):
                label2=Label(pages,text=var9[j][0],font=("Constantia",15,"underline"),fg="RoyalBlue4")
                label2.grid(row=2+j,column=2)
                label2.bind("<Button-1>",lambda detail2:class9_detail())
            for k in range(0,variable2):
                label3=Label(pages,text=var10[k][0],font=("Constantia",15,"underline"),fg="RoyalBlue4")
                label3.grid(row=2+k,column=4)
                label3.bind("<Button-1>",lambda detail3:class10_detail())

def resetforteacher():
    t_id.set("0")
    t_password.set("")
def teacherlogin():
    page=Toplevel()
    page.geometry("1366x768")
    global t_id,t_password
    t_id=IntVar()
    t_password=StringVar()
    page.title("TEACHER LOGIN")
    Label(page,text="**TEACHER'S LOGIN**",font=("Copperplate Gothic Bold",28,"underline"),fg="purple").grid(row=0,column=2)
    Label(page,text="TEACHER ID",font=("Constantia",16,"bold"),fg="darkblue").grid(row=1,column=0,pady=40,padx=20)
    Label(page,text="TEACHER PASSWORD",font=("Constantia",16,"bold"),fg="darkblue").grid(row=2,column=0,padx=20)
    Entry(page,textvariable=t_id).grid(row=1,column=1,padx=50)
    Entry(page,textvariable=t_password,show="*").grid(row=2,column=1,padx=50)
    Button(page,text="SUBMIT",borderwidth=4,relief="raised",command=signup).grid(row=4,column=0,pady=40)
    Button(page,text="RESET",borderwidth=4,relief="raised",command=resetforteacher).grid(row=4,column=1,pady=40)

def scholarship():
    z=Toplevel()
    z.geometry("1366x768")
    z.title("Scholarship")
    Label(z,text="**SCHOLARSHIP CRITERIA**",font=("Copperplate Gothic Bold",28,"bold","underline"),fg="mistyrose4").grid(row=0,column=0)
    Label(z,text="CRITERIA FOR CLASS VIII:",font=("calibri 20 bold underline")).grid(row=1,column=0)
    Label(z,text=":- STUDENT MUST POSSESS 90% MARKS FOR FULL SCHOLARSHIP.",font=("calibri 14 bold")).grid(row=2,column=0)
    Label(z,text=":- 75% SCHOLARSHIP FOR THOSE STUDENTS WHO SCORED 85% MARKS.",font=("calibri 14 bold")).grid(row=3,column=0)
    Label(z,text=":- 50% SCHOLARSHIP FOR THOSE STUDENTS WHO SCORED 80% MARKS.",font=("calibri 14 bold")).grid(row=4,column=0)
    Label(z,text="CRITERIA FOR CLASS IX",font=("calibri 20 bold underline")).grid(row=5,column=0,pady=50)
    Label(z,text=":- STUDENT MUST POSSESS 90% MARKS FOR FULL SCHOLARSHIP.",font=("calibri 14 bold")).grid(row=6,column=0)
    Label(z,text=":- 50% SCHOLARSHIP FOR THOSE STUDENTS WHO SCORED 85% MARKS.",font=("calibri 14 bold")).grid(row=7,column=0)
    Label(z,text="CRITERIA FOR CLASS X",font=("calibri 20 bold underline")).grid(row=8,column=0,pady=50)
    Label(z,text=":- STUDENT MUST POSSESS 90% MARKS FOR FULL SCHOLARSHIP.",font=("calibri 14 bold")).grid(row=9,column=0)
    Label(z,text=":- 80% SCHOLARSHIP FOR THOSE STUDENTS WHO SCORED 85% MARKS.",font=("calibri 14 bold")).grid(row=10,column=0)
    Label(z,text=":- 65% SCHOLARSHIP FOR THOSE WHO SCORED 80% MARKS.",font=("calibri 14 bold")).grid(row=11,column=0)

def entry():
    username=name.get()
    pw=password.get()
    import mysql.connector
    obj1=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="coaching")
    c1=obj1.cursor()
    sql1="SELECT gmail,password,current_class FROM login WHERE gmail='{}' or password='{}' ".format(username,pw) 
    c1.execute(sql1)
    y1=c1.fetchall()
    for j in y1:
        if(j[0]==username and j[1]==pw):
             v=j[2]
             x="SELECT COUNT(current_class) FROM login WHERE current_class='{}' ".format(v)
             c1.execute(x)
             y2=c1.fetchall()

             nextpage=Toplevel()
             nextpage.geometry("1366x768")
             nextpage.title("WELCOME")

             if(v==10 and y2[0][0]<=40):
                Label(nextpage,text="CONGRATULATIONS!! YOU ARE REGISTERED",font=("Colonna MT",28,"underline","bold"),fg="plum4").grid(row=0,column=1)
                Label(nextpage,text="TEST MARKS",font=("Colonna MT",20,"underline","bold"),fg="midnight blue").grid(row=1,column=1,pady=20)
                Label(nextpage,text="PHYSICS",font=("Candara Light",20,"underline","bold"),fg="midnight blue").grid(row=2,column=0,pady=10)
                Label(nextpage,text="CHEMISTRY",font=("Candara Light",20,"underline","bold"),fg="midnight blue").grid(row=2,column=1,pady=10)
                Label(nextpage,text="MATHS",font=("Candara Light",20,"underline","bold"),fg="midnight blue").grid(row=2,column=2,pady=10)
                query1="SELECT first_name FROM login WHERE gmail='{}'".format(j[0])
                c1.execute(query1)
                result1=c1.fetchall()
                query2="SELECT physics,chemistry,maths FROM test_marks_of10 WHERE first_name='{}'".format(result1[0][0])
                c1.execute(query2)
                result2=c1.fetchall()
                for answer in result2:
                    Label(nextpage,text=answer[0],font=("Candara Light",15,"bold")).grid(row=3,column=0)
                    Label(nextpage,text=answer[1],font=("Candara Light",15,"bold")).grid(row=3,column=1)
                    Label(nextpage,text=answer[2],font=("Candara Light",15,"bold")).grid(row=3,column=2)
                    
                break   # j consists 3 values so loop works 3 times so it will give 3 pages simultaneously,thats why use break.
             elif(v==9 and y2[0][0]<=40):
                Label(nextpage,text="CONGRATULATIONS!! YOU ARE REGISTERED",font=("Colonna MT",28,"bold"),fg="plum4").grid(row=0,column=1)
                Label(nextpage,text="TEST MARKS",font=("Colonna MT",20,"underline","bold"),fg="midnight blue").grid(row=1,column=1,pady=20)
                Label(nextpage,text="PHYSICS",font=("Candara Light",20,"underline","bold"),fg="midnight blue").grid(row=2,column=0,pady=10)
                Label(nextpage,text="CHEMISTRY",font=("Candara Light",20,"underline","bold"),fg="midnight blue").grid(row=2,column=1,pady=10)
                Label(nextpage,text="MATHS",font=("Candara Light",20,"underline","bold"),fg="midnight blue").grid(row=2,column=2,pady=10)
                query3="SELECT first_name FROM login WHERE gmail='{}'".format(j[0])
                c1.execute(query3)
                result2=c1.fetchall()
                query4="SELECT physics,chemistry,maths FROM test_marks_of9 WHERE first_name='{}'".format(result2[0][0])
                c1.execute(query4)
                result3=c1.fetchall()
                for answer1 in result3:
                    Label(nextpage,text=answer1[0],font=("Candara Light",15,"bold")).grid(row=3,column=0)
                    Label(nextpage,text=answer1[1],font=("Candara Light",15,"bold")).grid(row=3,column=1)
                    Label(nextpage,text=answer1[2],font=("Candara Light",15,"bold")).grid(row=3,column=2)
                    
                break
             elif(v==8 and y2[0][0]<=40):
                Label(nextpage,text="CONGRATULATIONS!! YOU ARE REGISTERED",font=("Colonna MT",28,"bold"),fg="plum4").grid(row=0,column=0,columnspan=3)
                Label(nextpage,text="TEST MARKS",font=("Colonna MT",20,"underline","bold"),fg="midnight blue").grid(row=1,column=0,columnspan=3,pady=20)
                Label(nextpage,text="SCIENCE",font=("Candara Light",20,"underline","bold"),fg="midnight blue").grid(row=2,column=0,pady=10)
                Label(nextpage,text="MATHS",font=("Candara Light",20,"underline","bold"),fg="midnight blue").grid(row=2,column=1,pady=10)     
                query5="SELECT first_name FROM login WHERE gmail='{}'".format(j[0])
                c1.execute(query5)
                result4=c1.fetchall()
                query6="SELECT science,maths FROM test_marks_of8 WHERE first_name='{}'".format(result4[0][0])
                c1.execute(query6)
                result5=c1.fetchall()
                for answer2 in result5:
                    Label(nextpage,text=answer2[0],font=("Candara Light",15,"bold")).grid(row=3,column=0)
                    Label(nextpage,text=answer2[1],font=("Candara Light",15,"bold")).grid(row=3,column=1)
                    
                break
             else:
                Label(nextpage,text="OOPS!! THE SEATS ARE FILLED",font=("Colonna MT",28,"bold"),fg="plum4").grid(row=0,column=0)
                break
    


def register():
    q=first.get().upper()
    w=last.get().upper()
    e=gender.get()
    r=father.get().upper()
    t=mother.get().upper()
    y=current_class.get()
    u=previous_class_marks.get()
    i=mobile.get()
    o=address.get()
    p=gmail.get()
    h=pwd.get()
    import mysql.connector
    sql=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="coaching")
    c=sql.cursor()
    a="INSERT INTO login(first_name,last_name,gender,father_name,mother_name,current_class,previous_class_marks,mobile_no,address,gmail,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    b=(q,w,e,r,t,y,u,i,o,p,h)
    c.execute(a,b)
    sql.commit()
    Label(level,text="SUCCESSFULLY SIGNED UP :-)",font=("Castellar 12 bold"),fg="navy").grid(row=13,column=1,pady=20)

def resetforlogin():
    first.set("")
    last.set("")
    gender.set("")
    father.set("")
    mother.set("")
    current_class.set("0")
    previous_class_marks.set("0")
    mobile.set("0")
    address.set("")
    gmail.set("")
    pwd.set("")

def loginpage():
    global level
    level=Toplevel()
    level.geometry("1366x768")
    level.title("LOGIN PAGE")
    global first,last,gender,father,mother,current_class,previous_class_marks,mobile,address,gmail,pwd
    first=StringVar()
    last=StringVar()
    gender=StringVar()
    father=StringVar()
    mother=StringVar()
    current_class=IntVar()
    previous_class_marks=IntVar()
    mobile=IntVar()
    address=StringVar()
    gmail=StringVar()
    pwd=StringVar()
    Label(level,text="**LOGIN PAGE**",font=("Copperplate Gothic Bold",28,"underline"),fg="coral4").grid(row=0,column=3,columnspan=3)
    Label(level,text="FIRST NAME",font=("Candara Light",18,"bold"),fg="navy").grid(row=1,column=0)
    Label(level,text="LAST NAME",font=("Candara Light",18,"bold"),fg="navy").grid(row=2,column=0)
    Label(level,text="GENDER",font=("Candara Light",18,"bold"),fg="navy").grid(row=3,column=0)
    Label(level,text="FATHER'S NAME",font=("Candara Light",18,"bold"),fg="navy").grid(row=4,column=0)
    Label(level,text="MOTHER'S NAME",font=("Candara Light",18,"bold"),fg="navy").grid(row=5,column=0)
    Label(level,text="CURRENT STUDYING CLASS",font=("Candara Light",18,"bold"),fg="navy").grid(row=6,column=0)
    Label(level,text="PREVIOUS CLASS MARKS",font=("Candara Light",18,"bold"),fg="navy").grid(row=7,column=0)
    Label(level,text="MOBILE NUMBER",font=("Candara Light",18,"bold"),fg="navy").grid(row=8,column=0)
    Label(level,text="ADDRESS",font=("Candara Light",18,"bold"),fg="navy").grid(row=9,column=0)
    Label(level,text="** GMAIL ID",font=("Candara Light",18,"bold"),fg="navy").grid(row=10,column=0)
    Label(level,text="** SET PASSWORD",font=("Candara Light",18,"bold"),fg="navy").grid(row=11,column=0)
    Entry(level,textvariable=first).grid(row=1,column=1)
    Entry(level,textvariable=last).grid(row=2,column=1)
    Entry(level,textvariable=gender).grid(row=3,column=1)
    Entry(level,textvariable=father).grid(row=4,column=1)
    Entry(level,textvariable=mother).grid(row=5,column=1)
    Entry(level,textvariable=current_class).grid(row=6,column=1)
    Entry(level,textvariable=previous_class_marks).grid(row=7,column=1)
    Entry(level,textvariable=mobile).grid(row=8,column=1)
    Entry(level,textvariable=address).grid(row=9,column=1)
    Entry(level,textvariable=gmail).grid(row=10,column=1)
    Entry(level,textvariable=pwd).grid(row=11,column=1)
    Label(level,text="** 8 CHARACTERS ONLY",font=("Candara Light",12,"bold"),fg="coral4").grid(row=11,column=2)
    Button(level,text="SUBMIT",borderwidth=4,relief="raised",command=register).grid(row=12,column=0,pady=20)
    Button(level,text="RESET",borderwidth=4,relief="raised",command=resetforlogin).grid(row=12,column=1,pady=20)

def resetforregister():
    name.set("")
    password.set("")
def secpage():
    global a
    a=Toplevel()
    a.geometry("1366x768")
    a.title("Registration")
    global name
    global password
    name=StringVar()
    password=StringVar()
    f=Frame(a)
    f.pack()
    global f2
    f2=Frame(a)
    f2.pack()
    c=Label(f,text="**REGISTRATION**",font=("Broadway 28 bold underline"),fg="purple")
    c.grid(row=0,columnspan=10)
    Label(f2,text="STUDENT USERNAME", font=("Constantia",12,"bold"),fg="DeepPink4").grid(row=2,column=1,pady=30)
    Entry(f2,textvariable=name).grid(row=2,column=2)
    Label(f2,text="STUDENT PASSWORD", font=("Constantia",12,"bold"),fg="DeepPink4").grid(row=3,column=1)
    Entry(f2,textvariable=password,show="*").grid(row=3,column=2)
    Label(f2,text="**SCHOLARSHIP PROVIDED(BASED ON PREVIOUS YEAR MARKS)**",font=("Candara Light",12,"bold"),fg="red4").grid(row=2,column=3,padx=70)
    l1=Label(f2,text="CLICK ON THIS LINK FOR SCHOLARSHIP CRITERIA",font=("Candara Light",12,"bold","underline"),fg="red4")
    l1.grid(row=3,column=3,padx=70)
    l1.bind("<Button-1>",lambda t:scholarship())
    Button(f2,text="REGISTER",borderwidth=4,relief="groove",command=entry).grid(row=4,column=1,pady=20)
    Button(f2,text="RESET",borderwidth=4,relief="groove",command=resetforregister).grid(row=4,column=2,pady=20)
    l2=Label(f2,text="CREATE ACCOUNT,IF NOT ANY",font=("Candara Light",12,"underline","bold"),fg="DeepPink4")
    l2.grid(row=5,column=1)
    l2.bind("<Button-1>",lambda g:loginpage())
    Label(f2,text="OUR FACULTY MEMBERS",font=("Algerian",14,"underline","bold"),fg="midnight blue").grid(row=6,columnspan=10,pady=10)
    t1=ImageTk.PhotoImage(Image.open("t1.jpg"))
    Label(f2,image=t1,bg="black").grid(row=7,column=0)
    a1=ImageTk.PhotoImage(Image.open("t2.jpg"))
    Label(f2,image=a1,bg="black").grid(row=7,column=2)
    b1=ImageTk.PhotoImage(Image.open("t3.jpg"))
    Label(f2,image=b1,bg="black").grid(row=7,column=3)
    Label(f2,text="MS.SHIKHA SINGH",font=("Constantia",10,"bold","underline"),fg="dodgerblue4").grid(row=8,column=0)
    Label(f2,text="B.A, M.A, PHD",font=("Constantia",10,"bold"),fg="dodgerblue4").grid(row=9,column=0)
    Label(f2,text="(WITH 5 YEARS EXP.)",font=("Constantia",10,"bold"),fg="dodgerblue4").grid(row=10,column=0)
    Label(f2,text="(WITH 2 YEARS EXP.)",font=("Constantia",10,"bold"),fg="dodgerblue4").grid(row=10,column=2)
    Label(f2,text="(WITH 2 YEARS EXP.)",font=("Constantia",10,"bold"),fg="dodgerblue4").grid(row=10,column=3)
    Label(f2,text="B.TECH, M.TECH",font=("Constantia",10,"bold"),fg="dodgerblue4").grid(row=9,column=2)
    Label(f2,text="B.TECH, MBA",font=("Constantia",10,"bold"),fg="dodgerblue4").grid(row=9,column=3)
    Label(f2,text="MS.REKHA SHARMA",font=("Constantia",10,"bold","underline"),fg="dodgerblue4").grid(row=8,column=2)
    Label(f2,text="MR.SANJAY SINGHANIA",font=("Constantia",10,"bold","underline"),fg="dodgerblue4").grid(row=8,column=3)
    a.mainloop()
root=Tk()
root.geometry("1366x768")
root.title("welcome")    
Label(root,text="WELCOME TO OUR COACHING CENTER",font=("CASTELLAR",25,"underline","bold"),fg="black").pack()
bookimage=ImageTk.PhotoImage(Image.open("book.png"))
Label(root,image=bookimage,bg="black").pack(pady=30)
Label(root,text="HOME TUITION FOR CLASSES VIII, IX AND X(ALL SUBJECTS), BY BEST FACULTY MEMBERS",font=("Footlight MT Light",14,"bold"),fg="blue").pack()
Label(root,text="FRESH BATCHES FOR MENTIONED CLASSES START FROM: 1 NOVEMBER,2019",font=("Footlight MT Light",14,"bold"),fg="blue").pack()
Label(root,text="TIMINGS: FOR VIII(4PM-5PM), IX(5PM-6PM) AND X(6PM-7PM)",font=("Footlight MT Light",14,"bold"),fg="purple").pack()
Label(root,text="ADDRESS: 6/23, NAI BASTI, NEAR SEEMA MULTIPLEX, ALIGARH.",font=("Footlight MT Light",14,"bold"),fg="purple").pack()
Label(root,text="FOR MORE DETAILS CONTACT US AT: 9789673458, 9245673869", font=("Footlight MT Light",14,"bold"),fg="purple").pack()
b=Button(root,text="ENTER TO REGISTER",relief="raised",borderwidth=4,command=secpage)#relief=ridge,sunken,groove,solid
b.pack(pady=30)
Button(root,text="TEACHER'S LOGIN", relief="raised",borderwidth=4,command=teacherlogin).pack()
root.mainloop()
