# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
# Student name: Sachka Herath
# UOW Student:18098138
# IIT student:2019712
# Date:02/12/2020

print("---------------------------------------------------------")
#p=pass
#d=defer
#f=fail
#inputs as integers
p=int(input("Please enter your credits at pass:"))#p=pass
d=int(input("Please enter your credit at defer:"))#d=defer
f=int(input("Please enter your credit at fail:"))#f=fail

#condition set()
if (p==120):
    print("Progress")
elif(p==100):
    print("progress(module trailer)")
elif(f==80 or f==100 or f==120):
    print("Exclude")
elif (p==80 or p==60 or p==40 or p==20 or p==0):
    print("Do not Progress-module retriever")
else:
    print("An Error occurred,Please try again.THANK YOU !!!")
print("---------------------------------------------------------")
