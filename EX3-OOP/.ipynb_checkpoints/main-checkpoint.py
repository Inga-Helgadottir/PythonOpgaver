import settings
from tkinter import *
root = Tk()
root.configure(bg='black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper game')
root.resizable(False,False)

top_frame = Frame(
    root,
    bg='red',
    width=utils.get_width(100),
    height=utils.get_height(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root, 
    bg='orange',
    width=utils.get_width(25),
    height=utils.get_height(75)
)
left_frame.place(x=0,y=utils.get_height(25))
center_frame = Frame(
    root, 
    bg='grey',
    width=utils.get_width(75),
    height=utils.get_height(75)
)
center_frame.place(x=utils.get_width(25),y=utils.get_height(25))

btn1 = Button(
    center_frame,
    bg='purple',
    text='My Button'    
)
btn1.place(x=10, y=10)

c1 = Cell()
c1.create_btn_obj(center_frame)
#c1.cell_button_obj.place(x=0, y=0)
c1.cell_button_obj.grid(
    column=0, 
    row=0
)
c2 = Cell()
c2.create_btn_obj(center_frame)
# c1.cell_button_obj.place(x=0, y=0)
c2.cell_button_obj.grid(
    column=1, 
    row=0
)

for x in range(settings.GRIDWIDTH):
    for y in range(settings.GRIDHEIGHT):
        c = Cell()
        c.create_btn_obj(center_frame)
        # c1.cell_button_obj.place(x=0, y=0)
        c.cell_button_obj.grid(
            column=x, 
            row=y
        )
        btn.bind('<Button-1>',self.handle_left_click) # button 1 means left-click
        btn.bind('<Button-3>',self.handle_right_click) # button 3 means right-click
    
    def handle_right_click(self, event): # event is not needed, but tkinter needs it
        print(event)
        print(f'Right clicked: ({self.x},{self.y})')
        
root.mainloop() 
