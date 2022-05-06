from calendar import weekday

tipo_cliente = ''
lakewood = bridgewood = ridgewood = 0
lista_dia_semana = []

def get_cheapest_hotel():   #DO NOT change the function's name

    get_input()
    get_hotel_prices()

    if lakewood < bridgewood and lakewood < ridgewood:
        cheapest_hotel = 'Lakewood'
    elif bridgewood < lakewood and bridgewood < ridgewood:
        cheapest_hotel = 'Bridgewood'
    elif ridgewood < lakewood and ridgewood < bridgewood:
        cheapest_hotel = 'Ridgewood'
    elif lakewood == bridgewood == ridgewood:
        cheapest_hotel = 'Ridgewood'
    elif lakewood == bridgewood:
        cheapest_hotel = 'Bridgewood'
    elif lakewood == ridgewood:
        cheapest_hotel = 'Ridgewood'
    elif bridgewood == ridgewood:
        cheapest_hotel = 'Ridgewood'

    return cheapest_hotel

def get_input():
    global tipo_cliente

    while True:
        tipo_cliente = input('Tipo de cliente (reward ou regular): ').lower().strip()
        if tipo_cliente == 'regular' or tipo_cliente == 'reward':
            break

    for i in range(1, 4):
        while True:
            try: 
                dia = int(input(f'Dia {i}: '))
            except(ValueError, TypeError): 
                continue
            else:
                break
        
        while True:
            try: 
                mes = int(input(f'Mês {i}: '))
            except(ValueError, TypeError): 
                continue
            else:
                break
        
        while True:
            try: 
                ano = int(input(f'Ano {i}: '))
            except(ValueError, TypeError): 
                continue
            else:
                break
    
        dia_semana = weekday(ano, mes, dia)
        lista_dia_semana.append(dia_semana)

    return lista_dia_semana

def get_hotel_prices():
    global lakewood, bridgewood, ridgewood, tipo_cliente

    if tipo_cliente == 'regular':
        for i in range(0,3):
            if 4 >= lista_dia_semana[i] >= 0:
                lakewood += 110
                bridgewood += 160
                ridgewood += 220
            elif 6 >= lista_dia_semana[i] >= 5:
                lakewood += 90
                bridgewood += 60
                ridgewood += 150
    elif tipo_cliente == 'reward':
        for i in range(0,3):
            if 4 >= lista_dia_semana[i] >= 0:
                lakewood += 80
                bridgewood += 110
                ridgewood += 100
            elif 6 >= lista_dia_semana[i] >= 5:
                lakewood += 80
                bridgewood += 50
                ridgewood += 40
    
    return (lakewood, bridgewood, ridgewood)
    