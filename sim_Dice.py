# wap to create a function that will
# generate random 3 dice numbers and if all the 3 match are over, then
# display "you win" else display "you lose / try again"
import random
def streak():
    dices = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣']
    selection = random.choices(dices, k=3)
    if selection[0] == selection[1] == selection[2]:
        return selection, "You Win"
    else:
        return selection, "You Lose / Try Again"

ans, msg = streak()
print('Rolling the dices....')
print(" ".join(ans))
print(msg)