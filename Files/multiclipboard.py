import pyperclip
import shelve
import sys

shelf_file = 'multiclipboard.db'

def save_clipboard(key):
    with shelve.open(shelf_file) as clipboard:
        clipboard[key] = pyperclip.paste()
        print(f"Saved clipboard content to key: {key}")

def load_clipboard(key):
    with shelve.open(shelf_file) as clipboard:
        if key in clipboard:
            pyperclip.copy(clipboard[key])
            print(f"Loaded clipboard content from key: {key}")
        else:
            print(f"No entry found for key: {key}")

def list_clipboard_keys():
    with shelve.open(shelf_file) as clipboard:
        keys = list(clipboard.keys())
        if keys:
            print("Saved keys:")
            for key in keys:
                print(f"- {key}")
        else:
            print("No keys found in the clipboard database.")

def delete_clipboard_key(key):
    with shelve.open(shelf_file) as clipboard:
        if key in clipboard:
            del clipboard[key]
            print(f"Deleted key: {key}")
        else:
            print(f"No entry found for key: {key}")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python multiclipboard.py save <key> - Save clipboard to key")
        print("  python multiclipboard.py load <key> - Load clipboard from key")
        print("  python multiclipboard.py list - List all saved keys")
        print("  python multiclipboard.py delete <key> - Delete the key")
        return

    command = sys.argv[1].lower()

    if command == 'save' and len(sys.argv) == 3:
        save_clipboard(sys.argv[2])
    elif command == 'load' and len(sys.argv) == 3:
        load_clipboard(sys.argv[2])
    elif command == 'list':
        list_clipboard_keys()
    elif command == 'delete' and len(sys.argv) == 3:
        delete_clipboard_key(sys.argv[2])
    else:
        print("Invalid command or arguments.")
        print("Usage:")
        print("  python multiclipboard.py save <key> - Save clipboard to key")
        print("  python multiclipboard.py load <key> - Load clipboard from key")
        print("  python multiclipboard.py list - List all saved keys")
        print("  python multiclipboard.py delete <key> - Delete the key")

if __name__ == '__main__':
    main()
