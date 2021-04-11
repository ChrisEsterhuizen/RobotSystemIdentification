# -*- coding: utf-8 -*-
"""
Modified on Wednesday 16 Sept

@author: Chris Esterhuizen
"""

"""
==================
IMPORT LIBRARIES
==================
"""
import matplotlib
import serial
import numpy as np
from matplotlib import pyplot as plt
from mlxtend.evaluate import permutation_test
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import signal
import tkinter as tk

'''
=====================
Functions
=====================
'''



def read_serial_data():
    ser = serial.Serial('COM6', baudrate=115200, timeout=0.1)
    serial_counter = 0

    '''Serial Value .txt writer'''
    filepath_control = 'serial_data.txt'
    file_control = open(filepath_control, 'w', newline='\n')

    while serial_counter <= 20:
        data = ser.readline().decode('ascii')
        print(data)
        file_control.writelines(data)
        serial_counter = serial_counter + 1

    file_control.close()
    print('Serial reading is done')


def sendserial(s_write):
    try:
        ser = serial.Serial('COM6', baudrate=115200, timeout=0.1)
        #ser.write(bytes(str(s_write) + "\n", encoding='utf-8'))
        ser.write(str(s_write).encode())
        print(s_write)
    # print(str(word))
    # print("Byte sent succesfully")
    except:
        print("Serial write unsuccesful")

window = tk.Tk()
window.configure(background="dark orange")
window.title("Basic GUI")



# b2 = tk.Button(window, text="REVERSE", command=reverse, bg="firebrick2", fg="ghost white", font=("Comic Sans MS", 20))

b2 = tk.Entry(window)
b2.grid(row=2, column=1, padx=5, pady=10)

b1 = tk.Button(window, text="SEND", command=lambda:sendserial(b2.get()), bg="lime green", fg="gray7", font=("Comic Sans MS", 20))
b1.grid(row=1, column=1, padx=5, pady=10)

b3 = tk.Button(window, text="RECEIVE", command=read_serial_data(), bg="gold", fg="gray7", font=("Comic Sans MS", 20))
b3.grid(row=3, column=1, padx=5, pady=10)

def main():
    window.mainloop()
    # try:
    #     user_input = input('Duty Cycle % =>')
    #     # user_input = input('Duty Cycle % =>')
    #     read_serial_data()
    # except KeyboardInterrupt:
    #     user_input = input('Duty Cycle % =>')
    #     sendserial(user_input)
    #     user_input = input('Duty Cycle % =>')
    #     sendserial(user_input)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while 1:
        main()

