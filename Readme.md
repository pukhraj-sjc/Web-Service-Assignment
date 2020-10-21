## Web service assignment
Create a web service which combines two existing web services. The basic requirements of the task are:
1. Fetch a random name from ​https://api.namefake.com/
2. Fetch a random Chuck Norris joke from
http://api.icndb.com/jokes/random?firstName=John&lastName=Doe&limitTo=[nerdy]
3. Combine the results, replacing the first name and last name with the corresponding first name and last name from the random name service, and return them to the user.
4. Include tests for your web service
5. Containerize your web service (using Docker)

## Steps to run the web-service application
Create a clone of the repository in your local system
```
git clone https://github.com/pukhraj-sjc/web-service-assignment.git
```
Create a docker image from the Dockerfile, present in the directory.
Run the below command to create the image
```
docker build -t docker-flask:latest .
```
Once the docker image is created, run the below command to see the image listed
```
docker image ls
```
Create a container to start the web-service application
```
docker run --name flaskapp -p 5000:5000 docker-flask:latest
```
Once the webservice is started, run the below command to receive a respone from the web-application.
```
curl http://localhost:5000
```
## Testing the application
unit test's are also written to test the application.
Run flask_unit.py located inside the app directory to test the application
```
[root@localhost app]# python  flask_unit.py
...
----------------------------------------------------------------------
Ran 3 tests in 24.010s

OK
```
