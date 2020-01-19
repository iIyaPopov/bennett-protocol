# -*- coding: utf-8 -*-


import random as r
import dialog


def int_from_input(message, min_value, max_value):
    while(True):
        value_word = dialog.show_entry(message + "\n(значение от " + str(min_value) + " до " + str(max_value) + ")")
        try:
            value = int(value_word)
            if min_value <= value <= max_value:
                return value
            else:
                dialog.show_info("Ошибка", "Число не входит в указанный интервал")
        except ValueError:
            dialog.show_info("Ошибка", "Должно быть введено число")


def chose_variant_from_input(message, variants):
    variant = dialog.show_choose_mode(message, variants)
    try:
        variants.index(variant)
    except ValueError:
        dialog.show_info("Ошибка", "Неверное значение")
        variant = variants[0]
    return variant


def bit_from_photone(photone, basis):
    value = int(photone / 45) - 2 * basis
    if value < 0:
        value = 0
    if value > 1:
        value = 1
    return value


# Точность приемника Боба
accuracy = float(dialog.show_entry('Точноть приема (0...1)'))

# Алиса выбирает количество фотонов
apcm = 'Введите количество фотонов, которые Алиса хочет передать: '
apc = int_from_input(apcm, 0, 100)  # alice photones count

mode = dialog.show_choose_mode(['nope', 'auto', 'manually'])
# Алиса выбирает режим посылки
asmv = ['auto', 'manually']
asmm = 'Алиса будет посылать фотоны автоматически или вручную?'
# asm = chose_variant_from_input(asmm, asmv)  # alice sending mode
asm = mode[0]

# Ева выбирает режим перехвата
eimv = ['nope', 'auto', 'manually']
eimm = 'Ева будет перехватывать фотоны автоматически, вручную или не перехватывать?'
# eim = chose_variant_from_input(eimm, eimv)  # eve intercaption mode
eim = mode[1]

# Боб выбирает режим перехвата
bimv = ['auto', 'manually']
bimm = 'Боб будет перехватывать фотоны автоматически или вручную?'
# bim = chose_variant_from_input(bimm, bimv)  # bob intercaption mode
bim = mode[2]

print()
print('Alice: ')
print('Количество фотонов: ', apc)
print('Режим: ', asm)
print()
print('Eve: ')
print('Режим: ', eim)
print()
print('Bob: ')
print('Режим: ', bim)
print()

ab = []  # alice basis
ap = []  # alice photon
abits = []  # alice bits

eb = []  # eve basis
ep = []  # eve photon
ebits = []  # eve bits

bb = []  # bob basis
bp = []  # bob photon
bbits = []  # bob bits

aec = []  # alice eve channel
ebc = []  # eve bob channel

for i in range(apc):
    alice_basis = 0
    alice_bit = 0
    alice_photone = 0
    if asm == 'auto':
        alice_photone = r.randint(0, 3) * 45
        alice_basis = (r.randint(0, 1))
    if asm == 'manually':
        data = dialog.show_choose_data()
        # alice_photone_message = 'Какой фотон Алиса хочет передать?'
        # alice_photone = int_from_input(alice_photone_message, 0, 3) * 45
        alice_photone = data[1] * 45
        # alice_basis_message = 'Какой базис Алиса хочет использовать? Введите 0 если +, 1 если x: '
        # alice_basis = int_from_input(alice_basis_message, 0, 1)
        alice_basis = data[0]
    alice_bit = bit_from_photone(alice_photone, alice_basis)
    ab.append(alice_basis)
    abits.append(alice_bit)
    ap.append(alice_photone)

    alice_eve_photone = alice_photone
    aec.append(alice_eve_photone)

    eve_basis = 0
    eve_bit = 0
    eve_photone = 0
    eve_bob_photone = alice_eve_photone

    if eim == 'auto':
        eve_basis = (r.randint(0, 1))
    if eim == 'manually':
        # eve_basis_message = 'Какой базис Ева хочет использовать? Введите 0 если +, 1 если x: '
        # eve_basis = int_from_input(eve_basis_message, 0, 1)
        eve_basis = dialog.show_choose_basis('Евы')
    if eim != 'nope':
        eve_bit = bit_from_photone(alice_eve_photone, eve_basis)
        eve_photone = (eve_bit * 45) + (eve_basis * 90)
        eve_bob_photone = eve_photone

    eb.append(eve_basis)
    ebits.append(eve_bit)
    ep.append(eve_photone)
    ebc.append(eve_bob_photone)

    bob_basis = 0
    bob_bit = 0
    bob_photone = 0
    if bim == 'auto':
        bob_basis = (r.randint(0, 1))
    if bim == 'manually':
        # bob_basis_message = 'Какой базис Боб хочет использовать? Введите 0 если +, 1 если x: '
        # bob_basis = int_from_input(bob_basis_message, 0, 1)
        bob_basis = dialog.show_choose_basis('Боба')
    bob_bit = bit_from_photone(eve_bob_photone, bob_basis)
    bob_photone = (bob_bit * 45) + (bob_basis * 90)
    bb.append(bob_basis)
    bbits.append(bob_bit)
    bp.append(bob_photone)

alice_data = {'basis': ab, 'photone': ap, 'bits': abits}
eve_data = {'basis': eb, 'photone': ep, 'bits': ebits}
bob_data = {'basis': bb, 'photone': bp, 'bits': bbits}

print()
print('Alice: ')
print('Биты: ', abits)
print('Базисы: ', ab)
print('Фотоны: ', ap)
print()
print('Канал Алиса Ева: ', aec)
print()
print('Eve: ')
print('Биты: ', ebits)
print('Базисы: ', eb)
print('Фотоны: ', ep)
print()
print('Канал Ева Боб: ', ebc)
print()
print('Bob: ')
print('Биты: ', bbits)
print('Базисы: ', bb)
print('Фотоны: ', bp)
print()

akey = []
bkey = []
is_equals = []

for i in range(apc):
    if ab[i] == bb[i] and r.random() < accuracy:
        akey.append(abits[i])
        bkey.append(bbits[i])
        is_equals.append('+')
    else:
        is_equals.append('-')

keys = {'is_equals': is_equals, 'alice': akey, 'bob': bkey}
dialog.main_dialog(alice_data, eve_data, eim, bob_data, keys)
