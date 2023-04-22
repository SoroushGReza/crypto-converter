# Crypto converter
## Table of contents
### 1. [About](#about)
### 2. [Needed Tools](#needed-tools)
### 3. [Installation](#installation)
### 4. [Testing](#testing)
### 5. [Validation](#validation)
### 6. [Credits](#credits)
### 7. [Deployment](#deployment) 
### 8. [Design Choices](#design-choices) 
### 9. [Improvements](#improvements) <br>
### 10. [User Stories](#user-stories) <br>

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

# [Testing](#testing)
### 1. Run the main script like this:
### **python3 run.py**
##### (Note: If you are using a lower version than Python 3.x, you may need to use **"python"** instead of **"python3"**) <br> <br>
### 2. Replace "run.py" with your **actual** file name.
### 3. Choose a cryptocurrency 

![screenshot-1 choose a cryptocurrency](./assets/images/step1.png)
##### In this case we chose option 2, that is "GALA". <br><br>

### 4. Make sure to enter only **digits** and to only use the numbers that is a choice. In this case "1" and "2". <br><br>


### **Otherwise:**
![screenshot-tryagain1](./assets/images/tryagain1.png)
##### In this case user tried to choose "GALA" by writing "two" with letters. <br><br>

### 5. After choosing cryptocurrency to convert, you will be asked to enter the amount to be converted. 
![screenshot2 enter - amount to convert](./assets/images/step2.png)
##### Make sure to use a dot for entering decimals. <br><br>

### 6. The amount of the cryptocurrency you chose will now be converted to the currencies USD, EURO and SEK.
![screenshot3 - converted amount printed](./assets/images/step3.png)
##### As you can the the amount have been converted using the APIs to get up-to-date rates. Now the program will continue to ask for a new choice to convert, to avoid for the user to need to start the program again after each conversion. <br><br>

### 7. Make sure to only enter digits, and to separate whole numbers and decimals using a dot (.). <br><br>

### **Otherwise:**
![screenshot-tryagain2](./assets/images/tryagain2.png)
##### It will lead to an error saying "Only numbers allowed, try again." <br><br>

# [Validation](#validation)
### This code was validated using two validation sources <br>
* https://pep8ci.herokuapp.com/<br>

* https://extendsclass.com/python-tester.html <br>

#### The validation showed two syntax errors. (Trailing white space on line 58 and 77.) <br><br> 

Whitespaces deleted - Code passed without any syntax errors. 


# [Credits](#credits)
## Author
### This program is written by [Soroush G](https://www.linkedin.com/in/soroush-gholamreza-599173250/) <br><br>

## Special thanks to 
### [CoinGecko](https://www.coingecko.com/) - This project uses the [CoinGecko API](https://www.coingecko.com/en/api/documentation) for cryptocurrency prices. <br><br>

### [Exchange Rate API](https://www.exchangerate-api.com/) - This project uses the Exchange Rate API for exchange rates. <br><br>

### [Requests](https://docs.python-requests.org/en/latest/) - The "**requests**" library helps send HTTP requests. <br> <br>

### The code validation was made in: <br>
* https://pep8ci.herokuapp.com/# <br>
and <br>
* [Extend Class](https://extendsclass.com/python-tester.html) <br><br>


# [Deployment](#deployment)

# [Design Choices](#design-choices)
### - This tool uses a simple text interface, making it easy to use and work on many systems. <br> <br>
### - The tool handles erros to help the tool to recover from issues, like if the user input is invalid, or API issues. <br><br>

# [Improvements](#improvements)
### **Here are some ideas for future adjustments that could improve user experience.** <br> <br>

### 1. **Support more cryptocurrencies:** Expand the tool to support additional cryptocurrencies. That will make it more useful to wider range of users. <br><br>

### 2. **Flexibility:** Add possibility to convert crypto-to-crypto rates. <br><br>

# [User Stories](#user-stories)
## As a user I want to be able to: <br><br>
### ☑ See a list of available cryptocurrencies I can choose from for conversion. <br><br>

### ☑ Enter my choice from the given list, so the conversion process can get started. <br><br>

### ☑ Input the amount that I want to convert. <br><br>

### ☑ See an error message if I input invalid number or choice, so that I can correct my input. <br><br>

### ☑ Rely on the program to fetch the current exchange rates between USD and other currencies (EUR, SEK). <br><br>

### ☑ Rely on the program to fetch the current price of chosen cryptocurrency in USD so that the conversion is made with up-to-date data.<br><br>

### ☑ See converted amount of the chosen cryptocurrency in USD, EUR and SEK, to understand the value of different currencies.<br><br>

### ☑ See an error if there is any issue fetching the cryptocurrency price or exchange rates so that I can be aware of the problem.<br><br>

### ☐ See real-time rates and prices, that is more precise than just up-to-date.<br><br>

## ☑ = User stories satisfied<br>
## ☐ = Need further steps to satisfy

