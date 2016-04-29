import sys
import psycopg2

if len(sys.argv) == 1:
  conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
  cur = conn.cursor()
  
  #Query - No args
  cur.execute("SELECT word, count FROM Tweetwordcount ORDER BY word, count")
  records = cur.fetchall()
  for rec in records:
    print "(%s, %d)" %(rec[0], rec[1]), "\n"
  
  conn.commit()
  conn.close()

elif len(sys.argv) == 2:
  word=str(sys.argv[1])
  
  conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
  cur = conn.cursor()
  
  #Query - arg
  cur.execute("SELECT word, count FROM Tweetwordcount WHERE word=%s",[word])
  records = cur.fetchall()
  for rec in records:
    print "Total number of occurences of '%s': %d" %(rec[0], rec[1]), "\n"
  
  conn.commit()
  conn.close()

else:
  print 'Woww there cowboy, please limit yourself to just one word at a time!'
