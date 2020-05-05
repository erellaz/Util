from random import seed
from random import randint

ptext=r'C:\Users\xxl\Desktop\2020-04-05_13-28_testing.tar.gz'
ctext=r'C:\Users\xx\Desktop\2020-04-05_13-28_testing.enc'
dtext=r'C:\Users\xx\Desktop\dtext.tar.gz'

def kk(i):
    k1,k2,k3,k4,k5,k6,k7=(121,9,5,11,125,7,31)
    seed(k1*i+k7)
    for _ in range(i+k3):
        randint(0, 255)
    return (k2+i*k3+k4*randint(0,k5)+i^2*k6*randint(0,k7)^2)

def grx(toread,towrite,m):
    with open(towrite,'wb') as fout:
        with open(toread, 'rb') as fin:
            i=0
            while 1:
              byte_s = fin.read(1)
              if not byte_s:
                 break
              byte = byte_s[0]
              ki=kk(i)
              ebyte=(byte+m*ki)%256 
              ebyte_s=bytes([ebyte])
              fout.write(ebyte_s)
              #print(byte,"-",ebyte,"------",byte_s,"-",ebyte_s,"   --",i,ki%256)
              i+=1
              
grx(ptext,ctext,1)
grx(ctext,dtext,-1)            