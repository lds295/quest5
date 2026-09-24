def _is_valid(num_string):
    """
    Helper function to validate if the string is a properly formatted number.
    """
    if not isinstance(num_string, str):
        return False
        
    s = num_string.strip()
    if not s:
        return False
        
 
    if s[0] in ('+', '-'):
        s = s[1:]
        
    if not s: 

        return False
        
    parts = s.split('.')
    if len(parts) > 2:
        return False 
        
    if len(parts) == 1:
        return parts[0].isdigit()
        

    if not parts[0] and not parts[1]:
        return False  
        
    if parts[0] and not parts[0].isdigit():
        return False
        
    if parts[1] and not parts[1].isdigit():
        return False
        
    return True

def characteristic(num_string):
    """
    Extracts the characteristic (integer part) from a number string.
    
    Returns:
    tuple: (bool, int) - (True, characteristic) if valid, (False, 0) if invalid
    """
    if not _is_valid(num_string):
        return False, 0
        
   
    clean_str = num_string.strip()
    
   
    parts = clean_str.split('.')
    int_part = parts[0]
    

    if int_part == '' or int_part == '+' or int_part == '-':
        return True, 0
        
    return True, int(int_part)

def mantissa(num_string):
    """
    Extracts the mantissa (fractional part) from a number string.
    
    Returns:
    tuple: (bool, int, int) - (True, numerator, denominator) if valid, (False, 0, 0) if invalid
    """
    if not _is_valid(num_string):
        return False, 0, 0
        
    clean_str = num_string.strip()
    parts = clean_str.split('.')
    
    # If there is no decimal point (e.g. "42")
    if len(parts) == 1:
        return True, 0, 10
        
    frac_part = parts[1]
    
    # If the decimal point is at the end (e.g. "4.")
    if not frac_part:
        return True, 0, 10
        
    numerator = int(frac_part)
    denominator = 10 ** len(frac_part)
    
    return True, numerator, denominator
