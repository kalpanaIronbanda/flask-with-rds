launch ec2----
create rds----
ssh to ec2 


install dependencies
1.yum install python3
2.yum install python3-pip
3.pip install flask
4.dnf install mariadb105-server -y
5.pip install mysql-connector-python

connect to rds 
a.mysql -h host -u username -p
#switch to database
b.use collage
#create table (u can replace name,roll,grade column names as u needed )
c.CREATE TABLE <tableName>  (     name VARCHAR(50) NOT NULL,     roll INT NOT NULL,     grade CHAR(1) NOT NULL );
#insert values (whatever u gave above give the values for it)
d.INSERT INTO <tableName> (name, roll, grade) VALUES ('leo hank', 103, 'A');


create a folder and 
clone the repo
run the application in 
python3 app.py 


