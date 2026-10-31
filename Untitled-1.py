
import random

playing = True

while playing:
    print("-----------------------------")
    print("Bazi hads adad shoroo shod!")
    print("-----------------------------")
    
    secret = random.randint(1, 100)
    try_count = 0
    max_tries = 5
    win = False

    while try_count < max_tries:
        remaining = max_tries - try_count
        print("\nTalash", try_count + 1, "az", max_tries)
        print("Jan baghimande:", remaining)
        
        user_input = input("Adad ro vared kon (1 ta 100): ")
        
     
        if user_input.isdigit() == False:
            print("Lotfan faghat adad vared konid! (In try hesab nemishe)")
            continue
            
        guess = int(user_input)
        
        if guess < 1 or guess > 100:
            print("Adad bayad beyn 1 ta 100 bashe! (In try hesab nemishe)")
            continue

        
        try_count = try_count + 1

        if guess == secret:
            win = True
            print("\nTabrik! Dorost hads zadi.")
            
          
            if try_count == 1:
                print("Rotbe: Namoonei")
            elif try_count == 2:
                print("Rotbe: Kheili khoob")
            elif try_count == 3:
                print("Rotbe: Khoob")
            elif try_count == 4:
                print("Rotbe: Ghabool")
            elif try_count == 5:
                print("Rotbe: Ba shans bordi")
            break
            
        else:
            
            ekhtelaf = guess - secret
            if ekhtelaf < 0:
                ekhtelaf = ekhtelaf * -1 
            
          
            if ekhtelaf <= 5:
                print("Kheili nazdiki!")
            elif ekhtelaf <= 15:
                print("Nazdiki vali hanouz fasele dari!")
            else:
                print("Kheili doori!")
                
           
            if guess < secret:
                print("Bozorgtar vared kon")
            else:
                print("Kochektar vared kon")

    if win == False:
        print("\nBakhti! Forsat ha tamoom shod.")
        print("Adad makhfi in bood:", secret)

   
    javab = input("\nDoobare bazi konim? (y/n): ")
    if javab == "n" or javab == "N":
        playing = False
        print("Khodahafez!")