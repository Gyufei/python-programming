from Tkinter import *
from functools import partial as pa
from tkMessageBox import showinfo,showerror,showwarning

WARN='warn'
CRIT='crit'
REGU='regu'

sign={
    'do not enter':CRIT,
    'railroad crossing':REGU,
    '55\nspeed limit':REGU,
    'wrong way':CRIT,
    'merging traffic':WARN,
    'one way':REGU
}

critbu=lambda :showerror('Error','Error Button Pressed')
warnbu=lambda :showwarning('Warning','Warning Button Pressed')
regubu=lambda :showinfo('Info','Info Button Pressed')

top=Tk()
top.wm_title('Road Signs')
Button(top,text='quit',command=top.quit,bg='red',fg='white').pack()

mb=pa(Button,top)
Critbu=pa(mb,command=critbu,bg='white',fg='red')
Regubu=pa(mb,command=regubu,fg='white')
Warnbu=pa(mb,command=warnbu,fg='goldenrod1')

for i in sign:
    s=sign[i]
    cmd='%sbu(text=%r%s).pack(fill=X,expand=True)'%(
        s.title(),i,'.upper()' if s==CRIT else '.title()')
    eval(cmd)

top.mainloop()