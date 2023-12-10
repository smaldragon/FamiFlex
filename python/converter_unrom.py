import sys
argv = sys.argv

if len(sys.argv) >= 2:
    filename = sys.argv[1]
    org_data = None
    with open(filename, "rb") as f:
        org_data = f.read()
        org_data = org_data[16:]
        
        prg_data = org_data[:0x10000]
        print(len(prg_data))
        chr_data = []
        print(len(org_data),len(prg_data),len(chr_data))

    banks = int (len(prg_data) / 0x4000)
    banks_data = []
    for i in range(banks):
        banks_data.append(prg_data[(i*0x4000):((i+1)*0x4000)])

    with open("prg.65x", "wb") as f:
        copies = int((1024*512) / (1024*64))
        for u in range(copies):
            for i in range(banks):
                f.write(banks_data[i])
else:
    print("provide the name of a .nes file to convert in arguments")