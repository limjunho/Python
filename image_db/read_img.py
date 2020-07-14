import mysql.connector
from mysql.connector import Error

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

def readBLOB(number, photo):
    print("Reading BLOB data from images table")

    try:
        connection = mysql.connector.connect(host='192.168.1.8',
                                             database='image_db',
                                             user='junho',
                                             password='george7790')

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT * from images where id = %s"""

        cursor.execute(sql_fetch_blob_query, (number,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            image = row[2]
            print("Storing employee image on disk \n")
            write_file(image, photo)

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

readBLOB(1, "lena512.bmp")
