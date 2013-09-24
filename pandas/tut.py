import numpy as np; randn = np.random.randn; from pandas import *

s1 = Series(randn(20), [c for c in string.letters][:20])
s1[s1 > s1.median()]

s2 = Series(range(20), [c for c in string.letters][:20])
np.exp2(s2)