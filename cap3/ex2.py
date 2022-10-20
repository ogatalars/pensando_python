# def do_twice(f, x):
#     f()
#     f()
def do_twice(f,x):
    f()
    print(x)

def print_spam():
    print('spam')
    
do_twice(print_spam, 10)        

def do_four(f, x):
    do_twice(f, x)
    do_twice(f, x)

    
    