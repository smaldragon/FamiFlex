import sys

argv = sys.argv

if len(sys.argv) >= 2:
    filename = sys.argv[1]
    org_data = None
    with open(filename, "rb") as f:
        org_data = f.read()
        org_data = org_data[16:]
        
        prg_data = org_data[:0x4000]
        chr_data = org_data[0x4000:]
        print(len(org_data),len(prg_data),len(chr_data))
        
    with open("prg.65x", "wb") as f:
        copies = int((1024*512) / len(prg_data))
        f.write(prg_data*copies)
        
    with open("chr.bin", "wb") as f:
        copies = int((1024*512) / len(chr_data))
        f.write(chr_data*copies)
        
else:
    print("provide the name of a .nes file to convert in arguments")