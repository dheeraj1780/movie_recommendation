import mysql.connector


def recommend(usn,pwd):
    user = mysql.connector.connect(host="localhost", user="root", password="navya",database="mov_recommend")

    mycursor = user.cursor(dictionary=True)

    row = "SELECT * FROM user WHERE username = %s and password = %s "

    mycursor.execute(row , (usn,pwd))

    result = mycursor.fetchone()

    points={}

    for index, (key, value) in enumerate(result.items()):
        if index >= 3:
            points[key] = value


    points = dict(sorted(points.items() , key = lambda item: item[1] , reverse = True))

    maxi_points = []
    count = 0

    for i in points:
        maxi_points.append(i)
        count += 1
        if count>=3:
            break


    #print(maxi_points)

    mycursor.close()
    user.close()

    movie = mysql.connector.connect(host="localhost", user="root", password="navya",database="mov_recommend")

    mycursor = movie.cursor()

    mycursor.execute("SELECT * FROM movie")

    result = mycursor.fetchall()

    #print(result)

    mycursor.close()
    movie.close()
    
    r_movies = []
    nr_movies = []

    for i in result:
        if i[1] in maxi_points or i[2] in maxi_points or i[3] in maxi_points:
            r_movies.append(i[0])


    if r_movies:
        print("Recommended Movies")
        print(r_movies)
    else:
        print("No recommended movies available")

    for i in result:
        if i not in r_movies:
            nr_movies.append(i[0])

    print("Some more available movies")
    print(nr_movies)

    
            
