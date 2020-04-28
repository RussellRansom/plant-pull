import sqlite3
import mountainorchids

conn = sqlite3.connect('plants.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS plants
             (id text PRIMARY KEY, name text, qty int, price real)''')



begonias = mountainorchids.get_begonias()

for begonia in begonias:
	# Insert a row of data
	print(begonia)
	c.execute("INSERT INTO plants VALUES ('{}', '{}', {}, {}) ON CONFLICT(id) DO UPDATE SET qty={}, price={}".format(begonia['item_id'], begonia['name'], begonia['quantity'], begonia['price'], begonia['quantity'], begonia['price']))

	# Save (commit) the changes
	conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

