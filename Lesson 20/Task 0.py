def oraliq(min, max, qadam=2):
    sonlar = []
    while min<max:
        sonlar.append(min)
        min += qadam
    return sonlar