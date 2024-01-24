from tkinter import *
import mysql.connector as mysql
import tkinter.messagebox as MessageBox

def insert():
    id=s_id.get()
    name = s_name.get()
    last = s_last.get()
    classv = s_class.get()
    address = s_address.get()
    pin = s_pin.get()

    if( name=="" or last=="" or classv=="" or address=="" or pin==""):
        MessageBox.showinfo("Insert status", " All fields are require ")
    else:
        con = mysql.connect(host="localhost", user="root", passwd="Abhay@000", database="abhay")

        cursor=con.cursor()
        sql="insert into student values( %s , %s, %s, %s, %s, %s )"
        valu=(id,name,last,classv,address,pin)

        cursor.execute(sql,valu)
        con.commit();

        s_id.delete(0,'end')
        s_name.delete(0,'end')
        s_last.delete(0,'end')
        s_class.delete(0,'end')
        s_address.delete(0,'end')
        s_pin.delete(0,'end')

        show()
        MessageBox.showinfo("Insert status","inserted successfully");

        con.close()

def delete():
    if (s_id.get()==""):
        MessageBox.showinfo("Delete status ","Student id is compulsory fo delete")
    else:
        con = mysql.connect(host="localhost", user="root", passwd="Abhay@000", database="abhay")

        cursor = con.cursor()
        sql = "delete from student where sid='"+  s_id.get() +"'"

        cursor.execute(sql)
        con.commit();

        s_id.delete(0, 'end')
        s_name.delete(0, 'end')
        s_last.delete(0, 'end')
        s_class.delete(0, 'end')
        s_address.delete(0, 'end')
        s_pin.delete(0, 'end')

        show()
        MessageBox.showinfo("Delete status", "Delete successfully");
        con.close()

def update():
    id=s_id.get()
    fname=s_name.get()
    lname=s_last.get()
    classv=s_class.get()
    address=s_address.get()
    pin=s_pin.get()

    if (fname == "" or lname == "" or classv == "" or address == "" or pin == ""):
        MessageBox.showinfo("update status", " All fields are require ")
    else:
        con = mysql.connect(host="localhost", user="root", passwd="Abhay@000", database="abhay")

        cursor = con.cursor()
        sql = "update student set fname='" + fname + "',lname='" + lname + "',class='" + classv + "',address='" + address + "',pincode='" + pin + "' where sid='"+ id +"'"

        cursor.execute(sql)
        con.commit();

        s_id.delete(0, 'end')
        s_name.delete(0, 'end')
        s_last.delete(0, 'end')
        s_class.delete(0, 'end')
        s_address.delete(0, 'end')
        s_pin.delete(0, 'end')

        show()
        MessageBox.showinfo("update status", " update successfully");
        con.close()

def get():
    if (s_id.get()==""):
        MessageBox.showinfo("Get details","id is compulsory for getting details")

    else:
        con = mysql.connect(host="localhost", user="root", passwd="Abhay@000", database="abhay")

        cursor = con.cursor()
        sql = "select * from student where sid='"+ s_id.get()+"'"
        cursor.execute(sql)
        rows=cursor.fetchall()

        for row in rows:
              s_name.insert(0, row[1])
              s_last.insert(0, row[2])
              s_class.insert(0, row[3])
              s_address.insert(0, row[4])
              s_pin.insert(0, row[5])

        con.close();


def show():
    con = mysql.connect(host="localhost", user="root", passwd="Abhay@000", database="abhay")

    cursor = con.cursor()
    sql = "select * from student"
    cursor.execute(sql)
    i=1
    for student in cursor:
        for j in range(len(student)):
            e = Label( width=8, text=student[j])
            e.grid(row=i, column=j)

        i = i + 1



        e = Label( width=7, text='ID', borderwidth=2, relief='ridge', anchor='center', bg='yellow')
        e.grid(row=0, column=0,pady=2)
        e = Label( width=8, text='Name', borderwidth=2, relief='ridge', anchor='center', bg='yellow')
        e.grid(row=0, column=1)
        e = Label( width=8, text='Lastname', borderwidth=2, relief='ridge', anchor='center', bg='yellow')
        e.grid(row=0, column=2,)
        e = Label( width=7, text='Class', borderwidth=2, relief='ridge', anchor='center', bg='yellow')
        e.grid(row=0, column=3)
        e = Label( width=7, text='Address', borderwidth=2, relief='ridge', anchor='center', bg='yellow')
        e.grid(row=0, column=4)
        e = Label( width=7, text='Pincode', borderwidth=2, relief='ridge', anchor='center', bg='yellow')
        e.grid(row=0, column=5)



show();







root=Tk()
root.geometry("850x400")
root.title('CRUD operation')

Label(root,text="STUDENT CRUD OPERATION",font="Arial 20 bold",fg="blue").pack(pady=20)

Label(root,text="Student ID" ,font=('bold',10)).place(x=75,y=100)
Label(root,text="Student Name",font=('bold',10)).place(x=75,y=130)
Label(root,text="Last Name",font=('bold',10)).place(x=75,y=160)
Label(root,text="Class",font=('bold',10)).place(x=75,y=190)
Label(root,text="Address",font=('bold',10)).place(x=75,y=220)
Label(root,text="pincode",font=('bold',10)).place(x=75,y=250)




s_id=Entry(root)
s_id.place(x=200,y=100)
s_name=Entry(root)
s_name.place(x=200,y=130)
s_last=Entry(root)
s_last.place(x=200,y=160)
s_class=Entry(root)
s_class.place(x=200,y=190)
s_address=Entry(root)
s_address.place(x=200,y=220)
s_pin=Entry(root)
s_pin.place(x=200,y=250)

Button(root,text="Insert", font=('bold',10),command=insert).place(x=75,y=307)
Button(root,text="Delete", font=('bold',10),command=delete).place(x=150,y=307)
Button(root,text="Update",font=('bold',10),command=update).place(x=225,y=307)
Button(root,text="Get Details", font=('bold',10),command=get).place(x=300,y=307)


e=Listbox( width=70,height=15).place(x=400,y=97)




root.mainloop()


