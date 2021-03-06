import pandas as panda
import mysql.connector


panda.set_option('display.max_rows', None)
panda.set_option('display.max_columns', None)
panda.set_option('display.width', 1000)

db = mysql.connector.connect(
    host="localhost",  # jdbc: mysql: // localhost: 3306 /?user = root
    user="root",
    passwd="corbla99",
    database="shakerdiscoverycenter")


mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE shakerdiscoverycenter")

# create CHILD table
# mycursor.execute("CREATE TABLE CHILD (Child_id int PRIMARY KEY AUTO_INCREMENT, C_First_Name VARCHAR(255) NOT NULL, C_Middle_Name VARCHAR(255), C_Last_Name VARCHAR(255) NOT NULL, C_Gender CHAR, C_Dob DATE CHECK(TIMESTAMPDIFF(WEEK, C_Dob, SYSDATE()) >= 6) NOT NULL, C_Enrollment_Date  DATE NOT NULL, C_Address VARCHAR(100) NOT NULL, C_Apt VARCHAR(20), C_City  VARCHAR(100) DEFAULT 'Cleveland', C_State VARCHAR(2) DEFAULT 'OH', C_Zip int NOT NULL, C_Status VARCHAR(8) DEFAULT 'Acitive', C_DATE_Inactive DATE DEFAULT NULL)")

# inserting the CHILD records
# sql = "INSERT INTO CHILD (C_First_Name, C_Middle_Name, C_Last_Name, C_Gender, C_Dob, C_Enrollment_Date, C_Address, C_Apt, C_City, C_State, C_Zip, C_Status, C_Date_Inactive)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s, %s, %s)"

# val = [
#     ('Katie',	'Pauline',	'Allen',	'F',	'2018-08-20',	'2022-03-07',
#      '1620 Vineyard Drive',		None,		'Cleveland',	'OH',	44114,	'Active',	None),
#     ('Kevin',	'Paul',	'Allen',	'M',	'2018-08-20',	'2022-03-07',
#      '1620 Vineyard Drive',		None,		'Cleveland',	'OH',	44114,	'Active',	None),
#     ('Corey',	'James',	'Anderson',	'M',	'2020-02-04',	'2022-01-24',
#      '4186 Vineyard Drive',		None,		'Cleveland',	'OH',	44115,	'Active',	None),
#     ('Karen',	'Lorraine',	'Arellano',	'F',	'2021-12-13',	'2022-03-07',
#      '1045 Flynn Street',		None,		'Cleveland',	'OH',	44115,	'Active',	None),
#     ('Jessica',	'Pauline',	'Beck',	'F',	'2019-10-17',	'2022-04-04',
#      '1459 Harley Drive',		None,		'Cleveland',	'OH',	44115,	'Active',	None),
#     ('Michelle',	'Kory',	'Brown',	'F',	'2020-04-12',	'2022-04-02',
#      '3602 Lindholm Rd',		None,		'Cleveland',	'OH',	44120,	'Active',	None),
#     ('Carlos',	'Camryn',	'Buchanan',	'M',	'2021-11-11',	'2022-04-28',
#      '2783 Peaceful Lane',		None,		'Cleveland',	'OH',	44110,	'Active',	None),
#     ('Mark',	'Thane',	'Burton',	'M',	'2019-10-25',	'2022-04-12',
#      '2915 E 130th St',		None,		'Cleveland',	'OH',	44114,	'Active',	None),
#     ('Wendy',	'Marie',	'Carter',	'F',	'2021-03-22',	'2022-02-21',
#      '3147 E 130th St',		'Apt 221',	'Cleveland',	'OH',	44111,	'Active',	None),
#     ('April',	'Raine',	'Curry',	'F',	'2020-03-25',	'2022-03-15',
#      '3344 Flynn Street',		None,		'Cleveland',	'OH',	44115,	'Active',	None),
#     ('Timothy',	'Jason',	'Ferguson',	'M',	'2019-04-27',	'2022-04-11',
#      '2287 Parker Drive',		None,		'Cleveland',	'OH',	44115,	'Active',	None),
#     ('Lawrence',	'Michael',	'Friedman',	'M',	'2018-05-16',	'2022-04-25',
#      '4700 Parker Drive',		None,		'Cleveland',	'OH',	44115,	'Active',	None),
#     ('Melissa',	'Kathleen',	'Fuller',	'F',	'2021-12-27',	'2022-02-21',
#      '3146 E 130th St',		None,		'Cleveland',	'OH',	44120,	'Active',	None),
#     ('Jesus',	'Ramon',	'Garcia',	'M',	'2018-11-26',	'2022-05-09',
#      '2273 Ralph Drive',		None,		'Cleveland',	'OH',	44114,	'Active',	None),
#     ('Alexandra', 'Brenna',	'Garcia',	'F',	'2020-04-07',	'2022-03-28',
#      '2273 Ralph Drive',		None,		'Cleveland',	'OH',	44114,	'Active',	None),
#     ('Laura',	'Marie',	'Gilmore',	'F',	'2018-02-07',	'2022-01-17',
#      '3144 Parker Drive',		None,		'Cleveland',	'OH',	44114,	'Active',	None),
#     ('Steven',	'Ash',	'Hansen',	'M',	'2017-09-08',	'2022-02-14',
#      '2740 Peaceful Lane',		None,		'Cleveland',	'OH',	44109,	'Active',	None),
#     ('Matthew',	'Thomas',	'Hart',	'M',	'2020-04-21',	'2022-04-11',
#      '2811 S Park Blvd',		None,		'Cleveland',	'OH',	44120,	'Active',	None),
#     ('Debra',	'Maria',	'Hernandez', 'F',	'2021-08-30',	'2022-01-17',
#      '2421 Vineyard Drive',		None,		'Cleveland',	'OH',	44115,	'Active',	None),
#     ('Dylan',	'Justin',	'Holt',	'M',	'2019-09-19',	'2022-03-07',
#      '2396 Peaceful Lane',		None,		'Cleveland',	'OH',	44115,	'Active',	None),
#     ('Jason',	'Eugene',	'Huang',	'M',	'2019-11-21',	'2022-05-09',
#      '884 Peaceful Lane',		None,		'Cleveland',	'OH',	44110,	'Active',	None),
#     ('Crystal',	'Michele',	'Hudson',	'F',	'2019-03-08',	'2022-02-20',
#      '1434 Parker Drive',		None,		'Cleveland',	'OH',	44114,	'Active',	None),
#     ('Andrea',	'Justeene',	'Jackson',	'F',	'2019-02-02',	'2022-01-17',
#      '3321 Glenwood Avenue',		None,		'Cleveland',	'OH',	44106,	'Active',	None),
#     ('Bradley',	'Paul',	'Johnson',	'M',	'2018-10-22',	'2022-04-04',
#      '3932 Parker Drive',		None,		'Cleveland',	'OH',	44115,	'Active',	None),
#     ('Dory',	'Isla',	'Kane',	'F',	'2021-11-22',	'2022-01-17',	'3687 Rolliston Rd',
#      'Apt. 338', 'Cleveland', 'OH', 44120, 'Active', None),
#     ('Kristie',	'Isabelle',	'Kelly',	'F',	'2020-04-21',	'2022-04-11',
#      '942 Sunny Glen Lane',		None,		'Cleveland',	'OH',	44109,	'Active',	None),
#     ('Matthew',	'Richard',	'Lee',	'M',	'2021-10-25',	'2022-01-17',
#      '3429 Vineyard Drive',		None,		'Cleveland',	'OH',	44114,	'Active',	None),
#     ('Tammy',	'Rue',	'McDonald',	'F',	'2018-03-07',	'2022-02-14',
#      '4029 Meadowview Drive',	None,		'Cleveland',	'OH',	44191,	'Active',	None),
#     ('Jason', 'Jesus', 'Mendoza',	'M', '2019-09-26', '2022-03-14',
#      '3436 Peaceful Lane', None, 'Cleveland',	'OH',	44113,	'Active',	None),
#     ('Kenneth',	'Andrew',	'Miller',	'M',	'2017-10-27',	'2022-04-04',
#      '2546 Bingamon Road',		None,		'Cleveland',	'OH',	44114,	'Active',	None),
#     ('Leslie',	'Rachael',	'Moore',	'F',	'2021-12-27',	'2022-03-07',
#      '3384 Hiddenview Drive',	None,		'Cleveland',	'OH',	44115,	'Active',	None),
#     ('Emma',	'Madison',	'Moore',	'F',	'2021-11-15',	'2022-05-02',
#      '13800 Fairhill Road',		'Apt 322',	'Cleveland',	'OH',	44120,	'Active',	None),
#     ('David', 'Wade', 'Nelson', 'M',	'2021-10-22',	'2022-01-14',
#      '630 Peaceful Lane',	None,		'Cleveland',	'OH',	44115,	'Active',	None),
#     ('Sheri',	'Pauline',	'Ochoa',	'F',	'2019-03-09',	'2022-02-21',
#      '3489 Vineyard Drive',		None,		'Cleveland',	'OH',	44114,	'Active',	None),
#     ('Brenda',	'Sierra',	'Owens',	'F',	'2020-01-28',	'2022-01-17',
#      '3436 Flynn Street',		None,		'Cleveland',	'OH',	44115,	'Active',	None),
#     ('Wesley',	'Benson',	'Pierce',	'M',	'2020-01-25',	'2022-01-14',
#      '2253 Sunny Glen Lane',		None,		'Cleveland',	'OH',	44114,	'Active',	None),
#     ('Leslie',	'Charis',	'Ramirez',	'F',	'2018-09-24',	'2022-03-07',
#      '3481 Glenwood Avenue',		None,		'Cleveland',	'OH',	44115,	'Active',	None),
#     ('Gwendolyn',	'Isla',	'Ray',	'F',	'2020-08-09',	'2022-01-31',
#      '99 Peaceful Lane',		None,		'Cleveland',	'OH',	44106,	'Active',	None),
#     ('Robert',	'Justin',	'Reid',	'M',	'2022-02-21',	'2022-04-18',
#      '747 Parker Drive',		None,		'Cleveland',	'OH',	44115,	'Active',	None),
#     ('Dennis',	'Robert',	'Robinson',	'M',	'2021-10-25',	'2022-03-14',
#      '955 Parker Drive',		None,		'Cleveland',	'OH',	44115,	'Active',	None),
#     ('David',	'Blair',	'Rocha',	'M',	'2022-02-14',	'2022-05-09',
#      '1961 Vineyard Drive',		None,		'Cleveland',	'OH',	44109,	'Active',	None),
#     ('Jamie',	'Lynne',	'Smith',	'F',	'2020-11-08',	'2022-05-02',
#      '1796 Sunny Glen Lane',		None,		'Cleveland',	'OH',	44114,	'Active',	None),
#     ('Lynn',	'Izabelle',	'Smith',	'F',	'2017-09-14',	'2022-02-20',
#      '3710 Sunny Glen Lane',		None,		'Cleveland',	'OH',	44120,	'Active',	None),
#     ('Cody',	'Paul',	'Smith',	'M',	'2020-03-10',	'2022-02-28',
#      '3710 Sunny Glen Lane',		None,		'Cleveland',	'OH',	44120,	'Active',	None),
#     ('Victoria',	'Angelica',	'Stevens',	'F',	'2017-09-08',	'2022-02-14',
#      '4230 Sunny Glen Lane',		None,		'Cleveland',	'OH',	44105,	'Active',	None),
#     ('Amber',	'Rose',	'Thompson',	'F',	'2020-03-10',	'2022-02-28',
#      '2307 Parker Drive',		None,		'Cleveland',	'OH',	44109,	'Active',	None),
#     ('John',	'Richard',	'Turner',	'M',	'2020-08-02',	'2022-01-24',
#      '2852 Flynn Street',		None,		'Cleveland',	'OH',	44114,	'Active',	None),
#     ('Lauren',	'Angelina',	'Valdez',	'F',	'2021-05-24',	'2022-01-31',
#      '1398 Flynn Street',		None,		'Cleveland',	'OH',	44115,	'Active',	None),
#     ('Sarah',	'Rose',	'Williams',	'F',	'2021-10-19',	'2022-04-11',
#      '4862 Harley Vincent Drive',	None,		'Cleveland',	'OH',	44115,	'Active',	None),
#     ('Blair',	'Robert',	'Williams',	'M',	'2020-10-18',	'2022-04-11',
#      '4862 Harley Vincent Drive',	None,		'Cleveland',	'OH',	44115,	'Active',	None)
# ]

# mycursor.executemany(sql, val)

# db.commit()

# print(mycursor.rowcount, "record inserted.")

# create GUARDIAN table
# mycursor.execute("CREATE TABLE GUARDIAN (Guardian_id int PRIMARY KEY AUTO_INCREMENT, G_First_Name VARCHAR(255) NOT NULL, G_Middle_Int CHAR, G_Last_Name VARCHAR(255) NOT NULL, G_Cell_Phone bigint NOT NULL, G_Work_Phone bigint NOT NULL, G_W_Ext int DEFAULT NULL, G_Fee_Discount double DEFAULT 0.0, G_Address VARCHAR(100) NOT NULL, G_Apt VARCHAR(20), G_City VARCHAR(100) DEFAULT 'Cleveland', G_State CHAR(2) DEFAULT 'OH', G_Zip int NOT NULL)")

# inserting the GUARDIAN records
# sql = "INSERT INTO GUARDIAN (G_First_Name, G_Middle_Int, G_Last_Name, G_Cell_Phone, G_Work_Phone, G_W_Ext, G_Fee_Discount, G_Address, G_Apt, G_City, G_State, G_Zip)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s, %s)"

# val = [
# ('Paul', 'A', 'Allen', 2164439846, 2168358428, None, 0.1,
#  '1620 Vineyard Drive',	None,	'Cleveland',	'OH',	44114),
# ('Katherine',	'B',	'Allen', 4403671379, 2164439848, None,
#  0.1,	'1620 Vineyard Drive',	None,	'Cleveland',	'OH',	44114),
# ('Mark',	'J',	'Anderson',	2167987180, 2167780500,	None,	0,
#  '4186 Vineyard Drive',	None,	'Cleveland',	'OH',	44115),
# ('Karen',	'C',	'Anderson',	2165488778,	2167987182, None,	0,
#  '4186 Vineyard Drive',	None,	'Cleveland',	'OH',	44115),
# ('Jose',	'D',	'Arellano',	4406146516, 4403390845,	None,
#  0,	'1045 Flynn Street',	None,	'Cleveland',	'OH',	44115),
# ('Pauline',	'L',	'Arellano',	4402876190,	4406146518, None,
#  0,	'1045 Flynn Street',	None,	'Cleveland',	'OH',	44115),
# ('Peter',	'P',	'Beck',	9097059785, 2167517230,	345,	0,
#  '1459 Harley Vincent Drive', None, 'Cleveland',	'OH',	44115),
# ('Pauline',	'E', 'Beck', 4409151825, 2167987180, None, 0,
#  '1459 Harley Vincent Drive', None, 'Cleveland', 'OH',	44115),
# ('David',	'F',	'Brown',	4409728515, 2163988142,	None,	0,
#  '3602 Lindholm Rd',	None,	'Cleveland',	'OH',	44120),
# ('Jessica',	'K',	'Brown',	2162866585,	4409728517, None,
#  0,	'3602 Lindholm Rd',	None,	'Cleveland',	'OH',	44120),
# ('Steve',	'G',	'Buchanan',	2167283959, 4408762660,	None,
#  0,	'2783 Peaceful Lane',	None,	'Cleveland',	'OH',	44110),
# ('Rio',	'H',	'Buchanan',	4409913076,	2167283961, None,	0,
#  '2783 Peaceful Lane',	None,	'Cleveland',	'OH',	44110),
# ('Mark',	'I',	'Burton',	4409915940, 2164863318,	None,
#  0,	'2915 E 130th St',	None,	'Cleveland',	'OH',	44114),
# ('Tammy',	'J',	'Burton',	4407943426,	4409915942, None,
#  0,	'2915 E 130th St',	None,	'Cleveland',	'OH',	44114),
# ('Savannah',	'M',	'Carter', 2166176367, 2164799978,	None,	0,
#  '3147 E 130th St',	'Apt. 221',	'Cleveland',	'OH',	44111),
# ('Richard',	'K',	'Carter',	4407604464, 2166176369, None,	0,
#  '3147 E 130th St',	'Apt. 221',	'Cleveland',	'OH',	44111),
# ('William',	'L',	'Curry',	2164215041, 2168557288,	None,
#  0,	'3344 Flynn Street',	None,	'Cleveland',	'OH',	44115),
# ('Susan',	'R',	'Curry',	2169456448,	2164215043, None,	0,
#  '3344 Flynn Street',	None,	'Cleveland',	'OH',	44115),
# ('Jason',	'M',	'Ferguson',	2167519751, 2162866586,	222,
#  0,	'2287 Parker Drive',	None,	'Cleveland',	'OH',	44115),
# ('Michelle',	'N',	'Ferguson',	2167211881,	2167519771, None,
#  0,	'2287 Parker Drive',	None,	'Cleveland',	'OH',	44115),
# ('Lawrence',	'M',	'Friedman',	2167519756, 2164215041, None,
#  0,	'4700 Parker Drive',	None,	'Cleveland',	'OH',	44115),
# ('Ruth',	'M',	'Friedman',	2165611506,	2167519776, None,
#  0,	'4700 Parker Drive',	None,	'Cleveland',	'OH',	44115),
# ('John',	'G',	'Fuller', 4404520800, 2164439846, None,
#  0,	'3146 E 130th St',	None,	'Cleveland',	'OH',	44120),
# ('Kathleen',	'H',	'Fuller', 2165153617, 4404520802, None,
#  0,	'3146 E 130th St',	None,	'Cleveland',	'OH',	44120),
# ('Francisco',	'J',	'Garcia', 2166013615, 2165488779,	None,
#  0.1,	'2273 Ralph Drive',	None,	'Cleveland',	'OH',	44114),
# ('Belkyss',	'L',	'Garcia', 2162800256, 2166013617, None,
#  0.1,	'2273 Ralph Drive',	None,	'Cleveland',	'OH',	44114),
# ('Steven',	'M',	'Gilmore',	4403736082, 2162866587,	None,
#  0,	'3144 Parker Drive',	None,	'Cleveland',	'OH',	44114),
# ('Dawn',	'E',	'Gilmore',	2168347735,	4403736084, None,	0,
#  '3144 Parker Drive',	None,	'Cleveland',	'OH',	44114),
# ('Thomas',	'A',	'Hansen',	2167517229, 4409913078,	None,	0,
#  '2740 Peaceful Lane',	None,	'Cleveland',	'OH',	44109),
# ('Milan',	'B',	'Hansen', 2168835382,	2167517231, None,	0,
#  '2740 Peaceful Lane',	None,	'Cleveland',	'OH',	44109),
# ('Blaize',	'C',	'Hart',	2164811116, 4407943428,	None,	0,
#  '2811 S Park Blvd',	None,	'Cleveland',	'OH',	44120),
# ('Ann',	'T',	'Hart',	2168358427,	2164811118,	None,	0.25,
#  '2811 S Park Blvd',	None,	'Cleveland',	'OH',	44120),
# ('Ralph',	'R',	'Hernandez',	4403754662, 4407604466,	None,
#  0,	'2421 Vineyard Drive',	None,	'Cleveland',	'OH',	44115),
# ('Justine',	'M',	'Hernandez',	2167780499,	4403754664, None,
#  0,	'2421 Vineyard Drive',	None,	'Cleveland',	'OH',	44115),
# ('Dylan',	'J',	'Holt',	2166850302, 2169456450,	None,	0,
#  '2396 Peaceful Lane',	None,	'Cleveland',	'OH',	44115),
# ('Brenna',	'V',	'Holt',	4403390844,	2166850304, None,	0,
#  '2396 Peaceful Lane',	None,	'Cleveland',	'OH',	44115),
# ('Allan',	None,	'Huang',	2162427559, 2167211883,	None,	0,
#  '884 Peaceful Lane',	None,	'Cleveland',	'OH',	44110),
# ('Christine',	'E',	'Huang',	2167517229,	2162427561, None,
#  0,	'884 Peaceful Lane',	None,	'Cleveland',	'OH',	44110),
# ('Donald',	'J',	'Hudson',	2166492220, 2165611508,	None,
#  0,	'1434 Parker Drive',	None,	'Cleveland',	'OH',	44114),
# ('Odessa',	'M',	'Hudson',	2163988141,	2166492222, None,
#  0,	'1434 Parker Drive',	None,	'Cleveland',	'OH',	44114),
# ('Raymond',	'C',	'Jackson',	2164439847, 2165153619,	None,	0,
#  '3321 Glenwood Avenue',	None,	'Cleveland',	'OH',	44106),
# ('Ruby',	'J',	'Jackson',	4408762659,	2164439849, None,	0,
#  '3321 Glenwood Avenue',	None,	'Cleveland',	'OH',	44106),
# ('Terence',	'P',	'Johnson',	2167987181, 2162800258,	None,
#  0,	'3932 Parker Drive',	None,	'Cleveland',	'OH',	44115),
# ('Bonnie',	'R',	'Johnson',	2164863317,	2167987183,	None,
#  0,	'3932 Parker Drive',	None,	'Cleveland',	'OH',	44115),
# ('Eugene',	'B',	'Kane',	4406146517, 2168347737,	None,	0,
#  '3687 Rolliston Rd',	'Apt. 338',	'Cleveland',	'OH',	44120),
# ('Jennifer',	'I',	'Kane',	2164799977,	4406146519, None,	0,
#  '3687 Rolliston Rd',	'Apt. 338',	'Cleveland',	'OH',	44120),
# ('Darryl',	'M',	'Kelly',	2167059786, 2168835384,	None,	0,
#  '942 Sunny Glen Lane',	None,	'Cleveland',	'OH',	44109),
# ('Lynne',	'L',	'Kelly',	2168557287,	2169456449,	None,	0.5,
#  '942 Sunny Glen Lane',	None,	'Cleveland',	'OH',	44109),
# ('John',	None,	'Lee', 4409728516, 2168358429,	None,	0,
#  '3429 Vineyard Drive',	None,	'Cleveland',	'OH',	44114),
# ('Yuli',	None,	'Lee',	4408754231,	4409728518, None,	0,
#  '3429 Vineyard Drive',	None,	'Cleveland',	'OH',	44114),
# ('Kevin',	'V',	'McDonald',	2167283960, 2167780501,	None,	0,
#  '4029 Meadowview Drive',	None,	'Cleveland',	'OH',	44191),
# ('Leslie',	'C',	'McDonald',	2164137106,	2167283962, None,	0,
#  '4029 Meadowview Drive',	None,	'Cleveland',	'OH',	44191),
# ('Jesus',	'J',	'Mendoza',	4409915941, 4403390846,	None,	0,
#  '3436 Peaceful Lane',	None,	'Cleveland',	'OH',	44113),
# ('Jessica',	None,	'Mendoza',	4409519981,	4409915943, None,
#  0,	'3436 Peaceful Lane',	None,	'Cleveland',	'OH',	44113),
# ('Bob',	None,	'Miller', 2166176368, 2167517231,	None,	0,
#  '2546 Bingamon Road',	None,	'Cleveland',	'OH',	44114),
# ('Rose',	'A',	'Miller',	2164902856,	2166176370, None,	0,
#  '2546 Bingamon Road',	None,	'Cleveland',	'OH',	44114),
# ('Wesley',	None,	'Moore', 2164215042, 2163988143,	None,	0,
#  '3384 Hiddenview Drive',	None,	'Cleveland',	'OH',	44115),
# ('Angelica',	'R',	'Moore', 2162866586,	2164215044, None,	0,
#  '3384 Hiddenview Drive',	None,	'Cleveland',	'OH',	44115),
# ('Dennis',	'M',	'Moore', 2167519761, 4408762661,	None,	0,
#  '13800 Fairhill Road',	'Apt 322',	'Cleveland',	'OH',	44120),
# ('Stephanie',	'M',	'Moore',	4409913077,	2167519781, None,	0,
#  '13800 Fairhill Road',	'Apt 322',	'Cleveland',	'OH',	44120),
# ('Roger',	'W',	'Nelson',	2167519766, 2164863319,	None,	0,
#  '630 Peaceful Lane',	None,	'Cleveland',	'OH',	44115),
# ('Emma',	None,	'Nelson',	4407943427,	2167519786, None,	0,
#  '630 Peaceful Lane',	None,	'Cleveland',	'OH',	44115),
# ('Sierra',	'P',	'Ochoa',	4404520801, 2164799979,	None,	0,
#  '3489 Vineyard Drive',	None,	'Cleveland',	'OH',	44114),
# ('Cherish',	'S',	'Owens',	4407604465,	4404520803,	None,
#  0,	'3436 Flynn Street',	None,	'Cleveland',	'OH',	44115),
# ('Sarah',	'B',	'Pierce', 2166013616, 2168557289,	None,	0.75,
#  '2253 Sunny Glen Lane',	None,	'Cleveland',	'OH',	44114),
# ('Christina',	'C',	'Ramirez',	2169456449,	2166013618, None,
#  0,	'3481 Glenwood Avenue',	None,	'Cleveland',	'OH',	44115),
# ('Ronald',	'I',	'Ray', 4403736083, 2161817231,	None,	0,
#  '99 Peaceful Lane',	None,	'Cleveland',	'OH',	44106),
# ('Hannah',	'J',	'Reid',	2167211882,	4403736085,	None,	0,
#  '747 Parker Drive',	None,	'Cleveland',	'OH',	44115),
# ('Roberta',	'R',	'Robinson',	2167517230, 2167200106,	None,
#  0,	'955 Parker Drive',	None,	'Cleveland',	'OH',	44115),
# ('Shirley',	'J',	'Richardson',	2165611507,	2167517232, None,
#  0.8,	'1961 Vineyard Drive',	None,	'Cleveland',	'OH',	44109),
# ('Evelyn',	'I',	'Jones', 2164811117, 2162582981,	None,	0.8,
#  '1796 Sunny Glen Lane',	None,	'Cleveland',	'OH',	44114),
# ('Sarah',	None,	'Smith', 4403754663, 2167965856,	None,	0,
#  '3710 Sunny Glen Lane',	None,	'Cleveland',	'OH',	44120),
# ('Eunice',	'A',	'Stevens', 2162800257, 4403754665, None,	0,
#  '4230 Sunny Glen Lane',	None,	'Cleveland',	'OH',	44105),
# ('Cheryl',	'S',	'Holm',	2166850303, 2162866588,	None,	0,
#  '2307 Parker Drive',	None,	'Cleveland',	'OH',	44109),
# ('Victoria',	None,	'Turner',	2168347736,	2166850305,	None,
#  0,	'2852 Flynn Street',	None,	'Cleveland',	'OH',	44114),
# ('Carmen',	'A',	'Valdez', 2162427560, 2169913079,	None,
#  0,	'1398 Flynn Street',	None,	'Cleveland',	'OH',	44115),
# ('Elton',	'R',	'Williams',	2168835383,	2162427562,	None,	0,
#  '4862 Harley Vincent Drive',	None,	'Cleveland',	'OH',	44115),
# ('Sarah',	None,	'Williams',	2166492221, 2167943429,	None,	0,
#  '4862 Harley Vincent Drive',	None,	'Cleveland',	'OH',	44115),
# ]
# mycursor.executemany(sql, val)

# db.commit()

# create the GUARDIANCHILD Table
# mycursor.execute(
#     "CREATE TABLE GUARDIANCHILD (Guardian_id int NOT NULL,  Child_id  int NOT NULL , PRIMARY KEY (Guardian_id, Child_id), CONSTRAINT FK_Guardian_id  FOREIGN KEY (Guardian_id) REFERENCES GUARDIAN(Guardian_id), CONSTRAINT FK_Child_id  FOREIGN KEY (Child_id) REFERENCES CHILD(Child_id))")


# # inserting the GUARDIANCHILD records

# sql = "INSERT INTO GUARDIANCHILD (Guardian_ID, Child_ID) VALUES (%s, %s)"
# val = [
#     (1,	1),
#     (1,	2),
#     (2,	1),
#     (2,	2),
#     (3,	3),
#     (4,	3),
#     (5,	4),
#     (6,	4),
#     (7,	5),
#     (8,	5),
#     (9,	6),
#     (10,	6),
#     (11,	7),
#     (12,	7),
#     (13,	8),
#     (14,	8),
#     (15,	9),
#     (16,	9),
#     (17,	10),
#     (18,	10),
#     (19,	11),
#     (20,	11),
#     (21,	12),
#     (22,	12),
#     (23,	13),
#     (24,	14),
#     (24,	15),
#     (25,	14),
#     (25,	15),
#     (26,	15),
#     (27,	16),
#     (28,	16),
#     (29,	17),
#     (30,	17),
#     (31,	18),
#     (32,	18),
#     (33,	19),
#     (34,	19),
#     (35,	20),
#     (36,	20),
#     (37,	21),
#     (38,	21),
#     (39,	22),
#     (40,	22),
#     (41,	23),
#     (42,	23),
#     (43,	24),
#     (44,	24),
#     (45,	25),
#     (46,	25),
#     (47,	26),
#     (48,	26),
#     (49,	27),
#     (50,	27),
#     (51,	28),
#     (52,	28),
#     (32,	29),
#     (54,	29),
#     (55,	30),
#     (56,	30),
#     (57,	31),
#     (58,	31),
#     (59,	32),
#     (60,	32),
#     (61,	33),
#     (62,	33),
#     (63,	34),
#     (64,	35),
#     (65,	36),
#     (66,	37),
#     (67,	38),
#     (68,	39),
#     (69,	40),
#     (70,	41),
#     (71,	42),
#     (71,	43),
#     (72,	44),
#     (73,	45),
#     (74,	46),
#     (75,	47),
#     (76,	48),
#     (77,	49),
#     (77,	50),
#     (78,	49),
#     (78,	50),
# ]

# mycursor.executemany(sql, val)

# db.commit()

# print(mycursor.rowcount, "record inserted.")

# view the Guardian Child Report
# mycursor.execute("SELECT G_First_Name, G_Last_Name, C_First_Name, C_Last_Name FROM CHILD, GUARDIAN, GUARDIANCHILD WHERE CHILD.Child_id = GUARDIANCHILD.Child_id  AND GUARDIAN.Guardian_id = GUARDIANCHILD.Guardian_ID")
# myresult = mycursor.fetchall()
# for x in myresult:
#     x = pd.DataFrame(myresult, columns=[
#         'GuardianFirst', 'GuardianLast', 'ChildFirst', 'ChildLast'])
# print(x)

# view guardian monthly fee report
# mycursor.execute("SELECT G_First_Name, G_Last_Name, C_First_Name, C_Last_Name, Round(datediff(now(), C_Dob)/30, 0) as Age_in_months, G_Fee_Discount, 1000-(1000*G_Fee_Discount) AS Monthly_Fee FROM CHILD, GUARDIAN, GUARDIANCHILD WHERE CHILD.Child_id=GUARDIANCHILD.Child_id  And GUARDIAN.Guardian_id=GUARDIANCHILD.Guardian_ID")
# myresult = mycursor.fetchall()
# for x in myresult:
#     x = panda.DataFrame(
#         myresult, columns=['GuardianFirst', 'GuardianLast', 'ChildFirst', 'ChildLast', 'AgeInMonths', 'FeeDiscount', 'MonthlyFee'])
# print(x)

# view all GUARDIAN records and fields
def displayAllGuardians():
    mycursor.execute("SELECT * FROM GUARDIAN")
    myresult = mycursor.fetchall()
    for x in myresult:
        x = panda.DataFrame(myresult, columns=['ID', 'First', 'MiddleInit', 'Last',
                                               'CellPhone', 'WorkPhone', 'Ext', 'FeeDiscount', 'Address', 'Apt', 'City', 'State', 'Zip'])
    print(x)


# view all CHILD records and fields
def displayAllChildren():
    mycursor.execute("SELECT * FROM CHILD")
    myresult = mycursor.fetchall()
    for x in myresult:
        x = panda.DataFrame(myresult, columns=['ID', 'First', 'Middle', 'Last', 'Gender', 'DOB',
                                               'Date_Started', 'Address', 'Apt', 'City', 'State', 'Zip', 'Status', 'Date_Inactive'])
    print(x)


# startup
# MAIN SCREEN
print("*************************SHAKER DISCOVERY CENTER***************")
print("***************************************************************")

while(True):
    print("\n!=========================*************=======================!")

    print("! PLEASE ENTER 1 TO DISPLAY ALL CHILDREN                        |")
    print("! PLEASE ENTER 2 TO DISPLAY ALL GUARDIANS                       |")
    print("! PLEASE ENTER 3 TO DISPLAY ALL GUARDIANS AND CHILDREN          |")
    print("! PLEASE ENTER 4 TO SEARCH FOR A CHILD                          |")
    print("! PLEASE ENTER 5 TO SEARCH FOR A GUARDIAN's CONTACT INFORMATION |")
    print("! PLEASE ENTER 6 TO SEARCH FOR A CHILD's EMERGENCY CONTACT      |")
    print("! PLEASE ENTER 7 TO ENROLL A NEW CHILD                          !")
    print("! PLEASE ENTER 8 TO SET A CHILD TO INACTIVE                     !")
    print("! PLEASE ENTER 9 TO EXIT                                        !")
    print("\n!=====================*****THANK YOU*****=====================!")
    choice = int(input("\n SELECTION : "))
    if choice == 1:
        displayAllChildren()
    elif choice == 2:
        displayAllGuardians()
    elif choice == 3:
        displayALLGurdianChildren()
    elif choice == 4:
        searchChild()
    elif choice == 5:
        searchGuardian()
    elif choice == 6:
        searchEmergencyContact()
    elif choice == 7:
        newChild()
    elif choice == 8:
        inactivateChild()
    elif choice == 9:
        break
    else:
        print("Sorry , Invalid input, Please Try Again !!! ")
