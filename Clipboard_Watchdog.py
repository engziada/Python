from datetime import datetime as dt  
import os
import sys
import pyperclip
from PIL import ImageGrab,Image
from pynput import keyboard
import re
from win32gui import GetWindowText, GetForegroundWindow

saving_path = os.getcwd().replace('/', '\\')
clipboard_list=[]
cursors={}

def on_release(key):
    # print(f"{key}: Pressed")
    if key == keyboard.Key.print_screen:
        if is_image():
            print("Image found in clipboard")
            save_image_file()
        else:
            print("No valid image in clipboard")

    elif type(key) == keyboard._win32.KeyCode:
        try:
            if key.char == '\x03':  # ctrl+c
                # print(GetForegroundWindow())
                # print("Something copied to clipboard!")
                text_copied=pyperclip.paste()
                clipboard_list.append(text_copied)
                pyperclip.copy(clipboard_list[0])

            elif key.char == '\x16':
                win_id=GetForegroundWindow()
                if win_id in cursors.keys():
                    cursors[win_id] = cursors[win_id]+1 if cursors[win_id] < len(clipboard_list)-1 else 0
                else:
                    cursors[win_id]=1 if len(cursors)==0 else 0

                # print(cursors)

                # del clipboard_list[0]
                pyperclip.copy(clipboard_list[cursors[win_id]])

        except IndexError:
            print("My clipboard is empty")

    elif key == keyboard.Key.esc:
        print("Exiting")
        return False


def is_image():
    image = ImageGrab.grabclipboard()
    return isinstance(image, Image.Image)


def save_image_file():
    saving_timestamp = re.sub("[^0-9]", "", str(dt.now()))
    image_path = f'{saving_path}\clipboard_{saving_timestamp}.png'
    image = ImageGrab.grabclipboard()
    image.save(image_path, 'png')
    print(f"Image saved to: {image_path}")


def main():
    if len(sys.argv) > 0 and os.path.exists(sys.argv[0]):
        saving_path = os.path.dirname(sys.argv[0].replace('/','\\'))
    print(f"Saving to path: {saving_path}")

    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
