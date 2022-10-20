import math 

degrees = 0

x = math.sin(degrees / 360.0 * 2 * math.pi) 
x = math.exp(math.log(x + 1))

# >>> minutes = hours * 60                # correto
# >>> hours * 60 = minutes                # errado!
# SyntaxError: can't assign to operator