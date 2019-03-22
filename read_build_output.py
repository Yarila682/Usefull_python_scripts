
import argparse
import sys
import time
import os

def main():
     args = parse_args()

     
     if args.waiting_time:
          wait_time = float(args.waiting_time)
     else:
          wait_time = 10


     if args.search_string:
                         search_string = args.search_string
     else:
                         search_string = ''
     
     line_number = 1

     try:
          print "Opening file..."
          f = open(args.file)
          
          if not args.force_realtime_reading:
              
               for line in f:
                    if search_string != '':
                              
                         if line.find(args.search_string) != -1:
                            print_line(line,args.timeout,line_number)
                            line_number += 1
                         else:
                          
                          print_line(line,args.timeout,line_number)
                          line_number += 1

               do_real_life_reading(args.file,f,line_number,args.timeout,wait_time,search_string)
               
          else:
               f.seek(0,2)
               do_real_life_reading(args.file,f,line_number,args.timeout,wait_time,search_string)
             
     except Exception as e:
        print "Exception:"
        print e
     finally:
          f.close()
          print('Close file')

def do_real_life_reading(path,f,line_number,timeout,waiting_time = 10,search_string = ''):

     print "----------------------------"
     print "| Real life reading section |"
     print "----------------------------"

     # time_stamp1 = os.path.getmtime(path)
     #size1 = os.path.getsize(path)

     line = f.readline()

     if line == '':
          print "Waiting {0} sec for new data... ".format(waiting_time)
          time.sleep(waiting_time) 
          line = f.readline()
     
     
     size2 = os.path.getsize(path) / 1024 / 1024
     print "Size: {0} Mb ".format(size2)
     print "Tell: {0}".format(f.tell() / 1024 / 1024)

     
     
     while line != '':
         # print "Entering the zize equality loop"
         # time_stamp1 = time_stamp2
          size1 = size2
          line = f.readline()
          
          if search_string != '':
                       if line.find(search_string) != -1:
                            print_line(line,timeout,line_number)
                            line_number += 1
          else:
                          print_line(line,timeout,line_number)
                          line_number += 1

          if f.readline() == '':
              print "Waiting {0} sec for new data ".format(waiting_time) 
              time.sleep(waiting_time)
              size2 = os.path.getsize(path)


def print_line(line, timeout,line_number):

     
             print 'Line number: {0}'.format(line_number) 
             print "------------------------------------------------------"
             print line
             print "------------------------------------------------------"

             

             if timeout:
                  
                  t = float(timeout)
                  time.sleep(t)
     

def parse_args():
     parser = argparse.ArgumentParser(description='Bootstrap this project')
     parser.add_argument('-f', '--file',
                 help='File to read',
                 required=True)
     parser.add_argument('-t', '--timeout',
                 help='String read timeout (in seconds)',
                 required=False)
     parser.add_argument('-s', '--search_string',
                 help='String to search in line',
                 required=False)
     parser.add_argument('-w', '--waiting_time',
                 help='A time to wait for log updates',
                 required=False)
     parser.add_argument('-force', '--force_realtime_reading',
                         action='store_true',
                 help='Setup a reltime reading mode',
                 required=False)

     return parser.parse_args()

if __name__ == '__main__':
     sys.exit(main())
