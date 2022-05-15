def Karatsuba(num1, num2):
    if len(str(num1)) == 1 or len(str(num2)) == 1:
        return num1*num2

        #When one of the terms has only one digit it isn't possible to perform the Karatsuba algorithm, so the result
        #is calculated directly.

    if len(str(num1))//2 != 0:
        a = int(str(num1)[0])
        b = int(str(num1)[1:int(len(str(num1)))])
        c = int(str(num2)[0])
        d = int(str(num2)[1:int(len(str(num2)))])

        #When the numbers have odd-digits a and c are chosen as single digit numbers and b and d end up having
        #n-1 digits.
    else:
        a = int(str(num1)[0:int(len(str(num1))/2)])
        b = int(str(num1)[int(len(str(num1))/2):int(len(str(num1)))])
        c = int(str(num2)[0:int(len(str(num2))/2)])
        d = int(str(num2)[int(len(str(num2))/2):int(len(str(num2)))])

        #If the inputs have an even number of digits a, b, c and d end up as numbers of n/2 digits. 
    if len(str(a)) != 1:
        ac = Karatsuba(a, c)
        bd = Karatsuba(b, d)
        abcd = Karatsuba(a+b, c+d)-ac-bd
        return 10**(2*len(str(b)))*ac+10**(2*len(str(b))/2)*abcd+bd

        #The distinct terms for the algorithm are calculated recursively and the result of the multiplication
        #is returned.
    else:
        if len(str(b)) > len(str(a)):
            bd = Karatsuba(b, d)
            abcd = Karatsuba(a+b, c+d)-a*c-bd
            return 10**(2*len(str(b)))*a*c+10**(2*len(str(b))/2)*abcd+bd 

            #b is chosen to be higher of higher length than a when multiplying odd digit numbers. Same with c and d
            #In that case it's necessary to calculate through Karatsuba specifically the terms bd and (a+b)(c+d),
            #since they will involve multiplications of higher digit numbers.

        return 10**(2*len(str(b)))*a*c+10**(2*len(str(b))/2)*((a+b)*(c+d)-a*c-b*d)+b*d 
        
        #Multiplication of single digits is reached at this stage, which doesn't require recursions.
