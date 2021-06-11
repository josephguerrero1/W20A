import dbcreds
import mariadb
import dbconnect
import traceback

# Option 1: Write a new post


def newPost():
    conn = dbconnect.get_db_connection()
    cursor = dbconnect.get_db_cursor(conn)
    if(conn == None or cursor == None):
        print("Error in database connection!")
        dbconnect.close_db_cursor(cursor)
        dbconnect.close_db_connection(conn)
        return
    try:
        content = input("Enter blog post content: ")
        cursor.execute(
            f"INSERT INTO blog_post(username, content) VALUES('{username}', '{content}')")
        conn.commit()
    except:
        print("Error in posting content!")
        traceback.print_exc()
    dbconnect.close_db_cursor(cursor)
    dbconnect.close_db_connection(conn)

# Option 2: See all other posts


def viewPosts():
    conn = dbconnect.get_db_connection()
    cursor = dbconnect.get_db_cursor(conn)
    if(conn == None or cursor == None):
        print("Error in database connection!")
        dbconnect.close_db_cursor(cursor)
        dbconnect.close_db_connection(conn)
        return
    try:
        cursor.execute(
            "SELECT * FROM blog_post")
        content_rows = cursor.fetchall()
        for content in content_rows:
            print(f"Username: {content[0]}           Content: {content[1]}")
    except:
        print("Something went wrong viewing all the posts!")
        traceback.print_exc()
    dbconnect.close_db_cursor(cursor)
    dbconnect.close_db_connection(conn)


# Created a variable "username" to store what the user types in as their username.
# Used the input function so the user can type in their username as a string data type.
# Used a while True loop to create an infinite loop.

while True:

    username = input("Enter your username: ")

    print("Please select an option:")

    print("Write a new post: 1")
    print("See all other posts: 2")

    selection = input("Selection: ")
    intSelection = int(selection)

    # Will run whichever function is needed based on what option the user selected.

    if(intSelection == 1):
        newPost()
        print("Content has been posted successfully!")
    elif(intSelection == 2):
        viewPosts()
    else:
        print("Invalid Selection!")

    # User can enter Y or N to exit the application, breaking the while loop, or keep it going, by entering N.

    endLoop = input("Exit application? Enter Y or N: ")

    if(endLoop == "Y"):
        break
