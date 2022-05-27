# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
# Student name: Sachka Herath
# UOW Student:18098138
# IIT student:2019712
# Date:03/12/2020

print("--------------------------------------------------------------")
#p=pass
#d=defer
#f=fail
#creating a user defined function
def find_process():
    if (p==120):
        print("Progress")
    elif(p==100):
        print("progress(module trailer)")
    elif(f==80 or f==100 or f==120):
        print("Exclude")
    elif (p==80 or p==60 or p==40 or pI==20 or p==0):
        print("Do not Progress-module retriever")
    else:
        print("An Error occurred,Please try again.THANK YOU !!!")
##---------------------------------------------------------------------##

p=(input("Please enter your credits at pass:"))##p=pass (input as a string)
if (p.isdigit()):#checking whether that the input ia an integer
    p=int(p)#convert string in to integer
    if (p == 0 or p == 20 or p==40 or p==60 or p==80 or p==100 or p==120):

        d=(input("Please enter your credit at defer:"))##d=defer
        if(d.isdigit()):#checking whether that the input ia an integer
            d=int(d)#convert string in to integer
            if(d == 0 or d == 20 or d==40 or d==60 or d==80 or d==100 or d==120):
                
                f=(input("Please enter your credit at fail:"))##f=fail
                if(f.isdigit()):#checking whether that the input ia an integer
                    f=int(f)#convert string in to integer
                    if(f == 0 or f == 20 or f==40 or f==60 or f==80 or f==100 or f==120):

                        if((p+d+f)==120):#This is to check if the total of the 3 inputs are 120
                                
                            find_process()#calling user defined function
                                    
                        else:
                            print("Total incorrect")
      
                    else:
                        print("out of range")
                            
                else:
                    print("Integer required")
                        
            else:
                print("out of range")
                    
        else:
            print("Integer required")  
            
    else:
        print("out of range")

else:
    print("Integer required")
    
print("--------------------------------------------------------------")
           
          







    
