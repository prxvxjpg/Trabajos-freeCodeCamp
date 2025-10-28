import copy
import random

class Hat:
# keyword arguments arbitrarios: Captura cualquier argumento adicional que no esté definido explícitamente. 
# Este es un diccionario con pares clave-valor.
# Los keyword arguments (**kwargs) son útiles para aceptar un número arbitrario de argumentos adicionales.    
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def contents(self):
        contents1 = []
        for clave, valor in self.kwargs.items():
            contents1 += [str(clave) for _ in range(valor)]
        return contents1
    
    def draw(self, num_of_colors):
        contents2 = []
        for clave, valor in self.kwargs.items():
            contents2 += [str(clave) for _ in range(valor)]
        extracted_colors = random.sample(contents2, num_of_colors)
        return extracted_colors
            

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    veces_que_cumple_condicion = 0
#    i = 1
#    while i <= num_experiments:
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_counts = {ball: drawn_balls.count(ball) for ball in set(drawn_balls)}
        conditions = all(drawn_counts.get(key, 0) >= val for key, val in expected_balls.items())
        if conditions:
            veces_que_cumple_condicion += 1
    
    return print(veces_que_cumple_condicion / num_experiments)

    """for _ in range(num_experiments):
        conditions = all(hat.draw(num_balls_drawn).count(key) >= val for key, val in expected_balls.items())
        if conditions is True:
            veces_que_cumple_condicion += 1
#        i += 1
    
    return print(veces_que_cumple_condicion / num_experiments)"""
    


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)

hat1 = Hat(yellow=3, blue=2, green=6)
print(hat1.draw(2))



"""Los keyword arguments (**kwargs) son útiles para aceptar un número arbitrario de argumentos adicionales.
Puedes mezclar argumentos explícitos con **kwargs para capturar valores opcionales.
Usar kwargs.get() te permite manejar valores predeterminados en caso de que un argumento no esté presente.
La combinación de *args y **kwargs da flexibilidad para aceptar cualquier tipo de argumentos."""