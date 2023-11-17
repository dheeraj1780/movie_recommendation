import mysql.connector

def update_points(mov,usn,pwd):
    movie = mysql.connector.connect(host="localhost", user="root", password="navya",database="mov_recommend")

    mycursor = movie.cursor()

    stmt = "SELECT genre1 , genre2 , genre3 FROM movie WHERE name = %s"

    mycursor.execute(stmt , (mov,))

    result = mycursor.fetchone()

    results = list(result)

    for i in range(3):
        if results[i] == 'None':
            results.pop()

    #print(results)

    mycursor.close()
    movie.close()

    user = mysql.connector.connect(host="localhost", user="root", password="navya",database="mov_recommend")

    mycursor = user.cursor()

    for i in range (len(results)):
        stmt = f"UPDATE user SET {results[i]} = {results[i]} + %s WHERE username = %s and password = %s"
        mycursor.execute(stmt, (5,usn,pwd))
        user.commit()

    mycursor.close()
    user.close()

    

