def add_time(start, duration, dia=None):
  dias = {
      "Saturday": 0,
      "Sunday": 1,
      "Monday": 2,
      "Tuesday": 3,
      "Wednesday": 4,
      "Thursday": 5,
      "Friday": 6
  }

  #Separo la hora inicial en hora, minuto, y AM-PM
  start = start.split(":")
  str2 = start[1].split(" ")
  hora = int(start[0])
  minuto = int(str2[0])
  momDia = str2[1]

  #Separo la duracion
  dur = duration.split(":")
  durHora = int(dur[0])
  durMin = int(dur[1])

  #Hago la suma y cambio acorde las cosas
  nHora = hora + durHora
  nMin = minuto + durMin
  while nMin > 60:
    nHora += 1
    nMin -= 60

  #Contador para ver cuántas veces pasa de PM a AM (cambio de día)
  cambioDia = 0
  while nHora >= 12:
    nHora -= 12
    if momDia == "PM":
      momDia = "AM"
      cambioDia += 1
    else:
      momDia = "PM"

  #Acomodo cuando queda 1 solo dígito los minutos o cuando son las 12
  if nMin <= 9:
    nMin = "0" + str(nMin)
  else:
    str(nMin)
  if nHora == 0:
    nHora = 12
  #Armo el String
  resultado = f"{nHora}:{nMin} {momDia}"
  #Dia que terminó y cantidad de días que pasan
  #Si no paso de día va a quedar vacio
  parentesis = ""
  if cambioDia == 1:
    parentesis = " (next day)"
  elif cambioDia > 1:
    parentesis = f" ({cambioDia} days later)"

  #Día de la semana
  if dia is not None:
    valor = dias[dia.lower().capitalize()]
    #Busco el int del dia inicial, le sumo la cantida de dias que pasaron y a partir de esto sé en que dia voy a terminar
    dia_actual = (valor + cambioDia) % 7
    #A partir del numero, encuentro el string en la lista de dias
    dia = next(key for key, value in dias.items() if value == dia_actual)
    return f"{resultado}, {dia}{parentesis}"
  else:
    return resultado + parentesis
