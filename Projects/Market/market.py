from random import randint
import math
import time

cart = []
remaining_products = {}
menu = {"Apple":0.50,"Orange":0.75,"Banana":1.00,"Strawberry":0.20,"Cherry":0.10,"Lemon":0.75,"Melon":5.00,"Pineapple":2.50}

class shopping:
    def _init_(self):
        pass

    def show_products_prices():
        for i,j in enumerate(sorted(menu)):
            time.sleep(0.2)
            print(i,":",j,menu[j],"$\n")
        
    def show_products():
        print("Products for sale:\n")
        for i in list(sorted(menu)):
            if i == list(sorted(menu))[len(menu) - 1]:
                print(i)
            else:
                print(i,end = ", \n")
                
    def show_available_products():
        print("Products remaining:")
        for i in menu:
            remaining_products[i] = randint(0,100)
        for i,j in enumerate(sorted(remaining_products)):
            time.sleep(0.2)
            print(i,":",j,":",remaining_products[j],"available\n")
        
    def add_item(cart,item,amount):
        for i in range(amount):
            cart.append(item)
        print(amount,item,"(s) are added to cart\n")

    def remove_item(cart,item,amount):
        for i in range(amount):
            cart.remove(item)
        print(amount,item,"(s) are removed from your cart\n")

shopper = shopping

def shopping_option():
    while True:
        time.sleep(2)
        print("""If you want to check the prices, type 1.
If you wish to have a look at products list, type 2.
If you want to see which products are available, type 3.
If you decide to add products in your cart, type 4.
If you change your opinion and want to remove products from your cart, type 5.
If you finished your shopping and want to exit, type 6.\n""")
        option = input()
        if option == '1':
            shopper.show_products_prices()
        elif option == '2':
            shopper.show_products()
        elif option == '3':
            shopper.show_available_products()
        elif option == '4':
            while True:
                item = str(input("Assign the item you wish to add in your cart. "))
                lmenu = list(menu)
                for i in range(len(lmenu)):
                    if item == lmenu[i]:
                        amount = int(input("Assign the amount of the item you wish to add in your cart. "))
                        shopper.add_item(cart,item,amount)
                        print("Your cart now contains: ",cart,"\n")
                        break
                    elif item != lmenu[i] and i == 7:
                        print("The item you demand doesn't exist in the product list.\n")
                        break
                break
        elif option == '5':
            if len(cart) > 0:
                while True:
                    item = str(input("Assign the item you wish to remove from your cart. "))
                    for i in range(len(cart)):
                        if item == cart[i]:
                            amount = int(input("Assign the amount of the item you wish to remove from your cart. "))
                            shopper.remove_item(cart,item,amount)
                            print("Your cart now contains: ",cart,"\n")
                            break
                        elif item!= cart[i] and i == len(cart) - 1:
                            print("This item is already removed from your cart.\n")
                            break
                    break
            else:
                print("Your cart is already empty.\n")
        elif option == '6':
            print("Thank you for visiting our market. Have a good day!")
            break
        else:
            print("There is no option defined for",option,"\n")

shopping_option()
