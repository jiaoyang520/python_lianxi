s = "  *  xiangyang       *   "
print(s.split('y'))

s1 = s.split('a', maxsplit=2)
print(s1)

print(s.replace('a', 'o'))
print(s.replace('a', 'j', 1))

print(s.center(30))
print(s.center(30, '@'))
print(s.ljust(30, '#'))
print(s.rjust(30, '&'))
print(s.zfill(30))
print(s.strip())
print(s.rsplit())
print(s.lstrip())
