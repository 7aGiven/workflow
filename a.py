import fsb5

print(1)
with open("EnginexStartmelodymix.CrossingSound.fsb", "rb") as f:
    print(2)
    b = f.read()
print(3)
fsb = fsb5.FSB5(b)
print(4)
sample = fsb.samples[0]
print(5)
ogg = fsb.rebuild_sample(sample)
print(6)
with open("r.ogg", "wb") as f:
    f.write(ogg)
print(7)