def read_log_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            print(f"--- Reading Log File: {file_path} ---")
            for line in file:

                
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The log file at '{file_path}' was not found.")
    except PermissionError:
        print(f"Error: Insufficient permissions to read '{file_path}'.")

if __name__ == "__main__":
   
    with open("test_log.txt", "w") as f:
        f.write("2026-05-18 10:00:00 INFO User logged in\n")
        f.write("2026-05-18 10:05:00 WARNING Failed login attempt\n")
        
    read_log_file("test_log.txt")
