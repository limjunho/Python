import mysql.connector
from mysql.connector import Error

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(number, name, photo):
    print("Inserting BLOB into images table")
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='image_db',
                                             user='junho',
                                             password='passwd123')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO images
                          (id, name, photo) VALUES (%s,%s,%s)"""

        Picture = convertToBinaryData(photo)

        # Convert data into tuple format
        insert_blob_tuple = (number, name, Picture) 
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple) 
        connection.commit()
        print("Image and file inserted successfully as a BLOB into images table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertBLOB(None, "test1", "lena512.bmp")
