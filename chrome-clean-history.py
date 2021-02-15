import sqlite3
import sys

userStr = str(sys.argv[1])
urlStr = str(sys.argv[2])

# establish the connection with 
# history database file which is 
# located at given location 
# you can search in your system 
# for that location and provide 
# the path here 
print ("C:\\Users\\" + userStr + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History")
conn = sqlite3.connect("C:\\Users\\" + userStr + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History") 

# point out at the cursor 
c = conn.cursor() 

# create a variable id 
# and assign 0 initially 
id = 0

# create a variable result 
# initially as True, it will 
# be used to run while loop 
result = True

# create a while loop and put 
# result as our condition 
while result: 
	
	result = False
	
	# a list which is empty at first, 
	# this is where all the urls will 
	# be stored 
	ids = [] 
	
	# we will go through our database and 
	# search for the given keyword 
	sqlStr = "SELECT id,url FROM urls WHERE url LIKE '%" + urlStr + "%'"
	print (sqlStr)
	for rows in c.execute(sqlStr): 
		
		# this is just to check all 
		# the urls that are being deleted 
		print(rows) 
		
		# we are first selecting the id 
		id = rows[0] 
		
		# append in ids which was initially 
		# empty with the id of the selected url 
		ids.append((id,)) 
		
	# execute many command which is delete 
	# from urls (this is the table) 
	# where id is ids (list having all the urls) 
	c.executemany('DELETE from urls WHERE id = ?',ids) 
	
	# commit the changes 
	conn.commit() 
	
# close the connection 
conn.close() 
