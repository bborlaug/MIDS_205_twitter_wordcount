import sys
import psycopg2

if len(sys.argv) == 1:
  conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
  cur = conn.cursor()
  
  #Query - No args
  cur.execute("SELECT word, count FROM Tweetwordcount ORDER BY word, count")
  records = cur.fetchall()
  for rec in records:
    print "word = ", rec[0]
    print "count = ", rec[1], "\n"
  
  conn.commit()
  conn.close()

elif len(sys.argv) == 2:
  print str(sys.argv[1])
  
  conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
  cur = conn.cursor()
  
  #Query - arg
  cur.execute("SELECT word, count FROM Tweetwordcount WHERE word=%s", word)
  records = cur.fetchall()
  for rec in records:
    print "word = ", rec[0]
    print "count = ", rec[1], "\n"
  
  conn.commit()
  conn.close()

else:
  print 'Woow there cowboy, please limit yourself to just one argument at a time!'
