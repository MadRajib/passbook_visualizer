import pikepdf
from os import path

def decrypt(filename,password="",output="decrypted.pdf"):
    if filename == "":
        raise Exception("File name Cannot Be Empty!")
    if not path.exists(filename):
        raise FileNotFoundError()


    with pikepdf.open(filename, password=password) as pdf:
        num_pages = len(pdf.pages)
        del pdf.pages[-1]
        pdf.save(output)
    
    print("Successfully Decrypted File")
    print("Saved in: ",output)