# Project Title
products ordering system 

## Features

1.User Authentication

    Signup and login functionality for users.
    Password change via Gmail integration.

2.Email Functionality
    Contact URL to send emails for user inquiries or feedback.

3.User Profile
    Users can create a profile with multiple addresses (locations).

4.Product Ordering:
    Users can view products, add them to the cart, and manage product quantities.
    Users can increase, decrease, or remove products from their cart.

5.Shopping Cart:
    All selected products are displayed in the shopping cart with their quantities.


6.Search Functionality:
     Users can search for products directly from the menu.

7.Payment Status:
     Payment status is tracked (e.g., "On the way," "Delivered," "Cancelled"). (Note: Payment processing is not implemented on the server side).


8.Map Integration:
     Maps are integrated into the platform for address management.

9.Feedback & Contact:
     Customer feedback or inquiries from the contact page are sent to the admin's email.

## Installation

1. clone the repository
   git clone <repository-url>

2. Install Dependencies
    pip install -r requirements.txt

3. Apply migrations
   python manage.py migrate

4. Run the server
   python manage.py runserver



## Technologies Used

Django
Python
HTML/CSS/JavaScript
Google Maps 
SMTP (for email functionality)


## Future Enhancement

Implement server-side payment functionality.
Optimize cart management with additional features.
Enhance the search functionality for better results