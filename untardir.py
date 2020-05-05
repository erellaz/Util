import tarfile

tarpath=r"C:\Users\xx\Desktop\dtext.tar.gz"

tar = tarfile.open(tarpath)
tar.extractall()
tar.close()