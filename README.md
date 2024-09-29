# Gameshark E-Commerce Platform

![Gameshark Logo](link-to-your-image.png)

## Design and Planning

The Gameshark e-commerce platform was designed with a focus on user experience, modern aesthetics, and seamless functionality. The planning phase included identifying key features, establishing user roles (e.g., customers, admins), and determining the overall architecture of the application. Wireframes and mockups were created to visualize the user interface and user flow, ensuring that the design aligns with the project goals.

## Introduction

Gameshark is an online platform that allows users to browse, review, and purchase gaming products. With a user-friendly interface and secure payment options, Gameshark aims to provide an exceptional shopping experience for gaming enthusiasts.

## Project Overview

The Gameshark project consists of multiple applications built on the Django framework. Key functionalities include:

- **Product Management**: Users can browse a variety of gaming products, each with detailed descriptions, images, and pricing.
- **Wishlist Feature**: Registered users can save their favorite products to a wishlist for future reference.
- **Reviews and Testimonials**: Users can leave reviews for products and share their testimonials, enhancing community engagement and trust.
- **User Authentication**: The platform includes secure user authentication, allowing users to sign up, log in, and manage their profiles.

## Goals of Gameshark Project

The primary goals of the Gameshark project are as follows:

1. **Provide a Seamless Shopping Experience**: Ensure that users can easily navigate the platform, find products, and make purchases without hassle.
2. **Foster Community Engagement**: Allow users to share their experiences through reviews and testimonials, helping others make informed decisions.
3. **Implement Robust Security**: Use secure authentication methods and data protection measures to safeguard user information.
4. **Enhance Product Visibility**: Utilize effective product categorization and search functionality to improve the discoverability of products.

## Conclusion

Gameshark is dedicated to creating a vibrant online shopping environment for gaming enthusiasts. By continually improving features and incorporating user feedback, we aim to enhance the overall experience for all users.

For more information, please visit our [GitHub Repository](link-to-your-github-repo).


## User Stories
### Epics and Must-Have Features
- **Easily Register for an account**
- **Easily login or logout**
- **Quickly identify deals, clearance items, and special offers**
- **View individual product details**
- **View a specific category of products**
- **Add a product to the shopping cart**
- **Delete a product from the shopping cart**
- **Adjust the quantity of items in the cart**
- **View items in the cart before purchase**
- **Edit/update product information**
- **Search for a product by name or description**
- **Sort multiple categories or products simultaneously**
- **Receive an email confirmation after checkout**
- **Have a personalized user profile**
- **Feel my personal and payment information is secure**

### Completed User Stories
1. **Easily login or logout**
2. **Easily Register for an account**
3. **View individual product details**
4. **Add a product to the shopping cart**
5. **Delete a product from the shopping cart**
6. **Adjust the quantity of items in my bag**
7. **Easily select the quantity of a product**
8. **View items in my bag to be purchased**
9. **Edit/update a product**
10. **Sort a specific category of products**
11. **View a list of available products**

## Bugs and Fixes
### Identified Bugs
- **Issue:** Users unable to add testimonials without being logged in.
  - **Fix:** Implemented a login requirement for submitting testimonials.
  
- **Issue:** SMTP authentication error when registering new users.
  - **Fix:** Configured SMTP settings correctly in settings.py.

## Challenges Faced
- **User Authentication:** Setting up user authentication was initially complex, particularly in ensuring users could only access their own reviews and wishlists.
- **Email Functionality:** Configuring email functionalities for user confirmations required attention to detail to prevent authentication errors.
- **Database Relationships:** Establishing correct foreign key relationships between products and reviews presented some challenges in maintaining data integrity.

## Future Features
- Implement a recommendation system based on user behavior.
- Add a search functionality for products.
- Create user roles with different permission levels (admin, seller, buyer).
- Introduce payment gateway integration for direct purchases.

## Conclusion
The Gameshark project aims to deliver a complete e-commerce experience. Through continuous improvements and user feedback, we intend to enhance the platform's functionality and usability further.
