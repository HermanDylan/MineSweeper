for row in " 1 2 3 4 ":
    print(row, end=" ")
print()
for row in range(1,5):
    print(" - ", end=" ")
for col in range(1,5):
    print()
    for col in range(1,5):
        print(" | ", end=" ")
print()
for row in range(1,5):
    print(" - ", end=" ")
    
heart = 5 
print("Commands: c=clear mine, m=mark mine, i=introduction, q=quit")
command = str(input(f"{playerName}, pleaese input your next action: "))
if command == c or m or i or q :
    print()
else:
    print("Invalid choice, please input either 'c', 'm', 'i' or 'q'.")
    command = str(input(f"{playerName}, please inpput your next action: "))