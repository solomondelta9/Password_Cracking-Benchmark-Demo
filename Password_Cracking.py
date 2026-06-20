import time
import hashlib
import itertools
from prettytable import PrettyTable

def generate_hash(password):
    
    '''
    Generate the MD5 hash value of a given password
    Parameters:
    - password (str): The password to be hashed
    Returns:
    - str: the MD5 hash value of the given password
    '''
    md5_hash = hashlib.md5()
    md5_hash.update(str(password).encode('utf-8'))
    
    pass
    return md5_hash.hexdigest()
    
    
def brute_force_password(target_hash, charset, max_length):
    """
    Attempts to discover the password for a given hash using brute force.
    Parameters:
    - target_hash (str): The hash digest of the target password.
    - charset (str): The set of characters to use for generating password combinations.
    - max_length (int): The maximum length of the password to attempt.

    Returns:
    - str: The discovered password if found, or None if not found.
    """
    
    attempts = 0
    start_time = time.time()
    # Iterate through all possible lengths up to max_length
    for length in range(1, max_length + 1):
        # Generate all combinations of the given length
        for combination in itertools.product(charset, repeat=length):
            # Join the combination to form a password
            pass
            candidate = "".join(combination)
            attempts +=1
            
            # Generate the hash of the candidate password
            pass
            candidate_hash = generate_hash(candidate)
            # Check if the hash matches the target hash
            pass
            if candidate_hash == target_hash:
                elapsed = time.time() - start_time
                return candidate, attempts, elapsed

    elapsed = time.time() - start_time
    return None, attempts, elapsed  # Password not found within the given constraints


def defineRT(charset, min_length, max_length):
    """
    Creates a rainbow table with generated passwords and md5 hash values.
    Each password uses only a limited string of characters in limited length.  
    Parameters:
    - charset (str): The set of characters to use for generating password combinations.
    - max_length (int): The maximum length of passwords.
    - min_length (int): The minimum length of passwords.

    Returns:
    - dict: The dictionary composed of pairs <md5 hash digest, password>
    """    
    rainbowTable = {}
    
    
    for length in range(min_length, max_length + 1):
        for combination in itertools.product(charset, repeat=length):
            md5Hash = hashlib.md5()
            
            password = "".join(combination)
            password_bytes = password.encode()
            
            md5Hash.update(password_bytes)
            md5Digest = md5Hash.hexdigest()
            rainbowTable[md5Digest] = password
            
            hashed_password = generate_hash(password)
            if hashed_password not in rainbowTable:
                rainbowTable[hashed_password] = password

    print(f"Rainbow Table Size: {len(rainbowTable)}")
    
    pass
    return rainbowTable
            
def displayRT(rainbowTable):
    '''
    Display the size of the rainbow table and then display ten rows in a pretty table
    Parameters:
    - rainbowTable (dict) : The rainbow table to be displayed 
    Returns:
    - None
    '''
    pass
    print(f"Rainbow Table Size: {len(rainbowTable)}\n")
    
    tbl = PrettyTable(["Hash Value", "Password Value"])
    for hashValue, pwValue in list(rainbowTable.items())[:10]:
      tbl.add_row([hashValue, pwValue])
      
    tbl.align["Hash Value"] = "l"
    tbl.align["Password Value"] = "l"
    print(tbl.get_string())
    
def main():
    pw = 'aa@12!'
    
    #create a variable target to store the md5 hash of pw
    target = generate_hash(pw) #should update this target hash value
    
    print(f"pw: {pw}")
    print(f"target (MD5): {target}")
    
    #Modify the below code to test brute_force_password and document the time to discover the password
    charset = 'ab12!@'
    found = brute_force_password(target, charset, 8)
    brute_force_start = time.time()
    found_pw, attempts, brute_force_elapsed = brute_force_password(target, charset, 8)
    brute_force_total = time.time() - brute_force_start
    
    if found_pw is not None:
        print(f"[Brute Force] Password found: {found_pw}")
    else:
        print("[Brute Force] Password not found within constraints.")
    print(f"[Brute Force] Attempts: {attempts}")
    print(f"[Brute Force] Time: {brute_force_total:.6f} seconds")

    #Modify the below code to test defineRT and document the time to construct the rainbow table
    rainbow_table_start = time.time()
    rainbow_table = defineRT(charset, 4, 6)
    rainbow_table_elapsed = time.time() - rainbow_table_start
    
    print(f"[Rainbow Table] Built in {rainbow_table_elapsed:.6f} seconds")
    
    #Write more code to check how many seconds used to discover the password given the target hash using the rainbow table
    lookup_start= time.time()
    pw_from_rainbow_table = rainbow_table.get(target)
    lookup_elapsed = time.time() - lookup_start
   
    
    if pw_from_rainbow_table:
        print(f"[Rainbow Table] Lookup found password: {pw_from_rainbow_table}")
    else:
        print(f"[rainbow Table] Lookuptime: {lookup_elapsed:.6f} seconds")
    
    #Call displayRT to test the function definition
    displayRT(rainbow_table)
      

if __name__=='__main__':
    main()
