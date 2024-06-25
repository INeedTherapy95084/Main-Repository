def remove_lines_ending_with_picture(file_path):
    try:
        # Read the lines from the file
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Filter out lines that end with 'picture'
        filtered_lines = [line for line in lines if not line.strip().endswith('picture')]
        
        # Write the filtered lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(filtered_lines)
            
        print(f"Successfully removed lines ending with 'picture' from {file_path}.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
remove_lines_ending_with_picture(r'E:\vscode\Main-Repository\Python\temp.txt')