from datetime import datetime
name=input("enter customer name : ")
lists='''
sugar Rs 20k/g
rice  Rs 30k/g
paneer Rs 40k/g
oil   Rs 60k/g'''
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]
items={'sugar':20,'rice':40,'panner':60,'oil':100}
option=int(input("To enter items press 1 : "))
if option==1:
           print(lists)
for i in range(len(items)):
    inp=int(input("are  you intrested to buy product press 1 or 2 : "))
    if inp==2:
        break
    if inp==1:
        item=input("enter your items :")
        quantity=int(input("enter the quantity : "))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry your item is not available")
    else:
        print("you entered a wrong number")
    inp1=input("can i bill the items : ")
    if 'yes':
        pass
        if finalamount!=0:
            print(25*"=","supermarket",25*"=")
            print(28*" ","kadapa")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',8*' ',ilist[i],3*' ',qlist[i],plist[i])
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)