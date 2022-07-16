def factorial(n):
    a=1
    if n < 0:
         print("Sorry, factorial does not exist for negative nbers")
    elif n == 0:
         print("The factorial of 0 is 1")
    
    for i in range(1,n + 1):
         a = a*i
        
        
    print(a)
    
 
    