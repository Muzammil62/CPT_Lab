import hashlib
trusted_dns_records={
    "google.com":
        hashlib.sha256("google.com".encode()).hexdigest(),
    "amazon.com":
        hashlib.sha256("amazon.com".encode()).hexdigest(),
    "facebook.com":
        hashlib.sha256("facebook.com".encode()).hexdigest()
}
user_domain=input("Enter Website domain:")
if user_domain in trusted_dns_records:
    
    user_hash=hashlib.sha256(user_domain.encode()).hexdigest()
    
    if user_hash==trusted_dns_records[user_domain]:
        print("\nWebsite is Authentic(Not Fake)")
        print("DNSSEC Verification Successful")
    else:
        print("\nWarning! Website data modified")
        print("DNSSEC Verification Failed")
else:
    print("\nFake Website Detected!")
    print("Domain not found in trusted DNS records.")