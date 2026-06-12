import random
from rich import print

agains = 0
friendly = ["Okay!", "Sure! ( •̀ ω •́ )✧", "Of course! (´▽`ʃ♡ƪ)", "No problem! (＾▽＾)", "You got it! (～￣▽￣)～"]
slightly_annoyed = ["Again? :]", "You really want to do this again? (´。＿。｀)", "Fine, but this is the last time! ( ͡° ͜ʖ ͡°)", "You are testing my patience! ^^", "I'll do it, but don't expect me to be happy about it! :) "]
angry = ["Seriously? (ಠ_ಠ)", "I am getting tired of this! ", "I am doing it for the money!", "Aaaghh!" ]
enough = ["I have had enough! (╯°□°）╯︵ ┻━┻", "I am done with this! (╯°□°）╯︵ ┻━┻", "No more! (╯°□°）╯︵ ┻━┻","I am not going to do this again! (╯°□°）╯︵ ┻━┻", "I am done with you! (ノಠ益ಠ)ノ彡┻━┻"]
not_possible = ["Maybe in another universe", "This is not possible", "I don't think so", "No", "No way"]
too_much = ["I am saving your life", "I thought you were a rational person, GET OUT!", "No, that's too much", "No, this is not good for you", "I am not going to do that", "really? anyway, I am not going to do that"]

def agains_fun(do):
        do = do.lower().strip()
        if do == "y":
            global agains
            agains += 1
            if agains < 4:
                print(f"[italic white]{random.choice(friendly)}[/italic white]")
                return True
            elif agains < 6:
                print(f"[italic green]{random.choice(slightly_annoyed)}[/italic green]")
                return True
            elif agains < 9:
                print(f"[italic yellow]{random.choice(angry)}[/italic yellow]")
                return True
            else:
                print(f"[bold red]{random.choice(enough)}[/bold red]")
                return False
            
        elif do == "n":
            print("[bold blue]Bye :D[/bold blue]")
            return False
        else:
            print("[purple] Invalid input. Please enter 'y' or 'n'. [/purple]")
            return agains_fun(input("Do you want to print more? (y/n) ")) 

while True:
    times = input("How many times do you want to print? ")
    if not times.isdigit():
        print("[purple] Invalid input. Please enter a number between 1 and 100.[/purple]")
        continue
    times = int(times)
    if times < 1 : 
        print(random.choice(not_possible))
        break
    elif times > 100:
        print(random.choice(too_much))
        break
    elif 1 <= times <= 100: 
        for t in range(times): 
            print("[bold yellow] Hello World![/bold yellow]")
        do = input("Do you want to print more? (y/n) ")
        if agains_fun(do) == False:
            break  
    else: 
        print("[purple] Invalid input. Please enter a number between 1 and 100.[/purple]")


                
 