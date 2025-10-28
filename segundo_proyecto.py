# Segundo proyecto de freeCodeCamp
def add_time(start, duration, day = ""):
    operando = None
    hrs_hora_inicial = None
    minutos_hora_inicial = None
    digitos_hora_inicial = ""
    momento_inicial = ""                   # AM o PM
    digitos_hora_final = ""
    minutos_adicionales = None
    horas_adicionales = None
    cambio_horario = ""
    d1 = None
    dias_de_la_semana = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    final = ""

    for inicio in start:
        if inicio.isdigit():
            digitos_hora_inicial += inicio
            if len(digitos_hora_inicial) == 3:
                hrs_hora_inicial = int(digitos_hora_inicial[:1])
                minutos_hora_inicial = int(digitos_hora_inicial[1:])
            elif len(digitos_hora_inicial) == 4:
                hrs_hora_inicial = int(digitos_hora_inicial[:2])
                minutos_hora_inicial = int(digitos_hora_inicial[2:])


    if "".join(list(filter(lambda x: 'AM' in x, start.split()))) == "AM":
        momento_inicial = "".join(list(filter(lambda x: 'AM' in x, start.split())))
    elif "".join(list(filter(lambda y: 'PM' in y, start.split()))) == "PM":
        momento_inicial = "".join(list(filter(lambda y: 'PM' in y, start.split())))


    for operando in duration:
        if operando.isdigit():
            digitos_hora_final += operando
        else:
            pass


    minutos_adicionales = int(digitos_hora_final[-2:])
    horas_adicionales = int(digitos_hora_final[:-2])
    
    suma_minutos = minutos_hora_inicial + minutos_adicionales
    suma_horas = hrs_hora_inicial + horas_adicionales

    #Hasta este punto ya tenemos los digitos que se ingresan a la función ordenados por momento, hora y minutos al inicio y los que se suman

    q1 = None   # Parte entera de la divión entre la suma de minutos sobre 60
    q2 = None   # Parte entera de la divión entre la suma de horas sobre 12
    r1 = None   # Residuo de la divión entre la suma de minutos sobre 60
    r2 = None   # Residuo de la divión entre la suma de horas sobre 12

    if suma_minutos > 60:
        q1 = suma_minutos // 60
        suma_horas += q1
        r1 = suma_minutos % 60
    else: 
        q1 = 0
        r1 = suma_minutos
    
    if suma_horas > 11:
        q2 = suma_horas // 12
        r2 = suma_horas % 12
        if r2 == 0:
            r2 = 12 ###
        else:
            pass
    else:
        q2 = 0
        r2 = suma_horas

    def cambiar_momento(cadena1, cadena2, n):
        for i in range(n):
            if i % 2 == 0:
                cambio_horario = cadena2
            else:
                cambio_horario = cadena1
        return cambio_horario
    

# Nota: d1 indica los días transcurridos dependiendo del momento inicial (AM o PM)

    if day == "":
        if q2 > 0:
            if momento_inicial == "AM":
                d1 = q2 // 2
                if r1 < 10:
                    if d1 == 1:
                        final = f'{r2}:0{r1} {cambiar_momento("AM", "PM", q2)} (next day)'
                    elif d1 == 0:
                        final = f'{r2}:0{r1} {cambiar_momento("AM", "PM", q2)}'
                    else:
                        final = f'{r2}:0{r1} {cambiar_momento("AM", "PM", q2)} ({d1} days later)'
                else:
                    if d1 == 1:
                        final = f'{r2}:{r1} {cambiar_momento("AM", "PM", q2)} (next day)'
                    elif d1 == 0:
                        final = f'{r2}:{r1} {cambiar_momento("AM", "PM", q2)}'
                    else:
                        final = f'{r2}:{r1} {cambiar_momento("AM", "PM", q2)} ({d1} days later)'
            elif momento_inicial == "PM":
                if q2 % 2 == 1:
                    d1 = (q2 // 2) + 1
                    if r1 < 10:
                        if d1 == 1:
                            final = f'{r2}:0{r1} {cambiar_momento("PM", "AM", q2)} (next day)'
                        elif d1 == 0:
                            final = f'{r2}:0{r1} {cambiar_momento("PM", "AM", q2)}'
                        else:
                            final = f'{r2}:0{r1} {cambiar_momento("PM", "AM", q2)} ({d1} days later)'
                    else: 
                        if d1 == 1:
                            final = f'{r2}:{r1} {cambiar_momento("PM", "AM", q2)} (next day)'
                        elif d1 == 0:
                           final = f'{r2}:{r1} {cambiar_momento("PM", "AM", q2)}'
                        else:
                            final = f'{r2}:{r1} {cambiar_momento("PM", "AM", q2)} ({d1} days later)'
                else:
                    d1 = (q2 // 2)
                    if r1 < 10:
                        if d1 == 1:
                            final = f'{r2}:0{r1} {cambiar_momento("PM", "AM", q2)} (next day)'
                        elif d1 == 0:
                            final = f'{r2}:0{r1} {cambiar_momento("PM", "AM", q2)} (next day)'
                        else:
                            final = f'{r2}:0{r1} {cambiar_momento("PM", "AM", q2)} ({d1} days later)'
                    else: 
                        if d1 == 1:
                            final = f'{r2}:{r1} {cambiar_momento("PM", "AM", q2)} (next day)'
                        elif d1 == 0:
                            final = f'{r2}:{r1} {cambiar_momento("PM", "AM", q2)}'
                        else:
                            final = f'{r2}:{r1} {cambiar_momento("PM", "AM", q2)} ({d1} days later)'               
        else:
            if r1 < 10:
                final = f'{r2}:0{r1} {momento_inicial}'
            else:
                final = f'{r2}:{r1} {momento_inicial}'

    else:
        # Mostrar el día
        day = day.lower().capitalize() #Para convertir todas las letras de la cadena a minúsculas excepto la primera, que debe estar en mayúscula
        posicion = dias_de_la_semana.index(day)        
        if q2 > 0:
            if momento_inicial == "AM":
                d1 = q2 // 2
                if r1 < 10:
                    if d1 == 1:
                        final = f'{r2}:0{r1} {cambiar_momento("AM", "PM", q2)}, {dias_de_la_semana[posicion + d1 % 7]} (next day)'
                    elif d1 == 0:
                        final = f'{r2}:0{r1} {cambiar_momento("AM", "PM", q2)}, {dias_de_la_semana[posicion + d1 % 7]}'
                    else:
                        final = f'{r2}:0{r1} {cambiar_momento("AM", "PM", q2)}, {dias_de_la_semana[posicion + d1 % 7]} ({d1} days later)'
                else:
                    if d1 == 1:
                        final = f'{r2}:{r1} {cambiar_momento("AM", "PM", q2)}, {dias_de_la_semana[posicion + d1 % 7]} (next day)'
                    elif d1 == 0:
                        final = f'{r2}:{r1} {cambiar_momento("AM", "PM", q2)}, {dias_de_la_semana[posicion + d1 % 7]}'
                    else:
                        final = f'{r2}:{r1} {cambiar_momento("AM", "PM", q2)}, {dias_de_la_semana[posicion + d1 % 7]} ({d1} days later)'
            elif momento_inicial == "PM":
                if q2 % 2 == 1:
                    d1 = (q2 // 2) + 1
                    if r1 < 10:
                        if d1 == 1:
                            final = f'{r2}:0{r1} {cambiar_momento("PM", "AM", q2)}, {dias_de_la_semana[posicion + d1 % 7]} (next day)'
                        elif d1 == 0:
                            final = f'{r2}:0{r1} {cambiar_momento("PM", "AM", q2)}, {dias_de_la_semana[posicion + d1 % 7]}'
                        else:
                            final = f'{r2}:0{r1} {cambiar_momento("PM", "AM", q2)}, {dias_de_la_semana[posicion + d1 % 7]} ({d1} days later)'
                    else: 
                        if d1 == 1:
                            final = f'{r2}:{r1} {cambiar_momento("PM", "AM", q2)}, {dias_de_la_semana[posicion + d1 % 7]} (next day)'
                        elif d1 == 0:
                           final = f'{r2}:{r1} {cambiar_momento("PM", "AM", q2)}, {dias_de_la_semana[posicion + d1 % 7]}'
                        else:
                            final = f'{r2}:{r1} {cambiar_momento("PM", "AM", q2)}, {dias_de_la_semana[(posicion + d1) % 7]} ({d1} days later)'
                else:
                    d1 = (q2 // 2)
                    if r1 < 10:
                        if d1 == 1:
                            final = f'{r2}:0{r1} {cambiar_momento("PM", "AM", q2)}, {dias_de_la_semana[posicion + d1 % 7]} (next day)'
                        elif d1 == 0:
                            final = f'{r2}:0{r1} {cambiar_momento("PM", "AM", q2)}, {dias_de_la_semana[posicion + d1 % 7]} (next day)'
                        else:
                            final = f'{r2}:0{r1} {cambiar_momento("PM", "AM", q2)}, {dias_de_la_semana[posicion + d1 % 7]} ({d1} days later)'
                    else: 
                        if d1 == 1:
                            final = f'{r2}:{r1} {cambiar_momento("PM", "AM", q2)}, {dias_de_la_semana[posicion + d1 % 7]} (next day)'
                        elif d1 == 0:
                            final = f'{r2}:{r1} {cambiar_momento("PM", "AM", q2)}, {dias_de_la_semana[posicion + d1 % 7]}'
                        else:
                            final = f'{r2}:{r1} {cambiar_momento("PM", "AM", q2)}, {dias_de_la_semana[posicion + d1 % 7]} ({d1} days later)'
        else:
            if r1 < 10:
                final = f'{r2}:0{r1} {momento_inicial}, {dias_de_la_semana[(posicion) % 7]}'
            else:
                final = f'{r2}:{r1} {momento_inicial}, {dias_de_la_semana[(posicion) % 7]}'      

 
    return final 

print(add_time('8:16 PM', '466:02', 'tuesday'))