print("-------------------------------------------------------------------------------------")
print("-------------------------------------FORMER SHOP-------------------------------------")
print("-------------------------------------------------------------------------------------")
print("\n\n")
product=["rice","wheat"]
price=[50,64]
quantity=[100,200]
inve=[]
profit=0
bill1=0
bill2=0
product1=[]
price1=[]
quantity1=[]
cg=int(input("enter  1 to continue : "))
while(cg==1):
    print("1......former\n2.....customer\n3.......exit\n\n")
    choice=int(input("enter the choice  :"))
    print("\n\n")
    if(choice==1):
        print("welcome to former page...............")
        user=input("USERNAME : ")
        p=input("Password : ")
        if (user=="sakthi" and p=="123"):
            print("login successfull..........\n\n")
            print("1.add item\n2.profit/lose\n3.view peoducts\n4.Updtae\n5.exit")
            ch=int(input("enter your choice : "))
            iq=int(input("press 1 to continue..............:"))
            while(iq==1):
                if (ch==1):
                    print("-------------YOUR CART------------------\n")
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
                    
                    print("your products are added..................\n\n")
                    print("***************************************")
                    print("----------------YOUR CART---------------\n\n")
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
                    if(len(product)<=0):
                        print("No values  found !!!!!!")
                    else:
                        print("\n\n")
                        pa=int(input("enter the number of products : "))
                        i=0
                        while i<pa:
                            pname=input("enter the product name : ")
                            if pname in product:
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
                            else:
                                print("first shound add the product.....")
                            i=i+1
                        cf=input("do you exit [y/n] : ")
                        if (cf.lower()=="y"):
                            break
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
                elif(ch==4):
                    print("------------------------Update-------------------------")
                    print("\n\n")
                    en=int(input("enetr the number of products  : "))
                    for i in range(en):
                        name=input("enter the name of product : ")
                        if name in product:
                            print("\t\t1Update quantity\n\t\t2.Update price")
                            cj=int(input("Enter your choice : "))
                            if(cj==1):
                                y=product.index(name)
                                qe=int(input("enter the quantity : "))
                                quantity[y]=quantity[y]+qe
                            elif(cj==2):
                                z=product.index(name)
                                pl=int(input("enter the price : "))
                                price[z]=pl
                    
                            else:
                                print("enter valid choice....")
                        else:
                            print("product not in list ...please add the product............!!!\n")
                    print("----------------YOUR CART---------------\n\n")
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
    else:
        print("Enter correct choice..................")
        
                
        
        
            
