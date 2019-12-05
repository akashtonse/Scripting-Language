def kel_to_cel():
    k=int(input("Enter temperature in kelvin: "))
    print('Temperature in Celcius is:{}'.format(k-273.15),'C')
    lst.append((k-273.15,k))

def cel_to_kel():
    c = int(input("Enter temperature in celcius: "))
    print('Temperature in Kelvin is:{}'.format(c + 275.15),'K')
    lst.append((c, c+273.15))

cont=True
lst=[]
while cont:
    a=int(input("\nEnter 1 to convert kelvin to celcius\n"
                "Enter 2 to convert celcius to kelvin\n"
                'Enter 3 to view history\n'
                "Enter 4 exit\n"
                ))
    if(a==1):
        kel_to_cel()
    elif(a==2):
        cel_to_kel()
    elif(a==3):
        print('[(celcius,kelvin)]')
        lst.sort()
        print(lst)
    elif(a==4):
        cont=False

