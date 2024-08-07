def remove_lines_ending_with_picture(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        filtered_lines = []
        for line in lines:
            try:
                if not line.strip().endswith('picture'):
                    filtered_lines.append(line)
            except UnicodeEncodeError:
                continue
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(filtered_lines)
            
        print(f"Successfully removed lines ending with 'picture' or containing invalid characters from {file_path}.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

        
remove_lines_ending_with_picture(r'D:\E Drive\vscode\Main-Repository\Python\temp.txt')