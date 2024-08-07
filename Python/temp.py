def remove_lines_ending_with_picture(file_path):
    try:
        # Read the lines from the file
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Filter out lines that end with 'picture' or contain invalid characters
        filtered_lines = []
        for line in lines:
            try:
                # Check if the line ends with 'picture'
                if not line.strip().endswith('picture'):
                    # Attempt to encode the line with the 'charmap' codec
                    line.encode('charmap')
                    filtered_lines.append(line)
            except UnicodeEncodeError:
                # Skip lines that cause encoding errors
                continue
        
        # Write the filtered lines back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(filtered_lines)
            
        print(f"Successfully removed lines ending with 'picture' or containing invalid characters from {file_path}.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
# remove_lines_with_picture_or_invalid_encoding('path/to/your/textfile.txt')

        
remove_lines_ending_with_picture(r'D:\E Drive\vscode\Main-Repository\Python\temp.txt')