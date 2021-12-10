class InventoryManagement:
    import json
    fd = open("data.json", 'r')
    txt = fd.read()
    data = json.loads(txt)
    fd.close()
    def __init__(rice, pulses, wheats):
        rice.pulses = pulses
        rice.wheats = wheats

    print("Enter New Product ID :- ")
    id = input()
     
    if id not in data.keys():
        print("Enter Product Name :- ")
        name = input()
         
        print("Enter Price of Product(price for product quantity as 1) :- ")
        price = input()
         
        print("Enter Category of Product :- ")
        category = input()
         
        print("Enter Quantity of Product :- ")
        quantity = input()
         
        print("Enter The Date on Which Product is Added in Inventory :- ")
        date = input()
         
        data[id] = {'name': name, 'price': price,
                    'category': category, 'quantity': quantity, 'date': date}
        print("Please Press '0' to Add New Attributes\
        /Properties of Product or Press '1' to Continue :- ")
        z = int(input())
         
        if(z == 0):
            print("Enter Number of New Attributes/Properties of Product :- ")
            n = int(input())
             
            for i in range(n):
                print("Enter Attribute Name That you Want To Add :- ")
                nam = input()
                print("Enter The "+str(nam)+" of Product :- ")
                pro = input()
                data[id][nam] = pro
        print("Product ID "+str(id)+" Added Successfully...!!!")
         
    else:
        print("The Product ID you Have Entered Is Already Present\
        t in DataBase Please Check...!!!")
    js = json.dumps(data)
    fd = open("data.json", 'w')
    fd.write(js)
    fd.close()