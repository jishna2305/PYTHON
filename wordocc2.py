def count_char(text):
  for i in range(len(text)):
    if len(text) == 0:
      break;
    ch = text[0]
    if ch == ' ' or ch == '\t':
      continue
    print(ch + " - ", text.count(ch))
    text = text.replace(ch, '').strip()
count_char('python programming')
