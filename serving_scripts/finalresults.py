import sys

if len(sys.argv) == 1:
  print 'No args, really??'

elif len(sys.argv) == 2:
  print str(sys.argv[2])

else:
  print 'Woow there cowboy, please limit yourself to just one argument at a time!'
