import tkinter as tk
from currency import get_curreny_ratio # import library 

window = tk.Tk()
window.title('고성능 환율 계산기')
window.geometry('{}x{}+{}+{}'.format(300, 200, 100, 100))

label = tk.Label(window, text='대기중', height=2) # button object 
label.pack() # locate
def entry_event_fn(user_input):
    currency_symbol = { 'USD': '$', 'EUR': '€', 'JPY': '¥' }
    try:
        # get currency ratio using pre-implemented library
        usd_krw_ratio = get_curreny_ratio(currency) 
        print(usd_krw_ratio)
        result = float(entry.get()) * usd_krw_ratio
        label.config(text='{} {}'.format(currency_symbol[currency], result))
    except: # handling errors (e.g. string type input)
        label.config(text='연산 불가능')
entry = tk.Entry(window) # entry object 
entry.bind('<Return>', entry_event_fn) # register event function 
entry.pack() # locate 

def click():
    global currency
    currency = tk_currency.get()

tk_currency = tk.StringVar(value =None) 
currency = None
radio_btn1 = tk.Radiobutton(
    window, text='USD', value='USD', variable=tk_currency, tristatevalue=0, command=click)
radio_btn2 = tk.Radiobutton(
    window, text='EUR', value='EUR', variable=tk_currency, tristatevalue=0, command=click)
radio_btn3 = tk.Radiobutton(
    window, text='JPY', value='JPY', variable=tk_currency, tristatevalue=0, command=click)
radio_btn1.pack()
radio_btn2.pack()
radio_btn3.pack()

window.mainloop()

