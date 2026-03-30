import hashlib

password = "admin123"
hash_value = hashlib.md5(password.encode()).hexdigest()

print(hash_value)....
