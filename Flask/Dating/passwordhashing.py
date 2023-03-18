import MySQLdb
from werkzeug.security import generate_password_hash, check_password_hash

# Connect to MySQL database
db = MySQLdb.connect(host='localhost', user='root',
                     passwd='P@ssw0rd1234567', db='dating')
cursor = db.cursor()

# Select column to hash
column_name = 'password'

# Retrieve data from the column
query = f"SELECT {column_name} FROM user"
cursor.execute(query)
rows = cursor.fetchall()

# Iterate through rows and hash the column value
for row in rows:
    value = row[0]
    hashed_value = generate_password_hash(value, method='sha256')

    # Update the row with the hashed value
    update_query = f"UPDATE user SET {column_name} = %s WHERE {column_name} = %s"
    cursor.execute(update_query, (hashed_value, value))

# Commit changes and close connection
db.commit()
cursor.close()
db.close()
