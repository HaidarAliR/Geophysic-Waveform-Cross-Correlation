# jalankan skrip ini dengan komputer yg sudah terinstal python 2.x.x
# skrip ini digunakan untuk mengkonversi data buletin BMKG menjadi data input hypodd

# isi nama file input dan output
fileinput = 'wcc_p3k_07.txt'
fileoutput = 'dtp3k_07.cc'

# baca isi file input dan buka file output
file = open(fileinput,'r')
baris = file.readlines()
for i in range(len(baris)):
	baris[i]=baris[i].split()
file.close()
file = open(fileoutput,'w')
# print(len(baris))

list_sta = ['501', 'A08', 'A21', 'A22', 'A23', 'A25', 'A33', 'A73', 'A74', 'AAX']
#initial row
Ev1 = baris[1][0]
Ev2 = baris[1][1]
Sta = list_sta[int(baris[1][2])]
Coef = ('%.3f')%float(baris[1][3])
Lag = ('%.3f')%float(baris[1][5])
file.write('# '+Ev1.ljust(5)+Ev2.ljust(5)+'0.0'+'\n'+Sta.ljust(5)+Lag.ljust(8)+Coef.ljust(8)+' P'+'\n')
# start iteration

for i in range(2,len(baris)):
    Ev1 = baris[i][0]
    Ev2 = baris[i][1]
    Sta = list_sta[int(baris[i][2])-1]
    Coef = ('%.3f')%float(baris[i][3])
    Lag = ('%.3f')%float(baris[i][5])
    if baris[i][0]==baris[i-1][0] and baris[i][1]==baris[i-1][1]:
        file.write(Sta.ljust(5) + Lag.ljust(8) + Coef.ljust(8) + ' P' + '\n')

    else:

         file.write('# '+Ev1.ljust(5)+Ev2.ljust(5)+'0.0'+'\n'+Sta.ljust(5)+Lag.ljust(8)+Coef.ljust(8)+' P'+'\n')

    i = i + 1
file.close()
