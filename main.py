'''
Un laboratorio está desarrollando un robot capaz de interactuar con personas.
Para que la interacción con éste sea lo más natural posible, es necesario que el artefacto sea capaz de detectar los
sentimientos de las personas que lo rodean.
En una primera etapa el laboratorio decide simplificar esta tarea de la siguiente forma: dado un diccionario en donde
cada palabra posee un puntaje entre -10 y 10 el robot analizará la “positividad” de diversos textos.
Las palabras con mayor puntaje son aquellas que los seres humanos comúnmente consideran positivas.
Por ejemplo: la palabra “fantástico” tiene puntaje 10 y “destestable” tiene -10. 
Nuestra tarea es desarrollar un algoritmo que, dado este diccionario y un texto, nos diga qué tan positivo es este
último, hallando el promedio de la positividad de las palabras.
Cualquier palabra que no se halle en el diccionario tendrá el valor 0.
'''


'''
1 - Convertir cadena a minuscula
2 - Quitar caracteres especiales
3 - Split cadena
4 - Contabilizar resultado
'''

import string
import unicodedata

class Positivity():

  @staticmethod
  def cast_to_lower(text: string) -> string:
    """
    Retorna una cadena en formato lowe case
    """
    return text.lower()

  @staticmethod
  def clear_text(text: string)-> string:
    """
    Dado una cadena de string, quita acentos y algunos caracteres especiales
    """
    s = ''.join((c for c in unicodedata.normalize('NFD',text) if unicodedata.category(c) != 'Mn'))
    s = s.replace(',','').replace('.','').replace('-','').replace('*','')
    s = s.replace("\\s{2,}", " ")
    return s

  @staticmethod
  def split_text(text: string)-> dict:
    """
    Dado una cadena de tipo string devuelve un diccionario
    """
    return text.split(' ')

  def compute(self, text: string, data: dict) -> float:
    lower_text = self.cast_to_lower(text)
    cleat_text = self.clear_text(lower_text)
    source_data = self.split_text(cleat_text)

    suma = 0
    cantidad = 0
    for word in source_data:  
      if word != '':
        cantidad += 1
        if word in data:        
          suma += data[word]
    
    return suma/cantidad
