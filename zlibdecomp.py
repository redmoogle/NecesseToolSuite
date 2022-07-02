from pathlib import Path
import zlib

fi = open('res.data', 'rb')
decompressed_data = zlib.decompress(fi.read())
prev_byte = None
filelen = 0
offset = 0
count = 0
while(True):
    hexbyte = decompressed_data[count]
    if(chr(hexbyte).isalnum()):
        filelen = int(prev_byte)
        pathname = decompressed_data[count:count+filelen].decode('ascii')
        if(pathname == ""):
            break
        print(f'Extracting: {pathname}')
        datalen = int.from_bytes(decompressed_data[count+filelen:count+filelen+4], byteorder='big')
        path = Path(f'project/' + pathname)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(decompressed_data[count+filelen+4:count+filelen+4+datalen])
        decompressed_data = decompressed_data[count+filelen+4+datalen:len(decompressed_data)]
        count = 0
    prev_byte = hexbyte
    count += 1

print('FINISHED')
