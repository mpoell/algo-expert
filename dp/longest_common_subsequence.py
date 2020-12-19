"""
Write a function that takes in two strings and returns
their longest common subsequence.

A subsequence of a stirng is a set of characters that 
arent necessarily adjacent in the string but that are
in the same order as they appear int he string. For 
instance, the characters [a, c, d] for a subsequence
of the string "abcd", and so the the characters [b, d].
Note that a single character in a string and the string
itself are both valid subsequences of the string.

Assume that there will only be one longest common 
subsequence.
"""
# Time: O(NM * min(N,M)) | Space: O(NM * min(N,M))
def longest_common_subsequence(str1, str2):
  lcs = [[[] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
  for i in range(1, len(str2) + 1):
    for j in range(1, len(str1) + 1):
      if str2[i - 1] == str1[j - 1]:
        lcs[i][j] = lcs[i - 1][j - 1] + [str2[i - 1]]
      else:
        lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1], key=len)
  return lcs[-1][-1]
  



def main():
  string1 = "ZXVVYZW"
  string2 = "XKYKZPW"

  print(longest_common_subsequence(string1, string2))

if __name__ == "__main__":
  main()