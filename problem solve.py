Ram_having_mangoes = 10
Children = 2
divide = Ram_having_mangoes / Children
def fun():
    # Divide the mangoes to the two children
    # Show as a local variable
    print("Child_1=" ,int(divide))
    print("Child_2=" ,int(divide))


# show the Global variable
Child_1= 5
Child_2= 5
print("Global var Child_1=" ,Child_1)
print("Global var Child_2=",Child_2)
fun()
