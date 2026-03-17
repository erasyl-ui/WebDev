def xyz_there(str):
  
  target_str = "xyz"
  xyz_index = str.find(target_str)
  
  if (xyz_index == 0):
   
    return True
    
  elif (xyz_index == -1):
   
    return False
    
  else:
    
    for i, ch in enumerate(str):
      if (i > 0):
        
        if ((str[i-1] != ".") and (str[i:i+3] == target_str)):
          return True
          
   
    return False
    
    
