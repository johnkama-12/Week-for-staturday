#learning about if statement
print("Welcome to Saturday")
print( 5 > 3)
print( 5 < 3)
print(5==3)
print(5==5)
print(5 != 3)

print("apple" < "banana")
print("apple" > "banana")

age = 20
is_girl=True
raining=False
score=49

if  age >= 20 and is_girl:
    print("Na fo yan am")

if age <= 19 and is_girl:
    print("Na fo yan am")
    
if  age >= 20 or is_girl:
    print("Na fo yan am")

if  age <=  19 or is_girl:
    print("Na fo yan am")

if not raining:
    print("go outside")
    
#learning about if statement

if score >=50:
    print("you pass")
    
#learning about else statement
if score >= 50:
    print("pass")
    
else:
    print("fail")
    
#learning about elif statement

if score >= 90:
    print("A")
    
elif score >=80 or score >= 89:
    print("B")   
 
elif score >=70 or score >=70:
    print('C')
     
elif score >=50 or score >=60:
    print("D")
      
else:
    
    print("F")

#learing about nested if

if score >= 90:
    print("A")
    
    if score == 91:
        print("u get 91")
        
    elif score == 92:
         print("u get 92")
    
    elif score == 93:
         print("u get 93")
         
    elif score == 94:
         print("u get 94")
         
    elif score == 95:
         print("u get 95") 
    else:
        print("u get", score)
elif score >=80 or score >= 89:
    print("B")
    if score >= 81:
         print("u get 81")
    
    elif score >=82:
        print("u get 82")
    
    elif score >=83:
        print("u get 83")
        
    elif score >=84:
        print("u get 84")
    
    elif score >=85:
        print("u get 85")
        
    else:
        print("u get", score)
 
elif score >=70 or score >=70:
    print('C')
    
    if score >= 71:
        print("u get 71")
        
    elif score >= 72:
        print("u get 72")
        
    elif score >=73:
        print("u get 73")
        
    elif score >=74:
        print("u get 73")
    
    elif score >=75:
        print("u get 75")
    else:
        print("u get", score)
elif score >=50 or score >=60:
    print("D")
      
else: 
    print("F")