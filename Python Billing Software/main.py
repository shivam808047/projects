from tkinter import *
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
import os,tempfile
import random,smtplib
# Functionlity Part
billnumber = random.randint(500,1000)

if not os.path.exists('bills'):
    os.mkdir('bills')



# Function to display the graph
def analyze_graph():
    try:
        # Load the CSV file
        csv_file = 'retail_bills.csv'  # Adjust the path if needed
        data = pd.read_csv(csv_file)

        # Group by Product and sum the quantities
        grouped_data = data.groupby('Product')['Quantity'].sum().reset_index()

        # Plot the graph
        plt.figure(figsize=(10, 6))
        plt.bar(grouped_data['Product'], grouped_data['Quantity'], color='skyblue')
        plt.title('Product vs Quantity', fontsize=16)
        plt.xlabel('Product', fontsize=12)
        plt.ylabel('Quantity', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Show the graph
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")





def clear():
    bathsoapEntry.delete(0,END)
    FacecreamEntry.delete(0,END)
    HairGelEntry.delete(0,END)
    HairSprayEntry.delete(0,END)
    BodyLotionEntry.delete(0,END)
    FaceWashEntry.delete(0,END)

    DaalEntry.delete(0,END)
    BrownEntry.delete(0,END)
    RiceEntry.delete(0,END)
    OilEntry.delete(0,END)
    TeaEntry.delete(0,END)
    SugerEntry.delete(0,END)

    PepsiEntry.delete(0,END)
    CocacolaEntry.delete(0,END)
    MaazaEntry.delete(0,END)
    SpriteEntry.delete(0,END)
    FrootiEntry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    BillEntry.delete(0,END)

    cosmeticpriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    coldDrinkpriceEntry.delete(0,END)
    cosmetictaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    coldDrinktaxEntry.delete(0,END)

    textarea.delete(1.0,END)





    bathsoapEntry.insert(0,0)
    FacecreamEntry.insert(0,0)
    HairGelEntry.insert(0,0)
    HairSprayEntry.insert(0,0)
    BodyLotionEntry.insert(0,0)
    FaceWashEntry.insert(0,0)

    DaalEntry.insert(0,0)
    BrownEntry.insert(0,0)
    RiceEntry.insert(0,0)
    OilEntry.insert(0,0)
    TeaEntry.insert(0,0)
    SugerEntry.insert(0,0)

    PepsiEntry.insert(0,0)
    CocacolaEntry.insert(0,0)
    MaazaEntry.insert(0,0)
    SpriteEntry.insert(0,0)
    FrootiEntry.insert(0,0)


def send_gmail():
    try:

        ob = smtplib.SMTP('smtp.gmail.com',587)
        ob.starttls()
        ob.login(senderEntry.get(),passwoedEntry.get())
        message = email_textarea.get(1.0,END)
        
        ob.sendmail(senderEntry.get(),recieverEntry.get(),message)
        ob.quit()
        messagebox.showinfo("success",'Bill is successfully sent',parent=root1)
        root1.destroy()
    except:
        messagebox.showerror('Error','Something went wrong,please try again',parent=root1)



def send_email():
    global root1
    global senderEntry,passwoedEntry,email_textarea,recieverEntry
    if textarea.get(1.0,END) =='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        root1 = Toplevel()
        root1.grab_set()
        root1.title('Send Mail')
        root1.config(bg='gray20')
        root1.resizable(0,0)

        senderFrame = LabelFrame(root1,text="SENDER",font=('arial','16','bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        senderLabel = Label(senderFrame,text="Sender's Email",font=('arial','14','bold'),bg='gray20',fg='white')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)

        senderEntry = Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)


        passwordLabel = Label(senderFrame,text="Password",font=('arial','14','bold'),bg='gray20',fg='white')
        passwordLabel.grid(row=1,column=0,padx=10,pady=8)

        passwoedEntry = Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
        passwoedEntry.grid(row=1,column=1,padx=10,pady=8)


        recipientFrame = LabelFrame(root1,text="RECIPIENT",font=('arial','16','bold'),bd=6,bg='gray20',fg='white')
        recipientFrame.grid(row=1,column=0,padx=40,pady=20)

        recieverLabel = Label(recipientFrame,text="Email Address",font=('arial','14','bold'),bg='gray20',fg='white')
        recieverLabel.grid(row=0,column=0,padx=10,pady=8)

        recieverEntry = Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        recieverEntry.grid(row=0,column=1,padx=10,pady=8)

        messageLabel = Label(recipientFrame,text="Message",font=('arial','14','bold'),bg='gray20',fg='white')
        messageLabel.grid(row=1,column=0,padx=10,pady=8)

        email_textarea = Text(recipientFrame,font=('arial','14','bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)

        email_textarea.insert(END,textarea.get(1.0,END).replace('\t\t\t','\t\t').replace('-',''))

        sendButton = Button(root1,text='SEND',font=('arial','16','bold'),width=15,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=20)
        


    root1.mainloop()



def print_bill():
    if textarea.get(1.0,END) =='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file =  tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')



def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == BillEntry.get():
            f= open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror("error",'Invalid Bill Number')





def save_bill():
    global billnumber
    result =  messagebox.askyesno('confirm','Do you want to save the bill')
    if result:
        bill_content = textarea.get(1.0,END)
        file = open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill number {billnumber} is saved successfully')
        billnumber = random.randint(500,1000)
def bill_area():
    if nameEntry.get() == '' or phoneEntry.get() =='':
        messagebox.showerror('Error','Customer Details Are Required')
    elif cosmeticpriceEntry.get()=='' and grocerypriceEntry=='' and coldDrinkpriceEntry=='':
        messagebox.showerror('Error','No Product are selected')
    if cosmeticpriceEntry.get() =='0 Rs' and grocerypriceEntry =='0 Rs' and coldDrinkpriceEntry=='0 Rs':
        messagebox.showerror('Error','No product selected')
        
    else:
    
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t**Welcome Customer** \n')
        textarea.insert(END,f'\n Bill Number: {billnumber}')
        textarea.insert(END,f'\n Customer Name: {nameEntry.get()}')
        textarea.insert(END,f'\n Phone Number: {phoneEntry.get()}\n')
        textarea.insert(END,f'\n------------------------------------------------------\n')
        textarea.insert(END,'Product\t\t\t Quantity\t\t price')
        textarea.insert(END,f'\n------------------------------------------------------\n')

        # for costamic product
        if bathsoapEntry.get() != '0':
            textarea.insert(END,f'\nBath soap\t\t\t{bathsoapEntry.get()}\t\t{soap_value} Rs')
        if FacecreamEntry.get() != '0':
            textarea.insert(END,f'\nFace Cream\t\t\t{FacecreamEntry.get()}\t\t {facecream_value} Rs')
        
        if FaceWashEntry.get() != '0':
            textarea.insert(END,f'\nFace Wash\t\t\t{FaceWashEntry.get()}\t\t {faceWash_value} Rs')   
        if HairSprayEntry.get() != '0':
            textarea.insert(END,f'\nHair Spray \t\t\t{HairSprayEntry.get()}\t\t {Hairspray_value} Rs')
        if HairGelEntry.get() != '0':
            textarea.insert(END,f'\nHair Gel \t\t\t{HairGelEntry.get()}\t\t {Gel_value} Rs')
        if BodyLotionEntry.get() != '0':
            textarea.insert(END,f'\nBody Lotion\t\t\t{BodyLotionEntry.get()}\t\t {bodyLotion_value} Rs')

        textarea.insert(END,f'\n------------------------------------------------------\n')

        # for grocery product
        if RiceEntry.get() != '0':
            textarea.insert(END,f'\nRice\t\t\t{RiceEntry.get()}\t\t {rice_value} Rs')
        if DaalEntry.get() != '0':
            textarea.insert(END,f'\nDaal\t\t\t{DaalEntry.get()}\t\t {daal_value} Rs')
        if SugerEntry.get() != '0':
            textarea.insert(END,f'\nSuger\t\t\t{SugerEntry.get()}\t\t {Suger_value} Rs')
        if OilEntry.get() != '0':
            textarea.insert(END,f'\nOil\t\t\t{OilEntry.get()}\t\t {Oil_value} Rs')
        if BrownEntry.get() != '0':
            textarea.insert(END,f'\nBrownRice\t\t\t{BrownEntry.get()}\t\t {brown_vlaue} Rs')
        if TeaEntry.get() != '0':
            textarea.insert(END,f'\nTea\t\t\t{TeaEntry.get()}\t\t {Tea_value} Rs')

        textarea.insert(END,f'\n------------------------------------------------------\n')
        # for cold Drink
        if MaazaEntry.get() != '0':
            textarea.insert(END,f'\nMaaza\t\t\t{MaazaEntry.get()}\t\t {Maaza_vlaue} Rs')
        if PepsiEntry.get() != '0':
            textarea.insert(END,f'\nPepsi\t\t\t{PepsiEntry.get()}\t\t {Peepsi_value} Rs')
        if SpriteEntry.get() != '0':
            textarea.insert(END,f'\nSprite\t\t\t{SpriteEntry.get()}\t\t {Sprite_value} Rs')
        if DewEntry.get() != '0':
            textarea.insert(END,f'\nDew\t\t\t{DewEntry.get()}\t\t {Dew_value} Rs')
        if CocacolaEntry.get() != '0':
            textarea.insert(END,f'\nCoke\t\t\t{CocacolaEntry.get()}\t\t {coke_value} Rs')
        if FrootiEntry.get() != '0':
            textarea.insert(END,f'\n Frooti\t\t\t{FrootiEntry.get()}\t\t {Frooti_value} Rs')



        textarea.insert(END,f'\n------------------------------------------------------\n')

        if cosmetictaxEntry.get() != '0.0 Rs':
            textarea.insert(END,f'\ncosmetic Tex\t\t\t{cosmetictaxEntry.get()}')
        if grocerytaxEntry.get() != '0.0 Rs':
            textarea.insert(END,f'\nGrocery Tex\t\t\t{grocerytaxEntry.get()}')
        if coldDrinktaxEntry.get() != '0.0 Rs':
            textarea.insert(END,f'\ncold Drink Tex\t\t\t{coldDrinktaxEntry.get()}')

        textarea.insert(END,f'\n------------------------------------------------------\n')

        
        textarea.insert(END,f'\n\nTotal Bill \t\t\t{totalBill}')
        
        textarea.insert(END,f'\n------------------------------------------------------\n')
        save_bill()



def total():
    # cosmetic price
    global soap_value,facecream_value,faceWash_value,Hairspray_value,Gel_value,bodyLotion_value
    soap_value = int(bathsoapEntry.get())*20
    facecream_value = int(FacecreamEntry.get())*90
    faceWash_value = int(FaceWashEntry.get())*75
    Hairspray_value = int(HairSprayEntry.get())*105
    Gel_value = int(HairGelEntry.get())*40
    bodyLotion_value = int(BodyLotionEntry.get())*50

    totalcosmeticprice = soap_value+facecream_value+faceWash_value+Gel_value+ Hairspray_value + bodyLotion_value
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,f'{totalcosmeticprice} Rs')
    cosmaticTax = totalcosmeticprice*0.03
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,f'{cosmaticTax} Rs')

    global rice_value,daal_value,Suger_value,Oil_value,brown_vlaue,Tea_value
    #grocery price  calculation
    rice_value = int(RiceEntry.get())*120
    daal_value = int(DaalEntry.get())*130
    Suger_value = int(SugerEntry.get())*45
    Oil_value = int(OilEntry.get())*180
    brown_vlaue = int(BrownEntry.get())*70
    Tea_value = int(TeaEntry.get())*20

    totalgroceryprice = rice_value+daal_value+Suger_value+Oil_value+brown_vlaue+Tea_value
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,f'{totalgroceryprice} Rs')
    groceryTax = totalgroceryprice*0.02
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,f'{groceryTax} Rs')

    # Cold Drinks
    global Maaza_vlaue,Peepsi_value,Sprite_value,Dew_value,Frooti_value,coke_value
    Maaza_vlaue =int( MaazaEntry.get())*50
    Peepsi_value = int(PepsiEntry.get())*70
    Sprite_value = int(SpriteEntry.get())*65
    Dew_value = int(DewEntry.get())*55
    Frooti_value = int(FrootiEntry.get())*80
    coke_value = int(CocacolaEntry.get())*75

    totalColdDrinkprice = Maaza_vlaue+Peepsi_value+Sprite_value+Dew_value+Frooti_value+coke_value
    coldDrinkpriceEntry.delete(0,END)
    coldDrinkpriceEntry.insert(0,f'{totalColdDrinkprice} Rs')
    coldDrinkTax = totalColdDrinkprice*0.03
    coldDrinktaxEntry.delete(0,END)
    coldDrinktaxEntry.insert(0,f'{coldDrinkTax} Rs')

    global totalBill

    totalBill = totalColdDrinkprice + totalcosmeticprice + totalgroceryprice + cosmaticTax+ coldDrinkTax + groceryTax








# User Interface Part 

root = Tk()
root.title('Retail Billing System')
root.geometry('1270x686')
root.iconbitmap('icon.ico.jpg')
# heading 
headingLabel = Label(root,text='Retail Billing System',font=('times new roman',30,'bold'),bg='gray20',fg='green',bd=12,relief=GROOVE)
headingLabel.pack(fill=X,pady=10)

# customer details frame
customer_detail_frame = LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),fg='green',bd=8,relief=GROOVE,bg='gray20')
customer_detail_frame.pack(fill=X)

nameLabel= Label(customer_detail_frame,text='Name',font=('time new roman',15,'bold'),bg='gray20',fg='white')
nameLabel.grid(row=0,column=0,padx=20,pady=2)
nameEntry = Entry(customer_detail_frame,font=('arial',15),bd=2,width=18)
nameEntry.grid(row=0,column=1,padx=8)


phoneLabel= Label(customer_detail_frame,text='phone Number',font=('time new roman',15,'bold'),bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)
phoneEntry = Entry(customer_detail_frame,font=('arial',15),bd=2,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

BillnumberLabel= Label(customer_detail_frame,text='Bill Number',font=('time new roman',15,'bold'),bg='gray20',fg='white')
BillnumberLabel.grid(row=0,column=4,padx=20,pady=2)
BillEntry = Entry(customer_detail_frame,font=('arial',15),bd=2,width=18)
BillEntry.grid(row=0,column=5,padx=8)

searchButton = Button(customer_detail_frame,text="Search",font=('arial',12,'bold'),bd=3,width=16,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)


# Product Frame
productFrame = Frame(root)
productFrame.pack(pady=10,fill=X)

cosmeticsFrame = LabelFrame(productFrame,text='Cosmetics',font=('times new roman',15,'bold'),bg='gray20',fg='green',bd=12,relief=GROOVE)
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel = Label(cosmeticsFrame,text='Bath Soap',font=('time new roman',15,'bold'),bg='gray20',fg='white')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
bathsoapEntry = Entry(cosmeticsFrame,font=('time new roman',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)


FacecreamLabel = Label(cosmeticsFrame,text='Face cream',font=('time new roman',15,'bold'),bg='gray20',fg='white')
FacecreamLabel.grid(row=1,column=0,pady=9,sticky='w')
FacecreamEntry = Entry(cosmeticsFrame,font=('time new roman',15,'bold'),width=10,bd=5)
FacecreamEntry.grid(row=1,column=1,pady=9,padx=10)
FacecreamEntry.insert(0,0)


FaceWashLabel = Label(cosmeticsFrame,text='Face Wash',font=('time new roman',15,'bold'),bg='gray20',fg='white')
FaceWashLabel.grid(row=2,column=0,pady=9,sticky='w')
FaceWashEntry = Entry(cosmeticsFrame,font=('time new roman',15,'bold'),width=10,bd=5)
FaceWashEntry.grid(row=2,column=1,pady=9,padx=10) 
FaceWashEntry.insert(0,0)

HairSprayLabel = Label(cosmeticsFrame,text=' Hair Spray',font=('time new roman',15,'bold'),bg='gray20',fg='white')
HairSprayLabel.grid(row=3,column=0,pady=9,sticky='w')
HairSprayEntry = Entry(cosmeticsFrame,font=('time new roman',15,'bold'),width=10,bd=5)
HairSprayEntry.grid(row=3,column=1,pady=9,padx=10) 
HairSprayEntry.insert(0,0)

HairGelLabel = Label(cosmeticsFrame,text='Hair Gel ',font=('time new roman',15,'bold'),bg='gray20',fg='white')
HairGelLabel.grid(row=4,column=0,pady=9,sticky='w')
HairGelEntry = Entry(cosmeticsFrame,font=('time new roman',15,'bold'),width=10,bd=5)
HairGelEntry.grid(row=4,column=1,pady=9,padx=10)
HairGelEntry.insert(0,0) 

BodyLotionLabel = Label(cosmeticsFrame,text='Face Wash',font=('time new roman',15,'bold'),bg='gray20',fg='white')
BodyLotionLabel.grid(row=5,column=0,pady=9,sticky='w')
BodyLotionEntry = Entry(cosmeticsFrame,font=('time new roman',15,'bold'),width=10,bd=5)
BodyLotionEntry.grid(row=5,column=1,pady=9,padx=10) 
BodyLotionEntry.insert(0,0)


#Grosary Frame
groceryFrame = LabelFrame(productFrame,text='Grocery',font=('times new roman',15,'bold'),bg='gray20',fg='green',bd=12,relief=GROOVE)
groceryFrame.grid(row=0,column=1)

RiceLabel = Label(groceryFrame,text='Rice',font=('time new roman',15,'bold'),bg='gray20',fg='white')
RiceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
RiceEntry = Entry(groceryFrame,font=('time new roman',15,'bold'),width=10,bd=5)
RiceEntry.grid(row=0,column=1,pady=9,padx=10)
RiceEntry.insert(0,0)

OilLabel = Label(groceryFrame,text='Oil',font=('time new roman',15,'bold'),bg='gray20',fg='white')
OilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
OilEntry = Entry(groceryFrame,font=('time new roman',15,'bold'),width=10,bd=5)
OilEntry.grid(row=1,column=1,pady=9,padx=10)
OilEntry.insert(0,0)

DaalLabel = Label(groceryFrame,text='Daal',font=('time new roman',15,'bold'),bg='gray20',fg='white')
DaalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
DaalEntry = Entry(groceryFrame,font=('time new roman',15,'bold'),width=10,bd=5)
DaalEntry.grid(row=2,column=1,pady=9,padx=10)
DaalEntry.insert(0,0)

BrownriceLabel = Label(groceryFrame,text='Brown rice',font=('time new roman',15,'bold'),bg='gray20',fg='white')
BrownriceLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
BrownEntry = Entry(groceryFrame,font=('time new roman',15,'bold'),width=10,bd=5)
BrownEntry.grid(row=3,column=1,pady=9,padx=10)
BrownEntry.insert(0,0)

SugerLabel = Label(groceryFrame,text='Suger',font=('time new roman',15,'bold'),bg='gray20',fg='white')
SugerLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
SugerEntry = Entry(groceryFrame,font=('time new roman',15,'bold'),width=10,bd=5)
SugerEntry.grid(row=4,column=1,pady=9,padx=10)
SugerEntry.insert(0,0)

TeaLabel = Label(groceryFrame,text='Tea',font=('time new roman',15,'bold'),bg='gray20',fg='white')
TeaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
TeaEntry = Entry(groceryFrame,font=('time new roman',15,'bold'),width=10,bd=5)
TeaEntry.grid(row=5,column=1,pady=9,padx=10)
TeaEntry.insert(0,0)

# cold Drinks Frame
coldDrinkFrame = LabelFrame(productFrame,text='Cold Drink',font=('times new roman',15,'bold'),bg='gray20',fg='green',bd=12,relief=GROOVE)
coldDrinkFrame.grid(row=0,column=2)

CocacolaLabel = Label(coldDrinkFrame,text='Coke',font=('time new roman',15,'bold'),bg='gray20',fg='white')
CocacolaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
CocacolaEntry = Entry(coldDrinkFrame,font=('time new roman',15,'bold'),width=10,bd=5)
CocacolaEntry.grid(row=0,column=1,pady=9,padx=10)
CocacolaEntry.insert(0,0)

FrootiLabel = Label(coldDrinkFrame,text='Frooti',font=('time new roman',15,'bold'),bg='gray20',fg='white')
FrootiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
FrootiEntry = Entry(coldDrinkFrame,font=('time new roman',15,'bold'),width=10,bd=5)
FrootiEntry.grid(row=1,column=1,pady=9,padx=10)
FrootiEntry.insert(0,0)

DewLabel = Label(coldDrinkFrame,text='Dew',font=('time new roman',15,'bold'),bg='gray20',fg='white')
DewLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
DewEntry = Entry(coldDrinkFrame,font=('time new roman',15,'bold'),width=10,bd=5)
DewEntry.grid(row=2,column=1,pady=9,padx=10)
DewEntry.insert(0,0)

SpriteLabel = Label(coldDrinkFrame,text='Sprite',font=('time new roman',15,'bold'),bg='gray20',fg='white')
SpriteLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
SpriteEntry = Entry(coldDrinkFrame,font=('time new roman',15,'bold'),width=10,bd=5)
SpriteEntry.grid(row=3,column=1,pady=9,padx=10)
SpriteEntry.insert(0,0)

PepsiLabel = Label(coldDrinkFrame,text='Pepsi',font=('time new roman',15,'bold'),bg='gray20',fg='white')
PepsiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
PepsiEntry = Entry(coldDrinkFrame,font=('time new roman',15,'bold'),width=10,bd=5)
PepsiEntry.grid(row=4,column=1,pady=9,padx=10)
PepsiEntry.insert(0,0)

MaazaLabel = Label(coldDrinkFrame,text='Maaza',font=('time new roman',15,'bold'),bg='gray20',fg='white')
MaazaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
MaazaEntry = Entry(coldDrinkFrame,font=('time new roman',15,'bold'),width=10,bd=5)
MaazaEntry.grid(row=5,column=1,pady=9,padx=10)
MaazaEntry.insert(0,0)


#billing Area
billingFrame = Frame(productFrame)
billingFrame.grid(row=0,column=3,padx=10)

billingLabel = Label(billingFrame,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billingLabel.pack(fill=X)

scrollbar = Scrollbar(billingFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea = Text(billingFrame,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()

scrollbar.config(command=textarea.yview)



# product manue
billmenuFrame = LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),bg='gray20',fg='green',bd=12,relief=GROOVE)
billmenuFrame.pack(fill=X)

cosmeticpriceLabel = Label(billmenuFrame,text='Cosmetic Price',font=('time new roman',15,'bold'),bg='gray20',fg='white')
cosmeticpriceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
cosmeticpriceEntry = Entry(billmenuFrame,font=('time new roman',15,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=9,padx=10)

grocerypriceLabel = Label(billmenuFrame,text='Grocery Price',font=('time new roman',15,'bold'),bg='gray20',fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
grocerypriceEntry = Entry(billmenuFrame,font=('time new roman',15,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=9,padx=10)

coldDrinkpriceLabel = Label(billmenuFrame,text='Cold Drink Price',font=('time new roman',15,'bold'),bg='gray20',fg='white')
coldDrinkpriceLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
coldDrinkpriceEntry = Entry(billmenuFrame,font=('time new roman',15,'bold'),width=10,bd=5)
coldDrinkpriceEntry.grid(row=2,column=1,pady=9,padx=10)

# tax area 

cosmetictaxLabel = Label(billmenuFrame,text='Cosmetic Tax',font=('time new roman',15,'bold'),bg='gray20',fg='white')
cosmetictaxLabel.grid(row=0,column=2,pady=9,padx=10,sticky='w')
cosmetictaxEntry = Entry(billmenuFrame,font=('time new roman',15,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=9,padx=10)

grocerytaxLabel = Label(billmenuFrame,text='Grocery Tax',font=('time new roman',15,'bold'),bg='gray20',fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=9,padx=10,sticky='w')
grocerytaxEntry = Entry(billmenuFrame,font=('time new roman',15,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=9,padx=10)

coldDrinktaxLabel = Label(billmenuFrame,text='Cold Drink Tax',font=('time new roman',15,'bold'),bg='gray20',fg='white')
coldDrinktaxLabel.grid(row=2,column=2,pady=9,padx=10,sticky='w')
coldDrinktaxEntry = Entry(billmenuFrame,font=('time new roman',15,'bold'),width=10,bd=5)
coldDrinktaxEntry.grid(row=2,column=3,pady=9,padx=10)


buttonFrame = Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton= Button(buttonFrame,text='Total',font=('areal',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)


# Bill button


billButton= Button(buttonFrame,text='Bill',font=('areal',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

#email button


emailButton= Button(buttonFrame,text='Email',font=('areal',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=5)

#print button
printButton= Button(buttonFrame,text='Print',font=('areal',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=5)

#clear Button
clearButton= Button(buttonFrame,text='Clear',font=('areal',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)

analyzeButton= Button(buttonFrame,text='Analyze',font=('areal',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=analyze_graph)
analyzeButton.grid(row=0,column=5,pady=20,padx=5)




root.mainloop()