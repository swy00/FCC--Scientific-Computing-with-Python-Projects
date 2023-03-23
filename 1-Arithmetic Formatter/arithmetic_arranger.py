def arithmetic_arranger(problems,resolver=False):
    #Inicializo resolver en False por si no se pasa el argumento, en caso de que haya argumento se sobreescribe
    problemas_acomodados = []
    #Primer condicion, la cantidad de problemas
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for index,value in enumerate(problems):
        operacion = value.split(" ")
        #Segunda condicion,se admite sumas y restas nada más
        if operacion[1] not in "+-":
            return "Error: Operator must be '+' or '-'."
        #Tercera condicion, solo digitos se admiten
        #Intento convertir en integer, si explota es porque no son numeros
        try:
            num1 = int(operacion[0])
            num2 = int(operacion[2])
        except ValueError:
            return "Error: Numbers must only contain digits."

        #Cuarta condicion,numeros de solo 4 dígitos      
        if len(operacion[0]) > 4 or len(operacion[2]) > 4:
        #Tengo que usar "or" porque en python | es un operador de bits (BitwiseOperators)
            return "Error: Numbers cannot be more than four digits."
        #Encuentro el valor mas largo
        longest_val = max(len(operacion[0]), len(operacion[2]))
        #Hago que el width sea 2 valores mas largo que el numero mas largo
        width = longest_val + 2
        #Resulvo con f-strings"formatted string literals"
        #Primera Fila de valores
        F1 = f"{operacion[0]:>{width}}" 
        #con :>{width} hago que el valor esté a la derecha y el width indica el ancho del campo de caracteres
        #Segunda fila de valores con la operacion al inicio
        F2 = operacion[1] + f"{operacion[2]:>{width-1}}" #-1 ya que operacion[1] ocupa 1 lugar
        #Cantidade de "-" que corresponde dependiendo el length de los numeros
        palitos = '-' * width 
        
        
        try:
          problemas_acomodados[0]+= (' ' *4) + F1
        except IndexError:
          problemas_acomodados.append(F1)

        try:
          problemas_acomodados[1]+= (' ' *4) + F2
        except IndexError:
          problemas_acomodados.append(F2)

        try:
          problemas_acomodados[2]+= (' ' *4) + palitos
        except IndexError:
          problemas_acomodados.append(palitos)
        #En caso de que se quiera el resultado
        if resolver:
            if operacion[1] == "+":
               ans = int(operacion[0]) + int(operacion[2])
            elif operacion[1] == "-":
               ans = int(operacion[0]) - int(operacion[2])
            
            a = f"{str(ans):>{width}}"
            try:
              problemas_acomodados[3]+= (' ' *4) + a
            except IndexError:
              problemas_acomodados.append(a)
    #Armo el resultado con f-strings, el ultimo valor se ejecuta si necesito el resultado o no      
    resultado = f"{problemas_acomodados[0]}\n{problemas_acomodados[1]}\n{problemas_acomodados[2]}"
    if len(problemas_acomodados) > 3:
        resultado = resultado + f"\n{problemas_acomodados[3]}"
    return (resultado)
#arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)  