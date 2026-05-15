import time

def slow_print(text):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(0.05)
    print()
    time.sleep(0.1)

def intro_sequence():
    slow_print("This is the intro sequence to the game.")
    slow_print("Proper text and lore will be implemented later")

intro_sequence()