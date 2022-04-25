# DataChain

In the modern era of technology, data is often defined as the new oil. It plays a key role
in the decision making process that can make or break an institution. Machine Learning
models are the key components that help in predicting the hidden patterns in the given
data. Since these models are data-driven and sometimes require a massive amount of
data, it is beyond the reach of the common man. The proposed platform aims to bridge
this gap between the layman and the process of creating, and maintaining the state of
art machine learning algorithms. The proposed platform employs the blockchain as a
transaction and user identity platform and offers the services of creating various models
that are based on different types of ML algorithms like Incremental Learning, Deep
Learning and Conventional Machine Learning Algorithms. The paper also discusses the
various problems of handling the GAS fees and the real-time updation of the model. The
platform perceives the accumulated models and datasets as the resources and is free
from the parties like DataBrokers.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. S
### Prerequisites
It is assumed that the Node JS(>14) and Python(>3.0) and MySQL are installed in your local machine.
As the project is a DeCentralised Application, Metamask is necessary for the proper working and it can be found [here](https://metamask.io/).

The project is uses Svelte JS as Frontend, Flask as server and MySQL as the Persistant Storage. The project employs the Ethereum blockchain and the smart contracts are implemented in the Solidity and uses Ganache for deploying the local ethereum blockchain. The Ganche and Flask installation can be found in the following link.

* [Ganache App Image](https://trufflesuite.com/ganache/)
* [Flask installation](https://flask.palletsprojects.com/en/2.1.x/installation/)

```
pip install mysql-connector-python 
npm install -g truffle
```

### Installing

* #### Blockchain:
  * Ethereum is used as a trust establishment platform. Start the Appimage of the Ganche and create a new workspace. Add the truffle-config.js to the workspace.
  * Navigate to the Smart Contract Folder in Terminal and execute the following command

```
truffle migrate -reset
```
* #### Server
  * It is assumbed that a new virtual environment is created and Flask is installed in it. And the virtual environment is activated.
  * To fireup the server execute the following commands:

```
export FLASK_APP=server
flask run -p 3000
```

* #### FrontEnd
  * It is assumbed that node is installed in the locla machine.
  * To install all the necessary packages, navigate to the FrontEnd directory, then run the following command

```
npm install
```
 * In order to start the develeopment server,use this command
 ```
npm run dev
```
* #### Database
  * To import the database folder, import the SQL dump file from Database direcoty, into the MySQL database.



## Screenshots

![](/screenshots/1.png)

![](/screenshots/2.png)

![](/screenshots/3.png)



## Built With

* [Svelte](https://svelte.dev/) - The Front End JS Platfrom
* [Flask](https://flask.palletsprojects.com/en/2.1.x/) - Server 
* [MySQL](https://www.mysql.com/) - Persistant Storage
* [Solidity](https://soliditylang.org/) - Language used to Deploy Smart Contract
* [Truffle Suite](https://trufflesuite.com/) - Tools for Developing and Testing and Deploying Smart Contract


## Authors

* **Venakta Raghava Kurada** - *Initial work* - [K.V.Raghava](https://github.com/R9512)

## Acknowledgments

* Shri. Dr. Pallav K Baruah
* Rajarshi V


## 🤝 Support
Contributions, issues, and feature requests are welcome!
