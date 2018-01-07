n = int(input("Enter N : "))
n50 = 0
n20 = 0
n10= 0
while (n50 * 50) < n :
    n20 = 0
    while (n50*50 + n20*20) < n :

        n10 = (n - n50*50 - n20*20 ) //10
        print("50 : %d - 20 : %d - 10 : %d" % (n50,n20,n10))
        n20 +=1
    n50+=1