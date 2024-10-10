# Gameshark E-Commerce Platform

![Gameshark Logo](https://github.com/dhardi/gameshark/blob/main/static/images/responnsive.png)


- [Live site](https://gameshark-4e405cfc132a.herokuapp.com/)

## Design and Planning

The Gameshark **B2C** e-commerce platform was designed with a focus on user experience, modern aesthetics, and seamless functionality. The planning phase included identifying key features, establishing user roles (e.g., customers, admins), and determining the overall architecture of the application. Wireframes and mockups were created to visualize the user interface and user flow, ensuring that the design aligns with the project goals.

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


# Entity-Relationship Diagram (ERD) for E-Commerce Website

![E-Commerce pt1](https://github.com/dhardi/gameshark/blob/main/static/images/diagrampt1.png)

![E-Commerce pt2](https://github.com/dhardi/gameshark/blob/main/static/images/diagramp2.png)

## Overview
This **Entity-Relationship Diagram (ERD)** represents the structure of the e-commerce system, showcasing the relationships between the major entities in the database. The entities and their relationships are essential to manage the interactions and data flow within the system. Below is a detailed explanation of each entity and their relationships.

### Entities

1. **User**
   - **Attributes**: `user_id`, `name`, `email`, `password`, `address`, `phone_number`, `is_admin`
   - **Description**: This entity stores information about registered users. A user can either be a customer or an admin.
   - **Relationships**:
     - A **User** can have multiple **Orders**.
     - A **User** can add **Products** to their **Wishlist**.
     - A **User** can create and manage multiple **Carts**.
     - A **User** can write multiple **Reviews**.

2. **Product**
   - **Attributes**: `product_id`, `name`, `description`, `price`, `category`, `stock_quantity`
   - **Description**: Represents products available in the store.
   - **Relationships**:
     - A **Product** can appear in multiple **Orders**.
     - A **Product** can be part of multiple **Wishlists**.
     - A **Product** can be added to multiple **Carts**.
     - A **Product** can have multiple **Reviews** written by different users.

3. **Order**
   - **Attributes**: `order_id`, `order_date`, `total_amount`, `payment_status`, `shipping_status`
   - **Description**: Stores information about customer orders.
   - **Relationships**:
     - An **Order** belongs to a single **User**.
     - An **Order** contains multiple **Products** (through an intermediary **Order_Product** relationship table).

4. **Cart**
   - **Attributes**: `cart_id`, `user_id`, `creation_date`
   - **Description**: Tracks items that users are considering purchasing.
   - **Relationships**:
     - A **Cart** belongs to a **User**.
     - A **Cart** contains multiple **Products** (through a **Cart_Product** table).

5. **Wishlist**
   - **Attributes**: `wishlist_id`, `user_id`, `creation_date`
   - **Description**: Allows users to save products they are interested in for future purchases.
   - **Relationships**:
     - A **Wishlist** belongs to a **User**.
     - A **Wishlist** contains multiple **Products**.

6. **Review**
   - **Attributes**: `review_id`, `user_id`, `product_id`, `rating`, `comment`, `review_date`
   - **Description**: Tracks user reviews and ratings for products.
   - **Relationships**:
     - A **Review** belongs to a **User**.
     - A **Review** is associated with a single **Product**.

7. **Payment**
   - **Attributes**: `payment_id`, `order_id`, `payment_method`, `payment_status`, `payment_date`
   - **Description**: Manages payment details for completed orders.
   - **Relationships**:
     - A **Payment** is linked to a single **Order**.

### Relationship Summary

- **User** ↔ **Order**: One user can place multiple orders, but each order belongs to one user.
- **User** ↔ **Cart**: A user can create one or more carts, each holding selected products.
- **User** ↔ **Wishlist**: A user can maintain multiple wishlists.
- **User** ↔ **Review**: Users can write reviews for products they've purchased.
- **Order** ↔ **Product**: Orders can include many products, and each product can appear in multiple orders (via the **Order_Product** table).
- **Cart** ↔ **Product**: Carts contain multiple products, with the **Cart_Product** table facilitating this relationship.
- **Wishlist** ↔ **Product**: Products can appear in multiple wishlists.
- **Payment** ↔ **Order**: Payments are associated with specific orders.
- **Review** ↔ **Product**: Each review is linked to a specific product.

# Wireframes

## Home
![Home](https://github.com/dhardi/gameshark/blob/main/static/images/home_wireframes.png)
*Description:* The homepage layout showcasing featured products, categories, and promotional banners.

---

## Products
![Products](https://github.com/dhardi/gameshark/blob/main/static/images/products_wireframes.png)
*Description:* The products page layout that displays a grid of available products, filters, and sorting options.

---

## Product Detail
![Product Detail](https://github.com/dhardi/gameshark/blob/main/static/images/product_detail_wireframe.png)
*Description:* Detailed view of a selected product, including images, descriptions, reviews, and the add-to-cart button.

---

## My Profile
![My Profile](https://github.com/dhardi/gameshark/blob/main/static/images/my_profile.png)
*Description:* User profile page that allows users to view and edit their personal information, including order history and saved items.

---

## Wishlist
![Wishlist](https://github.com/dhardi/gameshark/blob/main/static/images/wishlist_wireframes.png)
*Description:* A dedicated page for users to view and manage their saved items for future purchases.

---

## Bag
![Bag](https://github.com/dhardi/gameshark/blob/main/static/images/bag_wireframes.png)
*Description:* Shopping cart layout showing selected items, their prices, and a checkout button.

---

## Review
![Review](https://github.com/dhardi/gameshark/blob/main/static/images/review_wireframes.png)
*Description:* Page for users to submit and read product reviews, including star ratings and written feedback.

---

## Testimonial
![Testimonial](https://github.com/dhardi/gameshark/blob/main/static/images/testimonial_wireframes.png)
*Description:* Section for displaying user testimonials and feedback about the e-commerce platform one testimonial per order.


# Features Overview

## Home Page
- **Desktop View:**
  ![Home Desktop](https://github.com/dhardi/gameshark/blob/main/static/images/menu_hero.png)

- **Mobile View:**
  ![Home Mobile](https://github.com/dhardi/gameshark/blob/main/static/images/home_mobile.png)

---

## Product Listings
- **Desktop View:**
  ![Products Desktop](https://github.com/dhardi/gameshark/blob/main/static/images/produtcs_list.png)

- **Mobile View:**
  ![Products Mobile](https://github.com/dhardi/gameshark/blob/main/static/images/products_mobile.png)

---

## Product Detail Page
- **Desktop View:**
  ![Product Detail Desktop](https://github.com/dhardi/gameshark/blob/main/static/images/produtc_detail_rename.png)

- **Mobile View:**
  ![Product Detail Mobile](https://github.com/dhardi/gameshark/blob/main/static/images/product_detail_mobile.png)

---

## User Profile
- **Desktop View:**
  ![My Profile Desktop](https://github.com/dhardi/gameshark/blob/main/static/images/profile.png)

- **Mobile View:**
  ![My Profile Mobile](https://github.com/dhardi/gameshark/blob/main/static/images/profile_mobile.png)

---

## Wishlist
- **Desktop View:**
  ![Wishlist Desktop](https://github.com/dhardi/gameshark/blob/main/static/images/wishlist.png)

- **Mobile View:**
  ![Wishlist Mobile](https://github.com/dhardi/gameshark/blob/main/static/images/wishlist_mobile.png)

---

## Shopping Bag
- **Desktop View:**
  ![Bag Desktop](https://github.com/dhardi/gameshark/blob/main/static/images/bag.png)

- **Mobile View:**
  ![Bag Mobile](https://github.com/dhardi/gameshark/blob/main/static/images/bag_mobile.png)

---

## Reviews
- **Desktop View:**
  ![Review Desktop](https://github.com/dhardi/gameshark/blob/main/static/images/review_desktop.png)

- **Mobile View:**
  ![Review Mobile](https://github.com/dhardi/gameshark/blob/main/static/images/review_add_mobile.png)

---

## Testimonials
- **Desktop View:**
  ![Testimonial Desktop](https://github.com/dhardi/gameshark/blob/main/static/images/testimonial_add.png)

- **Mobile View:**
  ![Testimonial Mobile](https://github.com/dhardi/gameshark/blob/main/static/images/testimonial_add_mobile2.png)

  ## Footer
- **Desktop View:**
  ![Testimonial Desktop](https://github.com/dhardi/gameshark/blob/main/static/images/footer_desktop.png)

- **Mobile View:**
  ![Testimonial Mobile](https://github.com/dhardi/gameshark/blob/main/static/images/footer_mobile.png)




# Color Scheme 

## Primary Colors

| Color Name       | Color Code | Example                         |
|------------------|------------|---------------------------------|
| Primary Blue     | `#007BFF`  | ![#007BFF](https://via.placeholder.com/20/007BFF/000000?text=+) |
| Secondary Green   | `#28A745`  | ![#28A745](https://via.placeholder.com/20/28A745/000000?text=+) |
| Accent Orange     | `#FFC107`  | ![#FFC107](https://via.placeholder.com/20/FFC107/000000?text=+) |

## Neutral Colors

| Color Name       | Color Code | Example                         |
|------------------|------------|---------------------------------|
| Light Gray       | `#F8F9FA`  | ![#F8F9FA](https://via.placeholder.com/20/F8F9FA/000000?text=+) |
| Medium Gray      | `#6C757D`  | ![#6C757D](https://via.placeholder.com/20/6C757D/000000?text=+) |
| Dark Gray        | `#343A40`  | ![#343A40](https://via.placeholder.com/20/343A40/000000?text=+) |
| White            | `#FFFFFF`  | ![#FFFFFF](https://via.placeholder.com/20/FFFFFF/000000?text=+) |
| Black            | `#000000`  | ![#000000](https://via.placeholder.com/20/000000/FFFFFF?text=+) |

## Status Colors

| Color Name       | Color Code | Example                         |
|------------------|------------|---------------------------------|
| Success Green    | `#28A745`  | ![#28A745](https://via.placeholder.com/20/28A745/000000?text=+) |
| Warning Yellow    | `#FFC107`  | ![#FFC107](https://via.placeholder.com/20/FFC107/000000?text=+) |
| Danger Red       | `#DC3545`  | ![#DC3545](https://via.placeholder.com/20/DC3545/000000?text=+) |

---

## Usage
- **Primary Colors** are used for buttons, links, and key elements that require emphasis.
- **Neutral Colors** provide background colors, borders, and subtle elements.
- **Status Colors** indicate notifications, alerts, and messages to users.




# Deployment

This document provides a step-by-step guide for deploying your project. All deployment steps are available at the following link:

- [Complete Deployment Guide](https://github.com/dhardi/gameshark/blob/main/Deployment.md)

# Marketing

This document provides Marketing ideas and planning 

- [Marketing](https://github.com/dhardi/gameshark/blob/main/markting.md)

# Testing

all the testing you can find here

- [Testing](https://github.com/dhardi/gameshark/blob/main/TESTING.md)



## **Technologies used**


* Django
  * Django was used as the python framework in the project.
  * Django all auth was used to handle user authentication and related tasks i.e. sign in, sign up, sign out.
* Heroku
  * Used to deploy the page and make it publicly available.
* Heroku PostgreSQL & ElephantSQL
  * Used for the database during deployment.
* SQLlite3
	* Was used during development as a database to test models.
* HTML
  * HTML was the base language used to lay out the skeleton of all templates.
* CSS
  * Custom CSS is used to style the page .
* Javascript
  * I have used Javascript to manipulate the DOM and communicate with the backend to create, read, update, and delete data from the database.
* Bootstrap 
  * Used to style HTML, CSS,  javascript. 
* Font awesome
  * All icons throughout the page.
* AWS S3
  * Used to store static and media files.
* Stripe
  * Used to handle payments.



## **Honorable Mentions**

* [David Bowers](https://dev-bowers.com/) - I would like to take a moment to honor David Bowers, an exceptional mentor and dear friend. David's unwavering support and guidance have profoundly impacted my personal and professional growth. His wisdom, kindness, and ability to inspire those around him have been a beacon of light during challenging times. I am truly grateful for his friendship and mentorship, which have encouraged me to strive for excellence and become the best version of myself.

* I want to take a moment to express my heartfelt gratitude to my family, especially to my wife Loredana. There were many long hours when I was deeply focused on my projects, and during that time, their unwavering support and understanding made all the difference. Loredana's patience and encouragement were invaluable, providing me with the strength to persevere through challenging moments. I am truly thankful for the love and support from my family and Loredana, which has inspired me to pursue my dreams relentlessly.

## **Credits**

* [Code Institute](https://codeinstitute.net/) 
* Balsamiq was used to create the wireframes.
* The site was developed using Gitpod.
* GitHub was used to store my repository.
* [W3cschool](https://www.w3schools.com) used to remeber the syntax of various languages.
* [Stackoverflow](https://stackoverflow.com/) for debugging and finding solutions to problems.
* Fonts were taken from [Google Fonts](https://fonts.google.com/)
* [favicon generator](https://www.favicon-generator.org/) was used to generate the favicon.
* [Diagram](https://www.eraser.io/diagramgpt) was used to create the database diagram.

### **Media**  
  * [Hero](https://www.pinterest.com/) 
* Products images and descriptions were taken from the following sites
  * [Amazon](https://www.amazon.co.uk/)