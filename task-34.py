import time


failed_attempts = {}
THRESHOLD_ATTEMPTS = 3
LOCKOUT_WINDOW = 10  
def login_attempt(username, success):
    current_time = time.time()
    
    if success:
        print(f"[SUCCESS] User '{username}' logged in successfully.")
        if username in failed_attempts:
            del failed_attempts[username]
        return True

   
    if username not in failed_attempts:
        failed_attempts[username] = []
    
    failed_attempts[username].append(current_time)
    
    
    failed_attempts[username] = [t for t in failed_attempts[username] if current_time - t < LOCKOUT_WINDOW]
    
    print(f"[FAILED] Failed login attempt for '{username}'.")
    
    
    if len(failed_attempts[username]) >= THRESHOLD_ATTEMPTS:
        print(f"🚨 [ALERT] Unauthorized access detected! Suspicious activity on user '{username}'.")
        return False


if __name__ == "__main__":
    print("[+] Simulating login tracking...")
    login_attempt("admin", False)
    time.sleep(1)
    login_attempt("admin", False)
    time.sleep(1)
    login_attempt("admin", False)
