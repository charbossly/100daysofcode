import string
import random

punctuations = string.punctuation
uppercases = string.ascii_uppercase
lowercases = string.ascii_lowercase
letters =  string.ascii_letters
digits = string.digits

dictionnaire = {
        "a":punctuations,
        "b":uppercases,
        "c":lowercases,
        "d":letters,
        "e":digits
    }
print('================Generate Password===============')

length = int(input('Precise your password length\n'))

print('Select your password options\n')

result = input('''
a:with punctuations
b:with upercases letters
c:with lowercases letters
d:with letters
e:with digits
''')

use = ''
for i in result.split():
    if i in dictionnaire:
        use += dictionnaire[i]

print('Your password is:')
print(''.join(random.choice(use) for i in range(length)))

