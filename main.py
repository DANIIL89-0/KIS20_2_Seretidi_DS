z = input()

e = '''!()—[]{};:'"\,<>./?@#$%^&*_~-'''
for i in range(len(e)):
    z = z.replace(e[i], "")
print(z)
