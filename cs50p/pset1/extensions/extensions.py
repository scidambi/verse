file = input("File Name:")

file = file.split('.')
format0 = file[0].strip().lower()

if len(file) >1:
    format1 = file[1].strip().lower()
else:
    format1 = ""

print(format0)

if format1 == "gif" or format1 == "jpg" or format1 == "jpeg" or format1 == "png":
    print("image/",format1, sep="")

elif format1 == "pdf" or format1 == "zip":
    print("application/",format1, sep="")

elif format1 == "txt":
    print("text/",format1, sep="")

else: 
    print("application/octet-stream")