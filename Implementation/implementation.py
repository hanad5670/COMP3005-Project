import psycopg2

#-------------------------------------------------HELPER FUNCTIONS-------------------------------------------------#


def connectToDataBase():

    connection = psycopg2.connect(
        host="localhost",
        database="FinalProject",
        user="postgres",
        password="COMP3005FP")

    return connection, connection.cursor()

# Checking if number input can be made a float


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def closeConnection(connection, cursor):
    connection.close()
    cursor.close()


def validator(max, value, exitVal=None):
    if (value == exitVal):
        return exitVal
    while (not (value.isdigit() and 1 <= int(value) <= max)):
        print("Error: please enter a valid number between 1 and", max)
        value = input("Enter the number of the option you would like:")

    return int(value)

# Function to add Genres


def addGenre(genreList, genre):
    match genre:
        case 1:
            genreList.append("Fiction")

        case 2:
            genreList.append("Non-Fiction")

        case 3:
            genreList.append("Fantasy")

        case 4:
            genreList.append("SciFi")

        case 5:
            genreList.append("Action")

        case 6:
            genreList.append("Adventure")

        case 7:
            genreList.append("Comedy")

        case 8:
            genreList.append("Drama")

        case _:
            return

#-------------------------------------------------------LOGIN + SIGNUP----------------------------------------------#
# SIGNUP FUNCTION


def signUp(cur, conn):
    print("/****************************/\n")
    print("Enter your new user information:\n")

    # User Validation
    username = input("Username: ")
    username = username.lower()
    cur.execute("SELECT userid from users where userid='" +
                username + "'")
    possibleUsr = cur.fetchone()

    while ((possibleUsr != None) or (len(username) > 15 or len(username) < 1)):
        if (possibleUsr != None):
            print("Error: Username is already taken")

        else:
            print("Invalid input. username must be between 1 and 15 characters")

        username = input("Username: ")
        username = username.lower()
        cur.execute("SELECT userid from users where userid='" +
                    username + "'")
        possibleUsr = cur.fetchone()

    # Password Validation
    password = input("Password: ")

    while (len(password) > 254 or len(password) < 1):
        print("Invalid input. password must be between 1 and 254 characters")
        password = input("Password: ")

    # Email Validation
    email = input("Email Address: ")
    email = email.lower()
    cur.execute("SELECT email_address from users where email_address='" +
                email + "'")
    possibleEmail = cur.fetchone()

    while ((possibleEmail != None) or (len(email) > 254 or len(email) < 1)):
        if (possibleEmail != None):
            print("Error: email is already in use")

        else:
            print("Invalid input. email must be between 1 and 254 characters")

        email = input("Email Address: ")
        email = email.lower()
        cur.execute("SELECT email_address from users where email_address='" +
                    email + "'")
        possibleEmail = cur.fetchone()

    # Name Validation
    name = input("Name: ")
    while (len(name) > 31 or len(name) < 1):
        print("Invalid input. name must be between 1 and 31 characters")
        name = input("Name: ")

    # Address Validation
    address = input("Address: ")
    while (len(address) > 31 or len(address) < 1):
        print("Invalid input. address must be between 1 and 31 characters")
        address = input("Address: ")

    # Phone Number Validation
    phoneNum = input("Phone Number: ")
    while (len(phoneNum) != 10 or (not phoneNum.isdigit())):
        print("Invalid input. phone number must be a 10 digit number")
        phoneNum = input("Phone Number: ")

    # Credit Card Validation
    creditCard = input("Credit Card Number: ")
    while (len(creditCard) != 16 or (not creditCard.isdigit())):
        print("Invalid input. credit card number must be a 16 digit number")
        creditCard = input("Credit Card Number: ")

    cur.execute("""INSERT into USERS (userid, email_address, name, address, phone_number, credit_card, password)
                 VALUES (%s, %s, %s,%s, %s,%s, %s);""",
                (username, email, name, address, phoneNum, creditCard, password))
    conn.commit()

    return username


def login(cur, conn):
    print("/****************************/\n")
    print("Please enter your login credentials:\n")

    username = input("Username: ")
    password = input("Password: ")
    cur.execute("SELECT userid, password from users where userid='" +
                username + "' and password='" + password + "'")
    user = cur.fetchone()

    while (user == None):
        signup = input(
            "Invalid username or password. Enter 1 to try again or 2 to create a new account: ")
        signup = validator(2, signup)

        if (signup == 1):
            username = input("Username: ")
            password = input("Password: ")
            cur.execute("SELECT userid, password from users where userid='" +
                        username + "' and password='" + password + "'")
            user = cur.fetchone()

        else:
            user = signUp(cur, conn)
            return user

    return user[0]

#---------------------------------------------------------ADD AND REMOVE BOOKS------------------------------------------------#
# Adding Publisher Function:


def addPublisher(cur):

    print("/****************************/\n")
    print("PUBLISHER INFORMATION\n")

    # Email Validation
    pubEmail = input("Email Address: ")
    pubEmail = pubEmail.lower()
    cur.execute("SELECT email_address from PUBLISHER where email_address='" +
                pubEmail + "'")
    possiblePemail = cur.fetchone()

    while ((possiblePemail != None) or (len(pubEmail) > 254 or len(pubEmail) < 1)):
        if (possiblePemail != None):
            cur.execute(
                "SELECT publishersId FROM Publisher WHERE email_address='" + possiblePemail[0] + "'")
            publisher = cur.fetchall()
            return publisher[0]

        else:
            print("Invalid input. email must be between 1 and 254 characters")

        pubEmail = input("Email Address: ")
        pubEmail = pubEmail.lower()
        cur.execute("SELECT email_address from PUBLISHER where email_address='" +
                    pubEmail + "'")
    possiblePemail = cur.fetchone()

    # Name Validation
    name = input("Name: ")
    while (len(name) > 31 or len(name) < 1):
        print("Invalid input. name must be between 1 and 31 characters")
        name = input("Name: ")

    # Address Validation
    address = input("Address: ")
    while (len(address) > 31 or len(address) < 1):
        print("Invalid input. address must be between 1 and 31 characters")
        address = input("Address: ")

    # Bank Validation:
    bank = input("Bank Number: ")
    while (len(bank) != 16 or (not bank.isdigit())):
        print("Invalid input. enter a 16 digit bank number")
        bank = input("Bank Number: ")

    # Phone Num Validation
    phoneNums = []
    phone = input(
        "Enter all phone numbers for publisher. Type q when done: ")

    while (phone != 'q' or phoneNums == []):
        if (phoneNums == [] and phone == 'q'):
            print("Error: must have at least one phone number")

        while ((not phone.isdigit()) or (len(phone) != 10)):
            print("Invalid input. Enter a 10 digit phone number")
            phone = input(
                "Enter all phone numbers for publisher: ")

        phoneNums.append(phone)

        phone = input(
            "Enter all phone numbers for publisher. Type q when done: ")

    cur.execute("""INSERT into PUBLISHER (email_address, name, address, banking_account )
                 VALUES (%s, %s, %s,%s);""",
                (pubEmail, name, address, bank))

    for p in phoneNums:
        cur.execute("SELECT publishersId from PUBLISHER where email_address='" +
                    pubEmail + "'")
        pid = cur.fetchone()
        cur.execute("""INSERT into PHONE_NUMBER (publishersId, phone_number)
                 VALUES (%s, %s);""",
                    (pid, p))

    return pid


def addBookToStore(cur, conn):

    # ISBN Validation:
    isbn = input("ISBN: ")
    cur.execute("SELECT ISBN from BOOK where ISBN='" +
                isbn + "'")
    possibleISBN = cur.fetchone()

    while ((possibleISBN != None) or (not isbn.isdigit()) or (len(isbn) != 13)):
        if (possibleISBN != None):
            print("Error: book with this ISBN already exists")

        else:
            print("Invalid input. isbn must be a 13 digit number")

        isbn = input("ISBN: ")
        cur.execute("SELECT ISBN from BOOK where ISBN='" +
                    isbn + "'")
        possibleISBN = cur.fetchone()

    # Title Validation
    title = input("Title: ")
    while (len(title) > 31 or len(title) < 1):
        print("Invalid input. title must be between 1 and 31 characters")
        title = input("Title: ")

    # Quantity Validation
    quantity = input("Quantity: ")
    while ((not quantity.isdigit()) or (len(quantity) > 9 or len(quantity) < 1)):
        print("Invalid Input. please enter valid quantity of books")
        quantity = input("Quantity: ")

    quantity = int(quantity)
    if (quantity < 11 or quantity > 100):
        quantity = 100

    # Number of Pages Validation
    numPages = input("How many Pages?: ")
    while ((not numPages.isdigit()) or (len(numPages) > 9 or len(numPages) < 1)):
        print("Invalid Input. please enter a number between 1000 and 1")
        numPages = input("How many Pages?: ")

    numPages = int(numPages)
    if (numPages < 11 or numPages > 1000):
        numPages = 1000

    # Price Validation:
    price = input("Price: ")
    while ((not isfloat(price)) or (len(price) > 9 or len(price) < 1)):
        print("Invalid Input. Please enter a reasonable price for a book")
        price = input("Price: ")

    price = float(price)
    price = round(price, 2)

    # Genre choices:
    genres = []
    print("\nWhat are the genres of the book?\n")
    print("1.Fiction    2.Non-Fiction    3.Fantasy    4.SciFi    5.Action    6.Adventure    7.Comedy    8.Drama")
    print("Type q once you have finished choosing genres")
    genreInput = input("Enter your choice: ")
    genre = validator(8, genreInput, 'q')
    addGenre(genres, genre)

    while (genre != 'q' or genres == []):

        if (genres == []):
            print("Error: you must have at least one genre\n")

        print("\nWhat are the genres of the book?\n")
        print("1.Fiction    2.Non-Fiction    3.Fantasy    4.SciFi    5.Action    6.Adventure    7.Comedy    8.Drama")
        print("Type q once you have finished choosing genres")
        genreInput = input("Enter your choice: ")
        genre = validator(8, genreInput, 'q')
        addGenre(genres, genre)

    # Authors Validation:
    authors = []
    author = input(
        "Enter names of author(s) for this book. Type q when there are no names left: ")

    while (author != 'q' or authors == []):
        if (authors == [] and author == 'q'):
            print("Error: must have at least one author for a book")

        while ((len(author) > 31 or len(author) < 1)):
            print("Invalid input. Author names must be between 1 and 31 characters")
            author = input(
                "Enter names of author(s) for this book. ")

        authors.append(author)

        author = input(
            "Enter names of author(s) for this book. Type q when there are no names left: ")

        # Percentage Validation:
    percent = input("Publisher's percentage of sales (Enter as decimal): ")
    while ((not isfloat(percent)) or (len(percent) > 9 or len(percent) < 1)):
        print("Invalid Input. Please enter a reasonable percentage for the publisher")
        percent = input("Publisher's percentage of sales (Enter as decimal): ")

    percent = float(percent)
    percent = round(percent, 4)

    # ADDING BOOK PUBLISHER:
    pubID = addPublisher(cur)

    cur.execute("""INSERT into BOOK (ISBN, title, quantity, number_of_pages, price, total_sales)
                 VALUES (%s, %s, %s,%s, %s,%s);""",
                (isbn, title, int(quantity), int(numPages), price, 0))

    cur.execute("""INSERT into PUBLISHES (ISBN, publishersId, percentage)
                 VALUES (%s, %s, %s);""",
                (isbn, pubID, percent))

    for g in genres:
        cur.execute("""INSERT into GENRE (ISBN, genre)
                    VALUES (%s, %s);""",
                    (isbn, g))

    for a in authors:
        cur.execute("""INSERT into AUTHOR (ISBN, author)
                    VALUES (%s, %s);""",
                    (isbn, a))

    conn.commit()

    return isbn


def rmBookFromStore(cur, conn):
    print("/****************************/\n")

    # ISBN To Remove:
    isbn = input("ISBN of book to remove: ")
    cur.execute("SELECT ISBN from BOOK where ISBN='" +
                isbn + "'")
    possibleISBN = cur.fetchone()

    while ((possibleISBN == None)):
        print("Error: This isbn does not exist")
        isbn = input("ISBN of book to remove:")
        cur.execute("SELECT ISBN from BOOK where ISBN='" +
                    isbn + "'")
        possibleISBN = cur.fetchone()

    # Get publishers ID and check if the publisher must be removed
    cur.execute("SELECT publishersId from PUBLISHES where ISBN='" + isbn + "'")
    publisher = cur.fetchone()[0]
    cur.execute("DELETE FROM Publishes WHERE ISBN='" + isbn + "'")

    # Delete From Book, Genre and Author Tables:
    cur.execute("DELETE FROM Genre WHERE ISBN='" + isbn + "'")
    cur.execute("DELETE FROM Author WHERE ISBN='" + isbn + "'")
    cur.execute("DELETE FROM Book WHERE ISBN='" + isbn + "'")

    # Checking if publisher still has books
    cur.execute(
        "SELECT publishersId from PUBLISHES where publishersId='" + str(publisher) + "'")
    possiblePublisher = cur.fetchone()

    if (possiblePublisher == None):
        cur.execute("DELETE FROM Phone_Number WHERE publishersId='" +
                    str(publisher) + "'")

        cur.execute("DELETE FROM Publisher WHERE publishersId='" +
                    str(publisher) + "'")
        print("Publisher " + str(publisher) + " Removed")

    print("Book " + isbn + " Removed")

    conn.commit()

    # Owner Menu

#---------------------------------------------------SALES FUNCTIONS-----------------------------------------------------#


def viewReport(cur, conn):
    print("/****************************/\n")
    print("Select what sales you would like to view\n")
    print("1: Sales vs. Expenditures\n2: Sales by Author\n3: Sales by Genre")
    inputNum = input("Enter the number of the option you would like:")
    choice = validator(3, inputNum)

    match choice:
        case 1:
            viewSalesVsExp(cur)
        case 2:
            viewSalesAuth(cur)
        case 3:
            viewSalesGnr(cur)


# SALES VS EXPENDITURES:
def viewSalesVsExp(cur):
    cur.execute("SELECT ISBN, total_sales FROM BOOK")
    books = cur.fetchall()
    sales = 0
    expend = 0

    for book in books:
        isbn = str(book[0])
        sale = float(book[1])

        cur.execute(
            "SELECT percentage FROM PUBLISHES WHERE ISBN='" + isbn + "'")
        percent = float(cur.fetchone()[0])
        sales += sale
        expend += (sale * percent)

    sales = round(sales, 2)
    expend = round(expend, 2)
    print("Total Sales for ALL BOOKS: ", sales)
    print("Total Expenditures (Amount going to publishers): ",  expend)

# SALES BY GENRE


def viewSalesGnr(cur):
    print("/****************************/\n")
    cur.execute(
        "SELECT genre, total_sales FROM Genre, Book WHERE Genre.isbn = Book.isbn")
    genres = cur.fetchall()
    genreSales = {}

    for g in genres:
        genre = g[0]
        money = g[1]

        if (genre in genreSales):
            genreSales[genre] += money
        else:
            genreSales[genre] = money

    for g in genreSales:
        print("Sales for " + g + ": " + str(genreSales[g]))
    return

# SALES BY AUTHOR


def viewSalesAuth(cur):
    print("/****************************/\n")
    cur.execute(
        "SELECT author, total_sales FROM Author, Book WHERE Author.isbn = Book.isbn")
    authors = cur.fetchall()
    authorSales = {}

    for a in authors:
        author = a[0]
        money = a[1]

        if (author in authorSales):
            authorSales[author] += money
        else:
            authorSales[author] = money

    for a in authorSales:
        print("Sales for " + a + ": " + str(authorSales[a]))
    return

#----------------------------------------------------------MENUS--------------------------------------------------#


def ownerMenu(cur, conn):
    choice = 0

    while (choice != 4):
        print("/****************************/\n")
        print("ADMIN MODE\n")
        print("1: Add Book\n2: Remove Book\n3: View Sales Report\n4: Logout")
        inputNum = input("Enter the number of the option you would like:")
        choice = validator(4, inputNum)

        match choice:
            case 1:
                addBookToStore(cur, conn)

            case 2:
                rmBookFromStore(cur, conn)

            case 3:
                viewReport(cur, conn)

            case 4:
                return

            case _:
                return


def menu_for_user(userid, cur, conn):
    selection = 0
    sale = {}

    while (selection != 5):
        print("/***********************************/")
        print("Welcom To Look Inna Book store Menu: ")
        print("1. Search for book ")
        print("2. Add book to cart ")
        print("3. View Cart ")
        print("4. Log out ")
        print("/***********************************/")

        selection = input("Enter your selection (1-4): ")
        selection = validator(4, selection)

        match selection:
            case 1:
                searchBook(cur)

            case 2:
                addBook(cur, sale)

            case 3:
                viewCart(cur, conn, userid, sale)
                sale = {}

            case 4:
                print("Thank you for shopping with us !")
                selection = 5

#------------------------------------------------------------USER FUNCTIONS--------------------------------------------------------#


def addBook(cur, sale):
    # ASKS USER FOR A ISBN AND ATTEMPTS TO RETRIVE IT FROM THE DATABASE
    print("Please enter the ISBN of the book you want to purchase")
    isbn = input("ISBN: ")
    cur.execute("SELECT *  from book where isbn='" +
                isbn + "' ")
    book = cur.fetchone()

    while (book == None):
        isbn = input(
            "Invalid ISBN please enter a valid ISBN or 1 to return to main menu: ")
        if (isbn == '1'):
            return None
        cur.execute("SELECT *  from book where isbn='" +
                    isbn + "' ")
        book = cur.fetchone()

    # CHECKS IF THE DATABASE HAS THE AMOUNT OF BOOKS THE USER WANTS
    print("Please enter the how many copies of ", book[1], " you want")
    amount = input("amount: ")
    amount = validator(book[2], amount)

    # calculate total sale
    totalSale = amount * book[4]

    # keep track of ISBN, AMOUNT BOUGHT AND TOTAL SALE  FOR THE VIEW CART
    if isbn in sale:
        amount = sale.get(isbn)[0] + amount
        totalSale = sale.get(isbn)[1] + totalSale
        sale[isbn] = [amount, totalSale]
    else:
        sale[isbn] = [amount, totalSale]


def searchBook(cur):
    print("1. Search for book by author")
    print("2. Search for book by title")
    print("3. Search for book by genre")
    print("4. Search for book by ISBN")
    searchType = input("Enter a number between 1  and 4: ")
    searchType = validator(4, searchType)

    match searchType:
        case 1:
            print("Please enter the author of the book you want")
            author = input("Name: ")
            authorName = author
            cur.execute("SELECT isbn  from author where author='" +
                        author + "' ")
            author = cur.fetchall()

            while (len(author) == 0):
                author = input(
                    "Currently have no book by author enter a valid author or 1 to return to main menu: ")
                if (author == '1'):
                    return None
                cur.execute("SELECT isbn  from author where author='" +
                            author + "' ")
                author = cur.fetchall()

            print("/***********************************/")
            print("Here are the books found: ")
            for x in author:
                isbn = x[0]
                # gets books information
                cur.execute("SELECT *  from book where isbn='" +
                            isbn + "' ")
                book = cur.fetchone()
                # need to get publisher information (Should this be publisher ID? need to figure that out)
                cur.execute("SELECT PUBLISHER.name FROM PUBLISHER INNER JOIN PUBLISHES ON PUBLISHES.publishersId = PUBLISHER.publishersId where isbn='" +
                            isbn + "' ")
                publisherName = cur.fetchone()[0]

                # need to get the genre too
                cur.execute("SELECT genre FROM genre where isbn='" +
                            isbn + "' ")
                genre = cur.fetchall()

                print("ISBN:", isbn, "Author:", authorName, "Title:",
                      book[1], "Genre:", genre, "Publisher:", publisherName, "Number of pages:", book[3], "Price: $", book[4])
            print("/***********************************/")

        case 2:
            # The title is case sensitive so the title has to be the exact same from user
            print("Please enter the title of the book you want to purchase")
            title = input("Title: ")

            cur.execute("SELECT *  from book where title='" +
                        title + "' ")
            book = cur.fetchone()

            while (book == None):
                title = input(
                    "Invalid title please enter a valid title or 1 to return to main menu: ")
                if (title == '1'):
                    return None
                cur.execute("SELECT *  from book where title='" +
                            title + "' ")
                book = cur.fetchone()

            isbn = book[0]
            # need to get publisher information (Should this be publisher ID? need to figure that out)
            cur.execute("SELECT PUBLISHER.name FROM PUBLISHER INNER JOIN PUBLISHES ON PUBLISHES.publishersId = PUBLISHER.publishersId where isbn='" +
                        isbn + "' ")
            publisherName = cur.fetchone()[0]

            # need to get the author too
            cur.execute("SELECT author FROM author where isbn='" +
                        isbn + "' ")
            authorName = cur.fetchone()[0]

            cur.execute("SELECT genre FROM genre where isbn='" +
                        isbn + "' ")
            genre = cur.fetchall()
            print("/***********************************/")
            print("Here are the books found: ")
            print("ISBN:", isbn, "Author:", authorName, "Title:",
                  book[1], "Genre:", genre, "Publisher:", publisherName, "Number of pages:", book[3], "Price: $", book[4])
            print("/***********************************/")
        case 3:
            print("Please enter the genre of the book you want")
            genre = input("Genre: ")
            genreName = genre
            cur.execute("SELECT isbn  from genre where genre='" +
                        genre + "' ")
            genre = cur.fetchall()

            while (len(genre) == 0):
                genre = input(
                    "Currently have no book for that genre enter a valid genre or 1 to return to main menu: ")
                if (genre == '1'):
                    return None
                cur.execute("SELECT isbn  from genre where genre='" +
                            genre + "' ")
                genre = cur.fetchall()

            print("/***********************************/")
            print("Here are the books found: ")
            for x in genre:
                isbn = x[0]
                # gets books information
                cur.execute("SELECT *  from book where isbn='" +
                            isbn + "' ")
                book = cur.fetchone()
                # need to get publisher information (Should this be publisher ID? need to figure that out)
                cur.execute("SELECT PUBLISHER.name FROM PUBLISHER INNER JOIN PUBLISHES ON PUBLISHES.publishersId = PUBLISHER.publishersId where isbn='" +
                            isbn + "' ")
                publisherName = cur.fetchone()[0]

                # need to get the author too
                cur.execute("SELECT author FROM author where isbn='" +
                            isbn + "' ")
                authorName = cur.fetchone()[0]

                print("ISBN:", isbn, "Author:", authorName, "Title:",
                      book[1], "Genre:", genreName, "Publisher:", publisherName, "Number of pages:", book[3], "Price: $", book[4])
            print("/***********************************/")

        case 4:
            print("Please enter the ISBN of the book you want to purchase")
            isbn = input("ISBN: ")

            cur.execute("SELECT *  from book where isbn='" +
                        isbn + "' ")
            book = cur.fetchone()

            while (book == None):
                isbn = input(
                    "Invalid ISBN please enter a valid ISBN or 1 to return to main menu: ")
                if (isbn == '1'):
                    return None
                cur.execute("SELECT *  from book where isbn='" +
                            isbn + "' ")
                book = cur.fetchone()

            # need to get publisher information (Should this be publisher ID? need to figure that out)
            cur.execute("SELECT PUBLISHER.name FROM PUBLISHER INNER JOIN PUBLISHES ON PUBLISHES.publishersId = PUBLISHER.publishersId where isbn='" +
                        isbn + "' ")
            publisherName = cur.fetchone()[0]

            # need to get the author too
            cur.execute("SELECT author FROM author where isbn='" +
                        isbn + "' ")
            authorName = cur.fetchone()[0]

            cur.execute("SELECT genre FROM genre where isbn='" +
                        isbn + "' ")
            genre = cur.fetchall()
            print("/***********************************/")
            print("Here are the books found: ")
            print("ISBN:", isbn, "Author:", authorName, "Title:",
                  book[1], "Genre:", genre, "Publisher:", publisherName, "Number of pages:", book[3], "Price: $", book[4])
            print("/***********************************/")


def viewCart(cur, conn, userid, sale):
    completeSale = 0
    if (len(sale) == 0):
        return print("Your cart is currently empty.")

    print("/***********************************/")
    print("Here is what is currently in your cart: ")
    for keys in sale:
        completeSale += sale.get(keys)[1]
        print("ISBN: ", keys, "Number of books: ", sale.get(keys)
              [0], " Total amount owed: $", sale.get(keys)[1])
    print("Total: $", completeSale)
    print("/***********************************/")

    print("Please enter 2 to move to check out or 1 to return to store: ")
    check = input("Enter(1 or 2): ")
    check = validator(2, check)

    if check == 1:
        return

    print("Please enter 2 if billing and shipping information is the same else enter 1: ")
    check = input("Enter(1 or 2): ")
    check = validator(2, check)

    if check == 1:
        print("here!")
        # email Validation
        email = input("Name: ")
        while (len(email) > 254 or len(email) < 1):
            print("Invalid email. email must be between 1 and 254 characters")
            email = input("Email: ")

        # Address Validation
        address = input("Address: ")
        while (len(address) > 31 or len(address) < 1):
            print("Invalid input. address must be between 1 and 31 characters")
            address = input("Address: ")

        # Phone Number Validation
        phoneNum = input("Phone Number: ")
        while (len(phoneNum) != 10 or (not phoneNum.isdigit())):
            print("Invalid input. phone number must be a 10 digit number")
            phoneNum = input("Phone Number: ")

        # Credit Card Validation
        creditCard = input("Credit Card Number: ")
        while (len(creditCard) != 16 or (not creditCard.isdigit())):
            print("Invalid input. credit card number must be a 16 digit number")
            creditCard = input("Credit Card Number: ")

    else:
        cur.execute("SELECT * FROM users where users.userid='" +
                    userid + "' ")
        userinfo = cur.fetchall()[0]
        email = userinfo[2]
        address = userinfo[4]
        phoneNum = userinfo[5]
        creditCard = userinfo[6]

    cur.execute("""INSERT into orders (total_price,track_info)
                 VALUES (%s, %s);""",
                (completeSale, 3))

    cur.execute("SELECT LASTVAL() ")
    order_number = cur.fetchone()[0]

    cur.execute("""INSERT into checks_out (userid, order_number, chk_address, chk_email_address, chk_phone_number, chk_credit_card)
                 VALUES (%s, %s, %s, %s, %s, %s);""",
                (userid, order_number, address, email, phoneNum, creditCard))

    for keys in sale:
        cur.execute("""INSERT into GETS (ISBN, order_number, num_bought)
                 VALUES (%s, %s, %s);""",
                    (keys, order_number, sale.get(keys)[0]))

        cur.execute("SELECT *  from book where isbn='" +
                    keys + "' ")
        book = cur.fetchone()

        quantity = book[2]
        total_Sale = book[5]

        if quantity - sale.get(keys)[0] < 10:
            quantity = 100
        else:
            quantity -= sale.get(keys)[0]

        total_Sale += sale.get(keys)[1]

        cur.execute("UPDATE book SET quantity = " +
                    str(quantity) + " WHERE isbn = '" + keys + "'",)
        cur.execute("UPDATE book SET total_sales = " +
                    str(total_Sale) + " WHERE isbn = '" + keys + "'",)

    conn.commit()
    print("Order Complete")
#------------------------------------------------------------LOGIC FOR FULL APP-----------------------------------------------------#


def startMenu():
    conn, cur = connectToDataBase()
    userid = ""

    print("/****************************/\n")
    print("Welcome to Look Inna Book! Please choose one of the options:\n")
    print("1: Login\n2: Sign up\n3: Quit")
    inputNum = input("Enter the number of the option you would like:")
    choice = validator(3, inputNum)

    match choice:
        case 1:
            userid = login(cur, conn)

        case 2:
            userid = signUp(cur, conn)

        case 3:
            return

        case _:
            return

    if (userid == "Owner"):
        ownerMenu(cur, conn)

    else:
        menu_for_user(userid, cur, conn)

    closeConnection(cur, conn)


#---------------------------------------------------MAIN-----------------------------------------------#
if __name__ == "__main__":
    startMenu()
