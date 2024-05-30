# CogniGuard 🕵️‍♂️✨
<div>
    <img align=top src="https://miro.medium.com/max/1400/1*c4YgRXYQayOVWxV37ourrw.png" width="100%"/>

<div>
<br>

## Overview

CogniGuard is a powerful web extension designed to empower users by identifying and combatting dark patterns on various websites, particularly focusing on E-commerce platforms. Ensuring users a transparent and ethical online experience.

##### About Dark Patterns => https://www.deceptive.design/

<p align="center">
  <img src="https://onionreads.com/wp-content/uploads/2024/01/Screenshot-2024-01-15-014420.png" alt="CogniGuard" width="600px" />
</p>

<iframe width="560" height="315" src="https://www.youtube.com/embed/1DoYa1wVWhA?si=FCnzDxHuiJs5_Q4P" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


![GitHub code size](https://img.shields.io/github/languages/code-size/4darsh-Dev/CogniGaurd?style=plastic)
![GitHub contributors](https://img.shields.io/github/contributors/4darsh-Dev/CogniGaurd?style=plastic)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/4darsh-Dev/CogniGaurd)
![GitHub issues](https://img.shields.io/github/issues/4darsh-Dev/CogniGaurd)
![GitHub License](https://img.shields.io/github/license/4darsh-Dev/CogniGaurd)
[![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)](https://github.com/4darsh-Dev/CogniGaurd)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://github.com/4darsh-Dev/CogniGaurd)
[![JavaScript]( 	https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://github.com/4darsh-Dev/CogniGaurd)
[![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://github.com/4darsh-Dev/CogniGaurd)
[![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://github.com/4darsh-Dev/CogniGaurd)
[![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)](https://github.com/4darsh-Dev/CogniGaurd)

<!-- ![GitHub Release](https://img.shields.io/github/v/release/4darsh-Dev/CogniGaurd) -->
![GitHub forks](https://img.shields.io/github/forks/4darsh-Dev/CogniGaurd)
![GitHub Repo stars](https://img.shields.io/github/stars/4darsh-Dev/CogniGaurd)

## Cogni-BERT Model Scores

### Sweeps Training Hyperparametrs

<p align="center">
  <img src="https://onionreads.com/wp-content/uploads/2024/05/cogni-bert-12sweeps.png" alt="BERT Fine-Tuned Sweep training " width="600px" />
</p>



## Project Setup Locally 🚀

### Link of Cogni-BERT Trained Model
1. Huggingface spaces link --> https://huggingface.co/spaces/4darsh-Dev/dark_pattern_detector_app/tree/main/models

### Setting up Django Backend

1. clone the git repository locally.
```bash 
git clone https://github.com/4darsh-Dev/CogniGaurd.git
```
2. Install python and setup virtual envionment. 
#### 1. Open terminal 
```bash 
pip install virtualenv 
```
```bash 
cd CogniGaurd
```
```bash 
cd api
```

```bash 
python -m venv myenv 
```
#### Activating virtual environment named as myenv
##### 1. In Windows 🪟
```bash 
.\myenv\Scripts\activate  
```
##### 2. In Linux/Mac 🐧
```bash
 source myenv/bin/activate
 ```

3. Installing required modules and libraries
```bash
 pip install -r requirements.txt 
 ```

4. Running Django Development Server
```bash 
python manage.py makemigrations 
```
```bash 
python manage.py migrate 
```
```bash 
python manage.py runserver 
```
-- Server will be started at localhost (example: http://127.0.0.1:8000/)

### Setting up CogniGuard Web Extension

1. Open Google Chrome Browser and visit url
``` bash
 chrome://extensions/ 
 ```
2. Turn on Developer Mode.
3. Click on load unpacked and then select the cogniguard-web folder with manifest.json
4. Click on extension icon and you will find the CogniGuard.
5. Open the desired website URL (https://snapdeal.com/) on web browser and then click on Analyze button.
6. The Analyzing process will start running on backend. 


## Tech Stack 🛠️

- **Web Extension:** HTML, CSS, JavaScript 
- **Python (BeautifulSoup, Scrapy):** Web scraping for price data analysis.
- **Django:** Backend for API management and Dark pattern report pattern for CogniGuard
- **BERT Model:** Fine-tuned for sophisticated pattern recognition.




## Screenshots 📸

[Include screenshots of the extension interface in action.] coming soon.

## Documentation 📖

Detailed documentation on usage, contribution guidelines, and API integration can be found in the [Documentation Link](https://github.com/4darsh-Dev/CogniGaurd/wiki).

## Contributors 🧑‍💻

- [@4darsh-Dev (Adarsh Maurya)](https://github.com/4darsh-Dev) - Project Lead

- [@amansingh494 (Aman Singh)](https://github.com/amansingh494) - FrontEnd Developer

- [@Anmolgoel29 (Anmol Goel)](https://github.com/Anmolgoel29) - Machine Learning

- [@DharmeshTanwar56 (Dharmesh Tanwar)](https://github.com/DharmeshTanwar56) - UI/UX Designer

- [@goldy-dev123 (Goldy)](https://github.com/goldy-dev123) - Technical Writing



## Acknowledgments 🙏

We express our gratitude to the incredible individuals who have contributed to the development and success of CogniGuard. 🌟 Your dedication, passion, and insights have played a pivotal role in shaping this project.

Special thanks to the open-source community for their continuous support and collaborative spirit. 🚀 Your contributions, whether big or small, have contributed to the growth and improvement of CogniGuard.

## Feedback 📬

We value your feedback! Report issues at adarsh@onionreads.com 
Propose features, or submit pull requests. Let's create a fair and transparent digital environment together! 🌐✨
