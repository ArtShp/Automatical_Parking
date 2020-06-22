base = {'counter': 0}

def car_input(state):
    if state == 'y':
        return True
    elif state == 'n':
        return False
def car_output(state):
    if state == 'y':
        return True
    elif state == 'n':
        return False

def wait_for_button(state):
    if state == 'y':
        return True
    elif state == 'n':
        return False
def scan_car_number(car_number):
    return car_number
def check_car_number(base, car_number):
    return car_number in base.values()
def add_to_base(base, car_number):
    base[base['counter']] = car_number
    base['counter'] += 1
def delete_from_base_number(base, car_number):
    for key in base.keys():
        if base[key] == car_number:
            del base[key]
            break
def delete_from_base_ticket(base, id):
    del base[id]
def give_ticket(base):
    print(f"Выдан талон №{base['counter']-1} на машину <{base[base['counter']-1]}>")
def take_ticket(base, id):
    return id in base.keys()
def scan_ticket(id):
    return id

def open_gate():
    print('Шлагбаум открыт.')
def car_passed(state):
    if state == 'y':
        return True
    elif state == 'n':
        return False
def close_gate():
    print('Шлагбаум закрыт.')

def check_input():
    car_is_there = car_input(input('\nЕсть ли машина на въезд(y/n): '))
    if car_is_there:
        button_is_pressed = False
        while not button_is_pressed:
            button_is_pressed = wait_for_button(input('Нажата ли кнопка(y/n): '))
        car_number = scan_car_number(input('Введите номер машины: '))
        add_to_base(base, car_number)
        print(base)
        give_ticket(base)
        open_gate()
        car_pass = False
        while not car_pass:
            car_pass = car_passed(input('Машина уже проехала(y/n): '))
        close_gate()
    else:
        pass
def check_output():
    car_is_there = car_input(input('\nЕсть ли машина на выезд(y/n): '))
    if car_is_there:
        car_number = scan_car_number(input('Введите номер машины: '))
        car_number_scanned = check_car_number(base, car_number)
        if car_number_scanned:
            delete_from_base_number(base, car_number)
            print(base)
        else:
            ticket_id = scan_ticket(int(input('Введите номер билета: ')))
            delete_from_base_ticket(base, ticket_id)
            print(base)
        open_gate()
        car_pass = False
        while not car_pass:
            car_pass = car_passed(input('Машина уже проехала(y/n): '))
        close_gate()
    else:
        pass
