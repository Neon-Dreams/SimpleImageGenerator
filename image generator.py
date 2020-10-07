import random
import threading

def generate():
    a=b''
    for i in range(2764800):
        a += random.randint(0, 255).to_bytes(1, 'big')
        print('Generated {} of 2764800'.format(i))
    return a

a = generate()

print('Generating Done')

with open('data.dat', 'rb') as dat:
    with open('image.bmp', 'wb') as file:
        print('Writing File')
        file.write(dat.read() + a)
        print('File Written')

input('Press Enter to exit...')
