'''
curl -X POST -d "username=akshat&password=root1234" http://127.0.0.1:8000/api/auth/token/


curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFrc2hhdCIsImV4cCI6MTU2MDYzOTM1NSwiZW1haWwiOiIifQ.rn9Vrcxi5_SQmjj2GgWzBr0w7vm4xNo9v17TprpZ-kk" http://127.0.0.1:8000/api/my/

curl -H "Authorization: JWT <your_token>" http://localhost:8000/protected-url/

curl  http://127.0.0.1:8000/api/my/


curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFrc2hhdCIsImV4cCI6MTU2MDY0MDExNCwiZW1haWwiOiIifQ.ixCqCIuDVDA4qeK9uvizgQOB3SpiOeg1JUfNlmsLvoE" -X POST -H "Content-Type: application/json" -d '{"username":"praja","password":"root1234", 
"profile":{"name":"praja", "email":"abc@gmail.com", "mobile":"9456439965", "gender":"Male", "dob":"2019-06-10"}}' http://localhost:8000/api/register



curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFrc2hhdCIsImV4cCI6MTU2MDY5MDUyOCwiZW1haWwiOiIifQ.KwPC-gzTLcFNY54bMRYlLxpQMRH61Ff58khErj1UTy8" http://localhost:8000/api/profile-list/

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFrc2hhdCIsImV4cCI6MTU2MDY5MDUyOCwiZW1haWwiOiIifQ.KwPC-gzTLcFNY54bMRYlLxpQMRH61Ff58khErj1UTy8" http://localhost:8000/api/retrieve/


curl -X POST -d "username=akshat&password=root1234" http://127.0.0.1:8000/api/login/

curl -X POST -d "id=6" http://127.0.0.1:8000/api/add-friend/

'''