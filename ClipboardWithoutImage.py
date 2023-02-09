import pyperclip
from pynput import keyboard
from win32gui import GetForegroundWindow

clipboard_list = []
cursors = {}

def on_release(key):
    if type(key) == keyboard._win32.KeyCode:
        try:
            if key.char == '\x03':  # ctrl+c
                text_copied = pyperclip.paste()
                clipboard_list.append(text_copied)
                pyperclip.copy(clipboard_list[0])

            elif key.char == '\x16':
                win_id = GetForegroundWindow()
                if win_id in cursors.keys():
                    cursors[win_id] = cursors[win_id] + \
                        1 if cursors[win_id] < len(clipboard_list)-1 else 0
                else:
                    cursors[win_id] = 1 if len(cursors) == 0 else 0

                pyperclip.copy(clipboard_list[cursors[win_id]])

        except IndexError:
            print("My clipboard is empty")

    elif key == keyboard.Key.esc:
        print("Exiting")
        return False


def main():
    print("Application is running in background,\nYou my press <ESC> anytime to terminate the program,\nWe are watching your clipboard now...")
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()

