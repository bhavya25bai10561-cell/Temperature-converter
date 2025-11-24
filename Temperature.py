ch=input("Press Y or y if you want to use temperature converter otherwise N or n: ")
while(ch=="Y" or ch=="y"):
    t=input("Press K or k to convert celsius into kelvin, Press C or c to convert fahrenheit into celsius, Press F or f to convert celsius into fahrenheit otherwise press A or a to convert kelvin into celsius: ")
    if(t=="K" or t=="k"):
        Celsius=float(input("Enter temperature in celsius:"))
        Kelvin=(Celsius+273.15)
        print("Your converted temperature is",Kelvin,"K")
    if(t=="C" or t=="c"):
        Fahrenheit=float(input("Enter temperature in fahrenheit:"))
        Celsius=(Fahrenheit-32)*(5/9)
        print("Your converted temperature is",Celsius,"C")
    if(t=="F" or t=="f"):
        Celsius=float(input("Enter temperature in celsius:"))
        Fahrenheit=(Celsius*(9/5))+32
        print("Your converted temperature is",Fahrenheit,"F")
    if(t=="A" or t=="a"):
        Kelvin=float(input("Enter temperature in kelvin:"))
        Celsius=(Kelvin-273.15)
        print("Your converted temperature is",Celsius,"C")
    ch=input("If you want to continue then press Y or y otherwise N or n: ")        
            
            
            