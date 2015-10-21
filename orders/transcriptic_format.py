import sys 
import uuid

print 'mutant_label,oligo_label,sequence,scale,purification'

for line in sys.stdin:
  spl = line.strip( ).split( )
  mutant = spl[0]
  oligos = spl[1:]

  for index, oligo in enumerate( oligos ):
    if len( oligo ) > 32:
      print '{0},{0}_{1},{2},25nm,standard'.format( mutant, 'oligo{}'.format( index ), oligo ) 
