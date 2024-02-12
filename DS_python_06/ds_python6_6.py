import string
alphabet = string.ascii_lowercase
print(alphabet)

s = input('Введите строку: ')
s = s.lower()

#cycle for word updating till the end condition 
while True:
    
    stop_the_cycle = 1
    
    #going through the whole alphabet
    for i, letter in enumerate(alphabet):
        
        #if there are 2 different same letters
        if s.find(letter) != -1 and \
        s.find(letter) != (len(s) - 1 - s[::-1].find(letter)):
            
            stop_the_cycle = 0

            #deleting them and putting in the end new letter
            s = s.replace(letter, "", 1)
            s = s[::-1].replace(letter, "", 1)[::-1]
            s += alphabet[(i + 1) % len(alphabet)]
    
    if stop_the_cycle == 1:
        print(s)
        break
        