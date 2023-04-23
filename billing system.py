print("-------------------------------------------------------------------------------------")
print("-------------------------------------FORMER SHOP-------------------------------------")
print("-------------------------------------------------------------------------------------")
print("\n\n")
product=[]
price=[]
quantity=[]
inve=[]
profit=0
bill1=0
bill2=0
product1=[]
price1=[]
quantity1=[]
cg=int(input("enter  1 to continue : "))
while(cg==1):
    print("1......former\n2.....customer\n3.......exit")
    choice=int(input("enter the choice  :"))
    if(choice==1):
        print("welcome to former page...............")
        user=input("USERNAME : ")
        p=input("Password : ")
        if (user=="sakthi" and p=="123"):
            print("login successfull..........")
            print("1.add item\n2.profit/lose\n3.view peoducts\n4.exit")
            ch=int(input("enter your choice : "))
            iq=int(input("press 1 to continue..............:"))
            while(iq==1):
                if (ch==1):
                    print("-------------YOUR CART-------------------")
                    pro=int(input("entr the  number of products : "))
                    i=0
                    while i<pro:
                        a=input("Product name :")
                        b=int(input("quantity : "))
                        c=int(input("price kg\l : "))
                        product.insert(i,a)
                        quantity.insert(i,b)
                        price.insert(i,c)
                        i=i+1
                    print("\n")
                    print("your products are added..................")
                    print("***************************************")
                    print("----------------YOUR CART---------------")
                    print("\tid\t\tproduct\t\t quantity\tprice\kg")
                    j=0
                    while j<len(product):
                        ie=j+1
                        print("\t",ie,"\t\t",product[j],"\t\t",quantity[j],"\t\t",price[j])
                        j=j+1
                        print("-------------------------------------------------------")
                    cf=input("do you exit [y/n] : ")
                    if (cf.lower()=="y"):
                        break
                elif(ch==2):
                    print("------------------------CALCULATION-----------------------")
                    print("\n\n")
                    pa=int(input("enter the number of products : "))
                    i=0
                    while i<pa:
                        pname=input("enter the product name : ")
                        for pname in product:
                            inv=int(input("enetr your investment :"))
                            pqu=int(input("enter the quantity : "))
                            x=product.index(pname)
                            pri=price[x]
                            diff=pri*pqu
                            dif=diff-inv
                            if(dif>0):
                                print("***********************************************")
                                print("profit : ",dif)
                            else:
                                print("***********************************************")
                                print("Loss  : ",dif)
                    i=i+1
                elif(ch==3):
                    print("----------------YOUR CART---------------")
                    print("\tid\t\tproduct\t\t quantity\tprice\kg")
                    j=0
                    while j<len(product):
                        ie=j+1
                        print("\t",ie,"\t\t",product[j],"\t\t",quantity[j],"\t\t",price[j])
                        j=j+1
                    print("-------------------------------------------------------")
                    break
                else:
                    break
    elif(choice==2):
        print("**************************************************************************************")
        print("------------------------------LIST OF PRODUCTS--------------------------")
        print("\tid\t\tproduct\t\t quantity\tprice\kg")
        j=0
        while j<len(product):
            ie=j+1
            print("\t",ie,"\t\t",product[j],"\t\t",quantity[j],"\t\t",price[j])
            j=j+1
            print("-------------------------------------------------------")
        print("\n\n")
        print("--------------CART---------------")
        n=int(input("enter the number of products : "))
        for i in range(n):
            prod=input("enter the product name : ")
            qu=int(input("enter the quantity : "))
            product1.insert(i,prod)
            quantity1.insert(i,qu)
            if prod in product:
                q=product.index(prod)
                pr=price[q]
                bill=pr*qu
                l=product.index(prod)
                qr=quantity[l]
                quan=qr-qu
                quantity[l]=quan
                bill1=bill1+bill
                price1.insert(i,bill)
        amount=int(input("Enter amount given  : "))
        balance=amount-bill1
        print("\tid\t\tproduct\t\t quantity\tprice")
        print("----------------------------------------------")
        j=0
        while j<n:
            ie=j+1
            print("\t",ie,"\t\t",product1[j],"\t\t",quantity1[j],"\t\t",price1[j])
            j=j+1
            print("-------------------------------------------------------")
        print("TOTAL bill : ",bill1)
        print("Balance amount : ",balance)
        
    elif(choice==3):
        exit()
                
        
        
            
