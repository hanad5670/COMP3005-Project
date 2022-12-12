CREATE TABLE USERS (
    userId       VARCHAR(15)     NOT NULL,
    password     VARCHAR(254)     NOT NULL,
    email_address     VARCHAR(254)  UNIQUE NOT NULL,
    name       VARCHAR(31)     NOT NULL,
    address     VARCHAR(30)  NOT NULL,
    phone_number         CHAR(10)             NOT NULL,
    credit_card CHAR(16) NOT NULL,
    PRIMARY KEY (userId)
);

CREATE TABLE BOOK (
    ISBN         CHAR(13)    NOT NULL,
    title        VARCHAR(31)     NOT NULL,
    quantity    INT NOT NULL,
    number_of_pages INT NOT NULL,
    price FLOAT(2) NOT NULL,
    total_sales FLOAT(2) NOT NULL,
    PRIMARY KEY (ISBN)
);

CREATE TABLE ORDERS (
    order_number       SERIAL     NOT NULL,
    total_price            FLOAT(2)             NOT NULL,
    track_info INT NOT NULL,
    PRIMARY KEY (order_number)
);

CREATE TABLE PUBLISHER (
    publishersId       SERIAL     NOT NULL,
    email_address     VARCHAR(254) UNIQUE NOT NULL,
    name       VARCHAR(31)     NOT NULL,
    address     VARCHAR(30)  NOT NULL,
    banking_account CHAR(16) NOT NULL,
    PRIMARY KEY (publishersId)
);

CREATE TABLE GETS (
    ISBN         CHAR(13)    NOT NULL,
    order_number         SERIAL       NOT NULL,
    num_bought INT NOT NULL,
    PRIMARY KEY (ISBN, order_number),
    FOREIGN KEY (ISBN) REFERENCES BOOK(ISBN),
    FOREIGN KEY (order_number) REFERENCES ORDERS(order_number)
);

CREATE TABLE CHECKS_OUT (
    userId       VARCHAR(15)     NOT NULL,
    order_number         SERIAL      NOT NULL,
    chk_address     VARCHAR(30)  NOT NULL,
    chk_email_address     VARCHAR(254) NOT NULL,
    chk_phone_number      CHAR(10)   NOT NULL,
    chk_credit_card CHAR(16) NOT NULL,
    PRIMARY KEY (userId, order_number),
    FOREIGN KEY (userId) REFERENCES USERS(userId),
    FOREIGN KEY (order_number) REFERENCES ORDERS(order_number)
);
CREATE TABLE PUBLISHES (
    ISBN         CHAR(13)    NOT NULL,
    publishersId       SERIAL  NOT NULL,
    percentage FLOAT(4),
    PRIMARY KEY (ISBN,publishersId),
    FOREIGN KEY (ISBN) REFERENCES BOOK(ISBN),
    FOREIGN KEY (publishersId) REFERENCES PUBLISHER(publishersId)
);

CREATE TABLE PHONE_NUMBER (
    publishersId       SERIAL   NOT NULL,
    phone_number         CHAR(10)             NOT NULL,
    PRIMARY KEY (publishersId, phone_number),
    FOREIGN KEY (publishersId) REFERENCES PUBLISHER(publishersId)
);

CREATE TABLE GENRE (
    ISBN         CHAR(13)    NOT NULL,
    genre        VARCHAR(31)     NOT NULL,
    PRIMARY KEY (ISBN, genre),
    FOREIGN KEY (ISBN) REFERENCES BOOK(ISBN)
);

CREATE TABLE AUTHOR (
    ISBN         CHAR(13)    NOT NULL,
    author        VARCHAR(31)     NOT NULL,
    PRIMARY KEY (ISBN, author),
    FOREIGN KEY (ISBN) REFERENCES BOOK(ISBN)
);
