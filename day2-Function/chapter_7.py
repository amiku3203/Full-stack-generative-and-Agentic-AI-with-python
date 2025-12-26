def special_chai(*ingredients, **extras):
    print("Ingredients",ingredients)
    print("Extras",extras)

special_chai("Cineman","Cardoman",sweetenre="Honey",foam="yes")

def chai_order(order=None):
    order.append("Masala")
    print(order)
    
chai_order()