from re import*
from tkinter import*
from time import*
class Str(str):
    type='Str'
    def get(self,text):
        a=str(sub('<{}>'.format(text),'#',sub('</{}>'.format(text),'#',self))).split('#')
        try:
            return a[1]
        except IndexError:
            return a[0]
        except:
            return None
def log_in():
    global use
    use=Tk()
    use.geometry('500x300')
    b=Label(use,text='用户名')
    b.pack()
    name=Entry(use,show=None)
    name.pack()
    c=Label(use,text='密码')
    c.pack()
    password=Entry(use,show='*')
    password.pack()
    def a():
        if name.get()!='' and password.get()!='':
            use.quit()  
    to_log_in=Button(use,bg='green',text='登入',command=a)
    to_log_in.pack()
    use.mainloop()
    return [name.get(),password.get()]
def ver_output(text:str,time=0.1,sign=[None],special={}):
    for i,t in enumerate(text):
        if i in special.keys():
            _sign=special[i]
        elif str(i) in special.keys():
            _sign=special[str(i)]
        else:
            _sign=sign[i%len(sign)]
        if _sign=='r':
            print('\033[31m'+t,end='')
        elif _sign=='g':
            print('\033[32m'+t,end='')
        elif _sign=='b':
            print('\033[34m'+t,end='')
        elif _sign=='y':
            print('\033[33m'+t,end='')
        elif _sign==None:
            print('\033[0m'+t,end='')
        elif _sign=='w':
            print('\033[0m'+t,end='')
        elif _sign.isdecimal()==True:
            print('\033[{}m'.format(_sign)+t,end='')
        sleep(time)
    print('')
