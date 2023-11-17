import mysql.connector

user = mysql.connector.connect(host="localhost", user="root", password="navya",database="mov_recommend")

mycursor = user.cursor()


def create_account():
    name = input("Enter your name: ")
    username = input("Kindly type a unique username: ")
    password = input("Give a password for your account: ")
    print("Your account has been created successfully")
    print("Please pick your wishlist. From the below which kind of movies do you like to watch.")
    print("1.action\n2.comedy\n3.drama\n4.sci_fi\n5.fantasy\n6.horror\n7.thriller\n8.mystery\n9.romance\n10.adventure\n11.animation\n12.family\n13.musical\n14.historical\n15.war\n16.western\n17.crime\n18.documentary\n19.sports\n20.biography")
    genre = input("Please choose any three: ")
    genres = genre.split(',')

    key = f"INSERT INTO user (name,username,password,{genres[0]},{genres[1]},{genres[2]}) VALUES (%s,%s,%s,%s,%s,%s)"
    value = (name,username,password,10,10,10)

    mycursor.execute(key,value)

    user.commit()
    user.close()
        

def login():
    username = input("Kindly type your username: ")
    password = input("Type your password: ")

    select_user = "SELECT * FROM user WHERE username = %s"

    mycursor.execute(select_user,(username,))
    result = mycursor.fetchone()

    if result:
        if result[2] == password:
            print("Login successful!!")
            return [username,password]
        else:
            print("Incorrect password")
    else:
        print("Incorrect username")
        
        

