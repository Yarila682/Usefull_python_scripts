import sys


def main():

    arr_post=[254,254,254]
    crc = 0    

    for x in arr_post:
        crc = crc + x #* 211
        #crc = crc ^ (crc>>8)
     
      
    crc = crc & 0xFF
    print crc


if __name__ == '__main__':
     sys.exit(main())
