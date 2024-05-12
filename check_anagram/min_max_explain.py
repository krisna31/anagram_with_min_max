import streamlit as st

def check_anagram_min_max_explain(str1, str2, how = min):
  '''
    Check if the word is anagram with min max method
  '''
  step = 1
  st.write(f"{step}. Checking if '{str1}' and '{str2}' are anagrams...")
  step += 1

  if len(str1) != len(str2): 
    st.write(f"{step}. The strings are not the same length, so they can't be anagrams.")
    return False
  
  # loop the entire string 
  while str1:
    # check if min(str1) on left side of str != min(str2) to right str then return false
    min_test = how(str1)
    st.write(f"{step}. Finding the {how.__name__} character in '{str1}' and '{str2}'...")
    step += 1
    min_original = how(str2)
    st.write(f"{step}. The {how.__name__} character in '{str1}' is '{min_test}' and in '{str2}' is '{min_original}'.")
    step += 1
    
    st.write(f"{step}. Comparing '{min_test}' from '{str1}' and '{min_original}' from '{str2}'...")
    step += 1

    # if it does same remove that char from test and original then continue checking
    if min_test != min_original:
      st.write(f"{step}. The characters '{min_test}' and '{min_original}' are not the same, so the strings are not anagrams. Returning False.")
      return False
    
    st.write(f"{step}. The characters '{min_test}' and '{min_original}' are the same, so they are removed from the strings, and the comparison continues...")
    step += 1
    
    st.write(f"{step}. Removing '{min_test}' from '{str1}' and '{min_original}' from '{str2}'...")
    step += 1
    str1 = str1.replace(min_test, '', 1)
    str2 = str2.replace(min_original, '', 1)
  
  # if never retuen false then return true the test and original must be anagram
  st.write(f"{step}. All characters match, so the strings are anagrams. Returning True.")
  return True