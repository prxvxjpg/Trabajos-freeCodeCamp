class Category:

    def __init__(self, category=""):
        self.ledger = []
        self.budget = 0  
        self.category = category
        self.Category = []
        self.Category += category
        self.defi =  0
        
    def deposit(self, amount, description = ""):
        self.ledger.append({'amount': amount, 'description': description})
        self.budget += amount


    def withdraw(self, amount, description = ""):
        if amount >= 0 and self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.budget -= amount 
            self.defi += amount
            return True
        else:
            return False

    def get_balance(self):
        return self.budget 
        
    def transfer(self, amount, another_budget):
        if self.check_funds(amount):
            self.budget -= amount
            self.ledger.append({'amount': -amount, 'description': f'Transfer to {another_budget.category}'}) #self.withdraw(amount, description = f"Transfer to {another_budget}")
            another_budget.deposit(amount, description = f'Transfer from {self.category}')            
            return True
        else: 
            return False

    def check_funds(self, amount):
        return self.get_balance() >= amount
    
    # Varios códigos sobre el print que no son explicados hasta el momento en freeCodeCamp:    
    def __str__(self):
        printar = ""
        titulo = self.category.center(30, "*")
        printar += titulo
        for item in self.ledger:
            description = item["description"]
            amount = item["amount"]
            printar += "\n"
            printar += f'{description[0:23]:23}{amount:7.2f}'
        printar += "\n"
        printar += "Total: "
        printar += format(self.budget, ".2f")
        return printar ## and presupuesto de cada categoria: str(self.budget)

# Ejemplo:
food = Category("Food")
clothing = Category("Clothing")
auto = Category('Auto')

food.deposit(1000, "deposit")
food.withdraw(600, "groceries")
food.withdraw(165.60, "books")
food.withdraw(175.10, "books")
food.transfer(50, clothing)

clothing.deposit(1000, "deposit")
clothing.withdraw(200, "groceries")

auto.deposit(1000, "deposit")
auto.withdraw(100, "groceries")

# Otro ejemplo:
"""food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)"""

def create_spend_chart(categories=[]):
    str_output = f"Percentage spent by category\n"
    divisores_diez = ["100", " 90", " 80", " 70", " 60", " 50", " 40", " 30", " 20", " 10", "  0"]
    Total = 0
    percentage_cat = []
    barra = []
    barrafinal = [] #Lista de cadenas final de los circulos de la barra acorde a sus porcentajes
    CATEGORIES = [] #Lista de categorias ingresadas en la función
    CATEGORIESFINAL = []
    lineas = "-"

    for cat in categories:
        Total += cat.defi
        percentage_cat.append(cat.defi)
        CATEGORIES.append(cat.category)
        
    percentage_cat1 = list(map(lambda x: int(100 * (x / Total)), percentage_cat)) #Porcentaje de cada categoria puesta en la función
    cantidad_barra = list(map(lambda x: int(10 * (x / Total)) + 1, percentage_cat)) #Número de "o" que deben estar en cada categoria

    for j in cantidad_barra:
        barra.append(j * "o")
    
    for k in barra:
        while len(k) < 11:
            k += " "
        barrafinal.append(k[::-1])
    
    if len(categories) == 1:
        for a, b in zip(divisores_diez, list(barrafinal[0])):
            str_output += f'{a}| {b}  \n'
    elif len(categories) == 2:
        for a, b, c in zip(divisores_diez, list(barrafinal[0]), list(barrafinal[1])):
            str_output += f'{a}| {b}  {c}  \n'    
    elif len(categories) == 3:
        for a, b, c, d in zip(divisores_diez, list(barrafinal[0]), list(barrafinal[1]), list(barrafinal[2])):
            str_output += f'{a}| {b}  {c}  {d}  \n'
    elif len(categories) == 4:
        for a, b, c, d, f in zip(divisores_diez, list(barrafinal[0]), list(barrafinal[1]), list(barrafinal[2]), list(barrafinal[3])):
            str_output += f'{a}| {b}  {c}  {d}  {f}  \n'            
    
    str_output += f"    {len(categories)*'---'}-\n"
    max_len = 0

    if len(CATEGORIES) == 1:
        max_len = len(CATEGORIES[0])
    if len(CATEGORIES) == 2:
        max_len = max(len(CATEGORIES[0]), len(CATEGORIES[1])) 
    if len(CATEGORIES) == 3:
        max_len = max(len(CATEGORIES[0]), len(CATEGORIES[1]), len(CATEGORIES[2]))  
    if len(CATEGORIES) == 4:
        max_len = max(len(CATEGORIES[0]), len(CATEGORIES[1]), len(CATEGORIES[2]), len(CATEGORIES[3]))

    for t in CATEGORIES:
        while len(t) <= max_len:
            t += " "
        CATEGORIESFINAL.append(t[::])    

    if len(CATEGORIES) == 1:
        for x in CATEGORIESFINAL[0]:
            str_output += f'     {x}  \n'
    if len(CATEGORIESFINAL) == 2:
        for x, y in zip(CATEGORIESFINAL[0], CATEGORIESFINAL[1]):
            str_output += f'     {x}  {y}  \n'   
    if len(CATEGORIESFINAL) == 3:
        for x, y, z in zip(CATEGORIESFINAL[0], CATEGORIESFINAL[1], CATEGORIESFINAL[2]):
            str_output += f'     {x}  {y}  {z}  \n'
    if len(CATEGORIESFINAL) == 4:
        for x, y, z, q in zip(CATEGORIESFINAL[0], CATEGORIESFINAL[1], CATEGORIESFINAL[2], CATEGORIESFINAL[3]):
            str_output += f'     {x}  {y}  {z}  {q}  \n'
    
    eliminar = 4 + len(CATEGORIES)*3 + 3


    return str_output[:-eliminar]

#    ITEMS IMPORTANTES:
#    print(divisores_diez)
#    print(barrafinal)
#    print(CATEGORIES)
#    print(percentage_cat)
#    print(food.budget, clothing.budget, auto.budget)

print(create_spend_chart([food, clothing, auto]))

 
# Alternativa más corta de la función create_spend_chart(categories):
'''
def create_spend_chart(categories):
    max_len = 0
    percentage = []

    for Cat in categories:
        percent = 0
        max_len = max(max_len, len(Cat.category))
        for item in Cat.ledger:
            if item["amount"] >=0:
                percent += item["amount"]
        if percent != 0:
            percent = (percent - Cat.budget)*100/percent
        percentage.append(int(percent))


    judul = 'Percentage spent by category  '
    str_output = judul
    space = ' '
    for i in range(10, -1, -1):
        space = '' if i == 10 else ' '
        if i == 0:
            space = '  '
        str_ = ''
        for num in range(len(percentage)):
            str_ += 'o  ' if i*10 <= percentage[num] else '   '
        str_output += f'\n{space}{i*10}| {str_}'
    str_output += f'\n    -{"-"*3*len(percentage)}'
    for num in range(max_len):
        str_cat = ''
        for i in range(len(categories)):
            str_cat += f'{categories[i].category[num]}  ' if num < len(categories[i].category) else '   '
        str_output += f'\n     {str_cat}'

    print(str_output)



create_spend_chart([food, clothing, auto])'''


