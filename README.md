# Python Keylogger
Simple keylogger written in Python to capture the keystrokes of a user and output them into raw and readable text files. Work in progress.

<br><br>

# Disclaimer

### __Malicious use of this program is illegal.__

### This program is for educational purposes only and is not to be used for any malicious purposes. This includes downloading it on a computer that you do not own or using it on an unknowing individual.

### Upon downloading this, your antivirus software may detect it as malware and try to quarantine or delete it.

<br><br>

# Usage
Run the keylogger in terminal with ```python3 keyboard.py```. The program will run in the background of all tasks while capturing any keys that are pressed. To stop keylogger, press the ```ESC``` key.

Upon stopping the program, two hidden files will be created if they do not already exists: ```.keyfile.txt``` and ```.rawfile.txt```. These files will have input appended to them if they already exist.

```.keyfile.txt``` is a text file that includes human readable text logged from the keystrokes of the user in the form of characters and digits. A backspace character is also printed to this file so deleted characters can still be seen.

```.rawfile.txt``` is a text file that includes all individual keystrokes that the user has input. This may be difficult to read, but it will show meta key presses (Alt, Ctrl, Cmd, etc.) as well as characters and digits.