import sqlite3
import mountainorchids

conn = sqlite3.connect('plants.db')

c = conn.cursor()

def check_begonias(c):

	c.execute("SELECT * from plants WHERE qty  > 0")

	results = c.fetchall()
	return results

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.

print(check_begonias(c))
conn.close()

