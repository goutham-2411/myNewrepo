print('Welcome dear customer!!')
print('The available products and quantity with cost are:')
store=['Milk:10:20/ltr','Curds:30:20/ltr','Rice:50:60/kg','Dal:20:30/kg','Butter:20:100/pack']
print(store)
#Finding whether the Customer is an existing customer or not...
def search(list, name):
    for i in range(len(list)):
        if (list[i] == name):
            return True
    return False
#Initialise a list with the names of existing customers..
E_C=['Harry','Joe','Tom','Zane']
name=input('Please enter your name:')
if search(E_C,name):
    print('Welcome back',name,',you are entitled for 10% discount!!')
else:
    print('Hello there newbie..!!',name,',welcome to the store')
#Entering the name of the products...(from the given 5 items)
print('How many items do you want to buy?')
n=int(input())
if(n>5):
    print('Out of range..Sorry for inconvinience')
    exit()
elif(0<n<5):
    print('Continue shopping..')
item=[]
print('Choose the products you want to buy...')
print('Do you want to buy Milk')
answer=input('1 or 0(1 for yes and 0 for no)?')
if(int(answer)==1):
    print('Added to cart')
    item.append('Milk')
else:
    print('ok..next item??')
print('Do you want to buy Curds')
answer=input('1 or 0(1 for yes and 0 for no)')
if(int(answer)==1):
    print('Added to cart')
    item.append('Curds')
else:
    print('ok..next item??')
print('Do you want to buy Rice')
answer=input('1 or 0(1 for yes and 0 for no)')
if(int(answer)==1):
    print('Added to cart')
    item.append('Rice')
else:
    print('ok..next item??')
print('Do you want to buy Dal')
answer=input('1 or 0(1 for yes and 0 for no)')
if(int(answer)==1):
    print('Added to cart')
    item.append('Dal')
else:
    print('ok..next item??')
print('Do you want to buy Butter')
answer=input('1 or 0(1 for yes and 0 for no)')
if(int(answer)==1):
    print('Added to cart')
    item.append('Butter')
else:
    print('ok..next item??')
print('Your added items are:',item) #to display the items ordered
#To enter the quantities
quant=[]
milk=input('Enter the quantity of milk you want(if not in your cart, enter 0):')
quant.append(milk)
curds=input('Enter the quantity of curd you want(if not in your cart, enter 0):')
quant.append(curds)
rice=input('Enter the quantity of rice you want(if not in your cart, enter 0):')
quant.append(rice)
dal=input('Enter the quantity of dal you want(if not in your cart, enter 0):')
quant.append(dal)
butter=input('Enter the quantity of butter you want(if not in your cart, enter 0):')
quant.append(butter)
print('Your entered quantities are:',quant)
#total price for each product
total=[]
milk=int(quant[0])*20
total.append(milk)
curds=int(quant[1])*20
total.append(curds)
rice=int(quant[2])*60
total.append(rice)
dal=int(quant[3])*30
total.append(dal)
butter=int(quant[4])*100
total.append(butter)
print('Your total amount of each product is:',total) #diplay's the price of each product purchased
amount=sum(total) #actual total
#Final bill for existing customer
if search(E_C,name):
    discount=((int(amount))/100)*10
    print('YOUR FINAL BILL IS...')
    print('Your items are',item)
    print('Quantites are:',quant)
    print('Total amount of each product is:',total)
    print('Final amount to be paid is:',discount)
    print('THANK YOU..... PLEASE VISIT AGAIN!!')
else: #Final bill for new customer
    amount=sum(total)
    print('YOUR FINAL BILL IS...')
    print('Your items are',item)
    print('Quantites are:',quant)
    print('Total amount of each product is:',total)
    print('Final amount to be paid is:',amount)
    print('THANK YOU..... PLEASE VISIT AGAIN!!')

