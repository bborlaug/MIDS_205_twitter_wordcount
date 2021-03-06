from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt



class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        #self.redis = StrictRedis()

    def process(self, tup):
        word = tup.values[0]

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.
        
	import psycopg2
	
	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
            
	cur = conn.cursor()
            
	if self.counts[word]<1:
        	# Insert word into db
                cur.execute("INSERT INTO Tweetwordcount (word,count) \
      VALUES (%s, 1)", [word]);
                conn.commit()
                self.counts[word] +=1
	else:
                #Update word count
                #Assuming you are passing the tuple (uWord, uCount) as an argument
                self.counts[word] += 1
                cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s", (self.counts[word], word))
                conn.commit()

        # Increment the local count
        # self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
