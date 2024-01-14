# CogniGuard 🕵️‍♂️✨

## Overview

CogniGuard is a powerful web extension designed to empower users by identifying and combatting dark patterns on various websites, particularly focusing on E-commerce platforms. Ensuring users a transparent and ethical online experience. Dark patterns are deceptive design practices that manipulate user behavior, eroding trust and hindering ethical online experiences.

![GitHub code size](https://img.shields.io/github/languages/code-size/4darsh-Dev/CogniGuard?style=plastic)


## Project Setup Locally 🚀

### Setting up Django API

1. clone the git repository locally.
```git clone https://github.com/4darsh-Dev/CogniGaurd.git```
2. Install python and setup virtual envionment
``` pip install virtualenv ```
``` virtualenv myenv ```
### Activating virtual environment named as myenv
### 1. In Windows 🪟
``` .\myenv\Scripts\activate  ```
### 2. In Linux/Mac 🐧
``` source myenv/bin/activate```

3. Installing required modules and libraries
``` pip install -r requirements.txt ```

4. Running Django Development Server
``` python manage.py makemigrations ```
``` python manage.py migrate ```
``` python manage.py runserver ```
-- Server will be started at localhost (example: http://127.0.0.1:8000/)

### Setting up CogniGuard Web Extension

1. Open Google Chrome Browser and visit url
``` chrome://extensions/ ```
2. Turn on Developer Mode.
3. Click on load unpacked at then select the cogniguard-web folder with manifest.json
4. Click on extension icon and you will find the CogniGuard.


## Tech Stack 🛠️

- **Web Extension:** HTML, CSS, JavaScript 
- **Python (BeautifulSoup, Scrapy):** Web scraping for price data analysis.
- **Django:** Backend for API management and Dark pattern report pattern for CogniGuard
- **BERT Model:** Fine-tuned for sophisticated pattern recognition.



## Features 🌐🔍


1. **JavaScript Code Analysis:** Uncover deceptive tactics through DOM manipulation and event listeners.
2. **Price Manipulation Detection:** Warn users of potential price manipulation and fake urgency.
3. **Crowdsourced Database:** Contribute to a collaborative platform by reporting dark patterns.
4. **Misleading Terms & Conditions Detection:** Identify complex terms and potential data leaks.
5. **Transparency Score Calculation:** Receive website transparency scores for an informed browsing experience.

## Screenshots 📸

[Include screenshots of the extension interface in action.] coming soon.

## Documentation 📖

Detailed documentation on usage, contribution guidelines, and API integration can be found in the [Documentation Link](https://github.com/4darsh-Dev/CogniGaurd/wiki).

## Authors 🧑‍💻

- [@4darsh-Dev (Adarsh Maurya)](https://github.com/4darsh-Dev) - Project Lead

- [@amansingh494 (Aman Singh)](https://github.com/amansingh494) - FrontEnd Developer

- [@DharmeshTanwar56 (Dharmesh Tanwar)](https://github.com/DharmeshTanwar56) - UI/UX Designer

- [@goldy-dev123 (Goldy)](https://github.com/goldy-dev123) - Technical Writing


## Contributing Guidelines 🤝🚀


Thank you for considering contributing to CogniGuard! We welcome your help in making this project even better.

Here are the key points to guide your contributions:

- **Fork the Repository:** Start by forking the CogniGuard repository to your own GitHub account. 🍴

- **Clone the Repository:** Clone the forked repository to your local machine using `git clone https://github.com/4darsh-Dev/CogniGaurd `. 💻

- **Create a Branch:** Create a branch for your contributions using a descriptive branch name. 🌿

- **Make Changes:** Implement your changes or additions, ensuring they align with the project's goals. 🚀

- **Testing:** Test your changes thoroughly to ensure functionality and prevent regressions. ✔️

- **Commit Changes:** Commit your changes with clear, concise messages. 💬

- **Create Pull Request:** Push your changes to your forked repository and create a Pull Request (PR) to the main CogniGuard repository. 🎉

- **Follow Code Standards:** Adhere to coding standards and guidelines defined in the project. 📋

- **Provide Detailed PR Description:** Clearly explain the purpose and impact of your PR. 📝

- **Participate in Discussions:** Engage in discussions related to your PR and address feedback promptly. 💬

By following these guidelines, you contribute to the growth and improvement of CogniGuard. Thank you for your valuable contributions! 🚀

## Roadmap 🗺️

Check out the project's roadmap to understand the planned features, improvements, and future milestones.
- Creating the CogniGaurd Frontend and Api integration.
- Building Datasets for fine tuning BERT Deep learning Model.
- Setting up python virtual environment with necessary modules and libraries.
- Fine Tuning BERT model for analyzing terms and conditions page.
- Testing the BERT model on random websites.
- Django Backend for serving CogniGuard Landing and report dark pattern pages.
- Setting up Database for Django app.
- ...updating soon

## Code of Conduct 🧑‍💼

Familiarize yourself with the project's code of conduct to ensure a positive and inclusive community.
- **Welcome to the CogniGuard Community!** 🚀
- **Values:** Prioritize inclusivity, respect, collaboration, open-mindedness, and transparency. 🌟
- **Expected Behavior:** Embrace positive language, constructive criticism, and acknowledgment of efforts. Adhere to guidelines and maintain a respectful tone. 🌈
- **Unacceptable Behavior:** Prohibit harassment, trolling, personal attacks, and privacy violations. 🚫
- **Reporting:** Promptly report violations. Investigation includes warnings or removal from the community. 🛡️
- **Conclusion:** We aim to create a space where everyone feels welcome, valued, and respected. Join us in fostering a positive and collaborative community! 🙌


## Acknowledgments 🙏

We express our gratitude to the incredible individuals who have contributed to the development and success of CogniGuard. 🌟 Your dedication, passion, and insights have played a pivotal role in shaping this project.

Special thanks to the open-source community for their continuous support and collaborative spirit. 🚀 Your contributions, whether big or small, have contributed to the growth and improvement of CogniGuard.

We appreciate the efforts of each tester, developer, and community member who has devoted time and expertise to make CogniGuard a valuable tool.

Thank you for being part of our journey and contributing to a transparent and user-centric online environment. 🌐 Your involvement is crucial to the success of CogniGuard!

## Feedback 📬

We value your feedback! Report issues at adarsh@onionreads.com 
Propose features, or submit pull requests. Let's create a fair and transparent digital environment together! 🌐✨
