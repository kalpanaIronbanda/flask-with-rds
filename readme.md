launch ec2----
create rds----
ssh to ec2 


install dependencies
1.yum install python3
2.yum install python3-pip
3.pip install flask
4.dnf install mariadb105-server -y
5.pip install mysql-connector-python--
->all the above will be installed by running dependencies.sh file

connect to rds 
a.mysql -h host -u username -p
#switch to database
b.use collage
#create table (u can replace name,roll,grade column names as u needed )
c.CREATE TABLE <tableName>  (     name VARCHAR(50) NOT NULL,     roll INT NOT NULL,     grade CHAR(1) NOT NULL );
#insert values (whatever u gave above give the values for it)
d.INSERT INTO <tableName> (name, roll, grade) VALUES ('leo hank', 103, 'A');

#if u r going with manually follow the below
1.create a folder and 
2.clone the repo and open the app.py file and give the credentials of the database
3.run the application 
---->python3 app.py 

#If u r using jenkins follow below
1.Install Jenkins on your server.
2.Install the necessary plugins such as Git plugin, AWS Pipeline plugin, etc.
3.Create a new pipeline job in Jenkins and configure the SCM settings to point to your Git repository that contains the Flask application code.
4.In the pipeline job configuration, under the "Pipeline" section, select "Pipeline script from SCM" in the "Definition" field and configure the SCM settings accordingly.
5.give the jenkinsfile and save it
6.now build the job and run the application in the target server


