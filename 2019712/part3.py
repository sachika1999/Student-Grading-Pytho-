# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
# Student name: Sachka Herath
# UOW Student:18098138
# IIT student:2019712
# Date:05/12/2020

def find_progress_q2(result):
#p=pass
#d=defer
#f=fail
    p=(input("Please enter your credits at pass:"))##p=pass
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
                                
                                if (p==120):
                                    result[0]=result[0]+1
                                    print("Progress")
                                elif(p==100):
                                    result[1]=result[1]+1
                                    print("progress(module trailer)")
                                elif(f==80 or f==100 or f==120):
                                    result[3]=result[3]+1
                                    print("Exclude")
                                elif (p==80 or p==60 or p==40 or p==20 or p==0):
                                    result[2]=result[2]+1
                                    print("Do not Progress-module retriever")
                                else:
                                    print("An Error occurred,Please try again.THANK YOU !!!")
                                    
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



print("--------------------------------------------------------")
print("Staff Version with Histogram\n")
result_count=[0,0,0,0]#creating a list
print()
find_progress_q2(result_count)#calling user defined function(q2)
is_y=True
#when user input y isTrus set to true, otherwise false
#while loop run untill user input q
while(is_y):
    print("Would you like to enter another set of data?")
    condition=input("Enter 'y' for yes or 'q' to quit and view results: ")
    print()
    if(condition=='y'):
        is_y=True
        find_progress_q2(result_count)

    elif(condition=='q'):
        is_y=False
        print("Exits loop")
        print("------------------------------")
        print("Horizontal Histogram")

        a=["Progress","Trailer","Retriever","Excluded"]

        for i in range(0,4):
            print(a[i],'',end='')
            print(result_count[i],"\t: ",end="")
            print("*"*result_count[i])

        print()
        print(sum(result_count)," outcomes in total")


    else:
        print("wrong input")

   
