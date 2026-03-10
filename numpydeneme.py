import numpy as np
import time

tablo = np.ones((3,5))
tablo[1,2] = 99
yenitablo=tablo.reshape(1,15).copy()
yenitablo[0,3] = 27


filtre = tablo > 1
yenifiltre = yenitablo >1
print(yenitablo[yenifiltre])
print(tablo[filtre])
