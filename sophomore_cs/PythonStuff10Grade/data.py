#Paste in this code, then test the 3 different read commands.
with open('2012_SAT_Results.csv','r') as text:
  #UNCOMMENT ONE of these:
  #something = text.read()
  something3 = text.read(8)
  for i in range(35):
      something2 = text.read(20)
      print(something2)
  for i in range(20):
      something = text.read()
  print(something)

#eol = end of line
#eof = end of file
  
  
+