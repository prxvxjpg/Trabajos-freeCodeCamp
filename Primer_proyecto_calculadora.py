def arithmetic_arranger(problems, show_answers=True):
    one = []
    two = []
    three = []
    four = []
    error = []
    for operation in problems:
        digitos = []
        set_numero_1 = []
        set_numero_2 = []  
        set_final = []
        resultados = []    
        final_boss = []  
        j = 1
        linea = "------"
        espacio_operaciones = "        "
        indice_final = None
        numero_1 = None
        numero_2 = None
        operador = None
        resultado = None
        resultado_suma = None
        resultado_resta = None

        if len(problems) > 5:
            error.append('Error: Too many problems.')
            break
        else:
            if operation[:j].isdigit():
                while operation[:j].isdigit():
                    j += 1
                    if j > 5:
                        error.append('Error: Numbers cannot be more than four digits.')
                        break
                    else:
                        if operation[j:j+1] == "+" and operation[j-1:j] == " " and operation[j+1:j+2] == " "  and operation[j+2:j+6].isdigit():
                            indice_final = j
                            resultado_suma = int(operation[:j]) + int(operation[j+1:])
                            numero_1 = int(operation[:j])
                            numero_2 = int(operation[j+1:])
                            set_numero_1.append(numero_1)
                            set_numero_2.append(numero_2)
                            resultado = int(operation[:j]) + int(operation[j+1:])
                            operador = operation[j:j+1]
                            resultados.append(resultado_suma)

                        elif operation[j:j+1]  == "-" and operation[j-1:j] == " " and operation[j+1:j+2] == " " and operation[j+2:j+6].isdigit():
                            indice_final = j
                            resultado_resta = int(operation[:j]) - int(operation[j+1:])
                            numero_1 = int(operation[:j])
                            numero_2 = int(operation[j+1:])
                            set_numero_1.append(numero_1)
                            set_numero_2.append(numero_2)                            
                            operador = operation[j:j+1]
                            resultado = int(operation[:j]) - int(operation[j+1:])
                            resultados.append(resultado_resta)                
                        else:
                            indice_final = j-1                            
            else: 
                error.append('Error: Numbers must only contain digits.')
                break
            if operation[j+2:].isdigit():
                if len(operation[j+2:]) > 4:
                    error.append('Error: Numbers cannot be more than four digits.')
                    break
                else:
                    pass
                    if operation[indice_final:indice_final+1] == "+":
                        pass
                    elif operation[indice_final:indice_final+1] == "-":
                        pass
                    else:
                        error.append("Error: Operator must be '+' or '-'.")
                        break
            else:
                error.append('Error: Numbers must only contain digits.')
                 
        
        digitos_primer_numero = indice_final-1
        digitos_segundo_numero = len(operation[indice_final+2:])        
        
        maximos = max(digitos_primer_numero, digitos_segundo_numero) #número de lineas "-"

        espacio_respuesta = max(digitos_primer_numero, digitos_segundo_numero) + 2

        if digitos_primer_numero > digitos_segundo_numero:
            if show_answers == False:
                distancia = digitos_primer_numero - digitos_segundo_numero
                set_final.append(f'  {numero_1}    \n{operador} {espacio_operaciones[:distancia]}{numero_2}    \n{linea[:maximos+2]}    ')
                one.append(str(f"  {numero_1}"))
                two.append(str(f"{operador} {espacio_operaciones[:distancia]}{numero_2}"))
                three.append(f"{linea[:maximos+2]}")
                
            else:
                distancia = digitos_primer_numero - digitos_segundo_numero
                set_final.append(f'  {numero_1}    \n{operador} {espacio_operaciones[:distancia]}{numero_2}    \n{linea[:maximos+2]}    ')
                one.append(str(f'  {numero_1}'))
                two.append(str(f"{operador} {espacio_operaciones[:distancia]}{numero_2}"))
                three.append(f"{linea[:maximos+2]}")
                if resultado_suma == None:
                    set_final.append(f'\n{espacio_operaciones[:espacio_respuesta-len(str(resultado_resta))]}{resultado_resta}    ')
                    four.append(f"{espacio_operaciones[:espacio_respuesta-len(str(resultado_resta))]}{resultado_resta}")
                else:
                    set_final.append(f'\n{espacio_operaciones[:espacio_respuesta-len(str(resultado_suma))]}{resultado_suma}    ')
                    four.append(f"{espacio_operaciones[:espacio_respuesta-len(str(resultado_suma))]}{resultado_suma}")
        elif digitos_segundo_numero > digitos_primer_numero:
            if show_answers == False:
                distancia = digitos_segundo_numero - digitos_primer_numero
                set_final.append(f'  {espacio_operaciones[:distancia]}{numero_1}    \n{operador} {numero_2}    \n{linea[:maximos+2]}    ')
                one.append(str(f"  {espacio_operaciones[:distancia]}{numero_1}"))
                two.append(str(f"{operador} {numero_2}"))
                three.append(f"{linea[:maximos+2]}")
            else:
                distancia = digitos_segundo_numero - digitos_primer_numero
                distancia = digitos_segundo_numero - digitos_primer_numero
                set_final.append(f'  {espacio_operaciones[:distancia]}{numero_1}    \n{operador} {numero_2}    \n{linea[:maximos+2]}    ')
                one.append(str(f"  {espacio_operaciones[:distancia]}{numero_1}"))
                two.append(str(f"{operador} {numero_2}"))
                three.append(f"{linea[:maximos+2]}")
                set_final.append(f'  {espacio_operaciones[:distancia]}{numero_1}    \n{operador} {numero_2}    \n{linea[:maximos+2]}    ')
                if resultado_suma == None:
                    four.append(f"{espacio_operaciones[:espacio_respuesta-len(str(resultado_resta))]}{resultado_resta}")
                    set_final.append(f'\n{espacio_operaciones[:espacio_respuesta-len(str(resultado_resta))]}{resultado_resta}    ')
                else:
                    four.append(f"{espacio_operaciones[:espacio_respuesta-len(str(resultado_suma))]}{resultado_suma}")
                    set_final.append(f'\n{espacio_operaciones[:espacio_respuesta-len(str(resultado_suma))]}{resultado_suma}    ')
        else:
            if show_answers == False:
                one.append(str(f"  {numero_1}"))
                two.append(str(f"{operador} {numero_2}"))
                three.append(f"{linea[:maximos+2]}")
            else:
                one.append(str(f"  {numero_1}"))
                two.append(str(f"{operador} {numero_2}"))
                three.append(f"{linea[:maximos+2]}")
                if resultado_suma == None:
                    four.append(f"{espacio_operaciones[:espacio_respuesta-len(str(resultado_resta))]}{resultado_resta}")
                    set_final.append(f'\n{espacio_operaciones[:espacio_respuesta-len(str(resultado_resta))]}{resultado_resta}    ')
                else:
                    four.append(f"{espacio_operaciones[:espacio_respuesta-len(str(resultado_suma))]}{resultado_suma}")
                    set_final.append(f'\n{espacio_operaciones[:espacio_respuesta-len(str(resultado_suma))]}{resultado_suma}    ')
        final_boss_set = ''.join([str(exercise) for exercise in set_final])
        final_boss = ''.join(final_boss_set)
    ONE = "    ".join(one)
    TWO = "    ".join(two)
    THREE = "    ".join(three)
    FOUR = "    ".join(four)
    ERROR = " ".join(error)
    final = ""
    if ERROR:
        final = ERROR
    else:
        if show_answers == True:
            final = f'{ONE}\n{TWO}\n{THREE}\n{FOUR}'
        else:
            final = f'{ONE}\n{TWO}\n{THREE}'   
         
    return final
    
print(arithmetic_arranger(["3822 - 2", "1223 + 49"]))



#hay un pequeño problema con digitos que comienzan en 0, ejemplo: 03

