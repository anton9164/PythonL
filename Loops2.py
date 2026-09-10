#This uses cycle and input from user, user needs to guess the secret word
secretword = "chupacabra"

while True:
    guess = input("Enter the secret word or you will enter the loop:")
    if guess == secretword:
        break
    else:
        print("Ha Ha, no it's not right word, Try again!")
print("Congrats, you left the loop!")
