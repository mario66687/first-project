from tkinter import *
import tkinter
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk , Image
import PIL
import cv2
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
window = Tk()
window.geometry("1500x1100+100+100")
window.resizable(True,True)
class MyInformation:
    la0 = Label(window) 
    la1 = Label(window)
    la2 = Label(window)
    la3 = Label(window) 
    la4 = Label(window)
    la5 = Label(window) 
    la6 = Label(window)
    la7 = Label(window)
    la8 = Label(window) 
    la00 = Label(window)
    la9 = Label(window) 
    la10 = Label(window)

    lab1 = Label(window)
    lab2 = Label(window)
    lab3 = Label(window)  
    lab4 = Label(window)
    lab5 = Label(window)  
    lab6 = Label(window)
    lab7 = Label(window)  
    lab8 = Label(window)
    lab9 = Label(window)
    lab10 = Label(window)
    lab11 = Label(window)  
    lab12 = Label(window)

    ent1=Entry(window)
    ent2=Entry(window)
    ent3=Entry(window)
    ent4=Entry(window)
    ent5=Entry(window)
    ent6=Entry(window)
    ent7=Entry(window)
    ent8=Entry(window)
    ent9=Entry(window)
    ent10=Entry(window)

    la0.config(text="개인정보")
    la1.config(text='이름 ')
    la2.config(text='나이 ')
    la3.config(text="학번 ")
    la4.config(text="학년 ")
    la5.config(text="전공 ")
    la6.config(text="email ")
    la00.config(text="학점 ")
    la7.config(text="1학년 ")
    la8.config(text="2학년 ")
    la9.config(text="3학년")
    la10.config(text="4학년 ")

    la0.place(x=50,y=0)

    la1.place(x=0,y=20)
    ent1.place(x=50,y=20)
    lab1.place(x=0,y=840)

    la2.place(x=0,y=40)
    ent2.place(x=50,y=40)
    lab2.place(x=0,y=860)

    la3.place(x=0,y=60)
    ent3.place(x=50,y=60)
    lab3.place(x=0,y=880)

    la4.place(x=0,y=80)
    ent4.place(x=50,y=80)
    lab4.place(x=0,y=900)

    la5.place(x=0,y=100)
    ent5.place(x=50,y=100)
    lab5.place(x=0,y=920)

    la6.place(x=0,y=120)
    ent6.place(x=50,y=120)
    lab6.place(x=0,y=940)

    la00.place(x=50,y=140)

    la7.place(x=0,y=160)
    ent7.place(x=50,y=160)
    lab7.place(x=0,y=960)

    la8.place(x=0,y=180)
    ent8.place(x=50,y=180)
    lab8.place(x=0,y=980)

    la9.place(x=0,y=200)
    ent9.place(x=50,y=200)
    lab9.place(x=0,y=1000)

    la10.place(x=0,y=220)
    ent10.place(x=50,y=220)
    lab10.place(x=0,y=1020)

def pprint() :
    mf=MyInformation()     
    mf.lab1.config(width=30,text='이름 '+ str(mf.ent1.get()))   
    mf.lab2.config(width=30,text='나이  '+ str(mf.ent2.get()))
    mf.lab3.config(width=30,text='학번  '+ str(mf.ent3.get()))
    mf.lab4.config(width=30,text='학년  '+ str(mf.ent4.get()))
    mf.lab5.config(width=30,text='전공  '+ str(mf.ent5.get()))
    mf.lab6.config(width=30,text='이메일  '+ str(mf.ent6.get()))   
    mf.lab7.config(width=30,text='1학년  '+ str(mf.ent7.get()))
    mf.lab8.config(width=30,text='2학년  '+ str(mf.ent8.get()))
    mf.lab9.config(width=30,text='3학년  '+ str(mf.ent9.get()))
    mf.lab10.config(width=30,text='4학년  '+ str(mf.ent10.get())) 
    

def save():
    mff=MyInformation()
    tx=open("C:/Users/user/Desktop/웹 프로그래밍/이건파이썬이여/2018_이민홍.txt",'w')
    data = '이름: ' + str(mff.ent1.get())
    tx.write(data)
    data0 = '\n나이: ' + str(mff.ent2.get())
    tx.write(data0)
    data1 = '\n학번: ' + str(mff.ent3.get())
    tx.write(data1)
    data2 = '\n학년: ' + str(mff.ent4.get())
    tx.write(data2)
    data3 = '\n전공: ' + str(mff.ent5.get())
    tx.write(data3)
    data4 = '\n이메일: ' + str(mff.ent6.get())
    tx.write(data4)
    data5 = '\n1학년 성적: ' + str(mff.ent7.get())
    tx.write(data5)
    data6 = '\n2학년 성적: ' + str(mff.ent8.get())
    tx.write(data6)
    data7 = '\n3학년 성적: ' + str(mff.ent9.get())
    tx.write(data7)
    data8 = '\n4학년 성적: ' + str(mff.ent10.get())
    tx.write(data8)
    tx.close()
def pprint2():
    op=open("C:/Users/user/Desktop/웹 프로그래밍/이건파이썬이여/2018_이민홍.txt",'r')
    ln=op.read()
    text=Text(window)
    text.insert("current",ln)
    text.place(x=400,y=840)
    op.close()
def Image_Processing():
    ph=PhotoImage(file="C:/Users/user/Desktop/웹 프로그래밍/이건파이썬이여/모코코미안해.png")
    phlb=Label(window,image=ph)
    phlb.image=ph
    phlb.place(x=350,y=0)
    ph2=PhotoImage(file="C:/Users/user/Desktop/웹 프로그래밍/이건파이썬이여/모코코안녕.png")
    phlb2=Label(window,image=ph2)
    phlb2.image=ph2
    phlb2.place(x=350,y=400)
def Rc_Circuit():
    R=100000
    C=0.000001
    dt=0.000001
    n_max=6000
    Ytemp=0
    Ydat=[]
    Xdat=[]
    Ndat=[]
    Ytemp=0
    Xdat.append(Ytemp)
    Ydat.append(Ytemp)
    num=dt/R/C
    for n in range (0,n_max):
        Xtemp=1 #Input 
        Ytemp1=Ytemp #Current Output
        Ytemp=(1-num)*Ytemp1+num*Xtemp #System Output Equation : Next Output
        Xdat.append(n*dt)
        Ydat.append(Ytemp)
        Ndat.append(n)
    plt.figure(1)

    plt.plot(Xdat,Ydat)
    plt.xlabel('Time(sec)')
    plt.ylabel('Vc')
    plt.title("Step Response")
    plt.grid(True)
    XXdat=np.array(0)
    YYdat=np.array(0)
    NNdat=np.array(0)
    num1=dt/R/C/2
    YYtemp=0
    for n in range (0,n_max):
        XXtemp=1 #Input 
        YYtemp1=YYtemp #Current Output
        YYtemp=(1-num1)*YYtemp1+num1*XXtemp #System Output Equation : Next Output
        XXdat=np.append(XXdat,n*dt)
        YYdat=np.append(YYdat,YYtemp)
        NNdat=np.append(NNdat,n)
    ppt=plt.figure(3)
    plt.plot(Xdat,Ydat,label="System1")
    plt.plot(XXdat,YYdat,label="System2")
    plt.xlabel('Time(sec)')
    plt.ylabel('Vc', fontsize=20)
    plt.axis([0,50000.1,0,50000])
    plt.legend(loc=0)
    plt.title("Step Response")
    plt.grid(True)
    llll=Label(window).place(x=700,y=150)
    cvs=FigureCanvasTkAgg(ppt,master=window)
    cvs.get_tk_widget().place(x=800,y=150)
    
btn=Button(window,text="입력 완료",command=pprint)
btn.place(x=0,y=800)
btn2=Button(window,text="저장",command=save)
btn2.place(x=100,y=800)
btn3=Button(window,text="출력",command=pprint2)
btn3.place(x=150,y=800)
btn4=Button(window,text="Image_Procesisng",command=Image_Processing)
btn4.place(x=200,y=800)
btn5=Button(window,text="RC_Cricuit",command=Rc_Circuit)
btn5.place(x=350,y=800)
window.mainloop()