import hashlib
import time

def dehash(hash, dict_file):
    # Open the dictionary file and read in the words
    with open(dict_file, 'r') as f:
        words = f.readlines()
    
    # Strip whitespace and calculate the hash for each word
    for word in words:
        word = word.strip()
        hashed_word = hashlib.sha1(word.encode('utf-8')).hexdigest()
        
        # Compare the hash to the target hash
        if hashed_word == hash:
            return word
    
    # If the hash is not found in the dictionary, return None
    return None


target_hash = 'dcd6732d222b9bc8ee3352545285c6377efdf417'
dict_file = 'D:/HTML-CSS/seltool/dict.txt'

start_time = time.time()
password = dehash(target_hash, dict_file)
end_time = time.time()

if password:
    print(f"Password found: {password}")
else:
    print("Password not found in dictionary")
