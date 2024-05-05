# My Implementation with min or max method
def check_anagram_min_max(str1, str2, how = min):
  '''
    Check if the word is anagram with min max method
  '''
  if len(str1) != len(str2): return False
  
  # loop the entire string 
  while str1:
    # check if min(str1) on left side of str != min(str2) to right str then return false
    min_test = how(str1)
    min_original = how(str2)
    
    # if it does same remove that char from test and original then continue checking
    if min_test != min_original:
      return False
      
    str1 = str1.replace(min_test, '', 1)
    str2 = str2.replace(min_original, '', 1)
  
  # if never retuen false then return true the test and original must be anagram
  return True