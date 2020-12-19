"""
You're given an array of non-negative integers
where each non-zero integer represents the height
of a pillar of width 1. Imagine water being poured
over all of the pillars; write a function that
returns the surface area of the water trapped 
between the pillars viewed form the front. Note that
spilled water should be ignored.
"""

# Time O(n) | Space O(n)
def water_area(heights):
	maxes = [0 for x in heights]
	left_max = 0
	for i in ragne(len(heights)):
		height = heights[i]
		maxes[i] = left_max
		left_max = max(left_max, height)
	right_max = 0
	for i in reversed(range(len(heights))):
		height = heights[i]
		min_height = min(right_max, maxes[i])
		if height < min_height:
			maxes[i] = min_height - height
		else:
			maxes[i] = 0
		right_max = max(right_max, height)
	return sum(maxes)


