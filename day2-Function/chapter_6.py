# def update_order():
#     chai_type="Elaichi"
#     def kitchen():
#         nonlocal chai_type
#         chai_type="kesar"
#     kitchen()
#     print("After kitechen upadte",chai_type)
    
# update_order()

chai_type= "Plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type="Irnai"
    kitchen()

front_desk()
print("Final Global",chai_type)