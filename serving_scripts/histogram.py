import sys
import string
import psycopg2

if len(sys.argv) == 1:
  print 'Enter an occurance range separated by a comma'

elif len(sys.argv) == 2:
  range=str(sys.argv[1])
  range_split = string.split(range,',')
  low= range_split[0]
  high = range_split[1]
  
  conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
  cur = conn.cursor()
  
  #Query - arg
  cur.execute("SELECT word, count FROM Tweetwordcount WHERE count >= %d AND count <= %d ORDER BY word, count", (low,high))
  records = cur.fetchall()
  for rec in records:
    print "(%s, %d)" %(rec[0], rec[1]), "\n"
  
  conn.commit()
  conn.close()

else:
  print 'Limit your range to two integers separated by a comma'
