# Phase-4-Project

# BARREL-AND-BOTTLE - Backend API

This repository contains the backend API code for a drink management system. The API is built using Flask, a popular Python web framework, and provides endpoints for managing drinks, customers, admins, sales, reviews, and user authentication. It uses a SQLite database to store and retrieve data.

## Features
The backend API offers the following features:

**Drink Management**: Allows users to perform CRUD operations (Create, Read, Update, Delete) on drinks. Users can retrieve a list of all drinks, get details of a specific drink, create a new drink, update an existing drink, and delete a drink.

**Customer Management**: Provides endpoints for managing customers. Users can retrieve a list of all customers, get details of a specific customer, create a new customer, update an existing customer, and delete a customer.

**Admin Management**: Allows administrators to manage admins. Admins can retrieve a list of all admins, create a new admin, update an existing admin, and delete an admin.

**Sales Management**: Enables users to create sales records by specifying the customer and drink IDs.

**Review Management**: Provides endpoints for retrieving all reviews.

**User Authentication**: Supports user registration and login functionality. Users can register a new account by providing a username, password, and email address. They can then log in using their credentials. Session management is implemented to maintain active user sessions.

## API Documentation
The backend API provides the following endpoints:

### Drinks
- **GET /drinks**: Retrieve a list of all drinks.
- **GET /drinks/{drink_id}**: Retrieve details of a specific drink.
- **POST /drinks**: Create a new drink.
- **PATCH /drinks/{id}**: Update an existing drink.
- **DELETE /drinks/{id}**: Delete an existing drink.

### Customers
- **GET /customers**: Retrieve a list of all customers.
- **GET /customers/{customer_id}**: Retrieve details of a specific customer.
- **POST /customers**: Create a new customer.
- **PATCH /customers/{id}**: Update an existing customer.
- **DELETE /customers/{id}**: Delete an existing customer.

### Admins
- **GET /admins**: Retrieve a list of all admins.
- **POST /admins**: Create a new admin.
- **PATCH /admins/{id}**: Update an existing admin.
- **DELETE /admins/{id}**: Delete an existing admin.

### Sales
- **GET /sales**: Retrieve a list of all sales.
- **POST /sales**: Create a new sale.

### Reviews
- **GET /reviews**: Retrieve a list of all reviews.

### Authentication
- **POST /register**: Register a new customer.
- **POST /login**: Log in a customer.
- **GET /check_session**: Check if a customer session is active.
- **GET /logout**: Log out a customer.

For detailed information about each endpoint, including request and response examples, please refer to the API documentation.

## Conclusion
The backend API provides a robust foundation for managing drinks, customers, admins, sales, reviews, and user authentication in a drink management system for the **BARREL-AND-BOTTLE**.

