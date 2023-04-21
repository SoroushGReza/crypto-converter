# Crypto converter
## Table of contents
### 1. [About](#about)
### 2. [Needed Tools](#needed-tools)
### 3. [Installation](#installation)
### 4. [How To Use](#how-to-use)
### 5. [Credits](#credits)
### 6. [Deployment](#deployment) <br> <br>

# [About](#about)
### This program is a simple tool to convert Ethereum (ETH) and Gala (GALA) into USD, EUR and SEK. This is a tool for people that want up-to-date exchange rates for better decision-making. Due to lack of time, the options of crypto currencies is kept to minimum.  <br> <br>

# [Needed Tools](#needed-tools)
## To use this program, make sure you have: 
### - Python 3.x
### - "requests" library <br> <br>

# [Installation](#installation)
## Follow this steps:
### 1. Download the project files or clone the repository. <br> <br>
### 2. Install Python packages with this command in the terminal: <br> 
![screentshot of pip installation](./assets/images/pipimg.png)
#### (In this example, we are using GitPod) <br> <br>
### 3. Get an API key for the Exchange Rate API by signing up [here](https://www.exchangerate-api.com/). <br> <br>
### 4. Make a file named "key.py" in the project folder. <br><br>
### 5. Add this line to the file: <br>
### **EXCHANGERATE_API_KEY = "<YOUR_API_KEY>"** <br> <br>
### 6.  You will replace the "<YOUR_API_KEY>" with your **actual** API key <br><br>

# [How To Use](#how-to-use)
### 1. Run the main script like this:
## **python <path_to_script>/cryptocurrency_converter.py** <br> <br>
### 2. Replace "<path_to_script>" with the **actual** path to you script. <br> <br>
### 3. Follow the steps to pick a cryptocurrency, type the amount you want to change, and see the results in USD, EUR, and SEK. <br><br>


# [Credits](#credits)
### - This project uses the [CoinGecko API](https://www.coingecko.com/en/api/documentation) for cryptocurrency prices. <br><br>

### - This project uses the [Exchange Rate API](https://www.exchangerate-api.com/) for exchange rates. <br><br>


# [Deployment](#deployment)