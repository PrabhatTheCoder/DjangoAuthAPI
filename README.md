# Django Rest Framework Authentication System

This project implements a complete authentication system using Django Rest Framework (DRF). It includes features such as registration, login, profile management, password change, sending reset password emails, and resetting passwords using tokens.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Authentication](#authentication)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration with email verification
- User login with JWT (JSON Web Tokens) authentication
- User profile management (update profile, change password)
- Sending email for password reset
- Resetting password using token authentication

## Setup

### Prerequisites

- Python (3.x recommended)
- Django
- Django Rest Framework
- Django Rest Framework SimpleJWT (for JWT authentication)
- Additional packages as required (e.g., django-cors-headers for handling CORS)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
2. Install dependencies:
   pip install -r requirements.txt
3. Run the development server:
   python manage.py runserver

## Usage

1. User Registration: Register a new user using the '/api/registration/' endpoint.
2. Email Verification: Verify the email address by clicking the link sent to the registered email.
3. User Login: Log in using the '/api/login/' endpoint to obtain an access token (JWT).
4. User Profile Management:
   - Access user profile endpoints ('/api/profile/') to manage user profile and change password.
5. Password Reset:
   - Request a password reset using '/api/send-reset-password-email/'.
   - Click the link sent to the registered email to reset the password using '/api/reset-password/<uid>/<token>/'.

## Endpoints

- Registration: '/api/registration/'
- Email Verification: '/api/auth/verify-email/<str:token>/'
- Login: '/api/login/'
- Password Change: '/api/password-change/'
- Request Password Reset: '/api/send-reset-password-email/'
- Reset Password: '/api/reset-password/<uid>/<token>/'
- User Profile: '/api/profile/'


## Authentication
- Authentication is handled using JWT (JSON Web Tokens).
- Include the access token in the Authorization header of authenticated requests:
  Authorization: Bearer <your_access_token>
