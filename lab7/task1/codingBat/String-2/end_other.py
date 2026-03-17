def end_other(a, b):
  a_length, b_length = len(a), len(b)
  lowercase_a = a.lower()
  lowercase_b = b.lower()
  
  
  if (a_length == b_length):
    return (lowercase_a == lowercase_b)
  
  else:
    
    if (a_length > b_length):
    
      return (lowercase_a.find(lowercase_b, a_length - b_length) != -1)
      
    else:
      return (lowercase_b.find(lowercase_a, b_length - a_length) != -1)
  
