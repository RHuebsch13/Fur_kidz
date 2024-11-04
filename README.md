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


#### User Account Management
- **User Registration/Login**: Allow customers to create accounts and log in to view their order history and save preferences.
- **Profile Management**: Users can update their personal information, shipping addresses, and payment methods.

#### Product Management
- **Product Catalog**: Display products with images, descriptions, prices, and specifications.
- **Categories and Filters**: Organize products into categories and enable filtering by various attributes (size, color, price range, etc.).
- **Product Search**: A search bar that allows users to find products quickly.

#### Shopping Cart
- **Add to Cart**: Users can add items to a virtual shopping cart.
- **View Cart**: Users can view the contents of their cart, including quantities and total prices.
- **Update Cart**: Options to change quantities or remove items from the cart.

#### Checkout Process
- **Secure Checkout**: A secure page for users to enter payment and shipping information.
- **Guest Checkout**: Allow users to purchase without creating an account.
- **Order Summary**: Provide a summary of the order before finalizing the purchase.
- **Integrated Payment Gateway**: Handle transactions securely through third-party services like Stripe.

#### Reviews and Ratings
- **Customer Reviews**: Allow users to leave feedback and rate products.

#### Mobile Responsiveness
- **Mobile-Friendly Design**: Ensure the website is responsive and usable on smartphones and tablets.

#### Security Features
- **SSL Certificate**: Secure the site with HTTPS to protect user data during transactions.
- **Data Protection**: Compliance with regulations (like GDPR) to protect user data.


### Left to Implement

#### Shipping and Delivery
- **Shipping Options**: Offer multiple shipping methods (standard, express, international, etc.).
- **Shipping Cost Calculation**: Automatically calculate shipping costs based on user location and selected shipping method.
- **Tracking Information**: Provide users with tracking information for their shipments.

#### Customer Support
- **Contact Us**: A page or section where customers can reach support via email, chat, or phone.
- **FAQs**: Frequently asked questions section to help users find answers quickly.
- **Live Chat**: Instant messaging support for real-time assistance.

#### Reviews and Ratings
- **Review Moderation**: Enable site administrators to approve or reject reviews.

#### Marketing Features
- **Discount Codes and Coupons**: Allow users to apply promotional codes during checkout.
- **Email Marketing Integration**: Capture user emails for newsletters and promotional campaigns.
- **Abandoned Cart Recovery**: Send reminders to users who leave items in their cart without completing the purchase.

#### Analytics and Reporting
- **Sales Reports**: Generate reports on sales, revenue, and inventory levels.
- **User Behavior Analytics**: Track how users interact with the site for insights on improving the user experience.

#### Social Media Integration
- **Social Sharing Buttons**: Allow users to share products on social media platforms.
- **Social Login**: Enable users to register and log in using their social media accounts.

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
##### 1. CREATE
- **Expected**: Users can create an account and add products to their cart.
- **Testing**: 
  - Registered a new user account successfully.
  - Added products to the shopping cart.
- **Result**: 
  - The account was created, and products were added to the cart as expected.
- **Fix**: No issues encountered.

##### 2. READ
- **Expected**: Users can view product listings, details, and their cart total.
- **Testing**: 
  - Accessed product listings and detailed product pages.
  - Monitored the cart total while adding/removing products.
- **Result**: 
  - Content not responsive to smaller screens.
- **Fix**: Adjusted media queries. 

##### 3. UPDATE
- **Expected**: Users can edit their profiles, update product quantities in their cart.
- **Testing**: 
  - Updated user profile information.
  - Changed product quantities in the cart.
- **Result**: 
  - Remove button removed all products from bag. Not one at a time if more than one of the same item.
- **Fix**: Updated handling so that one item at a time was removed if there was more than one of the same item.

##### 4. DELETE
- **Expected**: Users can delete their accounts and remove products from their cart, while administrators can remove products from inventory.
- **Testing**: 
  - Deleted a user account.
  - Removed products from the shopping cart.
  - Removed products from inventory as an administrator.
- **Result**: 
  - Account and product deletions executed successfully.
- **Fix**: No issues encountered.

##### 5. LOGIN
- **Expected**: Users can log in and log out easily.
- **Testing**: 
  - Successfully logged in with valid credentials and logged out.
  - Attempted login with invalid credentials to test error handling.
- **Result**: 
  - Login and logout functions worked as intended, and appropriate error messages displayed for failed attempts.
- **Fix**: No issues encountered.

##### 6. GUARDING FROM FORCED ACTIONS
- **Expected**: Users cannot access restricted pages without proper authentication.
- **Testing**: 
  - Attempted to access admin pages without logging in.
- **Result**: 
  - Access was denied, and users were redirected to the login page.
- **Fix**: No issues encountered.

##### 7. NAVIGATION
- **Expected**: Users can navigate through the site easily.
- **Testing**: 
  - Tested all navigation links (home, categories, product pages).
  - Ensured responsive design on various devices.
- **Result**: 
  - All links worked correctly, and the site was responsive.
- **Fix**: No issues encountered.

##### WEBHOOK
- expectated: The form is on the database if payment flows breaks.
- testing: In the JavaScript file - comment out the form submission and make another purchase.This simulates either a user who closed the page before the form was submitted
- result: behaves as expected

## User Stories Integration

1. **Viewing and Navigation**
   - Successfully viewed product listings and detailed product descriptions.
   - The homepage is clear and organized, showcasing featured products and popular categories.
   - Users can easily view their purchase total at any time.
   - BUGS: item images not responsive on smaller screens, updated media queries.

2. **Registration and User Accounts**
   - Users can create accounts, log in and out easily, recover passwords, and receive confirmation emails upon registration.

3. **Scrolling and Searching**
   - The search functionality is responsive and accurate.
   - Users can filter and sort products effectively by various criteria.

4. **Purchasing and Checkout**
   - The checkout process is simple and secure, allowing users to view cart summaries and receive email confirmations after purchases.
   - BUGS: JS file for Stripe elements was not loading correctly. Corrected file path

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
  * relational database was used, SQLite installed. This did not allow for some function so had to convert over to PostgreSQL using the code institute PostgreSQL URL provided. his worked must better.
  * spacing issues where the products heading did not display as they were covered with other content. Custom css was used to crrect this.
- After deployment:
- Issues picked up during testing:
* no delete confirmation message afer deleting. 

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
- Code institute Boutique Ado 
- [Stripe](https://docs.stripe.com/)
- [Django](https://docs.djangoproject.com/en/5.1/)
- [w3schools](https://www.w3schools.com/python/)
- [Payton Clark Smith](https://www.youtube.com/watch?v=mRWdhN4XFzo)


### Content
### Media
- [background image](https://www.shutterstock.com/image-photo/cute-dog-411895951?irclickid=yRMyssWdexyPRkhzyd03My66UkCWOJwuiXGeWQ0&irgwc=1&pl=77643-108110&utm_campaign=TinEye&utm_content=108110&utm_medium=Affiliate&utm_source=77643&utm_term=)
- [stock images](https://www.deviantart.com/)
- [stock images](https://www.pexels.com/)
- [stock images](https://www.flickr.com/)
- [stock images](https://www.pickpik.com/)
- [stock images](https://www.thecookierookie.com/)
- [stock image](https://longtermcarelink.wordpress.com/)
- [stock images](https://pixabay.com/)

### Design Inspiration
- Boutique Ado 