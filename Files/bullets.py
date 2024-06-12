def add_bullets_to_wiki_markup(file_path):
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Process each line to add bullets
        bulleted_lines = []
        for line in lines:
            stripped_line = line.strip()
            if stripped_line and not stripped_line.startswith('*'):
                bulleted_lines.append(f'* {stripped_line}')
            else:
                bulleted_lines.append(line)

        # Write the new content back to the file
        with open(file_path, 'w') as file:
            file.writelines(bulleted_lines)

        print(f"Bullets added to the wiki markup in {file_path}")

    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
file_path = 'C:\Programming\Python\Files\wiki_markup.txt'
add_bullets_to_wiki_markup(file_path)
