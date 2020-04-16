def is_prime(num):
  '''
    Define that number is prime
    Input - num: int
    Output - bool
  '''

  if num < 2:
    return False
  if num % 2 == 0:
    return num == 2
  d = 3
  while d * d <= num and num % d != 0:
    d += 2
  return d * d > num

