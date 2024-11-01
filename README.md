# FurKidz
*Am I Responsive Image - Completed Project*

## Table of Contents
- [UX](#ux)
  - [Project Goals](#project-goals)
  - [User Goals](#user-goals)
  - [User Stories](#user-stories)
  - [Design Choices](#design-choices)
  - [Developer Goals](#developer-goals)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Left to Implement](#left-to-implement)
- [Technology Used](#technology-used)
- [Testing](#testing)
  - [Results](#results)
  - [Manual Testing](#manual-testing)
  - [Automation Test](#automation-test)
  - [Validation Tests](#validation-tests)
  - [Lighthouse Testing](#lighthouse-testing)
  - [Bug Problems](#bug-problems)
- [Deployment](#deployment)
- [Credits](#credits)

## UX

### Project Goals
Create an e-commerce site that caters to people who enjoy spoiling their cats and dogs. The site will offer luxury items for pets, including toys, treats, beds, and clothes.

### User Goals
This project aims to assist users in:
- Viewing and navigation
- Registration and user accounts
- Scrolling and searching
- Purchasing and checkout
- Administration and store management

### User Stories

#### Viewing and Navigation
- As a user, I want to easily view products available for purchase.
- As a user, I want a clear and organized homepage, so that I can immediately see featured products, deals, and popular categories.
- As a user, I want to view detailed product descriptions, including images and specifications, so that I can make an informed decision before purchasing.
- As a user, I want to easily view my purchase total at any time.

#### Registration and User Accounts
- As a user, I want to easily create an account so that I can save my preferences and order history.
- As a user, I want to log in and log off easily.
- As a user, I want to be able to recover my password if I forget it.
- As a user, I want to receive an email confirming registration.

#### Scrolling and Searching
- As a user, I want a responsive and fast search bar that provides relevant results.
- As a user, I want to filter products by pet type (cat or dog), size, age, and brand, so that I can find the most suitable products for my pet's needs.
- As a user, I want to sort products by category (e.g., toys, food, accessories) for cats and dogs, so that I can quickly find items relevant to my pet.
- As a user, I want to filter search results by availability, so that I only see items that are currently in stock.

#### Purchasing and Checkout
- As a user, I want a simple and secure checkout process, so that I can complete my purchase quickly and confidently.
- As a user, I want to view a summary of my cart, including item details, quantities, and total cost, before proceeding to payment, so that I can ensure everything is correct.
- As a user, I want to receive an order confirmation and receipt via email immediately after purchase, so that I have a record of my transaction.

#### Administration and Store Management
- As an administrator, I want to manage the inventory, including adding, editing, or removing products, so that the store’s offerings are always up-to-date.
- As an administrator, I want to manage user accounts and permissions, so that I can ensure secure and proper access to the store’s backend.
- As an administrator, I want to view and manage orders, including tracking shipments and handling returns, so that I can ensure customer satisfaction.
- As an administrator, I want to create and manage promotional campaigns, including discount codes and featured products, so that I can drive sales.
- As an administrator, I want to generate reports on sales, inventory, and customer behavior, so that I can make informed decisions to optimize store performance.

### Developer Goals
Allow users to easily:
- Register to the website
- Log in to the website
- Navigate through the site
- Add words and definitions they want to share with others
- Edit words they've added, to correct possible mistakes or add updates
- Delete words they've added

### Design Choices

#### Fonts
#### Colors
- Colour Scheme: black, white, light pink #FAF0F0

#### Styling
- Backgrounds: The design choice of one solid background color was made to maintain accessibility for the user. Solid colors were used to make the content stand out.

#### Content
- Wireframes: Designed in Balsamiq, there are 3 wireframes for each page, providing planned layout and views on large screens, medium screens, and small screens.
  - Big Screens
  - Medium Screens
  - Small Screens

## Features

### Existing Features
### Left to Implement

## Technology Used
- Languages: HTML, CSS, JavaScript, Python
- Frameworks:
- Database:
- Wireframes: Balsamiq
- Favicon: Realfavicongenerator
- Mock-up Image of Site: Am I Responsive
- Responsiveness of the Site: Google Chrome Developer Tools - Used to test
- Icons: Font Awesome
- Logo: Canva
- Version Control: GitHub
- IDE: CodeInstitute IDE
- Deployment: Heroku
- Troubleshooting: Slack, tutor support
- Secret Key: RandomKeyGen
- Validation: W3C Validation Services (CSS and HTML), Pep8CI (Python), jshint (JavaScript)

## Testing

### Results

#### Manual Testing
- CREATE
- READ
- UPDATE
- DELETE
- LOGIN
- GUARDING FROM FORCED ACTIONS
- NAVIGATION

#### Automation Test
Automation testing is a software testing process that uses specialized tools and scripts to automatically execute test cases, compare actual results with expected outcomes, and report discrepancies. An example of this software is Jest. Only manual testing will be used for this development.

#### Validation Tests
- Python
- JavaScript
- View the PDF - CSS Validation
- View the PDF - HTML Validation

#### Lighthouse Testing
- View the PDF - Mobile
- View the PDF - Desktop

#### Bug Problems
- Bugs in initial building:
- After deployment:
- Issues picked up during testing:

## Deployment

### CI Full Template to Create This Project
1. Click on 'Use this template' and select 'Create a new repository'.
2. Enter your chosen repo name.
3. Click 'Create Repository'.
4. From the new GitHub repo, copy the page URL.
5. Open CodeInstitute IDE and navigate to the 'workspaces' page.
6. Click on 'New Workspace'.
7. Select a Repository and paste/search the GitHub repo URL into the box.
8. Click 'Create'.

### How to Work on the Project Code Within a Local IDE
1. To clone this project from GitHub:
   - Follow this link to the Project GitHub repository: [here](#)
   - Under repository name, select 'clone or download'.
   - Copy the clone URL from the repository.
   - In your IDE, open the terminal.
   - Change the working directory to the location where you want the cloned directory to be made.
   - Type `git clone` and your URL from step 3.

### Deployment to Heroku
1. Set Up Your Local Environment:
   - Ensure Git is installed. Check by running `git --version` in your terminal.
   - Ensure Heroku CLI is installed. Check by running `heroku --version` in your terminal.

2. Prepare Your Flask Application:
   - Ensure your Flask application follows a standard structure.
   - Create a virtual environment: `python -m venv venv`.
   - Install necessary packages: Flask, Pymongo, etc.
   - Run `pip3 freeze > requirements.txt` to create/update a `requirements.txt` file containing project dependencies.
   - Run `echo web: python app.py > Procfile` to create a Procfile. Check that the file contains the text 'web: python app.py' and delete any blank lines at the bottom.
   - Push the 2 new files to the GitHub repository.

3. On Heroku:
   - Log in.
   - Select 'Create New App', create a unique name for the app, and select your nearest region.
   - Click 'Create App'.
   - Navigate to the Deploy tab on the Heroku dashboard and select GitHub, search for your repository by name, and click 'Connect'.
   - Navigate to 'Settings', click 'Reveal Config Vars', and input the following: IP, MONGO_DBNAME, MONGO_URI, PORT, SECRET_KEY.
   - Go back to the Deploy tab and click on 'Enable Automatic Deploys'.
   - Click 'Deploy Branch'.
   - Once the build is complete, click on 'Open App' to launch the new app.

## Credits
### Code
### Content
### Media
- [background image](https://www.shutterstock.com/image-photo/cute-dog-411895951?irclickid=yRMyssWdexyPRkhzyd03My66UkCWOJwuiXGeWQ0&irgwc=1&pl=77643-108110&utm_campaign=TinEye&utm_content=108110&utm_medium=Affiliate&utm_source=77643&utm_term=)
### Design Inspiration