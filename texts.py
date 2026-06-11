import time

def slow_print(text):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(0.05)
    print()
    time.sleep(0.1)

def intro_sequence():
    slow_print("You wake up like any other day, it's dark even in the morning.")
    slow_print("The Corrupted King Averitt has started sending his dark forces to wreak havoc upon the world.")
    slow_print("You may be the only one brave enough to stop him.")
    slow_print("What will you do?")

intro_sequence()