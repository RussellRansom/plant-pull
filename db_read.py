import sqlite3
import mountainorchids

def check_begonias():
	conn = sqlite3.connect('plants.db')

	c = conn.cursor()
	c.execute("SELECT * from plants WHERE qty  > 0")

	results = c.fetchall()
	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	conn.close()
	return results


