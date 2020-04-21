import time

def permutations(sequence):
  # print sequence
  unit = [1, 2, 1, 2, 1]

  if len(sequence) >= 4:
    for i in range(4, (len(sequence) + 1)):
      unit = ((unit + [i - 1]) * i)[:-1]
      # print unit
    for j in unit:
      temp = sequence[j]
      sequence[j] = sequence[0]
      sequence[0] = temp
      yield sequence
  else:
    print('You can use PEN and PAPER')


s = [1,2,3,4,5]
# s = [x for x in 'PYTHON']

print(s)

z = permutations(s)
try:
  while True:
    # time.sleep(0.0001)
    print(next(z))
except StopIteration:
    print('Done')
