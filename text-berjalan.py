import random
import sys
import time
def tampil(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan tampil
        time.sleep(random.random() * 0.1)
#ubah angka 0.1 sesuai kebutuhan
#angka kecil adalah cepat
#angka besar adalah lambat
tampil('hallo teman-teman mata pelajaran python\nselamat belajar dalam ilmu teknologi pemrograman\nterima kasih.')