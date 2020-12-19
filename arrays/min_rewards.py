"""
Imagine that you're a teacher who's just graded the final
exam in a class. You have a list of student scores on the
final exam in a particulat order (not necessarily sorted), 
and you want to reward your students. You decide to do so 
fairly by giving them arbitrary rewards following two rules:

  1) All students must recieve at least one reward.
  2) Any given student must receive strictly more rewards than an
      adjacent student (student immediately to the right or left)
      with a lower score and must recive strictly fewer rewards
      than an adjacent student with a higher score.

Write a funciton that takes in a list of scores and returns the 
minimum number of rewards that you must give out to students to
satisfy the two rules.

Assume that all students have different, unique scores.
"""

# Time: O(n) | Space: O(n)
def min_rewards(scores):
  rewards = [1 for score in scores]

  # Capture decreases (iterate left to right)
  L = 0
  R = 1
  while R < len(scores):
    if scores[L] > scores[R]:
      L += 1
      R += 1
      continue
    elif scores[L] < scores[R]:
      rewards[R] = max(rewards[L] + 1, rewards[R])
      L += 1
      R += 1

  # Capture increases (iterate right to left)
  R = len(scores) - 1
  L = R - 1
  while L >= 0:
    if scores[L] < scores[R]:
      L -= 1
      R -= 1
      continue
    elif scores[L] > scores[R]:
      rewards[L] = max(rewards[L], rewards[R] + 1)
      L -= 1
      R -= 1
      
  return sum(rewards)









def main():
  scores = [8, 4, 2, 1, 3, 6 ,7, 9 ,5]

  print(min_rewards(scores))

if __name__ == "__main__":
  main()