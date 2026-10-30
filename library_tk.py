import tkinter as tk
from tkinter import Label, Entry, Button, Listbox
from unittest import result

import library
from library import Book, Library,User
import customtkinter as ctk




root=tk.Tk()
root.geometry("500x500")
root.title("library")
root.resizable(False,False)

library1=Library()
def add_click():
    name=entry1.get()
    author=entry2.get()
    year=entry3.get()
    price=entry4.get()
    status=entry5.get()
    book=Book(name,author,year,price,status)
    library1.add_book(book)
    show_click()
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    entry5.delete(0, tk.END)

def show_click():
    lst_box.delete(0,tk.END)
    res=library1.show_book()
    for item in res:
        lst_box.insert(tk.END,item)

def remove_click1():
    number=int(entry1.get())
    res=library1.remove_book(number)
    lst_box.delete(0,tk.END)
    lst_box.insert(tk.END,res)

def search_click():
    result=library1.search_book(entry1.get())
    lst_box.delete(0,tk.END)
    for item in result:
        lst_box.insert(tk.END,str(item))


def add_user():
    name=name_entry.get()
    user_ide=entry_user.get()
    user=User(name,user_ide)
    library1.add_user(user)
    lst_box.insert(tk.END,"کاربر اضافه شد")


def borrow_click():
   user_ide=entry_user.get()
   book_name=entry1.get()
   user=None
   book=None
   for u in library1.lst_users:
       if str(u.user_id)==str(user_ide):
           user=u
           print("4-کاربر بیدا شد")
           break
   for b in library1.lst_books:
       if b.name==book_name:
           book=b
           break
   if user is None:
       result="کاربری بیدا نشد"
   elif book is None:
       result="کتاب بیدا نشد"
   else:
       # print("user:",user.name,user.user_id)
       # print("book:",book.name,book.status)
       result=library1.borrow_book(user, book)
       lst_box.delete(0,tk.END)
       lst_box.insert(tk.END,result)

def return_click():
    user_ide=entry_user.get()
    book_name=entry1.get()
    user = None
    book = None
    for u in library1.lst_users:
        if u.user_id == user_ide:
            user = u
            break
    for b in library1.lst_books:
        if b.name == book_name:
            book = b
            break
    if user is None:
        result = "کاربری بیدا نشد"
    elif book is None:
        result = "کتاب بیدا نشد"
    elif book.status=="امانت داده شد":
        book.status = "موجود"
        library1.save_books()

        result = "کتاب با موفقیت بس گرفته شد"
    lst_box.delete(0, tk.END)
    lst_box.insert(tk.END, result)




lable_titel=Label(root,text="Library",font=(30))
lable_titel.place(x=235,y=15)

lable1=Label(root,text=": نام کتاب",font=("Arial",13,"bold"))
lable1.place(x=438,y=65)
entry1=Entry(root,width=15)
entry1.place(x=345,y=67)

lable2=Label(root,text=":نویسنده",font=("Arial",13,"bold"))
lable2.place(x=240,y=65)
entry2=Entry(root,width=13)
entry2.place(x=160,y=67)

lable3=Label(root,text=":سال",font=("Arial",13,"bold"))
lable3.place(x=460,y=105)
entry3=Entry(root,width=15)
entry3.place(x=360,y=107)

lable4=Label(root,text=":قیمت",font=("Arial",13,"bold"))
lable4.place(x=240,y=105)
entry4=Entry(root,width=15)
entry4.place(x=150,y=107)

lable5=Label(root,text=":وضعیت",font=("Arial",13,"bold"))
lable5.place(x=445,y=140)
entry5=Entry(root,width=15)
entry5.place(x=355,y=147)

user_id=Label(root,text=":آیدی کاربری",font=("Arial",13,"bold"))
user_id.place(x=220,y=147)
entry_user=Entry(root,width=15)
entry_user.place(x=130,y=149)

name_user=Label(root,text=":نام کاربر",font=("Arial",13,"bold"))
name_user.place(x=80,y=65)
name_entry=Entry(root,width=11)
name_entry.place(x=10,y=67)

button1=Button(root,text="افزودن کتاب",font=("Arial",10),bg="#FF91A4",command=add_click)
button1.place(x=28,y=200)

button2=Button(root,text="حذف کتاب",font=("Arial",10),bg="#FCF75E",command=remove_click1)
button2.place(x=75,y=250)

button3=Button(root,text="نمایش کتاب ها",font=("Arial",10),bg="#AA98A9",command=show_click)
button3.place(x=110,y=200)

button4=Button(root,text="جستجو کتاب",font=("Arial",10),bg="#DDA0DD",command=search_click)
button4.place(x=377,y=250)

button5=Button(root,text="گرفتن کتاب",font=("Arial",10),bg="#00FFBF",command=borrow_click)
button5.place(x=330,y=200)

button6=Button(root,text="بس دادن کتاب",font=("Arial",10),bg="#87CEFA",command=return_click)
button6.place(x=407,y=200)

button7=ctk.CTkButton(root,text="کاربر افزودن",corner_radius=20,command=add_user)
button7.place(x=185,y=230)



lable_res=Label(root,text="<---- نتیجه",font=("Arial",15,"bold"))
lable_res.place(x=350,y=340)
lst_box=Listbox(root,width=42,height=9)
lst_box.place(x=90,y=340)
root.mainloop()
