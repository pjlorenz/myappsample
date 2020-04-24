#  goal 27:
#    given 7 5's and 3 1's  --> fives_max = 5. fives_used = 5
#
#    given 3 5's and 12 1's --> fives_max = 3. fives_used = 3
#


def make_bricks(small, big, goal):
  total = small * 1 + big * 5
  fives_max = goal // 5
  fives_used = min(fives_max, big)
  ones_needed = goal - fives_used * 5
  return ones_needed >= small

  
    
final = make_bricks(1, 4, 12)
print(final)