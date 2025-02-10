from scamp import *
from notes import nf, nl

s = Session(tempo=120)

piano = s.new_part("piano")

c_scale = [0, 2, 4, 5, 7, 9, 11]
c_sc = []
for val in c_scale:
    c_sc.append(nl[val])
print(c_sc)


for i in range(4):
    for note in c_sc:
        n = nf[note][i]
        print(n, i)
        piano.play_note(n, 1, 1)

