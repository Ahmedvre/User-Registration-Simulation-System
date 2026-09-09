# User Registration Simulation System

A simple Python program that simulates a user registration system using in-memory data structures. It validates user input (name, email, password), registers valid users, and tracks failed registration attempts with clear error messages.

## Overview

This project simulates a basic user registration workflow without a real database. It uses two Python lists to act as in-memory storage:

- `registered_users` — stores successfully registered users
- `failed_registrations` — stores details of failed registration attempts, including the reason for failure

The system validates each user's name, email, and password against a set of rules before allowing registration, and prevents duplicate email registrations.

## Features

- **Name validation** — must be at least 3 characters long
- **Email validation** — must contain both `@` and `.`
- **Password validation** — must be at least 8 characters, contain at least one uppercase letter, and at least one digit
- **Duplicate email detection** — prevents registering the same email twice
- **Centralized error handling** — validation failures raise descriptive `ValueError` messages, which are caught and logged instead of crashing the program
- **Built-in test cases** — demonstrates both successful and failed registration scenarios

## How It Works

1. `validate_name()`, `validate_email()`, and `validate_password()` each check one piece of user input and return `True` or `False`.
2. `validate_user_data()` orchestrates the three checks above. If any check fails, it raises a `ValueError` with a message describing exactly what went wrong.
3. `create_user_account()` ties everything together:
   - Calls `validate_user_data()` to validate the input
   - Checks `registered_users` for a duplicate email
   - On success, builds a user dictionary (`name`, `email`, `password`, `status: "active"`) and appends it to `registered_users`
   - On failure, catches the `ValueError` and logs the email and error message to `failed_registrations`

## Project Structure

```
├── registration_system.py   # Main script: validation functions, registration logic, and tests
└── README.md
```

## Requirements

- Python 3.x
- No external dependencies (standard library only)

## Usage

Run the script directly to see the registration system in action:

```bash
python user-registration-simulation-system.py
```

## Validation Rules Summary

| Field    | Rule(s)                                                             |
|----------|-----------------------------------------------------------------------|
| Name     | At least 3 characters                                                 |
| Email    | Must contain `@` and `.`                                              |
| Password | At least 8 characters, 1 uppercase letter, 1 digit                    |

## Author

Ahmed Reda
