# É legal para uma função chamar outra; também é legal para uma função chamar a si própria. 
# Pode não ser óbvio porque isso é uma coisa boa, 
# mas na verdade é uma das coisas mais mágicas que um programa pode fazer. 
# Por exemplo, veja a seguinte função:

def countdown(n):
    if n <= 0:
        print("Blast!")
    else:
        print(n)
        countdown(n -1 )
        
countdown(10)       

# Uma função que chama a si mesma é dita recursiva; o processo para executá-la é a recursividade.

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)
    
    
print_n("Adorei escrever esse lance de recursividade -", 10)    