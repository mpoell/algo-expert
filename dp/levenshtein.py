"""
Write a function tha ttakes in two strings and
returns the minimum number of edit operations
that need to be performed on the first string to 
obtain the second string.

There are three edit operations: insertion of a 
character, deletion of a character, and 
substitution of a character for another.
"""

# Time O(mn) | Space O(mn)
def levenshtein(str1, str2):
  edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
  # [0, 1, 2, 3, 4, ...]
  # 1
  # 2
  # 3
  # 4

  for i in range(1, len(str2) + 1):
    edits[i][0] = edits[i - 1][0] + 1

  for i in range(1, len(str2) + 1):
    for j in range(1, len(str1) + 1):
      if str2[i - 1] == str1[j - 1]:
        edits[i][j]  = edits[i - 1][j - 1]
      else:
        edits[i][j] = min(edits[i - 1][j - 1], edits[i][j-1], edits[i - 1][j])

  return edits[-1][-1]


def main():
  str1 = "yabd"
  str2 = "abc"
  print(levenshtein(str1, str2))

if __name__ == "__main__":
  main()