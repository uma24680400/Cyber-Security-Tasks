import re

SUSPICIOUS_KEYWORDS = ["login", "verify", "secure", "bank", "update-account", "paypal"]
SUSPICIOUS_TLDS = [".xyz", ".top", ".click", ".loans", ".support"]

def analyze_url(url):
    url_lower = url.lower()
    score = 0
    reasons = []

    
    for word in SUSPICIOUS_KEYWORDS:
        if word in url_lower:
            score += 2
            reasons.append(f"Contains keyword '{word}'")

    
    for tld in SUSPICIOUS_TLDS:
        if url_lower.endswith(tld) or f"{tld}/" in url_lower:
            score += 3
            reasons.append(f"Uses suspicious TLD '{tld}'")

   
    if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url_lower):
        score += 4
        reasons.append("Uses raw IP address instead of a domain name")

    
    if url_lower.count('.') > 3 or url_lower.count('-') > 3:
        score += 2
        reasons.append("Excessive subdomains or dashes (obfuscation attempt)")

    print(f"\nAnalyzing: {url}")
    if score >= 4:
        print(f"🚨 [SUSPICIOUS] Risk Score: {score}/10")
        print("Reasons:", ", ".join(reasons))
    else:
        print("✓ [CLEAN] URL seems normal.")

if __name__ == "__main__":
    analyze_url("https://www.google.com")
    analyze_url("http://192.168.1.1/secure-login-activity/bank-update.xyz")
