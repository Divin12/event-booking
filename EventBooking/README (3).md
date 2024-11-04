# Apartment Booking Website

Welcome to the Apartment Booking Website, a Django-based project for managing apartment bookings. This README provides an overview of the project, instructions for setting it up, and details on how to launch the development server.

## Table of Contents
- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Launching the Development Server](#launching-the-development-server)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Apartment Booking Website is a web application designed to help users search for, book, and manage apartments. It includes features such as user registration, property listing, booking management, and user reviews.

## Getting Started

Follow these steps to set up the Apartment Booking Website on your local development environment.

### Prerequisites

Before you begin, ensure that you have the following prerequisites installed:

- Python (3.x)
- Django (3.x)
- We use the database db.sqlite3 (models)


### Installation

1. Download the project source code to your local machine.

2. Navigate to the project directory.
   
   
3. Create a virtual environment to isolate project dependencies (optional but recommended):

   ```bash
   python -m venv venv
   
   
   
venv\Scripts\activate

source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

    - Launching the Development Server
           python manage.py runserver
           
           
  
Don't create another super user, use this one to access the website: 
- Divin                        
- Password(123456)

Another account: 
- Victor
- Password(1234)

Anothe account: 
- Yannick
- Password(12345)





Contributing

If you'd like to contribute to the development of this project, please follow the best practices for contributing and feel free to submit pull requests. For bug reports or feature requests, please open an issue in the repository.


License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code as per the terms of the license.


The admin cannot book the apartment, only the customer
