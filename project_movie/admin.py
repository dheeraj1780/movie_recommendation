import mysql.connector

###table user
#user = mysql.connector.connect(host="localhost", user="root", password="navya",database="mov_recommend")

#mycursor = user.cursor()
#------------------------------------------------------------------------------------------------------------------
###table movie
movie = mysql.connector.connect(host="localhost", user="root", password="navya",database="mov_recommend")

mycursor = movie.cursor()

#--------------------------------------------------------------------------------------------------------------------------

###creating a table user
#mycursor.execute("CREATE TABLE user (name VARCHAR(255) , username VARCHAR(255) , password VARCHAR(255) , action INT DEFAULT 0, comedy INT DEFAULT 0, drama INT DEFAULT 0, sci_fi INT DEFAULT 0, fantasy INT DEFAULT 0, horror INT DEFAULT 0, thriller INT DEFAULT 0, mystery INT DEFAULT 0, romance INT DEFAULT 0, adventure INT DEFAULT 0, animation INT DEFAULT 0, family INT DEFAULT 0, musical INT DEFAULT 0, historical INT DEFAULT 0, war INT DEFAULT 0, western INT DEFAULT 0, crime INT DEFAULT 0, documentary INT DEFAULT 0, sports INT DEFAULT 0, biography INT DEFAULT 0)")

#-----------------------------------------------------------------------------------------------------------------------

###creating a table movie
#mycursor.execute("CREATE TABLE movie (name VARCHAR(255) , genre1 VARCHAR(255) DEFAULT 'None' , genre2 VARCHAR(255) DEFAULT 'None' , genre3 VARCHAR(255) DEFAULT 'None')")

#-----------------------------------------------------------------------------------------------------------------------

###inserting values in movie table
# key = "INSERT INTO movie (name,genre1,genre2) VALUES (%s,%s,%s)"
# value = ('Maayon','thriller','mystery')

# mycursor.execute(key,value)
# movie.commit()

#-----------------------------------------------------------------------------------------------------------------------

###To view the contents of a table
# mycursor.execute("SELECT * FROM movie")

# rows = mycursor.fetchall()

# for row in rows:
#     print(row)

