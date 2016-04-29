# Python Scripts
  
1. **finalresults.py** - Script that takes one word as an argument & replies with the total number of occurences for the word in the stream. If no arguments are passed, script will return all words in stream & their total number of occurences, sorted alphabetically in ascending order.   
    
  EX:   
  $ python finalresults.py hello  
  $ Total number of occurences of 'hello': 10  
  $  
  $ python finalresults.py  
  $ (Also, 2)  
  $ (Amazing, 1)  
  $ (Americans, 3)  
  $   ...  
  $   ..  
        
2. **histogram.py** - Script that takes two integers (k1, k2) & returns all words in the stream that have a greater (or equal) number of occurences than k1 & less (or equal number of) occurances than k2.  
    
EX: 
  $ python histogram.py 3,8  
  $ (Announces, 7)  
  $ (At, 4)  
  $ (Day, 3)  
  $   ...  
  $   ..  
