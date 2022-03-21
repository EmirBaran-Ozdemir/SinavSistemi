# -*- coding: utf-8 -*-
import sqlite3
import tkinter as tk
from tkinter import *




def uyeSayfasi():
    def kayıtOl():  
        print("ınnıujn")    
 
    
    pencere2 = tk.Tk()
    pencere2.title("Second Page")
    pencere2.geometry("500x450")
    pencere2.configure(bg="green")
    
    kullaniciAdi = tk.Label(pencere2 , text = "Kulanıcı adı giriniz: ",font = "Verdana 12 bold")
    kullaniciAdi.place(x=20,y=20)
    kullaniciAdiGiris = tk.Entry(pencere2,width=10)
    kullaniciAdiGiris.place(x=200,y=20)

    mail = tk.Label(pencere2,text = "Mailinizi giriniz :",font = "Verdana 12 bold")
    mail.place(x=20,y=60)
    mailGiris = tk.Entry(pencere2,width=10)
    mailGiris.place(x=200,y=60)
    
    passwordg = tk.Label(pencere2,text = "Şifreniz :",font = "Verdana 12 bold")
    passwordg.place(x=20,y=100)
    passworddg = tk.Entry(pencere2,width=10)
    passworddg.place(x=200,y=100)
    
    ad = tk.Label(pencere2,text = "Adınız :",font = "Verdana 12 bold")
    ad.place(x=20,y=140)
    adGiris = tk.Entry(pencere2,width=10)
    adGiris.place(x=200,y=140)
    
    soyad = tk.Label(pencere2,text = "Soyadınız :",font = "Verdana 12 bold")
    soyad.place(x=20,y=180)
    soyadGiris = tk.Entry(pencere2,width=10)
    soyadGiris.place(x=200,y=180)
    
    r = IntVar()
    rb1 = Radiobutton(pencere2,text = "Öğretmen",variable = r,value = 1)
    rb2 = Radiobutton(pencere2,text = "Öğrenci",variable = r,value = 2)
    rb3 = Radiobutton(pencere2,text = "Admin",variable = r,value = 3)
    rb1.place(x=20,y=220)
    rb2.place(x=110,y=220)
    rb3.place(x=190,y=220)
    
    btnUye = tk.Button(pencere2,text = "Kayıt Ol",font = "Verdana 12 bold",command = kayıtOl).place(x=100,y=250)
    
    pencere2.mainloop()      
    

 

pencere1 = tk.Tk()
pencere1.title("First Page")
pencere1.geometry("500x450")
pencere1.configure(bg="blue")

userName = tk.Label(text = "Kullanıcı Adınız :",font = "Verdana 12 bold")
userName.place(x=10,y=20)
userrName = tk.Entry(width=10)
userrName.place(x=165,y=20)

password = tk.Label(text = "Şifreniz :",font = "Verdana 12 bold")
password.place(x=10,y=65)
passwordd = tk.Entry(width=10)
passwordd.place(x=165,y=65)

girisYap = tk.Button(pencere1,text = "Giriş Yap",font= "Verdana 13 bold").place(x=10,y=95)

uyeOl = tk.Button(pencere1,text = "Üye Ol",font= "Verdana 13 bold",command = uyeSayfasi).place(x=130,y=95)


pencere1.mainloop() 



























