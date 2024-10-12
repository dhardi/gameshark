
# Testing

## Bug and Fix

## Challenges Faced

### 1. User Authentication
- **Challenge:** Setting up user authentication was initially difficult, especially ensuring users could only edit their own profile, wishlist, and testimonials.
- **Solution:** Implemented Django's authentication system along with custom decorators to restrict user access to specific pages based on their login status.

### 2. Email Functionality
- **Challenge:** Configuring email functionality for user registration and password recovery was challenging, especially when setting up SMTP servers.
- **Solution:** Correctly configured the SMTP settings in `settings.py`, ensuring proper error handling for common authentication errors.

### 3. Image Uploads
- **Challenge:** Ensuring that profile pictures and product images uploaded properly and displayed correctly across different sections.
- **Solution:** Added media configurations, handled image file storage paths, and applied checks for missing images to improve user experience.

### 4. Database Relationships
- **Challenge:** Managing relationships between products, categories, reviews, and users posed issues when setting up foreign keys.
- **Solution:** Corrected the database models to establish proper foreign key and many-to-many relationships, especially between products, categories, and user profiles.

### 5. Template Rendering Issues
- **Challenge:** The Django template sometimes failed to render context variables correctly, leading to issues with the display of dynamic content.
- **Solution:** Carefully debugged the template context in views, ensuring that the data passed to the templates was accurate and properly handled.

## Lessons Learned
- Thoroughly test template variables and context data to ensure smooth page rendering.
- Pay attention to database relationships and how they impact views and templates.
- Ensure that media files (such as profile images) are properly configured in Django's settings and handled carefully in templates.

## Future Features
- Implement a recommendation system based on user behavior.
- Create user roles with different permission levels (admin, seller, buyer).



### Testing (Post Development Phase)
#### Validation

##### HTML
## Impact on Functionality

Despite the presence of these errors, it is important to note that they do not hinder the overall functionality of the website. The site continues to operate as intended, allowing users to navigate and access its features without issues. 

### Conclusion

While these errors indicate areas for improvement in the HTML structure, they do not affect the site's performance or user experience. Addressing these issues will enhance code quality and maintainability, ensuring compliance with web standards.

![HTML Validation Image](https://github.com/dhardi/gameshark/blob/main/static/images/html.png)

##### CSS
[Description of CSS validation]

![CSS Validation Image](https://github.com/dhardi/gameshark/blob/main/static/images/css_validator.png)

##### JavaScript


![Review](https://github.com/dhardi/gameshark/blob/main/static/images/add_review_java.png)

![Testimonial](https://github.com/dhardi/gameshark/blob/main/static/images/add_testimonial_java.png)

![Product](https://github.com/dhardi/gameshark/blob/main/static/images/produtcs_java.png)

##### Python - PEP8 Standards using `pycodestyle`
[Adherence to Python's PEP8 coding standards by using the `pycodestyle` tool for validation. You can find screenshots of the tests in the link below.]

- [Detailed Python Testing and Validation](https://github.com/dhardi/gameshark/blob/main/python_testing.md)






# Lighthouse Scores

## Home Page
- **Desktop**  
  ![Desktop Lighthouse Score](https://github.com/dhardi/gameshark/blob/main/static/images/home_lighthouse.png)

- **Mobile**  
  ![Mobile Lighthouse Score](https://github.com/dhardi/gameshark/blob/main/static/images/home_mobile_lighthouse.png)

---

## Products Page
- **Desktop**  
  ![Desktop Lighthouse Score](https://github.com/dhardi/gameshark/blob/main/static/images/products_lighthouse.png)

- **Mobile**  
  ![Mobile Lighthouse Score](https://github.com/dhardi/gameshark/blob/main/static/images/produtcs_mobile_lighthouse.png)

---

## Product Details Page
- **Desktop**  
  ![Desktop Lighthouse Score](https://github.com/dhardi/gameshark/blob/main/static/images/product_detail_lighthouse.png)

- **Mobile**  
  ![Mobile Lighthouse Score](https://github.com/dhardi/gameshark/blob/main/static/images/produtcs_mobile_lighthouse.png)

---

## Review Page
- **Desktop**  
  ![Desktop Lighthouse Score](https://github.com/dhardi/gameshark/blob/main/static/images/review_lighthouse.png)

- **Mobile**  
  ![Mobile Lighthouse Score](https://github.com/dhardi/gameshark/blob/main/static/images/review_mobile_lighthouse.png)

---

## Shopping Cart Page
- **Desktop**  
  ![Desktop Lighthouse Score](https://github.com/dhardi/gameshark/blob/main/static/images/bag_lighthouse.png)

- **Mobile**  
  ![Mobile Lighthouse Score](https://github.com/dhardi/gameshark/blob/main/static/images/bag_mobile_lighthouse.png)

---

## Checkout Page
- **Desktop**  
  ![Desktop Lighthouse Score](https://github.com/dhardi/gameshark/blob/main/static/images/checkout_lighthouse.png)

- **Mobile**  
  ![Mobile Lighthouse Score](https://github.com/dhardi/gameshark/blob/main/static/images/checkout_mobile_lighthouse.png)

---

## Profile Page
- **Desktop**  
  ![Desktop Lighthouse Score](https://github.com/dhardi/gameshark/blob/main/static/images/profile_lighthouse.png)

- **Mobile**  
  ![Mobile Lighthouse Score](https://github.com/dhardi/gameshark/blob/main/static/images/profile_mobile_lighthouse.png)

---

## Checkout Success / Order History Page
- **Desktop**  
  ![Desktop Lighthouse Score](https://github.com/dhardi/gameshark/blob/main/static/images/checkout_lighthouse.png)

- **Mobile**  
  ![Mobile Lighthouse Score](https://github.com/dhardi/gameshark/blob/main/static/images/checkout_mobile_lighthouse.png)

---

## Wishlist Page
- **Desktop**  
  ![Desktop Lighthouse Score](https://github.com/dhardi/gameshark/blob/main/static/images/wishlist_lighthouse.png)

- **Mobile**  
  ![Mobile Lighthouse Score](https://github.com/dhardi/gameshark/blob/main/static/images/wishlist_mobile_lighthouse.png)

---

## Testimonial Page
- **Desktop**  
  ![Desktop Lighthouse Score](https://github.com/dhardi/gameshark/blob/main/static/images/testimonnial_lighthouse.png)

- **Mobile**  
  ![Mobile Lighthouse Score](https://github.com/dhardi/gameshark/blob/main/static/images/testimonial_mobile_lighthouse.png)

---


## User Stories

### Epic: Reviews
- **Delete Review**
  - **#33** by dhardi
- **Edit Review Product**
  - **#32** by dhardi
- **Review App**
  - **#31** by dhardi
- **Testimonial Edit**
  - **#30** by dhardi
- **Additional Reviews**
  - **#29** by dhardi

### Epic: Wishlist
- **Buy it from Wishlist**
  - **#28** by dhardi
- **Remove from Wishlist**
  - **#27** by dhardi
- **Wishlist Functionality**
  - **#26** by dhardi

### Epic: Products Management
- **Delete a Product**
  - **#25** by dhardi
- **Edit/Update a Product**
  - **#24** by dhardi
- **Add a Product**
  - **#23** by dhardi

### Epic: Order Confirmation
- **Receive an Email Confirmation After Checkout**
  - **#22** by dhardi
- **View an Order Confirmation After Checkout**
  - **#21** by dhardi

### Epic: Payment Security
- **Feel My Personal and Payment Information is Secure**
  - **#20** by dhardi
- **Easily Enter My Payment Information**
  - **#19** by dhardi

### Epic: Shopping Cart
- **Adjust the Quantity of Items in My Bag**
  - **#18** by dhardi
- **View Items in My Bag to Be Purchased**
  - **#17** by dhardi
- **Easily Select the Quantity of a Product**
  - **#16** by dhardi

### Epic: Search and Sorting
#### Search Functionality
- **Easily See What I've Searched for and the Number of Results**
  - **#15** by dhardi
- **Search for a Product by Name or Description**
  - **#14** by dhardi

#### Sorting Products
- **Sort Multiple Categories or Products Simultaneously**
  - **#13** by dhardi
- **Sort a Specific Category of Products**
  - **#12** by dhardi
- **Sort the List of Available Products**
  - **#11** by dhardi

### Epic: User Profile
- **Have a Personalized User Profile**
  - **#10** by dhardi

### Epic: Registration and Login
- **Receive an Email Confirmation After Registering**
  - **#9** by dhardi
- **Easily Recover My Password If Lost**
  - **#8** by dhardi
- **Easily Login or Logout**
  - **#7** by dhardi
- **Easily Register for an Account**
  - **#6** by dhardi

### Epic: Product Browsing
- **Easily View the Total of My Purchases at Any Time**
  - **#5** by dhardi
- **Quickly Identify Deals, Clearance Items, and Special Offers**
  - **#4** by dhardi
- **View Individual Product Details**
  - **#3** by dhardi
- **View a Specific Category of Products**
  - **#2** by dhardi
- **View a List of Products**
  - **#1** by dhardi


### Conclusion

Compiling all the user stories was a challenging yet ultimately rewarding endeavor. This process demanded meticulous attention to detail as I aimed to accurately capture each user’s unique needs and experiences. Balancing the varying priorities of stakeholders proved particularly difficult, with different users often presenting conflicting requirements that complicated the search for common ground. Additionally, ensuring that each story was not only clear and concise but also aligned with the overall product vision required significant effort and focus. Effective time management became critical as I navigated multiple iterations, gathered feedback, and made necessary revisions. Ultimately, these challenges enriched my understanding of user needs and contributed to creating a more comprehensive and user-centered product roadmap.

### **Manual Testing of User Stories**


#### **EPIC 1 - Set up and Deployment:**

Most of this epic were tasks for the development phase; therefore, the testing is the working of the overall site. Below is the one story that tested all tasks as one.

|passed | **Access a live url** so that I can **use the site on any device**.
|:---:|:---|
|&check;| Can access the site via the deployed URL on the desktop.
|&check;| Can access the site via the deployed URL on mobile.
|&check;| Can access the site via the deployed URL on a tablet.
|&check;| All images and styles are tacked and as expected.

#### **EPIC 2 - Viewing and Navigation:**

|passed | .**Clearly identity the sites purpose upon visiting** so that I can **determine if the site is what I am looking for.**
|:---:|:---|
|&check;| The site has a clear purpose and is easy to navigate.

|passed | **View a list of products** so that I can **select some to purchase.**
|:---:|:---|
|&check;| The site has a list of products.
|&check;| The list of products is paginated.
|&check;| The product list is ordered by default by ID.
|&check;| The list of products can be ordered by name ascending and descending.
|&check;| The list of products can be ordered by price ascending and descending.
|&check;| The list of products can be ordered by rating ascending and descending.
|&check;| The list of products can be filtered to show only those with an active sale.
|&check;| Add to cart button works as expected on all products and product details pages.

|passed | **View individual product details** so that I can **identify the price, description, detailed reviews, and product image enabling me to compare how the product differs from other items.**
|:---:|:---|
|&check;| The site has a product details page.
|&check;| The product details page shows the product image.
|&check;| The product details page shows the product name.
|&check;| The product details page shows the product price.
|&check;| The product details page shows the sale price if the item has a sale.
|&check;| The product details page shows the product description.
|&check;| The product details page shows the product rating.
|&check;| The product details page shows the product reviews.
|&check;| The product details page shows the review form if there are no reviews already.
|&check;| The product details page shows the product quantity selector.
|&check;| The product details page shows the product add to cart button.

|passed | **View the total of my purchases at any time** so that I can **see and review how much I am spending at any time whilst building an order.**
|:---:|:---|
|&check;| The site has a cart page.
|&check;| The cart page/preview shows the product image.
|&check;| The cart page/preview shows the product name.
|&check;| The cart page/preview shows the product price.
|&check;| The cart page/preview shows the current quantity in the cart.
|&check;| Cart preview shows when the item is added from any page.
|&check;| The cart page shows the product quantity selector, and the user can update their order quantity.
|&check;| The cart page/preview shows the cart total.
|&check;| The cart page/preview shows the amount left to spend to get free delivery.
|&check;| The cart page shows the delivery cost and grand total.
|&check;| The cart page allows the user to completely remove an item from their cart and updates the cart total.
|&check;| When the quantity is updated in the user's cart, the cart total updates accurately.

|passed | **Leave a review** so that I can **share my opinion of a product and leave a star rating.**
|:---:|:---|
|&check;| The site has a review form.
|&check;| The review form has a title field.
|&check;| The review form has a rating field.
|&check;| The review form has a body field.
|&check;| When there are no reviews, a review form is shown on the product detail page.
|&check;| When a review is submitted, the review is added to the product detail page.
|&check;| User cannot enter a value greater than 5 for the rating field.
|&check;| User cannot enter a value less than 1 for the rating field.
|&check;| User cannot submit a review without a title.
|&check;| User cannot submit a review without a rating.
|&check;| Author of the review can edit their review.
|&check;| Author of the review can delete their review.
|&check;| Author of the review can not edit or delete another user's review.
|&check;| success message is displayed when a review is submitted.

|passed | **View reviews of a product** so that I can **see what other people think of a product.**
|:---:|:---|
|&check;| The site has a review section on the product detail page.
|&check;| The review section shows the review title.
|&check;| The review heading indicates the review rating.
|&check;| The review heading previews the review body.
|&check;| The review heading shows the review author.
|&check;| The review heading indicates the review date.
|&check;| The review edit/delete buttons only show to the author and super users.
|&check;| Accordion opens and closes when clicked.
|&check;| Accordion only allows for one review to be expanded simultaneously to save display space.
|&check;| If there are no reviews, then an inline form is shown in place of the accordion.
|&check;| If reviews, there is a button below for the user to add a review.

|passed | **Identify any promotions that are available** so that I can **take advantage of them and obtain the best value for money possible.**
|:---:|:---|
|&check;| The site has a promotions page.
|&check;| The promotions page shows only active sales items.

|passed | **See clearly when something goes wrong on the site** so that I can **correct any errors and continue with my purchase.**
|:---:|:---|
|&check;| The site has a 404 page active when the URL is unknown.
|&check;| Relevant feedback is displayed as a toast message when the user cannot act.

|passed | * ... **See a pleasantly styled and easy to navigate site** so that I can **enjoy the experience of using the site.**
|:---:|:---|
|&check;| The site has a pleasant colour scheme.
|&check; | The site has a pleasing font scheme.
|&check; | The site has a pleasing layout.
|&check; | The site has pleasant navigation.
|&check; | The site has a pleasant footer.
|&check; | The site has a nice header.
|&check; | The site has an enjoyable product card.
|&check; | The site has a pleasant product detail page.
|&check; | The site has a nice cart page.
|&check; | The site has a nice checkout page.
|&check; | The site has a pleasant promotions page.
|&check; | Everything is aligned and spaced correctly.





#### **EPIC 3 - Registration and User Accounts:**

|passed | **Register for an account** so that I can **save my personal details, view my order history online.**
|:---:|:---|
|&check;| The site has a registration page.
|&check;| Users can not register with an email address that is already in use.
|&check;| Users can successfully register for the site
|&check;| Users can not register with a username that is already in use.
|&check;| Users can not register with a password similar to their user name.
|&check;| Users can not register with a password similar to their email address.
|&check;| Users can not register with a too short password.
|&check;| Errors are displayed to the user if any of the above are attempted.
|&check;| Success message is displayed to the user if registration is successful.
|&check;| User sees message to verify their email.
|&check;| Users can not log in until they have verified their email.
|&check;| Verification email is sent to the user.
|&check;| Verification email contains a link to confirm the user's email.
|&check;| Once verified, users, can log in with their username or email.
|&check;| Users are redirected to the login in page once the email is verified.

|passed | **Easily login or logout at any time** so that I can **access my personal account information and protect it from unauthorized viewing on shared devices.**
|:---:|:---|
|&check;| Log in/out options are visible on all pages under the account dropdown.
|&check;| Once logged out, personal information is no longer visible.
|&check;| Once logged in, the account options change to reveal a profile link.
|&check;| Once logged in/out, the user is redirected to the home page.
|&check;| User receives a success message when they log in/out.

|passed | ...**Save my personal details to my profile from the checkout page** so that I **don’t have to enter them every time I make a purchase.**
|:---:|:---|
|&check;| The site has a profile page.
|&check;| The profile page has a form to update the user's details.
|&check;| Checkout form takes the information available in the profile for the checkout process
|&check;| Details from checkout save if save info box checked
|&check;| Details from checkout do not save if the save info box is not checked
|&check;| Shipping address on previous order unaffected by updating details.

|passed | **Amend my personal details from my profile** so that I can **update information should there be any changes.**
|:---:|:---|
|&check;| User can update their details on the profile page.
|&check;| Appropriate error messages are shown if the user enters invalid information.
|&check;| Success message is displayed if the user updates their details successfully.
|&check;| Shipping address on previous order unaffected by updating details.

|passed | **Recover my password in case I forget it** so that I can **regain access to my account in the event I lose my password.**
|:---:|:---|
|&check;| The site has a password reset page.
|&check;| The password reset page has a form to enter the user's email address.
|&check;| Email is sent with password reset token.
|&check;| Link in the email takes the user to the password reset page.
|&check;| Password reset page has a form to enter the new password.
|&check;| User gets a success message once the password has been reset
|&check;| Users can now log in with their new password.

|passed | **Receive an email confirmation upon registration** so that I can **confirm the registration process worked correctly.**
|:---:|:---|
|&check;| Email sent upon registration asking for the user to verify their email address.

#### **EPIC 4 - Sorting and Searching:**

|passed | **Sort the list of available products** so that I can **view them in different orders. and find the highest/lowest rating/prices and sort alphabetically to aid in finding the most suitable products to suit my needs.**
|:---:|:---|
|&check;| Products can be sorted by name in ascending order.
|&check;| Products can be sorted by name in descending order.
|&check;| Products can be sorted by price in ascending order.
|&check;| Products can be sorted by price in descending order.
|&check;| Products can be sorted by rating in ascending order.
|&check;| Products can be sorted by rating in descending order.

|passed | **Search for a product by name or content in the product description** so that I can **find a specific product I am looking for.**
|:---:|:---|
|&check;| Search bar is visible on all pages.
|&check;| Search returns results based on the search term.
|&check;| Search query matches product name and description.
|&check;| search terms are displayed above the search results.
|&check;| Number of products returned is displayed above the search results.

|passed | **View a list of products in a specific category** so that I can **view all products in that category.**
|:---:|:---|
|&check;| Products can be filtered by category via the navbar links.
|&check;| Products can be filtered by sub-category via the navbar links.

#### **EPIC 5 - Purchasing and Checkout:**

|passed | **Select a quantity of a product** so that I can **buy the required amount of the product.**
|:---:|:---|
|&check;| Quantity can be selected on the product page.
|&check;| Quantity can be selected on the product detail page.
|&check;| User cannot set the quantity selector to more than the in-stock level
|&check;| User cannot set the quantity selector to less than 1
|&check;| User can set the quantity selector to the in-stock level
|&check;| User can set the quantity selector to 1
|&check;| User can use the plus and minus buttons to select the quantity.
|&check;| User cannot add a quantity of 0 to the cart.
|&check;| User cannot add more than the stock level to their cart.
|&check;| server-side checks prevent the user from adding more than the stock level to their cart even if they change the input max value in the dev tools.
|&check;| User receives a message if an item is added to the cart.
|&check;| User receives a notification if the new quantity selected takes the cart's total number of items over the stock level.
|&check;| Quantity selector is disabled if the product is out of stock.

|passed | **View items in my bag to be purchased** so that I can **identify the total cost of my purchases before checkout.**
|:---:|:---|
|&check;| The site has a shopping cart page.
|&check;| The shopping cart page has a list of all the items in the user's cart.
|&check;| The shopping cart page has a total price for all the user cart items.
|&check;| The shopping cart page has a button to proceed to checkout.
|&check;| The shopping cart page has a button to remove items from the cart.

|passed | **Adjust the quantity of individual items in my bag** so that I can **easily make changes to my bag.**
|:---:|:---|
|&check;| The quantity of each item in the cart can be changed and updated from the cart page.
|&check;| Total recalculates each time the quantity is adjusted.
|&check;| User is shown a success/error message when the state changes in the cart.
|&check;| User cannot set the quantity selector to more than the in-stock level
|&check;| User cannot set the quantity selector to less than 1
|&check;| User can set the quantity selector to 1.
|&check;| User can use the plus and minus buttons to select the quantity.
|&check;| User cannot add a quantity of 0 to the cart.

|passed | **Easily enter my payment information** so that I can **checkout quickly with no hassles by using information previously stored in the system.**
|:---:|:---|
|&check;| The site has a checkout page.
|&check;| The checkout page has a form to enter the user's payment details.
|&check;| The checkout page has a form to enter the user's shipping details.
|&check;| Payments are handled by Stripe.
|&check;| The checkout page has a button to complete the order.
|&check;| The checkout page has a button to cancel the order and return the user to the shopping cart.
|&check;| The checkout page has a button to save the user's details for future use.
|&check;| If checked, the details from the checkout form are saved to the user's profile.
|&check;| If it exists, the users saved details are pre-filled in the checkout form.

|passed | **View an order confirmation after checkout** so that I can **verify that I haven’t made any mistakes.**
|:---:|:---|
|&check;| The site has a checkout success page.
|&check;| The checkout success page has a message to confirm the order was successful.
|&check;| The checkout success page has a button to return to the home page.|
|&check;| The checkout success page has a button to take the user to the special offers page.
|&check;| Email is sent to the user confirming the order.
|&check;| order is available to the customer who made the order in their order history page.
|&check;| checkout success page for an order made by a registered user can only be seen by that user from the profile.
|&check;| once an order is confirmed on screen, the order confirmation can only be revisited from a registered user's profile/non-registered users cannot revisit the checkout success page.

|passed | **Receive an email confirmation after checking out** so that I can **keep a record of my purchases.**
|:---:|:---|
|&check;| Email is sent to the user confirming the order.
|&check;| Email contains the order number.
|&check;| Email has the order total.
|&check;| Email includes the order date.
|&check;| Email contains the delivery address.
|&check;| Email includes the delivery cost.
|&check;| Email has a contact email address for assistance.


|passed | **Access the checkout page** so that I can **review my order whilst entering my payment/shipping details**
|:---:|:---|
|&check;| The site has a checkout page.
|&check;| The checkout page has a form to enter the user's payment details.
|&check;| The checkout page has a form to enter the user shipping details.
|&check;| The checkout page has a button to complete the order.
|&check;| The checkout page has a button to cancel the order and return it to the shopping cart.
|&check;| The checkout page has a button to save the user's details for future use.
|&check;| If checked, the details from the checkout form are saved to the user's profile.
|&check;| If it exists, the users saved details are pre-filled in the checkout form.
|&check;| Saved points the checkbox is unchecked by default.
|&check;| Guest users are invited to register/sign in and warned that they could not view their order history online without registering.

|passed | **securely submit my payment details** so that I can **rest assured my financial information is safe**
|:---:|:---|
|&check;| Stripe payment system is used.
|&check;| Stripe payment system is PCI compliant.

#### **EPIC 6 - Admin and Store Management:**

|passed | **Add a product** so that I can **add new products to the store.**
|:---:|:---|
|&check;| Product can be added via the admin panel and is visible in the store front end.
|&check;| Newly added items had full functionality of pre-existing items.

|passed | **Edit a product** so that I can **update the details of a product.**
|:---:|:---|
|&check;| Product can be edited via the admin panel and is visible in the store front end.
|&check;| Quick edits can only be made from the front end by super users.

|passed | **Delete a product** so that I can **remove products that are no longer for sale.**
|:---:|:---|
|&check;| Product can be deleted via the admin panel and is no longer visible in the store front end.
|&check;| Quick delete can only be made from the front end by super users.
|&check;| product cannot be deleted by non-superuser using the URL.

|passed | **Add a promotion** so that I can **add new promotions to the store.**
|:---:|:---|
|&check;| Promotion can be added via the admin panel and is visible in the store front end.



#### **EPIC 7 - Product Reviews:**



|passed | **View reviews of a product** so that I can **see what other people think of a product.**
|:---:|:---|
|&check;| Once successfully submitted, the review is visible on the product details page.
|&check;| Author's name is in the accordion item heading.
|&check;| Review title is in the accordion item heading.
|&check;| Review text is previewed in the body of the accordion item.

|passed | **Edit my reviews of a product** so that I can **update my public opinion should it ever change*
|:---:|:---|  
|&check;| Review cannot be edited by a user who did not create the review (unless superuser) even by using the URL.  
|&check;| Edit review for is pre-populated with the review details.  
|&check;| A superuser can edit all reviews.  
|&check;| All reviews can be edited by the user who created the review.  
|&check;| Overall rating is re-calculated when a review is edited.  

|passed | **delete my reviews of a product** so that I can **remove previous reviews should I see fit**
|:---:|:---|
|&check;| Review cannot be deleted by a user who did not create the review (unless superuser) even by using the URL.
|&check;| A superuser can delete all reviews.
|&check;| All reviews can be deleted by the user who created the review.


#### **EPIC 8 - Marketing:**

|passed | **Send promotional emails** so that I can **promote new products and offers to my customers.**
|:---:|:---|
|&check;| Mail chimp form visible from all pages.
|&check;| Mail chimp form has a field to enter the email address.
|&check;| Mail chimp form has a button to submit the email address.
|&check;| Collected email addresses are stored in the mail chimp database.

|passed | **Set up a social media page** so that I can **promote my business and products to the global market.**
|:---:|:---|
|&check;| Facebook page is set up.
|&check;| Facebook page is linked in the footer.
|&check;| Facebook page links have correct rel attributes.
|&check;| Facebook page has a shop now button linked to the sight.

|passed | .**Increase my search engine ranking** so that I can **increase the number of visitors to my site.**
|:---:|:---|
|&check;| Each page has meta keywords.
|&check;| Site map done
|&check;| Robots.txt done