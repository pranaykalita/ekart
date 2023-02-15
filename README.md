## [pranaykalita/ekart](https://github.com/pranaykalita/ekart)
## [LIVE VIEW on Railway](ekart-production.up.railway.app)

#### building an e-commerce platform using Django. You will start by designing and implementing the core features of an e-commerce website, including product catalogs, shopping carts, and checkout pages. will also work on integrating payment gateways for secure transactions and implementing an order management system to keep track of customer orders.

# Requirements
- python 3.0+ 
- django

## initialization on local (CMD/CommandPromt)

### create Virtual Environment
```
python -m venv environmentName
```
### Activate Environment
```
environmentName\Scripts\Activate
```
### install Django
```
pip install django
```
### Run Server
``` 
python manage.py runserver
```
# 

# project Log

***02 Feb, 2023:***
- Requirements Analysis
- Project Planning

***03 Feb,2023:***
- understanding django basics
- learn to create first app
- Building a raff model of Database needed

***04 Feb,2023:***
- Design login page and registration page
- Trying Custom Model for User Authentication

***05 Feb,2023:***
- Understanding djago MVT
- setup created login registration page with templates and Static folder setup for css js etc static files

***06 Feb,2023:***
- completed login page design
- create a registration system with default user Model

***07 Feb,2023:***
- Databse Creation
- registration system functalities
- Understating Dynamic content to update with JINJA 
- create common navbar to use entire wepages using extends

***08 Feb,2023:***
- design account page to redirect after login
- DRF of Django
- setup virtual environment for project
- migrate the project completely to new environment
- render logged in user in required places

***09 Feb, 2023:***
- Offline Review
- New Task to create Converter app to conver csv to xls & xlsx

***10 Feb, 2023:***
- No Update

***13 Feb,2023:***
- fix login error
- add decorators for pages which need authentication
- show logged in user in navbar after loggedin
- creat project for converter app
- create template html form to get input file as csv from user

***14 Feb,2023:***
- try to Deploy on railway(install whitenose for css serving ,gunicorn )
- create proc file
