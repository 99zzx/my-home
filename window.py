import tkinter as tk
window=tk.Tk()
window.title('my home')
window.geometry('400x200')


var=tk.StringVar()
myLable=tk.Label(window,textvariable=var,font=('Arial',50),width=50,
           height=50)
myLable.pack()

on_hit=False

def hit_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        #var.set('you hit me')
        show_str('you hit me!')
    else:
        on_hit=False
        var.set('')

def show_str(mystr):
    var.set(mystr)

def my_window():
    window.mainloop()

#myButton=tk.Button(window,text='hit me',width=15,height=2,command=hit_me)
#myButton.pack()
    
if __name__ == '__main__':
    my_window()
