from tkinter import *
from datetime import datetime
import logging

logging.basicConfig(filename='LogCalc.log', level=logging.INFO, encoding='UTF-8')
logger = logging.getLogger()

def btn_click(item):
    global expression
    try:
        input_field['state'] = "normal"
        expression += item
        input_field.insert(END, item)
        n = expression
        if item == '=':
            result = str(eval(expression[:-1]))
            input_field.insert(END, result)
            expression = ""
            logger.info('Действие завершено')
            logger.info(f'{datetime.now().strftime("%H:%M:%S")} {n}{result}')
        input_field['state'] = "readonly"

    except ZeroDivisionError:
        input_field.delete(0, END)
        input_field.insert(0, 'Ошибка (деление на 0)')
        logger.info(f'{datetime.now().strftime("%H:%M:%S")} {n} На 0 делить нельзя')

        
    except SyntaxError:
        input_field.delete(0, END)
        input_field.insert(0, 'Ошибка')


def bt_clear():
    global expression
    expression = ""
    input_field['state'] = "normal"
    input_field.delete(0, END)
    input_field['state'] = "readonly"


root = Tk()
root.geometry("268x400")
root.title("Калькулятор")
root.resizable(0, 0)

frame_input = Frame(root)
frame_input.grid(row=0, column=0, columnspan=5, sticky="nsew")

input_field = Entry(frame_input, font='Arial 15 bold', width=24, state="readonly")
input_field.pack(fill=BOTH)

buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4'),
           ('cl','', '', '', '4'))

expression = ""

button = Button(root, text='C', command=lambda: bt_clear())
button.grid(row=1, column=3, sticky="nsew")

for row in range(4):
    for col in range(4):
        Button(root, width=2, height=3, text=buttons[row][col],
               command=lambda row=row, col=col: btn_click(buttons[row][col])).grid(row=row + 2, column=col, sticky="nsew", padx=1, pady=1)

root.mainloop()