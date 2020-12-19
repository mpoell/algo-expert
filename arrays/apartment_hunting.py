"""
You're looking to move into a new apartment, and youre
given a list of blocks where each block cointains an 
apartment that you could move into. In order to pick your
apartment, you wnat to optimize its location. You also have
a list of req's: a list of buildings that are important to you.
For instance, you might value having a school and a gym near
your apartment. The lsit of blocks that you have contains information
at every block about all of the buildings that are present and
absent at the block in question. FOr instance, for ever block,
you might know whether a school, a pool, an office, and a gym
are present.

In order to optimize your life, you want to minimize the farthest
distance you'd have to walk from your apartment to reach any of your
required buildings.

Write a function that takes in a lsit of blocks and a list of your
required buildings and that returns the location (index) of the block
thats most optimal for you.

If there are multiple msot optimal blocks, your function can return the index
of any one of them.
"""

def apartment_hunting(blocks, reqs):
  scores = {i: [] for i in range(len(blocks))}

  for i in range(len(blocks)):
    for req in reqs:
      scores[i].append(find_nearest(i, blocks, req))

  result = [max(scores[i]) for i in range(len(blocks))]
  best_score = min(result)

  for i, score in enumerate(result):
    if best_score == score:
      return i


def find_nearest(curr_block, blocks, req): #(2, blocks, "gym")
  """
  Return min distance of blocks
  to requirement
  """
  result = []
  for i in range(0, curr_block):
    if blocks[i][req]:
      result.append(curr_block - i)
  for i in range(curr_block, len(blocks)):
    if blocks[i][req]:
      result.append(i - curr_block)

  return min(result)


def main():
  # blocks = [
  #   {"gym": False, "school": True, "store": False},
  #   {"gym": True, "school": False, "store": False},
  #   {"gym": True, "school": True, "store": False},
  #   {"gym": False, "school": True, "store": False},
  #   {"gym": False, "school": True, "store": True}
  # ]

  # reqs = ["gym", "school", "store"] 

  
  blocks = [
    {"gym": True, "pool": False, "school": True, "store": False},
    {"gym": False, "pool": False, "school": False, "store": False},
    {"gym": False, "pool": False, "school": True, "store": False},
    {"gym": False, "pool": False, "school": False, "store": False},
    {"gym": False, "pool": False, "school": False, "store": True},
    {"gym": True, "pool": False, "school": False, "store": False},
    {"gym": False, "pool": False, "school": False, "store": False},
    {"gym": False, "pool": False, "school": False, "store": False},
    {"gym": False, "pool": False, "school": False, "store": False},
    {"gym": False, "pool": False, "school": True, "store": False},
    {"gym": False, "pool": True, "school": False, "store": False}
  ]

  reqs = ["gym", "pool", "school", "store"]


  print(apartment_hunting(blocks, reqs))

if __name__ == "__main__":
  main()

