def check_anagram_hash_map(a, b):
  '''
  Pendekatan Hash Map:
  https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/
  - Worst Case: O(n)
  - Best Case: O(n)
  The idea is a modification of the above approach where instead of creating an array of 256 characters HashMap is used to store characters and count of characters in HashMap. Idea is to put all characters of one String in HashMap and reduce them as they are encountered while looping over other the string.
  '''
	# Check if length of both strings is same or not
  if (len(a) != len(b)):
    return False

	# Create a HashMap containing Character as Key and
	# Integer as Value. We will be storing character as
	# Key and count of character as Value.
  map = {}
	# Loop over all character of String a and put in
	# HashMap.
  for i in range(len(a)):
		# Check if HashMap already contain current
		# character or not
    if (a[i] in map):
    # If contains increase count by 1 for that
    # character
      map[a[i]] += 1

    else:
			# else set that character in map and set
			# count to 1 as character is encountered
			# first time
      map[a[i]] = 1

	# Now loop over String b
  for i in range(len(b)):
		# Check if current character already exists in
		# HashMap/map
    if (b[i] in map):
			# If contains reduce count of that
			# character by 1 to indicate that current
			# character has been already counted as
			# idea here is to check if in last count of
			# all characters in last is zero which
			# means all characters in String a are
			# present in String b.
      map[b[i]] -= 1
    else:
      return False

	# Extract all keys of HashMap/map
  keys = map.keys()
	# Loop over all keys and check if all keys are 0.
	# If so it means it is anagram.
  for key in keys:
    if (map[key] != 0):
      return False

	# Returning True as all keys are zero
  return True