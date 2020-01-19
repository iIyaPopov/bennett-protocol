from tkinter import *
from tkinter.ttk import Combobox


def show_info(title, message):
    root = Tk()
    root.title(title)
    Label(root, text=message, font=("TimesNewRoman", 10), padx=2, pady=2).grid(row=0, column=0)
    Button(root, text='ОК', width='10', command=lambda dialog=root: close_dialog(dialog)).grid(row=1, column=0)
    root.mainloop()
    root.destroy()


def show_entry(message):
    root = Tk()
    root.title('Введите данные')
    root.geometry('340x70')
    Label(root, text=message, font=("TimesNewRoman", 8), padx=2, pady=2).grid(row=0, column=0, columnspan=2)
    entry = Entry(root, width=40)
    entry.grid(row=1, column=0)
    Button(root, text='ОК', width='10', command=lambda dialog=root: close_dialog(dialog)).grid(row=1, column=1)

    root.mainloop()

    res = entry.get()
    root.destroy()
    return res


def show_choose_mode1(values):
    results = {'Автоматически': 'auto', 'Вручную': 'manually', 'Не использовать': 'nope'}
    variants = {'auto': 'Автоматически', 'manually': 'Вручную', 'nope': 'Не использовать'}

    window = Tk()
    window.title("Выберите режим")

    Label(window, text='Выберите режимы работы', font=("TimesNewRoman", 8), padx=2, pady=2).grid(row=0, column=0, columnspan=2)

    combo = Combobox(window)
    if len(values) == 2:
        combo['values'] = (variants[values[0]], variants[values[1]])
    if len(values) == 3:
        combo['values'] = (variants[values[0]], variants[values[1]], variants[values[2]])
    combo.current(0)
    combo.grid(column=0, row=1)

    Button(window, text='ОК', width='10', command=lambda dialog=window: close_dialog(dialog)).grid(row=1, column=1)

    window.mainloop()

    res = combo.get()
    window.destroy()
    return results[res]


def show_choose_mode(values):
    results = {'Автоматически': 'auto', 'Вручную': 'manually', 'Не использовать': 'nope'}
    variants = {'auto': 'Автоматически', 'manually': 'Вручную', 'nope': 'Не использовать'}

    window = Tk()
    window.title("Выберите режим")

    Label(window, text='Режим Алисы:', font=("TimesNewRoman", 8), padx=2, pady=2).grid(row=0, column=0)
    Label(window, text='Режим Евы:', font=("TimesNewRoman", 8), padx=2, pady=2).grid(row=1, column=0)
    Label(window, text='Режим Боба:', font=("TimesNewRoman", 8), padx=2, pady=2).grid(row=2, column=0)

    combo_alice = Combobox(window)
    combo_alice['values'] = (variants[values[1]], variants[values[2]])
    combo_alice.current(0)
    combo_alice.grid(row=0, column=1)

    combo_eve = Combobox(window)
    combo_eve['values'] = (variants[values[0]], variants[values[1]], variants[values[2]])
    combo_eve.current(0)
    combo_eve.grid(row=1, column=1)

    combo_bob = Combobox(window)
    combo_bob['values'] = (variants[values[1]], variants[values[2]])
    combo_bob.current(0)
    combo_bob.grid(row=2, column=1)

    Button(window, text='ОК', width='10', command=lambda dialog=window: close_dialog(dialog)).grid(row=3, column=0, columnspan=2)

    window.mainloop()

    res = [combo_alice.get(), combo_eve.get(), combo_bob.get()]
    window.destroy()
    return [results[res[0]], results[res[1]], results[res[2]]]


def show_choose_photone():
    window = Tk()
    window.title("Выберите фотон")
    selected = IntVar()
    Radiobutton(window, text=chr(8594), font='Courier 20', value=0, variable=selected).grid(column=0, row=0)
    Radiobutton(window, text=chr(8599), font='Courier 20', value=1, variable=selected).grid(column=1, row=0)
    Radiobutton(window, text=chr(8593), font='Courier 20', value=2, variable=selected).grid(column=2, row=0)
    Radiobutton(window, text=chr(8598), font='Courier 20', value=3, variable=selected).grid(column=3, row=0)
    Button(window, text="ОК", command=lambda dialog=window: close_dialog(dialog)).grid(column=4, row=0)
    Label(window).grid(column=0, row=1)
    window.mainloop()
    res = selected.get()
    window.destroy()
    return res


def show_choose_data():
    window = Tk()
    window.title("Выберите данные")
    selected_basis = IntVar()
    Label(window, text='Выберите базис и фотон Алисы', font='Courier 10').grid(column=0, columnspan=2, row=0, sticky='n')
    Radiobutton(window, text='+', font='Courier 20', value=0, variable=selected_basis).grid(column=0, row=1, sticky='w')
    Radiobutton(window, text=chr(10005), font='Courier 15', value=1, variable=selected_basis).grid(column=0, row=2, sticky='w')

    selected = IntVar()
    Radiobutton(window, text=chr(8594), font='Courier 20', value=0, variable=selected).grid(column=1, row=1, sticky='w')
    Radiobutton(window, text=chr(8599), font='Courier 20', value=1, variable=selected).grid(column=1, row=2, sticky='w')
    Radiobutton(window, text=chr(8593), font='Courier 20', value=2, variable=selected).grid(column=1, row=3, sticky='w')
    Radiobutton(window, text=chr(8598), font='Courier 20', value=3, variable=selected).grid(column=1, row=4, sticky='w')

    Button(window, text="ОК", width=20, command=lambda dialog=window: close_dialog(dialog)).grid(column=0, columnspan=2, row=5)

    window.mainloop()

    photone = selected.get()
    basis = selected_basis.get()

    window.destroy()

    return [basis, photone]


def show_choose_basis(name):
    window = Tk()
    window.title("Выберите данные")
    selected_basis = IntVar()
    Label(window, text='Выберите базис ' + name, font='Courier 10').grid(column=0, row=0)
    Radiobutton(window, text='+', font='Courier 20', value=0, variable=selected_basis).grid(column=0, row=1)
    Radiobutton(window, text=chr(10005), font='Courier 15', value=1, variable=selected_basis).grid(column=0, row=2)
    Button(window, text="ОК", width=20, command=lambda dialog=window: close_dialog(dialog)).grid(column=0, row=3)

    window.mainloop()

    basis = selected_basis.get()

    window.destroy()

    return basis


def main_dialog(alice, eve, eim, bob, keys):
    window = Tk()
    window.title("BB84")

    basis = {0: '+', 1: chr(10005)}
    basis_font = {0: 'Courier 15', 1: 'Courier 10'}

    photone = {0: chr(8594), 45: chr(8599), 90: chr(8593), 135: chr(8598)}

    Label(window, text='Базис Алисы:', font='Courier 10').grid(row=0, column=0, sticky='w')
    Label(window, text='Биты Алисы:', font='Courier 10').grid(row=1, column=0, sticky='w')
    Label(window, text='Фотоны Алисы:', font='Courier 10').grid(row=2, column=0, sticky='w')

    Label(window, text='').grid(row=3, column=0)
    Label(window, text='Базис Евы:', font='Courier 10').grid(row=4, column=0, sticky='w')
    Label(window, text='Биты Евы:', font='Courier 10').grid(row=5, column=0, sticky='w')
    Label(window, text='Фотоны Евы:', font='Courier 10').grid(row=6, column=0, sticky='w')

    Label(window, text='').grid(row=7, column=0)
    Label(window, text='Базис Боба:', font='Courier 10').grid(row=8, column=0, sticky='w')
    Label(window, text='Биты Боба:', font='Courier 10').grid(row=9, column=0, sticky='w')
    Label(window, text='Фотоны Боба:', font='Courier 10').grid(row=10, column=0, sticky='w')

    Label(window, text='').grid(row=11, column=0)
    Label(window, text='Совпадения ключа:', font='Courier 10').grid(row=12, column=0, sticky='w')
    Label(window, text='Ключ Алисы:', font='Courier 10').grid(row=13, column=0, sticky='w')
    Label(window, text='Ключ Боба:', font='Courier 10').grid(row=14, column=0, sticky='w')

    Label(window, text='').grid(row=15, column=0)
    if keys is not None:
        Button(window, text='Зашифровать сообщение', command=lambda akey=keys['alice'], bkey=keys['bob']: encrypt(akey, bkey)).grid(row=16, column=0)

    len_data = len(alice['basis'])
    for i in range(len_data):
        Label(window, text=basis[alice['basis'][i]], font=basis_font[alice['basis'][i]]).grid(row=0, column=i+1)
        Label(window, text=photone[alice['photone'][i]], font='Courier 15').grid(row=2, column=i+1)
        Label(window, text=alice['bits'][i], font='Courier 15').grid(row=1, column=i+1)

        if eim != 'nope':
            Label(window, text=basis[eve['basis'][i]], font=basis_font[eve['basis'][i]]).grid(row=4, column=i+1)
            Label(window, text=photone[eve['photone'][i]], font='Courier 15').grid(row=6, column=i+1)
            Label(window, text=eve['bits'][i], font='Courier 15').grid(row=5, column=i+1)

        Label(window, text=basis[bob['basis'][i]], font=basis_font[bob['basis'][i]]).grid(row=8, column=i + 1)
        Label(window, text=photone[bob['photone'][i]], font='Courier 15').grid(row=10, column=i + 1)
        Label(window, text=bob['bits'][i], font='Courier 15').grid(row=9, column=i + 1)

        if keys is not None:
            Label(window, text=keys['is_equals'][i], font='Courier 15').grid(row=12, column=i+1, sticky='w')

    if keys is not None:
        Label(window, text=keys['alice'], font='Courier 15').grid(row=13, column=1, columnspan=len_data, sticky='w')
        Label(window, text=keys['bob'], font='Courier 15').grid(row=14, column=1, columnspan=len_data, sticky='w')

    window.mainloop()


def show_encrypt_dialog(data):
    window = Tk()
    window.title("Шифрование сообщения")

    Label(window, text='Сообщение Алисы:', font='Courier 10').grid(row=0, column=0, sticky='w')
    Label(window, text='Боб получил:', font='Courier 10').grid(row=1, column=0, sticky='w')
    Label(window, text='Боб расшифровал:', font='Courier 10').grid(row=2, column=0, sticky='w')

    Label(window, text=data['alice_msg'], font='Courier 10').grid(row=0, column=1, sticky='w')
    Label(window, text=data['bob_get'], font='Courier 10').grid(row=1, column=1, sticky='w')
    Label(window, text=data['bob_dec'], font='Courier 10').grid(row=2, column=1, sticky='w')

    window.mainloop()


def close_dialog(dialog):
    dialog.quit()


def encrypt(akey, bkey):
    if len(akey) > 7:
        alice_byte = 0
        for i in range(8):
            alice_byte |= (1 << i) * akey[i]
        #    alice_byte = alice_byte.to_bytes(1, byteorder='little')
        #    print(alice_byte)

        bob_byte = 0
        for i in range(8):
            bob_byte |= (1 << i) * bkey[i]
        #    bob_byte = bob_byte.to_bytes(1, byteorder='little')
        #    print(bob_byte)

        # Алиса вводит предложение
        print('Введите предложение, которое Алиса хочет передать: ')
        # aw = input()  # alice word
        aw = show_entry('Введите предложение, которое Алиса хочет передать: ')
        awb = aw.encode('utf-8')  # alice word bytes

        cwb = b''
        for byte in awb:
            cwb += bytes([byte ^ alice_byte])

        bwb = b''
        for byte in cwb:
            bwb += bytes([byte ^ bob_byte])

        print('Alice: ', awb)
        print('Channel: ', cwb)
        print('Bob: ', bwb)
        data = {'alice_msg': awb, 'bob_get': cwb, 'bob_dec': bwb}
        show_encrypt_dialog(data)
    else:
        show_info('Ошибка', 'Количество бит ключа недостаточно!')
        print('Количество бит ключа недостаточно!')

