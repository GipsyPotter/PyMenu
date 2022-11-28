import os
from pynput import keyboard
from pynput.keyboard import Key


def update_cur(math):
    global cur
    max = 4
    if math == "+":
        if cur < max - 1:
            cur += 1
        else:
            cur = 0
    elif math == "-":
        if cur > 0:
            cur -= 1
        else:
            cur = max - 1


def chose(index):
    global chosed
    if index == 0:
        print("Chose 1")
    elif index == 1:
        print("Chose 2")
    elif index == 2:
        print("Chose 3")
    elif index == 3:
        print("Chose 4")
    chosed = True


def on_key_release(key):
    if key == Key.up:
        update_cur("-")

    elif key == Key.down:
        update_cur("+")
    elif key == Key.enter:
        chose(cur)
    return False


def export_menu(opt: list, cur: int):
    for i in range(len(opt)):
        if i == cur:
            print(">>", opt[i])
        else:
            print("  ", opt[i])


def clear():
    os.system("cls")


if __name__ == '__main__':
    opt = ["opt 1", "opt 2", "opt 3", "opt 4"]
    cur = 0
    chosed = False
    while True:
        if chosed:
            break
        clear()
        export_menu(opt, cur)
        with keyboard.Listener(on_release=on_key_release) as listener:
            listener.join()
