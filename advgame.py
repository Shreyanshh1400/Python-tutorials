name=input("Enter your name")
print(f"Hello {name.title()}, welcome to the game")
playing=input("Do you want to play?")
if playing.lower()!="yes":
    quit()
print("Game start")
answer=int(input("You see two paths before you: one leading deeper into the fog (PATH 1), and another, barely visible, seemingly leading towards a faint glow (PATH 2)."))
if answer=="1":
    answer=input("You stumble forward, the fog growing thicker with every step. The whispers intensify, sounding like ancient, forgotten words. Suddenly, you hear a low growl directly ahead. You can either:1) RUN BACK in the direction you came. 2) STAND YOUR GROUND and try to see what's there.")
    if answer=="1":
        print("You turn and flee, tripping over roots and branches. The growl fades, but you find yourself back in the initial clearing, disoriented and no closer to an exit. You can now only take PATH 2.")
    else:
        print("A shadowy beast with glowing red eyes emerges from the fog. It lunges. You try to dodge, but it's too fast.GAME OVER. You were overwhelmed.")
elif answer=="2":
    print("You cautiously make your way towards the glow. The fog thins slightly here, and you notice the glow is coming from a small, dilapidated hut. The whispers are still present, but seem to originate from the hut. You see a flickering light inside.")
    answer=input("You are now at the hut. You can: 1)ENTER THE HUT to investigate. 2)PEEK THROUGH THE WINDOW first.")
    if answer=="1":
        answer=input("You push open the creaky door. Inside, a single flickering candle illuminates a dusty table. On the table, you see an old, leather-bound book. As you approach, the whispers grow louder, seeming to emanate from the book itself. You can: 1)OPEN THE BOOK. 2)LEAVE THE BOOK ALONE and look for another way out.")
        if answer=="1":
            print("As you open the book, a blinding light erupts from its pages, engulfing you. The whispers coalesce into a single, booming voice: You have awakened the ancient knowledge! The path is now clear! The light fades, and you find yourself standing outside the woods, the sun shining brightly. You have escaped!YOU WIN!")
        else:
            print("You decide the book is too risky. You search the rest of the hut but find nothing else of interest. Disappointed, you leave the hut and try to retrace your steps, but the fog has rolled back in, completely disorienting you.GAME OVER. You are lost forever in the Whispering Woods.")
    else:
        answer=input("You peer through a cracked pane of glass. You see an empty, dusty hut with a single flickering candle on a table. No one is inside. You realize the whispers are coming from behind the hut. You can now:1)GO AROUND THE HUT to investigate the source of the whispers.2)ENTER THE HUT now that you know it's empty.")
        if answer=="1":
            answer=input("You cautiously circle the hut. Behind it, you find a small, hidden cave entrance. The whispers are strongest here. You can:1) ENTER THE CAVE. 2)TURN BACK and go back to the hut.")
            if answer=="1":
                print("You step into the darkness. The whispers become a chorus, and you feel a strange pull. You stumble forward and suddenly fall through a hidden trapdoor. You land softly in a brightly lit, open field. The woods are behind you, and a clear path leads to a distant village. You have escaped!YOU WIN!")
            else:
                print("You decide the cave is too dangerous. You return to the front of the hut, but the fog has grown thick again, and you can no longer see the path you took to get there.GAME OVER. You are lost forever in the Whispering Woods.")
        else:
            answer=input("You enter the hut, now knowing it's empty. You see the old, leather-bound book on the table, just as you saw from the window. The whispers are still present, seeming to emanate from the book itself. You can:1)OPEN THE BOOK.2)LEAVE THE BOOK ALONE and look for another way out.")
            if answer=="1":
                print(r"As you open the book, a blinding light erupts from its pages, engulfing you. The whispers coalesce into a single, booming voice: You have awakened the ancient knowledge! The path is now clear! The light fades, and you find yourself standing outside the woods, the sun shining brightly.You have escaped,YOU WIN!")
            else:
                print("You decide the book is too risky. You search the rest of the hut but find nothing else of interest. Disappointed, you leave the hut and try to retrace your steps, but the fog has rolled back in, completely disorienting you.GAME OVER. You are lost forever in the Whispering Woods.")