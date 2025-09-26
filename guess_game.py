# guess the number game

def guess():
    chance = 3
    x = 0
    
    set = {"1","2","3","4","5",
           "6","7","8","9","10"}
    lst = list(set)
    liist = lst[0]
    
    while x < chance:
           x +=1
           num = input("enter a number: ")
           if num == liist:
                  print("you win")
                  return
           else:
                  print("try again")
    print(f"you lose !the number is {liist}")
      
      
guess()
    
    

 
       

    
    
    



