def count_char(text):
  for i in range(len(text)):
    if len(text) == 0:
      break;
    ch = text[0]
    if ch == ' ' or ch == '\t':
        continue
    count = 1
    for j in range(1, len(text)):
      if ch == text[j]:
        count += 1
    text = text.replace(ch, '').strip()
    print(ch + " - ", count)

count_char('python programming')
