import sys 
import uuid

print 'mutant_label,sequencing_primer,oligo_label,sequence,scale,purification'

for line in sys.stdin:
  spl = line.strip( ).split( )
  mutant = spl[0]
  oligos = spl[1:]

  for index, oligo in enumerate( oligos ):
    if len( oligo ) > 32:
      print '%s,NA,%s,%s,25nm,standard' % ( mutant, 'oligo{}'.format( index ), oligo ) 
