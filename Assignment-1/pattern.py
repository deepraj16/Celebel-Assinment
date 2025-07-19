def upper_traingle(n): 
    for i in range(n): 
        for j in range(i): 
            print("*",end="")
        print() 

def lower_traingle(n): 
    for i in range(n): 
        for j in range(i,n): 
            print("*",end="")
        print()              

def lower_pyramid(n): 
     for i in range(n): 
        for j in range(i,n): 
            print(" ",end="")
        for k in range(i): 
            print("*",end="")
        for k in range(i-1): 
            print("*",end="")    
        print()  

def upper_pyramid(n): 
     for i in range(n,0,-1): 
        for j in range(i,n): 
            print(" ",end="")
        for k in range(i): 
            print("*",end="")
        for k in range(i-1): 
            print("*",end="")    
        print()

    

try :
    n=int(input("Enter the height of pyramid : "))
    if n > 30:
        raise ValueError("Pyramid height too large. Please enter a value ≤ 30.")
    if n < 1:
        raise ValueError("Pyramid height must be a positive integer.")
    print("Upper triangular : ") 
    upper_traingle(n)
    print()
    print("Lower triangular : ")
    print()
    lower_traingle(n)
    print()
    print("The pyramid: ")
    lower_pyramid(n)
    print() 
    print("down pyramid") 
    upper_pyramid(n)

except ValueError as e:
    print("Error:", e)    
except : 
    print("Plese enter only  integer") 
