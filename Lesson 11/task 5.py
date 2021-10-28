mahsulotlar=['non' , 'pista' , 'shakar' , 'pasta' , 'priprava']
savat=[]
bor_mahsulotlar=[]
yuq_mahsulotlar=[]
son=int(input('Kiritiladigan mahsulotlar soni: '))
for n in range(son):
    savat.append(input(f"{n+1} mahsulotni kiriting: "))
for mahsulot in savat:
    if mahsulot.lower() in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        yuq_mahsulotlar.append(mahsulot)
if yuq_mahsulotlar:
    print("Quyidagi mahsulotlar do'konimizda yo'q:", yuq_mahsulotlar)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")