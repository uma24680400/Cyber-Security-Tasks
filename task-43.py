import re

def validate_registration_form(username, email, age, phone_number):
    print(f"\n[+] Processing Registration Evaluation for: '{username}'")
    is_valid = True
    
    
    if not re.match(r"^[a-zA-Z0-9]{4,15}$", username):
        print("  [🚨 INVALID] Username must be alphanumeric and between 4 to 15 characters.")
        is_valid = False
    else:
        print("  [✓] Username validation passed.")

    
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_regex, email):
        print("  [🚨 INVALID] Email format is completely invalid.")
        is_valid = False
    else:
        print("  [✓] Email format validation passed.")

   
    try:
        age_int = int(age)
        if age_int < 13 or age_int > 120:
            print("  [🚨 INVALID] Age must be a realistic integer between 13 and 120.")
            is_valid = False
        else:
            print("  [✓] Age boundaries verified.")
    except ValueError:
        print("  [🚨 INVALID] Age must be a valid numerical integer.")
        is_valid = False

    
    if not re.match(r"^\d{3}-\d{3}-\d{4}$", phone_number):
        print("  [🚨 INVALID] Phone format must explicitly match standard structural formatting (XXX-XXX-XXXX).")
        is_valid = False
    else:
        print("  [✓] Phone number structural layout accepted.")

   
    if is_valid:
        print("🎉 [SUCCESS] All inputs validated perfectly! Account creation permitted.")
        return True
    else:
        print("❌ [REJECTED] Form validation failed. Request dropped.")
        return False

if __name__ == "__main__":
    print("[+] Launching Input Validation Sanity Checks...")
    
    
    validate_registration_form("cyberNinja9", "user@example.com", 25, "555-867-5309")
    
   
    validate_registration_form("admin_user!!", "bad_email_at_domain.com", "not_an_age", "123-45-678")
