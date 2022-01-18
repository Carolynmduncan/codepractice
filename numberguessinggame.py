def run_game():
    art = """
___________.__              _______               ___.                    ________                            .__                   ________                       
\__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
  |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
  |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
  |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
                \/     \/          \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 
"""
    import random
    print(art)
    answer = random.randint(1, 100)
    turns = 0
    
#mode
    choice = input("Do you want to play the guessing game in easy mode or hard mode?\n")
    if choice.lower() == "easy":
        turns = 10
    if choice.lower() == "hard":
        turns = 5
        
#first guess and end of turns
    guess = int(input("Guess a number between 1 and 100.\n"))
    if turns == 0:
        print("You're out of turns.")
        
#compare answer to input
    while turns > 0:
        if guess > answer and turns > 0:
            turns -= 1
            print(f"Too high. You have {turns} turns left. \n")
            guess = int(input("Guess again.\n"))
        if guess < answer and turns > 0:
            turns -= 1
            print(f"Too low. You have {turns} turns left. \n")
            guess = int(input("Guess again.\n"))
        if guess == answer:
            turns = 0
            print(f"You guessed it! The number is {answer}.\n")
            
#restart game
    def restart_game():
        restart = input("Restart the game? Types Y or N. \n")
        if restart.upper() == "Y":
            run_game()
    restart_game()
    
run_game()
