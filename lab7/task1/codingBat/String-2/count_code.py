def count_code(str):
  
 
  
  occurences = 0
  
  for idx, ch in enumerate(str):
    if (ch == 'c'):
      
      
      if (len(str) > (3 + idx)):
       
        if (((str[idx + 1]) == 'o') and ((str[idx + 3]) == 'e')):
          occurences += 1
          
      else:
        
        return occurences
    
  return occurences
        
