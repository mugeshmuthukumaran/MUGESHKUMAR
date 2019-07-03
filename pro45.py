#mugi
n=input()
if n==n[::-1]:
    print("yes")
else:
    vin=n.strip("0")
    
    if vin==vin[::-1]:
        print("yes")
    else:
        vin=n.lstrip("0")
        
        if vin==vin[::-1]:
            print("yes")
        else:
            print("no")
