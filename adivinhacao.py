print("Welcome!!")
secret_number = 9
total_attempt = int(input("How many attempts do you want to use?"))
round = 1

while(round <= total_attempt):
    print("SCOREBOARD {} of {}".format(round, total_attempt))
    attempt = int(input("Your number: "))
    hit = attempt == secret_number
    less_than = attempt < secret_number
    greater_than = attempt > secret_number
    if(hit):
        print("Well played, you got it right!!")
        round = total_attempt
    else:
        if(less_than):
            print("Almost there! His attempt was next, it was smaller than our number.")
        elif(greater_than):
            print("Almost there! Your attempt was next, it was bigger than our number.")
    round = round + 1

