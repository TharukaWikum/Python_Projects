kp = int(input("Enter the keyboard price:-"))
mp = int(input("Enter the mouse price:-"))
top = int(0)
alls = int(0)

for i in range(0, 50):
        kq = int(input("Enter the selled keyboard Quentity:-"))
        mq = int(input("Enter the selled mouse Quentity:-"))

        tkp = kp * kq 
        tmp = mp * mq

        if kq >= 50:
            tskp = tkp * 0.2
            top = top + tkp - tskp
        else:
            top = top + tkp

        if mq >= 50:
            tsmp = tmp * 0.1
            top = top + tkp - tsmp
        else:
            top = top + tkp
        
        if (kq >=50 or mq >=50):
            print("Seller commision = ",tsmp + tskp)
        else:
            print("No commision available! Try hard again")
        print(top)
        a = input("Are there any seller available please type yes else type no:-")
        if a== "no":
            print("Owner Income = ", top)
        break 


    
