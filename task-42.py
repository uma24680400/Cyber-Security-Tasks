import re


SQLI_PATTERNS = [
    r"(\s|^)or\s+\d+=\d+",      
    r"union\s+select",           
    r"--;",                     
    r"drop\s+table",             
    r"/\*.*\*/"                  
]

def inspect_input(user_input):
    clean_input = user_input.lower()
    
    for pattern in SQLI_PATTERNS:
        if re.search(pattern, clean_input):
            print(f"🚨 [SQLi ALERT] Malicious query flag triggered on input: \"{user_input}\"")
            return False
            
    print(f"✓ [SAFE] Input validated: \"{user_input}\"")
    return True

if __name__ == "__main__":
    print("[+] Starting SQL Injection Signature Engine...")
    
   
    inspect_input("john_doe123")
    inspect_input("admin' OR 1=1 --")
    inspect_input("变换' UNION SELECT password FROM users --;")
