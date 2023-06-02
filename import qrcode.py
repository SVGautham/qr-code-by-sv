import qrcode
from tkinter import *
from tkinter import messagebox
#CODE FOR GENERATE FUNCTION BUTTON
def generateCode():
  
  qr = qrcode.QRCode(version = size.get(),
            box_size = 10,
            border = 5)
  qr.add_data(text.get()) 
  qr.make(fit = True) 
  img = qr.make_image() 
  fileDirec=loc.get()+'\\'+name.get() 
  img.save(f'{fileDirec}.png') 
  messagebox.showinfo("MESSAGE","QR CODE MADE AND SAVED IN LOCATION")
  
  
wn = Tk()
wn.title('QR Code Generator(USE IN FULLSCREEN)')
wn.geometry('800x800')
wn.config(bg='pink')
#Label for the window
headingFrame = Frame(wn,bg="pink",bd=11)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="QR CODE GENERATOR ", bg='pink', font=('Times',24,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
#CODE FOR TAKING INPUT
Frame1 = Frame(wn,bg="pink")
Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)
label1 = Label(Frame1,text="ENTER TEXT/URL TO MAKE QR CODE :- ",bg="yellow",fg='black',font=('Helvetica',13,'bold'))
label1.place(relx=0.05,rely=0.2, relheight=0.08)
text = Entry(Frame1,font=('Helvetica'))
text.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)
#CODE TO SAVE LOCATION
Frame2 = Frame(wn,bg="pink")
Frame2.place(relx=0.1,rely=0.35,relwidth=0.7,relheight=0.3)
label2 = Label(Frame2,text="ENTER LOCATION TO SAVE THE QR CODE IN FORM D:\ \C++ :- ",bg="yellow",fg='black',font=('Helvetica',13,'bold'))
label2.place(relx=0.05,rely=0.2, relheight=0.08)
loc = Entry(Frame2,font=('Times'))
loc.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)
#CODE FOR QR NAME
Frame3 = Frame(wn,bg="pink")
Frame3.place(relx=0.1,rely=0.55,relwidth=0.7,relheight=0.3)
label3 = Label(Frame3,text="ENTER THE NAME FOR THE IMAGE :- ",bg="yellow",fg='black',font=('Helvetica',13,'bold'))
label3.place(relx=0.05,rely=0.2, relheight=0.08)
name = Entry(Frame3,font=('Times'))
name.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)
#CODE FOR SIZE OF QR CODE IMAGE
Frame4 = Frame(wn,bg="pink")
Frame4.place(relx=0.1,rely=0.75,relwidth=0.7,relheight=0.3)
label4 = Label(Frame4,text="ENTER THE SIZE 1 to 40(in number) :- ",bg="yellow",fg='black',font=('Helvetica',13,'bold'))
label4.place(relx=0.05,rely=0.2, relheight=0.08)
size = Entry(Frame4,font=('Times'))
size.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.1)
#CODE FOR BUTTON
button = Button(wn, text='Generate Code',fg="yellow",bg="black",font=('Helvetica',18,'bold'),command=generateCode)
button.place(relx=0.35,rely=0.94, relwidth=0.25, relheight=0.05,)

wn.mainloop()
