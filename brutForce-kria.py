from colorama import init, Fore
init()

print(Fore.BLUE)  # Mavi renk
target = int(input("Enter Target: "))
for i in range(99999,1000000):
    print(i)
    if i == target:
        print(Fore.GREEN + "Password found", i)
        break