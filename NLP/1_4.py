str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
split_str = str.split()
one_ch = [1, 5, 6, 7, 8, 9, 15, 16, 19]  
atom = {}

for i, word in enumerate(split_str):
  if i + 1 in one_ch:
    atom[word[:1]] = i + 1  
  else:
    atom[word[:2]] = i + 1  

print(atom)
