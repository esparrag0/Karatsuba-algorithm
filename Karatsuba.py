def Karatsuba(num1, num2):
    if len(str(num1)) == 1 and len(str(num2)) == 1:
        return num1*num2
    if len(str(num1))//2 != 0:
        a = int(str(num1)[0])
        b = int(str(num1)[1:int(len(str(num1)))])
        c = int(str(num2)[0])
        d = int(str(num2)[1:int(len(str(num2)))])
    else:
        a = int(str(num1)[0:int(len(str(num1))/2)])
        b = int(str(num1)[int(len(str(num1))/2):int(len(str(num1)))])
        c = int(str(num2)[0:int(len(str(num2))/2)])
        d = int(str(num2)[int(len(str(num2))/2):int(len(str(num2)))])

    if len(str(a)) != 1:
        ac = Karatsuba(a, c)
        bd = Karatsuba(b, d)
        abcd = Karatsuba(a+b, c+d)-ac-bd
        return 10**(2*len(str(b)))*ac+10**(2*len(str(b))/2)*abcd+bd

        #The distinct terms for the algorithm are calculated recursively and the result of the multiplication
        #is returned.
    else:
        return 10**(2*len(str(b)))*a*c+10**(2*len(str(b))/2)*((a+b)*(c+d)-a*c-b*d)+b*d 
        
        #Multiplication of single digits is reached at this stage, which doesn't require recursions.
