import Tkinter as tk

awal = tk.Tk()
tunda = 100           # seperseribu penundaan per huruf
tulisan = tk.StringVar()
isi_tulisan = tk.Label(awal, textvariable=tulisan, height=20, width=80 )

def geser():
    geser.msg = geser.msg[1:] + geser.msg[0]
    tulisan.set(geser.msg)
    awal.after(tunda, geser)

geser.msg = ' Selamat belajar python, ini adalah contoh tulisan bergerak dan bergeser, waktu dhuhur jam 11:59 .....  '
geser()
isi_tulisan.pack()
awal.mainloop()