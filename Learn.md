# Learn.md ✍
# CogniGuard 🕵️‍♂️✨
CogniGuard is a powerful web extension designed to empower users by identifying and combatting dark patterns on various websites, particularly focusing on E-commerce platforms. Ensuring users a transparent and ethical online experience.
<br>
[About Dark Patterns]( https://www.deceptive.design/)

# Table of Contents 
1. [Introduction](#introduction-)
2. [Tech Stack](#tech-stack-)
3. [Contributing](#contributing-)
   - [Development Workflow](#development-workflow)
   - [Issue Report Process](#issue-report-process)
   - [Pull Request Process](#pull-request-process-)
4. [Setting Up on your machine](#setting-up-on-your-machine-)
5. [Resources for Beginners](#resources-for-beginners-)
   - [Basics of Git and GitHub](#basics-of-git-and-github-)
6. [Documentation](#documentation-)
7. [Code Reviews](#code-reviews-)
8. [Feature Requests](#feature-requests-)
9. [Spreading the Word](#spreading-the-word-)
11. [Motivation](#motivation-)

## Introduction 🖥️
CogniGuard allows users to calculate their carbon footprint based on various parameters. It provides detailed insights and suggestions on how to reduce their carbon emissions. The name "CogniGuard" is derived from "Prithvi" (Earth) and "We," emphasizing collective action and collaboration. 
Visit the live application [here](https://CogniGuard.onrender.com).

## Tech Stack 🗃️

- **Web Extension:** HTML, CSS, JavaScript 
- **Python (BeautifulSoup, Scrapy):** Web scraping for price data analysis.
- **Django:** Backend for API management and Dark pattern report pattern for CogniGuard
- **BERT Model:** Fine-tuned for sophisticated pattern recognition.

## Contributing 📝
Raise and issue; Get assigned and then work on fixing the issue.
We welcome contributions to CogniGuard! Follow these steps to contribute:

1. **Fork the Repository**: Create your own copy of the repository on your GitHub account.
![image](https://github.com/debangi29/CogniGaurd/assets/117537653/9f495dc8-79e9-4c99-af31-26fc14c0941f)



2. **Clone the Repository** : Clone the repository for making commits.
   ```bash
   git clone https://github.com/4darsh-Dev/CogniGaurd.git
   ```
      <br>
   
![image](https://github.com/debangi29/CogniGaurd/assets/117537653/7885fd34-36de-4934-9d2b-cd3aac767ee8)


3. **Create a New Branch** for your feature or bug fix: Make a separate branch to work on specific features or fixes and switch to the correct branch.
```bash
git checkout -b <new-branch-name>
```
4. **Make Changes** and commit them: Implement your changes and save them with a descriptive commit message.
```bash
git add .
git commit -m "Describe your changes"
```
5. **Push Your Changes** to your fork: Upload your committed changes to your GitHub fork.
   ```bash
   git push origin <branch_name>
   ```
6. **Create a Pull Request ✅**: Propose your changes to be merged into the original repository.
   <br>
   
![image](https://github.com/debangi29/CogniGaurd/assets/117537653/1b054c7a-5f46-48d3-b409-fa324c22ee3a)

### Development Workflow
- Always work on a new branch for each issue or feature.
- Keep your branch up to date with the main repository's master branch.
- Write clear and descriptive commit messages.
- Test your changes thoroughly before submitting a pull request.

### Issue Report Process
1. Go to the project's issues section.
2. Select the appropriate template for your issue.
3. Provide a detailed description of the issue.
4. Wait for the issue to be assigned before starting to work on it.

### **Pull Request Process 🚀**

1. Ensure that you have self reviewed your code.
2. Make sure you have added the proper description for the functionality of the code.
3. I have commented my code, particularly in hard-to-understand areas.
4. Add screenshot it help in review.
5. Submit your PR by giving the necesarry information in PR template and hang tight we will review it really soon.

# Setting Up on your machine ⚙️

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


## Resources for Beginners 📚
### Basics of Git and GitHub 📂
- [Forking a Repo](https://help.github.com/en/articles/fork-a-repo)
- [Cloning a Repo](https://help.github.com/en/articles/cloning-a-repository)
- [Creating a Pull Request](https://help.github.com/en/articles/creating-a-pull-request)
- [Getting Started with Git and GitHub](https://guides.github.com/introduction/git-handbook/)
- [Learn GitHub from Scratch](https://www.youtube.com/watch?v=w3jLJU7DT5E)


## 📍Documentation
Detailed documentation on usage, contribution guidelines, and API integration can be found in the [Documentation Link](https://github.com/4darsh-Dev/CogniGaurd/wiki).
- Document any significant changes or additions to the codebase.
- Provide clear explanations of the functionality, usage, and any relevant considerations.

## Code Reviews 🔎
- Be open to feedback and constructive criticism from other contributors.
- Participate in code reviews by reviewing and providing feedback.

## Feature Requests 🔥
We value your feedback! Report issues at adarsh@onionreads.com 
Propose features, or submit pull requests. Let's create a fair and transparent digital environment together! 🌐✨

## Spreading the Word 👐
- Share your experience and the project with others.
- Spread the word about the project on social media, developer forums, or any relevant community platforms.


Thank you for contributing to CogniGuard! Together, we can make a significant impact. Happy coding! 🚀
## Don't forget to ⭐ the repository!
