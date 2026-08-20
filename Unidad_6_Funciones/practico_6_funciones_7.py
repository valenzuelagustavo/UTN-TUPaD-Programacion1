### FUNCIONES ###

def operaciones_basicas(a, b):
    operaciones = (a*b , a+b, a-b, a/b)
    return operaciones

### PROGRAMA ###

num_a = float(input("Ingrese el primer número: "))
num_b = float(input("Ingrese el segundo número: "))

op_basicas = operaciones_basicas(num_a, num_b)

print(f"""
{num_a} x {num_b} = {op_basicas[0]}
{num_a} + {num_b} = {op_basicas[1]}
{num_a} - {num_b} = {op_basicas[2]}
{num_a} / {num_b} = {op_basicas[3]}

""")