import random
from rich import print

agains = 0
friendly = ["   ৹ Okay!", "   ৹ Sure! ( •̀ ω •́ )✧", "   ৹ Of course! (´▽`ʃ♡ƪ)", "   ৹ No problem! (＾▽＾)", "   ৹ You got it! (～￣▽￣)～"]
slightly_annoyed = ["   ৹ Again? :]", "   ৹ You really want to do this again? (´。＿。｀)", "   ৹ Fine, but this is the last time! ( ͡° ͜ʖ ͡°)", "   ৹ You are testing my patience! ^^", "   ৹ I'll do it, but don't expect me to be happy about it! :) "]
angry = ["   ৹ Seriously? (ಠ_ಠ)", "   ৹ I am getting tired of this! ", "   ৹ I am doing it for the money!", "   ৹ Aaaghh!" ]
enough = ["   ৹ I have had enough! (╯°□°）╯︵ ┻━┻", "   ৹ I am done with this! (╯°□°）╯︵ ┻━┻", "   ৹ No more! (╯°□°）╯︵ ┻━┻","   ৹ I am not going to do this again! (╯°□°）╯︵ ┻━┻", "   ৹ I am done with you! (ノಠ益ಠ)ノ彡┻━┻"]
not_possible = ["   ৹ Maybe in another universe", "   ৹ This is not possible", "   ৹ I don't think so", "   ৹ No", "   ৹ No way"]
too_much = ["   ৹ I am saving your life", "   ৹ I thought you were a rational person, GET OUT!", "   ৹ No, that's too much", "   ৹ No, this is not good for you", "   ৹ I am not going to do that", "   ৹ really? anyway, I am not going to do that"]
print("""[bold white]                 Welcome to [/bold white]
[italic yellow]              the Hello World[/italic yellow]
 [bold white]                 Printer![/bold white] 
    """)
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
            print("[italic white]   ৹ Bye :D[/italic white]")
            return False
        else:
            print("[purple]   ৹ Invalid input. Please enter 'y' or 'n'. [/purple]")
            return agains_fun(input("   ৹ Do you want to print more? (y/n) ")) 

while True:
    times = input("   ৹ How many times do you want to print it? ")
    if not times.isdigit():
        print("[purple]   ৹ Invalid input. Please enter a number between 1 and 100.[/purple]")
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
            print("[italic blue]   ৹ Hello, World![/italic blue]")
        do = input("   ৹ Do you want to print more? (y/n) ")
        if agains_fun(do) == False:
            break  
    else: 
        print("[purple]   ৹ Invalid input. Please enter a number between 1 and 100.[/purple]")


                
 