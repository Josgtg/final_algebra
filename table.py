name = "comidas"

schema = """
    nombre TEXT,
    valor_nutricional INTEGER,
    sabor INTEGER,
    textura INTEGER,
    presentacion INTEGER,
    tiempo_preparacion INTEGER
"""

insert = f"""
    INSERT INTO {name} VALUES(?, ?, ?, ?, ?, ?)
"""

data = [
    ["Ensalada César", 8, 7, 7, 8, 5],
    ["Pizza Margherita", 6, 9, 8, 7, 6],
    ["Sopa de Pollo", 7, 8, 6, 6, 5],
    ["Sushi", 9, 8, 9, 9, 7],
    ["Tacos de Carne", 7, 9, 8, 7, 6],
    ["Spaghetti Bolognese", 8, 8, 7, 7, 6],
    ["Hamburguesa", 5, 9, 7, 8, 5],
    ["Paella", 9, 8, 8, 9, 7],
    ["Ceviche", 8, 9, 9, 8, 5],
    ["Brownie", 4, 10, 8, 9, 4],
    ["Lasagna", 7, 9, 8, 9, 6],
    ["Tostadas de Tinga", 7, 8, 7, 8, 5],
    ["Ramen", 8, 9, 8, 8, 6],
    ["Pollo al Curry", 8, 8, 7, 8, 7],
    ["Falafel", 7, 8, 7, 7, 6],
    ["Burrito", 6, 9, 7, 7, 5],
    ["Ratatouille", 9, 8, 7, 9, 7],
    ["Empanadas", 6, 8, 8, 8, 5],
    ["Hummus", 8, 7, 6, 7, 4],
    ["Poke Bowl", 9, 8, 9, 9, 5],
    ["Galletas de Avena", 7, 9, 8, 8, 4],
    ["Enchiladas", 7, 9, 7, 8, 6],
    ["Quiche Lorraine", 8, 8, 7, 8, 7],
    ["Fajitas de Pollo", 7, 8, 7, 7, 6],
    ["Gazpacho", 8, 7, 6, 8, 5],
    ["Croquetas", 6, 8, 8, 8, 5],
    ["Bruschetta", 7, 8, 7, 8, 4],
    ["Chili con Carne", 7, 8, 7, 7, 6],
    ["Pollo Tikka Masala", 8, 9, 8, 8, 7],
    ["Crème Brûlée", 4, 9, 8, 9, 5]
]