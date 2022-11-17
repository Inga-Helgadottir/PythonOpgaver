from tkinter import Button
class Cell():
    def __init__(self, is_bomb=False):
       self.is_bomb = is_bomb
       self.cell_button_obj = None

    def create_btn_obj(self, location):
        self.location = location
        btn = Button(
            location,
            text='Text'
        )
        self.cell_button_obj = btn
