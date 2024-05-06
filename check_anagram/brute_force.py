def generate_anagrams(s):
  if len(s) == 1:
    return [s]
  else:
    anagrams = []
    for i, char in enumerate(s):
        for perm in generate_anagrams(s[:i] + s[i+1:]):
            anagrams.append(char + perm)
    return anagrams

def check_anagram_brute_force(str1, str2):
  '''
    Pendekatan Brute Force: 
    - Worst Case: O(n!)
    - Best Case: O(n!)
    1. Buat semua kemungkinan anagram dari string pertama.
    2. Bandingkan setiap anagram dengan string kedua.
    3. Jika ada yang sama, kembalikan True, jika tidak, kembalikan False.
  '''
  anagrams = generate_anagrams(str1)
  for anagram in anagrams:
      if anagram == str2:
          return True
  return False