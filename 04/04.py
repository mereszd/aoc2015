import hashlib

input = "iwrupvqb"
suffix = 0

while True:
    hashable = input + str(suffix)
    encoded_hashable = hashable.encode('utf-8')
    hashed = hashlib.md5(encoded_hashable).hexdigest()
    if hashed[0:6] == '000000':
        print(f"Found the answer! The full string is {hashable}, so the number is {str(suffix)}")
        break
    suffix += 1
