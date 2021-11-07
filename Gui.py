import tkinter as tk
from tkinter.constants import NUMERIC
import requests
from bs4 import BeautifulSoup

window = tk.Tk()
window.title('自動對發票')
window.geometry('1000x500')
lb_1 = tk.Label(window, text='歡迎使用對發票程式', font=('Arial', 24))
lb_1.grid(column=10,row=1)
Ey_ac = tk.Entry(window, font=('Arial', 12))
Ey_ac.grid(column=4,row=2)
but_1 = tk.Button(window, text='點我對發票', bg='white', fg='black', font=('Arial', 12) )
but_1.grid(column=1 , row=3 )
#Gui Setting

r = requests.get('https://invoices.com.tw/0708.html')
#Request html page
r.encoding = 'chcp 65001'
soup = BeautifulSoup(r.text,'html.parser')
Lucky_nums = soup.find_all("td",class_='number')
# 爬 class = number 的段落

Lucky_num1 = Lucky_nums[0].getText('number')
# 特別獎

Lucky_num2 = Lucky_nums[1].getText('number')
# 特獎

process = Lucky_nums[2].getText('number') + Lucky_nums[2].getText('number2')
Lucky_num3 = ""
for i in range(5):
    Lucky_num3 += process[i]
for i in range(11,14):
    Lucky_num3 += process[i]
# 頭獎1

Lucky_num4 = ""
for i in range(21,26):
    Lucky_num4 += process[i]
for i in range(32,35):
    Lucky_num4 += process[i]
# 頭獎2

Lucky_num5 = ""
for i in range(42,47):
    Lucky_num5 += process[i]
for i in range(53,56):
    Lucky_num5 += process[i]
# 頭獎3

Lucky_num6 = soup.find("td" , class_="number3").getText('number3')
# 增開

########################################
#               分隔島                 #
########################################




window.mainloop()