Plain = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Cipher = ['X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W']


message = input('Enter the message\n')
transcript = list(message.upper())


for idx,i in enumerate(message.upper()):
    if i in Plain:
       transcript[idx] = Cipher[Plain.index(i)]



print("Your message is:{}".format(message))
print("Your transcripted message:")
print("".join(transcript))
