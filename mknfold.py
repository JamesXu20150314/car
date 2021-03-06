#!/usr/bin/python
import sys
import random
import time

if len(sys.argv) < 2:
    print ('Usage:<filename> <k> [nfold = 5]')
    exit(0)

tt = time.time()
#print 'Time:' + str( tt )
random.seed( tt )

k = int( sys.argv[2] )
if len(sys.argv) > 3:
    nfold = int( sys.argv[3] )
else:
    nfold = 5

fi = open( sys.argv[1], 'r' )
ftr = open( sys.argv[1]+'.train', 'w' )
fvl = open( sys.argv[1]+'.valid', 'w' )
for l in fi:    
    #validation set should not be too large
    #k can be changed to provide more power(though this already random selected)
    if random.randint( 1 , nfold ) == k:
        fvl.write( l )
    else:
        ftr.write( l )

fi.close()
ftr.close()
fvl.close()

