insert into USERS (userid, password, email_address, name, address, phone_number, credit_card) values ('Owner', 'passw0rd', 'owner@lookingabook.com', 'Owner Owner', '123 Simson Street', '6133430000', '1234567890123456');
insert into USERS (userid, password, email_address, name, address, phone_number, credit_card) values ('talbert1', 'sxocPPa', 'talbert1@posterous.com', 'Tore Albert', '728 Maple Wood Junction', '6822185694', '5002350897565582');
insert into USERS (userid, password, email_address, name, address, phone_number, credit_card) values ('bgoggins2', 'uWAFeov', 'bgoggins2@wikipedia.org', 'Beltran Goggins', '8 Hauk Pass', '6317027839', '5002351269911248');
insert into USERS (userid, password, email_address, name, address, phone_number, credit_card) values ('dmarnes3', 'WwtWpHVl', 'dmarnes3@ucsd.edu', 'Dotti Marnes', '1758 3rd Terrace', '2814414449', '5010123880860041');
insert into USERS (userid, password, email_address, name, address, phone_number, credit_card) values ('kprobart4', 'GXQ88qhf', 'kprobart4@paypal.com', 'Katrine Probart', '9837 Del Mar Pass', '4709671923', '5010122716244248');
insert into USERS (userid, password, email_address, name, address, phone_number, credit_card) values ('ccrummy5', 'zurvZ67aD', 'ccrummy5@ycombinator.com', 'Corey Crummy', '8785 Elka Junction', '9003672409', '5010127496684943');
insert into USERS (userid, password, email_address, name, address, phone_number, credit_card) values ('clattie6', 'EwmNlK8zju', 'clattie6@odnoklassniki.ru', 'Codie Lattie', '010 Artisan Center', '7137274465', '5007668045438906');
insert into USERS (userid, password, email_address, name, address, phone_number, credit_card) values ('daldren7', '941ULgX', 'daldren7@noaa.gov', 'Duff Aldren', '092 Packers Trail', '3327652788', '5010121966302219');
insert into USERS (userid, password, email_address, name, address, phone_number, credit_card) values ('xhanbury8', 'Q4cMrODier', 'xhanbury8@sciencedaily.com', 'Xenia Hanbury', '4 Dahle Lane', '5868264387', '5002355138254854');
insert into USERS (userid, password, email_address, name, address, phone_number, credit_card) values ('eackenhead9', 'IWRDvh', 'eackenhead9@seattletimes.com', 'Ennis Ackenhead', '4 Monument Center', '3885168514', '5002359669325935');

insert into Book (isbn, title, quantity, number_of_pages, price, total_sales) values ('1403628983254', 'My Way Home (Így jöttem) ', 100, 69, 90.95, 0);
insert into Book (isbn, title, quantity, number_of_pages, price, total_sales) values ('8485227271657', 'One Shot', 100, 377, 60.62, 0);
insert into Book (isbn, title, quantity, number_of_pages, price, total_sales) values ('1753587816980', 'Rize', 100, 388, 52.46, 0);
insert into Book (isbn, title, quantity, number_of_pages, price, total_sales) values ('7036334452876', 'Smart Set, The', 100, 452, 21.53, 0);
insert into Book (isbn, title, quantity, number_of_pages, price, total_sales) values ('3774593833143', 'Bikini Summer II', 100, 344, 33.79, 0);
insert into Book (isbn, title, quantity, number_of_pages, price, total_sales) values ('6188731976665', 'Death Note 2: The Last Name', 100, 84, 4.33, 0);
insert into Book (isbn, title, quantity, number_of_pages, price, total_sales) values ('1898248637554', 'Steamboat Round the Bend', 100, 602, 77.27, 0);
insert into Book (isbn, title, quantity, number_of_pages, price, total_sales) values ('3394713144543', 'Tevye', 100, 22, 71.70, 0);
insert into Book (isbn, title, quantity, number_of_pages, price, total_sales) values ('2295938112895', 'Direct Contact', 100, 671, 63.23, 0);
insert into Book (isbn, title, quantity, number_of_pages, price, total_sales) values ('9233465039123', 'Sunnyside', 100, 367, 80.18, 0); 

insert into PUBLISHER (email_address, name, address, banking_account) values ('hpopescu0@feedburner.com', 'Hailee Popescu', '5695 Gina Avenue', 5010128953971948);
insert into PUBLISHER (email_address, name, address, banking_account) values ('gwestell1@weibo.com', 'Gennifer Westell', '6595 Huxley Center', 5002350913556946);
insert into PUBLISHER (email_address, name, address, banking_account) values ('clackemann2@amazon.com', 'Cybill Lackemann', '3 Buena Vista Hill', 5010121367360550);
insert into PUBLISHER (email_address, name, address, banking_account) values ('cblakemore3@cbslocal.com', 'Charline Blakemore', '1739 Hovde Lane', 5002358009725226);
insert into PUBLISHER (email_address, name, address, banking_account) values ('iglavias4@rediff.com', 'Inesita Glavias', '83 Elgar Court', 5002353160121182);
insert into PUBLISHER (email_address, name, address, banking_account) values ('awigan5@phoca.cz', 'Agna Wigan', '68 Linden Park', 5002356449946550);

INSERT INTO PUBLISHES
SELECT ISBN, publishersId FROM BOOK, PUBLISHER WHERE email_address='hpopescu0@feedburner.com' AND ISBN='1403628983254';
UPDATE PUBLISHES
SET percentage = .2 WHERE publishersId = (SELECT publishersId FROM PUBLISHER WHERE email_address='hpopescu0@feedburner.com') AND ISBN='1403628983254';
INSERT INTO PUBLISHES
SELECT ISBN, publishersId FROM BOOK, PUBLISHER WHERE email_address='gwestell1@weibo.com' AND ISBN='8485227271657';
UPDATE PUBLISHES
SET percentage = .1205 WHERE publishersId = (SELECT publishersId FROM PUBLISHER WHERE email_address='gwestell1@weibo.com') AND ISBN='8485227271657';
INSERT INTO PUBLISHES
SELECT ISBN, publishersId FROM BOOK, PUBLISHER WHERE email_address='clackemann2@amazon.com' AND ISBN='1753587816980';
UPDATE PUBLISHES
SET percentage = .1578 WHERE publishersId = (SELECT publishersId FROM PUBLISHER WHERE email_address='clackemann2@amazon.com') AND ISBN='1753587816980';
INSERT INTO PUBLISHES
SELECT ISBN, publishersId FROM BOOK, PUBLISHER WHERE email_address='cblakemore3@cbslocal.com' AND ISBN='7036334452876';
UPDATE PUBLISHES
SET percentage = .2 WHERE publishersId = (SELECT publishersId FROM PUBLISHER WHERE email_address='cblakemore3@cbslocal.com') AND ISBN='7036334452876';
INSERT INTO PUBLISHES
SELECT ISBN, publishersId FROM BOOK, PUBLISHER WHERE email_address='iglavias4@rediff.com' AND ISBN='3774593833143';
UPDATE PUBLISHES
SET percentage = .1 WHERE publishersId = (SELECT publishersId FROM PUBLISHER WHERE email_address='iglavias4@rediff.com') AND ISBN='3774593833143';
INSERT INTO PUBLISHES
SELECT ISBN, publishersId FROM BOOK, PUBLISHER WHERE email_address='awigan5@phoca.cz' AND ISBN='6188731976665';
UPDATE PUBLISHES
SET percentage = .1533 WHERE publishersId = (SELECT publishersId FROM PUBLISHER WHERE email_address='awigan5@phoca.cz') AND ISBN='6188731976665';
INSERT INTO PUBLISHES
SELECT ISBN, publishersId FROM BOOK, PUBLISHER WHERE email_address='awigan5@phoca.cz' AND ISBN='1898248637554';
UPDATE PUBLISHES
SET percentage = .1901 WHERE publishersId = (SELECT publishersId FROM PUBLISHER WHERE email_address='awigan5@phoca.cz') AND ISBN='1898248637554';
INSERT INTO PUBLISHES
SELECT ISBN, publishersId FROM BOOK, PUBLISHER WHERE email_address='gwestell1@weibo.com' AND ISBN='3394713144543';
UPDATE PUBLISHES
SET percentage = .1740 WHERE publishersId = (SELECT publishersId FROM PUBLISHER WHERE email_address='gwestell1@weibo.com') AND ISBN='3394713144543';
INSERT INTO PUBLISHES
SELECT ISBN, publishersId FROM BOOK, PUBLISHER WHERE email_address='clackemann2@amazon.com' AND ISBN='2295938112895';
UPDATE PUBLISHES
SET percentage = .1346 WHERE publishersId = (SELECT publishersId FROM PUBLISHER WHERE email_address='clackemann2@amazon.com') AND ISBN='2295938112895';
INSERT INTO PUBLISHES
SELECT ISBN, publishersId FROM BOOK, PUBLISHER WHERE email_address='hpopescu0@feedburner.com' AND ISBN='9233465039123';
UPDATE PUBLISHES
SET percentage = .1111 WHERE publishersId = (SELECT publishersId FROM PUBLISHER WHERE email_address='hpopescu0@feedburner.com') AND ISBN='9233465039123';

insert into phone_number (publishersId, phone_number) values ((SELECT publishersId FROM PUBLISHER WHERE email_address='hpopescu0@feedburner.com'), '2178153615');
insert into phone_number (publishersId, phone_number) values ((SELECT publishersId FROM PUBLISHER WHERE email_address='gwestell1@weibo.com'), '8348037029');
insert into phone_number (publishersId, phone_number) values ((SELECT publishersId FROM PUBLISHER WHERE email_address='clackemann2@amazon.com'), '4973236650');
insert into phone_number (publishersId, phone_number) values ((SELECT publishersId FROM PUBLISHER WHERE email_address='cblakemore3@cbslocal.com'), '3569563939');
insert into phone_number (publishersId, phone_number) values ((SELECT publishersId FROM PUBLISHER WHERE email_address='iglavias4@rediff.com'), '4135612789');
insert into phone_number (publishersId, phone_number) values ((SELECT publishersId FROM PUBLISHER WHERE email_address='awigan5@phoca.cz'), '5065370060');
insert into phone_number (publishersId, phone_number) values ((SELECT publishersId FROM PUBLISHER WHERE email_address='awigan5@phoca.cz'), '3985649077');
insert into phone_number (publishersId, phone_number) values ((SELECT publishersId FROM PUBLISHER WHERE email_address='gwestell1@weibo.com'), '9196209829');
insert into phone_number (publishersId, phone_number) values ((SELECT publishersId FROM PUBLISHER WHERE email_address='clackemann2@amazon.com'), '6159011575');
insert into phone_number (publishersId, phone_number) values ((SELECT publishersId FROM PUBLISHER WHERE email_address='hpopescu0@feedburner.com'), '7234021085');
insert into phone_number (publishersId, phone_number) values ((SELECT publishersId FROM PUBLISHER WHERE email_address='clackemann2@amazon.com'), '2307874648');

insert into author (isbn, author) values ('1403628983254', 'Kip Twelves');
insert into author (isbn, author) values ('1753587816980', 'Andrey Bennison');
insert into author (isbn, author) values ('1753587816980', 'Florry Scobie');
insert into author (isbn, author) values ('7036334452876', 'Adey Avramov');
insert into author (isbn, author) values ('3774593833143', 'Carolynn Boutflour');
insert into author (isbn, author) values ('6188731976665', 'Carolynn Boutflour');
insert into author (isbn, author) values ('1898248637554', 'Valle Bracegirdle');
insert into author (isbn, author) values ('3394713144543', 'Nerita Sidey');
insert into author (isbn, author) values ('8485227271657','Mitch Couch');
insert into author (isbn, author) values ('2295938112895', 'Moreen Godfree');
insert into author (isbn, author) values ('9233465039123','Charo Coldrick');

insert into genre (isbn, genre) values ('1403628983254', 'Fiction');
insert into genre (isbn, genre) values ('1753587816980', 'Non-Fiction');
insert into genre (isbn, genre) values ('1753587816980', 'Fantasy');
insert into genre (isbn, genre) values ('7036334452876', 'SciFi');
insert into genre (isbn, genre) values ('3774593833143', 'SciFi');
insert into genre (isbn, genre) values ('6188731976665', 'Action');
insert into genre (isbn, genre) values ('1898248637554', 'Adventure');
insert into genre (isbn, genre) values ('3394713144543', 'Comedy');
insert into genre (isbn, genre) values ('8485227271657', 'Drama');
insert into genre (isbn, genre) values ('2295938112895', 'Comedy');
insert into genre (isbn, genre) values ('9233465039123', 'Action');
insert into genre (isbn, genre) values ('9233465039123', 'Non-Fiction');
insert into genre (isbn, genre) values ('9233465039123', 'Adventure');
