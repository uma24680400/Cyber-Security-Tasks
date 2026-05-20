import time

class RateLimiter:
    def __init__(self, max_tokens, regen_rate):
        self.max_tokens = max_tokens
        self.regen_rate = regen_rate 
        self.tokens = max_tokens
        self.last_check = time.time()

    def allow_request(self):
        current_time = time.time()
        elapsed = current_time - self.last_check
        self.last_check = current_time

        
        self.tokens = min(self.max_tokens, self.tokens + (elapsed * self.regen_rate))

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False

if __name__ == "__main__":
   
    limiter = RateLimiter(max_tokens=5, regen_rate=1)
    print("[+] Simulating 8 rapid API requests...")

    for i in range(1, 9):
        if limiter.allow_request():
            print(f"Request {i}: [ALLOWED] Processing data...")
        else:
            print(f"Request {i}: 🚨 [BLOCKED] Rate limit exceeded (429 Too Many Requests).")
        time.sleep(0.2)  
