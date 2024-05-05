def frequency_table(s):
  freq_table = {}
  for char in s:
    if char in freq_table:
      freq_table[char] += 1
    else:
      freq_table[char] = 1
  return freq_table

def check_anagram_dynamic(str1, str2):
  '''
    **Pendekatan Dynamic Programming**:
    - Worst Case: O(n)
    - Best Case: O(n)
    1. Buat tabel frekuensi karakter untuk kedua string.
    2. Bandingkan tabel frekuensi karakter.
    3. Jika tabel frekuensi karakter sama, kembalikan True, jika tidak, kembalikan False.

  '''
  freq_table_str1 = frequency_table(str1)
  freq_table_str2 = frequency_table(str2)
  return freq_table_str1 == freq_table_str2