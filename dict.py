import hashlib


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


target_hash = '0ab613316a8825c9e9d8530fdc6898c76c2fc577'
dict_file = 'D:/HTML-CSS/seltool/dict.txt'

password = dehash(target_hash, dict_file)


if password:
    print(f"Password found: {password}")
else:
    print("Password not found in dictionary")
