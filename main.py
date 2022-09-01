

def get_pal(s=None):
	"""
	Check the supplied text for any sequence of characters that read the
	same forwards and backwards (palindrome).
	
	:param str s: String/text to check
	"""
	if s == s[::-1]: return s   # If the string itself is a palindrome
	size = len(s)               # Total chars in text
	
	# Always match 1st char since one char is technically a palindrome
	j, k = 1, 0                 # Length of longest substring match; index position of longest match
	for i in range(1, size):    # Loop through each char (skip first char since it's evaluated in the loop)
		si = i - j              # Start position of substring index
		a = s[si - 1:i + 1]     # Substring of cur position +/- 2 chars
		b = s[si:i + 1]         # Substring of cur position +/- 1 char
		
		# Evaluate 2+ chars away from current position
		if si > 0 and a == a[::-1]:
			j += 2              # Increment by 2 to include previous char
			k = si - 1          # Set index position of longest char match
			continue
			
		# Check next char vs current substring
		if b == b[::-1]:
			j += 1              # Increment longest substring length by 1
			k = si
			
	return s[k:k + j]
	
	
if __name__ == "__main__":
	text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
	longest_palindrome = get_pal(s=text)
	print(f"Longest palindrome: {longest_palindrome}")
