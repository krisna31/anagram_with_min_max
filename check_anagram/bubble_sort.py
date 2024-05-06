def sort_string(s):
    n = len(s)
    arr = list(s)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return ''.join(arr)

def check_anagram_bubble_sort(str1, str2):
  '''
    Pendekatan Bubble Sort:
    - Worst Case: O(n^2)
    - Best Case: O(n^2)
    1. Urutkan karakter-karakter dalam kedua string.
    2. Bandingkan karakter-karakter yang telah diurutkan.
    3. Jika karakter-karakter yang diurutkan sama, kembalikan True, jika tidak, kembalikan False.

  '''
  sorted_str1 = sort_string(str1)
  sorted_str2 = sort_string(str2)
  return sorted_str1 == sorted_str2