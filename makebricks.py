def make_bricks(small, big, goal):
  total = small * 1 + big * 5
  if total == goal:
    return True
  elif total < goal:
    return False
  elif total > goal:
    remainder = total - goal
    fives_over = remainder // 5
    if fives_over >= 1:
      amount_to_subtract = remainder - fives_over * 5
      if amount_to_subtract == 0:
        return True
      if amount_to_subtract > 0:
        return True
    elif fives_over < 1:
      if small - fives_over >= 0:
        return True
      else:
        return False

   
make_bricks(3, 1, 8)