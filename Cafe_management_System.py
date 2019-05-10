from tkinter import*
import random
import time;
import datetime

#====================================================user interface================================================================================================
root=Tk()
root.geometry("1350x750")
root.title("Cafe Management System")
root.configure(background='black')

Tops=Frame(root,width=1350,height=100,bd=4,relief="raise")
Tops.pack(side=TOP)

f1=Frame(root,width=900,height=650,bd=8,relief="raise")
f1.pack(side=LEFT)

f2=Frame(root,width=440,height=650,bd=8,relief="raise")
f2.pack(side=RIGHT)

ft2=Frame(f2,width=440,height=450,bd=12,relief="raise")
ft2.pack(side=TOP)
fb2=Frame(f2,width=440,height=250,bd=16,relief="raise")
fb2.pack(side=BOTTOM)

f1a=Frame(f1,width=900,height=330,bd=8,relief="raise")
f1a.pack(side=TOP)
f2a=Frame(f1,width=900,height=320,bd=6,relief="raise")
f2a.pack(side=BOTTOM)

f1aa=Frame(f1a,width=450,height=330,bd=16,relief="raise")
f1aa.pack(side=LEFT)
f1ab=Frame(f1a,width=450,height=330,bd=16,relief="raise")
f1ab.pack(side=RIGHT)

f2aa=Frame(f2a,width=450,height=330,bd=14,relief="raise")
f2aa.pack(side=LEFT)
f2ab=Frame(f2a,width=450,height=330,bd=14,relief="raise")
f2ab.pack(side=RIGHT)
Tops.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')

#=========================================================cost of item==================================================
def CostofItem():
    Item1=float(E_Drink1.get())
    Item2=float(E_Drink2.get())
    Item3=float(E_Drink3.get())
    Item4=float(E_Drink4.get())
    Item5=float(E_Drink5.get())
    Item6=float(E_Drink6.get())
    Item7=float(E_Drink7.get())
    Item8=float(E_Drink8.get())

    Item9=float(E_Desert1.get())
    Item10=float(E_Desert2.get())
    Item11=float(E_Desert3.get())
    Item12=float(E_Desert4.get())
    Item13=float(E_Desert5.get())
    Item14=float(E_Desert6.get())
    Item15=float(E_Desert7.get())
    Item16=float(E_Desert8.get())

    PriceofDrinks=(Item1*1.2)+(Item2*1.99)+(Item3*2.05)+(Item4*1.89)+(Item5*1.99)+(Item6*2.99)+(Item7*2.39)+(Item8*1.29)

    PriceofDeserts=(Item9*1.35)+(Item10*2.2)+(Item11*1.99)+(Item12*1.49)+(Item13*1.8)+(Item14*1.67)+(Item15*1.6)+(Item16*1.299)

    DrinksPrice="$",str('%.2f'%(PriceofDrinks))
    DesertsPrice="$",str('%.2f'%(PriceofDeserts))
    costofDeserts.set(DesertsPrice)
    costofDrinks.set(DrinksPrice)
    SC="$",str('%.2f'%(1.59))
    ServiceTax.set(SC)

    SubTotalofItems="$",str('%.2f'%(PriceofDrinks+PriceofDeserts+1.59))
    SubTotal.set(SubTotalofItems)

    Tax="$",str('%.2f'%((PriceofDrinks+PriceofDeserts+1.59)*0.15))
    PaidTax.set(Tax)
    TT=((PriceofDrinks+PriceofDeserts+1.59)*0.15)
    TC="$",str('%.2f'%(PriceofDrinks+PriceofDeserts+1.59+TT))
    TotalCost.set(TC)
#=========================================================Methods=======================================================
def qExit():
    qExit=messagebox.askyesno("Quit System","Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return

def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    costofDrinks.set("")
    costofDeserts.set("")
    ServiceTax.set("")
    txtReceipt.delete("1.0",END)    

    E_Drink1.set("0")
    E_Drink2.set("0")
    E_Drink3.set("0")
    E_Drink4.set("0")
    E_Drink5.set("0")
    E_Drink6.set("0")
    E_Drink7.set("0")
    E_Drink8.set("0")

    E_Desert1.set("0")
    E_Desert2.set("0")
    E_Desert3.set("0")
    E_Desert4.set("0")
    E_Desert5.set("0")
    E_Desert6.set("0")
    E_Desert7.set("0")
    E_Desert8.set("0")

    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var15.set("0")
    var16.set("0")
    
    
    txtDrink1.configure(state=DISABLED)
    txtDrink2.configure(state=DISABLED)
    txtDrink3.configure(state=DISABLED)
    txtDrink4.configure(state=DISABLED)
    txtDrink5.configure(state=DISABLED)
    txtDrink6.configure(state=DISABLED)
    txtDrink7.configure(state=DISABLED)
    txtDrink8.configure(state=DISABLED)

    txtDesert1.configure(state=DISABLED)
    txtDesert2.configure(state=DISABLED)
    txtDesert3.configure(state=DISABLED)
    txtDesert4.configure(state=DISABLED)
    txtDesert5.configure(state=DISABLED)
    txtDesert6.configure(state=DISABLED)
    txtDesert7.configure(state=DISABLED)
    txtDesert8.configure(state=DISABLED)

def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(10908,500876)
    randomref=str(x)
    Receipt_Ref.set("BILL"+ randomref)

    txtReceipt.insert(END,'Receipt ref:\t\t\t'+Receipt_Ref.get()+'\t\t'+DateofOrder.get()+"\n")
    txtReceipt.insert(END,'Items\t\t\t\t\t'+"Cost of Items \n\n")
    txtReceipt.insert(END,'Assam Tea\t\t\t\t\t'+E_Drink1.get()+"\n")
    txtReceipt.insert(END,'Aztec Cappucino\t\t\t\t\t'+E_Drink2.get()+"\n")
    txtReceipt.insert(END,'Cafe Americano\t\t\t\t\t'+E_Drink3.get()+"\n")
    txtReceipt.insert(END,'Cafe Frappe\t\t\t\t\t'+E_Drink4.get()+"\n")
    txtReceipt.insert(END,'Cafe Latte\t\t\t\t\t'+E_Drink5.get()+"\n")
    txtReceipt.insert(END,'Cafe Mocha\t\t\t\t\t'+E_Drink6.get()+"\n")
    txtReceipt.insert(END,'Classic Lemonade\t\t\t\t\t'+E_Drink7.get()+"\n")
    txtReceipt.insert(END,'CoCoa Latte\t\t\t\t\t'+E_Drink8.get()+"\n")
    txtReceipt.insert(END,'Belgian CoCoa Shot\t\t\t\t\t'+E_Desert1.get()+"\n")
    txtReceipt.insert(END,'Chocolate Flovoured icecream\t\t\t\t\t'+E_Desert2.get()+"\n")
    txtReceipt.insert(END,'CoCoa Fantasy\t\t\t\t\t'+E_Desert3.get()+"\n")
    txtReceipt.insert(END,'CoCOa Fantasy cake\t\t\t\t\t'+E_Desert4.get()+"\n")
    txtReceipt.insert(END,'Assam Mango Shots\t\t\t\t\t'+E_Desert5.get()+"\n")
    txtReceipt.insert(END,'Dark Passion\t\t\t\t\t'+E_Desert6.get()+"\n")
    txtReceipt.insert(END,'Twilight Dessert\t\t\t\t\t'+E_Desert7.get()+"\n")
    txtReceipt.insert(END,'Nuty Fudge Brownie\t\t\t\t\t'+E_Desert8.get()+"\n")
    txtReceipt.insert(END,'Cost of Drinks:\t\t' + costofDrinks.get() +'\Tax paid:\t\t' +PaidTax.get()+"\n")
    txtReceipt.insert(END,'Cost of Deserts:\t\t' + costofDeserts.get() +'\Sub Total:\t\t' +SubTotal.get()+"\n")
    txtReceipt.insert(END,'Service Tax:\t\t' + ServiceTax.get() +'\Total Cost:\t\t' + TotalCost.get()+"\n")
#=========================================================Heading=======================================================
lblinfo=Label(Tops,font=('arial',70,'bold'),text="  Cafe Management System  ",bd=10)
lblinfo.grid(row=0,column=0)

#=========================================================Variables=====================================================
DateofOrder=StringVar()
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")
var13.set("0")
var14.set("0")
var15.set("0")
var16.set("0")
Receipt_Ref=StringVar()
costofDrinks=StringVar()
costofDeserts=StringVar()
ServiceTax=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()

E_Drink1=StringVar()
E_Drink2=StringVar()
E_Drink3=StringVar()
E_Drink4=StringVar()
E_Drink5=StringVar()
E_Drink6=StringVar()
E_Drink7=StringVar()
E_Drink8=StringVar()

E_Desert1=StringVar()
E_Desert2=StringVar()
E_Desert3=StringVar()
E_Desert4=StringVar()
E_Desert5=StringVar()
E_Desert6=StringVar()
E_Desert7=StringVar()
E_Desert8=StringVar()

E_Drink1.set("0")
E_Drink2.set("0")
E_Drink3.set("0")
E_Drink4.set("0")
E_Drink5.set("0")
E_Drink6.set("0")
E_Drink7.set("0")
E_Drink8.set("0")

E_Desert1.set("0")
E_Desert2.set("0")
E_Desert3.set("0")
E_Desert4.set("0")
E_Desert5.set("0")
E_Desert6.set("0")
E_Desert7.set("0")
E_Desert8.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))


#=========================================================Calculator====================================================
def Chkbutton():
    if (var1.get()==1):
        txtDrink1.configure(state=NORMAL)
    elif var1.get()==0:
        txtDrink1.configure(state=DISABLED)
        E_Drink1.set("0")
    if (var2.get()==1):
        txtDrink2.configure(state=NORMAL)
    elif var2.get()==0:
        txtDrink2.configure(state=DISABLED)
        E_Drink2.set("0")
    if (var3.get()==1):
        txtDrink3.configure(state=NORMAL)
    elif var3.get()==0:
        txtDrink3.configure(state=DISABLED)
        E_Drink3.set("0")
    if (var4.get()==1):
        txtDrink4.configure(state=NORMAL)
    elif var4.get()==0:
        txtDrink4.configure(state=DISABLED)
        E_Drink4.set("0")
    if (var5.get()==1):
        txtDrink5.configure(state=NORMAL)
    elif var5.get()==0:
        txtDrink5.configure(state=DISABLED)
        E_Drink5.set("0")
    if (var6.get()==1):
        txtDrink6.configure(state=NORMAL)
    elif var6.get()==0:
        txtDrink6.configure(state=DISABLED)
        E_Drink6.set("0")
    if (var7.get()==1):
        txtDrink7.configure(state=NORMAL)
    elif var7.get()==0:
        txtDrink7.configure(state=DISABLED)
        E_Drink7.set("0")
    if (var8.get()==1):
        txtDrink8.configure(state=NORMAL)
    elif var8.get()==0:
        txtDrink8.configure(state=DISABLED)
        E_Drink8.set("0")
    if (var9.get()==1):
        txtDesert1.configure(state=NORMAL)
    elif var9.get()==0:
        txtDesert1.configure(state=DISABLED)
        E_Desert1.set("0")
    if (var10.get()==1):
        txtDesert2.configure(state=NORMAL)
    elif var10.get()==0:
        txtDesert2.configure(state=DISABLED)
        E_Desert2.set("0")
    if (var11.get()==1):
        txtDesert3.configure(state=NORMAL)
    elif var11.get()==0:
        txtDesert3.configure(state=DISABLED)
        E_Desert3.set("0")
    if (var12.get()==1):
        txtDesert4.configure(state=NORMAL)
    elif var12.get()==0:
        txtDesert4.configure(state=DISABLED)
        E_Desert4.set("0")
    if (var13.get()==1):
        txtDesert5.configure(state=NORMAL)
    elif var13.get()==0:
        txtDesert5.configure(state=DISABLED)
        E_Desert5.set("0")
    if (var14.get()==1):
        txtDesert6.configure(state=NORMAL)
    elif var14.get()==0:
        txtDesert6.configure(state=DISABLED)
        E_Desert6.set("0")
    if (var15.get()==1):
        txtDesert7.configure(state=NORMAL)
    elif var15.get()==0:
        txtDesert7.configure(state=DISABLED)
        E_Desert7.set("0")
    if (var16.get()==1):
        txtDesert8.configure(state=NORMAL)
    elif var16.get()==0:
        txtDesert8.configure(state=DISABLED)
        E_Desert8.set("0")  
        


#========================================================Drnks==========================================================
Drink1=Checkbutton(f1aa,text="Assam Tea\t\t",variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=Chkbutton)
Drink1.grid(row=0,column=0)
Drink2=Checkbutton(f1aa,text="Aztec Cappucino \t\t",variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=Chkbutton).grid(row=1,column=0)
Drink3=Checkbutton(f1aa,text="Cafe Americano \t\t",variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=Chkbutton).grid(row=2,column=0)
Drink4=Checkbutton(f1aa,text="Cafe Frappe \t\t",variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=Chkbutton).grid(row=3,column=0)
Drink5=Checkbutton(f1aa,text="Cafe Latte \t\t",variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=Chkbutton).grid(row=4,column=0)
Drink6=Checkbutton(f1aa,text="Cafe Mocha \t\t",variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=Chkbutton).grid(row=5,column=0)
Drink7=Checkbutton(f1aa,text="Classic Lemonade\t",variable=var7,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=Chkbutton).grid(row=6,column=0)
Drink8=Checkbutton(f1aa,text="Cold Cocoa Latte \t\t",variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=Chkbutton).grid(row=7,column=0)

#========================================================Deserts==========================================================
Desert1=Checkbutton(f1ab,text="Belgian Choco Shot\t\t",variable=var9,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=Chkbutton).grid(row=0,column=0)
Desert2=Checkbutton(f1ab,text="Chocolate Flavoured Shot\t\t",variable=var10,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=Chkbutton).grid(row=1,column=0)
Desert3=Checkbutton(f1ab,text="Cocoa Fantasy \t\t\t",variable=var11,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=Chkbutton).grid(row=2,column=0)
Desert4=Checkbutton(f1ab,text="Cocoa Fantast Cake \t\t",variable=var12,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=Chkbutton).grid(row=3,column=0)
Desert5=Checkbutton(f1ab,text="Mango Shots \t\t\t",variable=var13,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=Chkbutton).grid(row=4,column=0)
Desert6=Checkbutton(f1ab,text="Dark Passion \t\t\t",variable=var14,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=Chkbutton).grid(row=5,column=0)
Desert7=Checkbutton(f1ab,text="Twilight Desert \t\t\t",variable=var15,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=Chkbutton).grid(row=6,column=0)
Desert8=Checkbutton(f1ab,text="Nuty Fudge Brownie \t\t",variable=var16,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=Chkbutton).grid(row=7,column=0)

#=======================================================Enter Widget for Drinks===================================================================
txtDrink1=Entry(f1aa,font=('arial',18,'bold'),textvariable=E_Drink1,bd=8,width=6, justify='left',state=DISABLED)
txtDrink1.grid(row=0,column=1)
txtDrink2=Entry(f1aa,font=('arial',18,'bold'),textvariable=E_Drink2,bd=8,width=6, justify='left',state=DISABLED)
txtDrink2.grid(row=1,column=1)
txtDrink3=Entry(f1aa,font=('arial',18,'bold'),textvariable=E_Drink3,bd=8,width=6, justify='left',state=DISABLED)
txtDrink3.grid(row=2,column=1)
txtDrink4=Entry(f1aa,font=('arial',18,'bold'),textvariable=E_Drink4,bd=8,width=6, justify='left',state=DISABLED)
txtDrink4.grid(row=3,column=1)
txtDrink5=Entry(f1aa,font=('arial',18,'bold'),textvariable=E_Drink5,bd=8,width=6, justify='left',state=DISABLED)
txtDrink5.grid(row=4,column=1)
txtDrink6=Entry(f1aa,font=('arial',18,'bold'),textvariable=E_Drink6,bd=8,width=6, justify='left',state=DISABLED)
txtDrink6.grid(row=5,column=1)
txtDrink7=Entry(f1aa,font=('arial',18,'bold'),textvariable=E_Drink7,bd=8,width=6, justify='left',state=DISABLED)
txtDrink7.grid(row=6,column=1)
txtDrink8=Entry(f1aa,font=('arial',18,'bold'),textvariable=E_Drink8,bd=8,width=6, justify='left',state=DISABLED)
txtDrink8.grid(row=7,column=1)

#========================================================Enter Widget of Deserts==========================================================
txtDesert1=Entry(f1ab,font=('arial',18,'bold'),textvariable=E_Desert1,bd=8,width=6, justify='left',state=DISABLED)
txtDesert1.grid(row=0,column=1)
txtDesert2=Entry(f1ab,font=('arial',18,'bold'),textvariable=E_Desert2,bd=8,width=6, justify='left',state=DISABLED)
txtDesert2.grid(row=1,column=1)
txtDesert3=Entry(f1ab,font=('arial',18,'bold'),textvariable=E_Desert3,bd=8,width=6, justify='left',state=DISABLED)
txtDesert3.grid(row=2,column=1)
txtDesert4=Entry(f1ab,font=('arial',18,'bold'),textvariable=E_Desert4,bd=8,width=6, justify='left',state=DISABLED)
txtDesert4.grid(row=3,column=1)
txtDesert5=Entry(f1ab,font=('arial',18,'bold'),textvariable=E_Desert5,bd=8,width=6, justify='left',state=DISABLED)
txtDesert5.grid(row=4,column=1)
txtDesert6=Entry(f1ab,font=('arial',18,'bold'),textvariable=E_Desert6,bd=8,width=6, justify='left',state=DISABLED)
txtDesert6.grid(row=5,column=1)
txtDesert7=Entry(f1ab,font=('arial',18,'bold'),textvariable=E_Desert7,bd=8,width=6, justify='left',state=DISABLED)
txtDesert7.grid(row=6,column=1)
txtDesert8=Entry(f1ab,font=('arial',18,'bold'),textvariable=E_Desert8,bd=8,width=6, justify='left',state=DISABLED)
txtDesert8.grid(row=7,column=1)

#========================================================Cost item Information=======================================================================
lblcostofDrinks=Label(f2aa,font=('arial',16,'bold'),text="cost of Drinks",bd=8).grid(row=2,column=0)
lblcostofDeserts=Label(f2aa,font=('arial',16,'bold'),text="cost of Drinks",bd=8).grid(row=3,column=0)
lblServiceTax=Label(f2aa,font=('arial',16,'bold'),text="Service Tax",bd=8).grid(row=4,column=0)

txtcostofDrinks=Entry(f2aa,font=('arial',16,'bold'),textvariable=costofDrinks,bd=8,insertwidth=2,justify='left')
txtcostofDrinks.grid(row=2,column=1)
txtcostofDessert=Entry(f2aa,font=('arial',16,'bold'),textvariable=costofDeserts,bd=8,insertwidth=2,justify='left')
txtcostofDessert.grid(row=3,column=1)
txtServiceTax=Entry(f2aa,font=('arial',16,'bold'),textvariable=ServiceTax,bd=8,insertwidth=2,justify='left')
txtServiceTax.grid(row=4,column=1)

#========================================================Payment Information=======================================================================
lblPaidTax=Label(f2ab,font=('arial',16,'bold'),text="Paid Tax",bd=8).grid(row=2,column=0)
lblSubTotal=Label(f2ab,font=('arial',16,'bold'),text="Sub Total",bd=8).grid(row=3,column=0)
lblTotalCost=Label(f2ab,font=('arial',16,'bold'),text="TotalCost",bd=8).grid(row=4,column=0)

txtPaidTax=Entry(f2ab,font=('arial',16,'bold'),textvariable=PaidTax,bd=8,insertwidth=2,justify='left')
txtPaidTax.grid(row=2,column=1)
txtSubTotal=Entry(f2ab,font=('arial',16,'bold'),textvariable=SubTotal,bd=8,insertwidth=2,justify='left')
txtSubTotal.grid(row=3,column=1)
txtTotalCost=Entry(f2ab,font=('arial',16,'bold'),textvariable=TotalCost,bd=8,insertwidth=2,justify='left')
txtTotalCost.grid(row=4,column=1)

#=========================================================Receipt IOnformation=====================================================================
lblReceipt=Label(ft2,font=('arial',16,'bold'),text="Receipt:",bd=2).grid(row=0,column=0)
txtReceipt=Text(ft2,width=59,height=22,bg="white",bd=8,font=('arial',11,'bold'))
txtReceipt.grid(row=1,column=0)

#=========================================================Buttons================================================================================
btnTotal=Button(fb2,padx=16,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Total",command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(fb2,padx=16,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Receipt",command=Receipt).grid(row=0,column=1)
btnReset=Button(fb2,padx=16,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Reset",command=Reset).grid(row=0,column=2)
btnExit=Button(fb2,padx=16,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Exit",command=qExit).grid(row=0,column=35)


root.mainloop();
