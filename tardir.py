import tarfile
import os.path
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%Y-%m-%d_%H-%M")
print("Date and time =", dt_string)	

output_filename=r"C:\Users\xx\Desktop\\"+ dt_string + "_testing" + ".tar.gz"
print(output_filename)
source_dir=r"C:\Users\xx\Desktop\test"

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
        
make_tarfile(output_filename, source_dir)