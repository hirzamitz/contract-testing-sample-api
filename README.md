# Sample project for contract testing using pact

This project focuses on contract testing using the python version of [pact](https://docs.pact.io/implementation_guides/python/readme).

## Setting up the project 
Please install virtualenv from [here](https://pypi.python.org/pypi/virtualenv), if you don't have it
 
## Getting to know the sample services

* Open the project directory
* Create a virtual environment using ```virtualenv contract-testing-project```
* Install flask using ```contract-testing-project/bin/pip install flask```
* Install the requests module using ```contract-testing-project/bin/pip install requests```
* Run the provider application: ```./provider_app.py```
* Run the consumer application: ```./consumer_app.py```
* Check the REST the endpoints and understand what has been implemented for the provider application (http://127.0.0.1:5000/)
* Check the REST the endpoints and understand what has been implemented for the consumer application (http://127.0.0.1:5001/)

## License
[MIT](https://choosealicense.com/licenses/mit/)



