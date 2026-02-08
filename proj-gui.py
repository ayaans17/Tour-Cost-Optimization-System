from tkinter import *
import tkinter.font as tkFont
root=Tk()
root.title("PYTHON PROJECT")
root['bg'] = 'white'
root.geometry("400x400")
fontStyle = tkFont.Font( size=30)
fontStyle1 = tkFont.Font( size=20)
label0=Label(root,text="WELCOME TO SOV TOURS AND TRAVELS", width = 50, bg='blue',fg='black', font=fontStyle)
label0.place(x=100, y= 10)
label1=Label(root,text="enter Name : ", font = fontStyle1, bg='red' )
label1.place(y=70)
label2=Label(root,text="Starting City :", font = fontStyle1,bg='red')
label2.place(y=120)
label3=Label(root,text="Gender :", font = fontStyle1,bg='red')
label3.place(y=180)
var6 = IntVar()
c6=Radiobutton(root, text="MALE", variable=var6, font = fontStyle1 , value=1, bg='blue',fg='black')
c6.place(x=150, y = 180)
c7=Radiobutton(root, text="FEMALE", variable=var6, font = fontStyle1 , value=2, bg='blue',fg='black')
c7.place(x=280, y = 180)
c8=Radiobutton(root, text="OTHER", variable=var6, font = fontStyle1 , value=3, bg='blue',fg='black')
c8.place(x=445, y = 180)
entry1=Entry(root, width = 50, font = fontStyle1)
entry1.place(x=170, y = 70)
var1 = IntVar()
c1=Radiobutton(root, text="MUMBAI", variable=var1, font = fontStyle1, value=1, bg='blue',fg='black')
c1.place(x=180, y = 120)
c2=Radiobutton(root, text="DELHI", variable=var1, font = fontStyle1,value=2, bg='blue',fg='black')
c2.place(x=320, y = 120)
c3=Radiobutton(root, text="HYDERABAD", variable=var1, font = fontStyle1, value=3, bg='blue',fg='black')
c3.place(x=435, y = 120)
c4=Radiobutton(root, text="JAIPUR", variable=var1, font = fontStyle1, value=4, bg='blue',fg='black')
c4.place(x=635, y = 120)
c5=Radiobutton(root, text="AHMEDABAD", variable=var1, font = fontStyle1, value=5, bg='blue',fg='black')
c5.place(x=760, y = 120)

#function to find minimum key
def minkey(g, v, n):
    m = 100
    for j in range(0, 5):
        if (m > g[n][j] and g[n][j] > 0 and v[j] == 0):
            m = g[n][j]
            i = j
    g[i][n] = 0
    v[i] = 1
    return i

import array
#function to compute minimum distance
def mst(g,s):
     m=0
     v=array.array('i',[0,0,0,0,0])
     j=int(s)
     for i in range(0,4):
          if(i==s):
               continue
          k=j
          j=minkey(g,v,j)
          m=m+g[k][j]
          print("\n",m)
     print("\nminimum cost for the tour is : L",m)
     if(var1.get()==1):
        c="MUMBAI"
     elif(var1.get()==2):
        c="DELHI"
     elif(var1.get()==3):
        c="HYDERABAD"
     elif(var1.get()==4):
        c="JAIPUR"
     else:
        c="AHMEDABAD"
        mst(g,5)
     h= "Your Minimum Cost For The Tour Starting From " + c + " is :" + str(m)
     label6= Label(root,text=h, font = fontStyle1)
     label6.place(x=170,y=380)


#button for calling function from starting city
def buttontotal():
    if(var6.get()==1):
         hello="Hello Mr. " + entry1.get() + ","
    else:
         hello="Hello Miss. " + entry1.get() + ","
    label5=Label(root,text=hello, font = fontStyle1)
    label5.place(x=170, y=330)
    g=[[0,16,4,0,0],
	 [16,0,10,15,8],
	 [4,10,0,5,0],
	 [0,15,5,0,7],
         [0,8,0,7,0]]
    if(var1.get()==1):
        mst(g,1)
    elif(var1.get()==2):
        mst(g,2)
    elif(var1.get()==3):
        mst(g,3)
    elif(var1.get()==4):
        mst(g,4)
    else:
        mst(g,5)

#to close the GUI Window
def bt():
    root.destroy()


buttont = Button(root, text="Total", command=buttontotal, font=fontStyle1)
buttont.place(x=170, y=250)
buttonq = Button(root, text='Quit', command=bt, font=fontStyle1)
buttonq.place(x=270, y=250)
label4 = Label(root, text=var1.get(), font=fontStyle1)
# if(var1.get()==1):
#   entry3.insert(0,"yess")
root.mainloop()