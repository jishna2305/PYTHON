def count_char(text):
  count = {}
  for ch in text:
    if ch == ' ' or ch == '\t':
      continue
    if ch in count:
      count[ch] += 1
    else:
      count[ch] = 1
    for k, v in count.items():
      print('Charcater {} occurs {} times'.format(k,v))
count_char('python programming')
