'''Concatenate n strings from the index where a vowel occurs.
Eg- abcd, bcdef, fgkl, dseiou
O/p- abcdeefeiou
l=['abcd','bcdef','fgkl','dseiou']
v='aeiou'
s1=" "
for c in l:

   s=[c1 for c1 in c if c1 in v]
print(s)
for v in s:
    s1+=v


print(s1)
'''
l=['abcd','bcdef','fgkl','dseiou']
v='aeiou'
s1=" "
for c in l:

  for c1 in c :
      if c1 in v:
          s1+=c1
print(s1)
