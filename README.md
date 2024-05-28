# Django Bookstore Application

Welcome to the Django Bookstore Application! This application allows users to log in, browse a library of books, and view details about each book.

## Features

- **User Authentication:** Users can sign up, log in, and log out.
- **Book Library:** Browse a list of available books.
- **Book Details:** View detailed information about each book.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/jimmy8000/bookstore.git
    cd bookstore
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

### Authentication

- **Sign Up:** Create a new account to access the bookstore.
- **Log In:** Log in with your credentials.
- **Log Out:** Log out from the application.

### Book Library

- **Browse Books:** View a list of all available books.
- **Book Details:** Click on a book to see more details, including title, author, description, and publication date.

## Project Structure

```plaintext
django-bookstore/
│
├── bookstore/                # Main Django application directory
│   ├── settings.py           # Django settings
│   ├── urls.py               # URL routing
│   ├── wsgi.py               # WSGI configuration
│   └── ...
│
├── books/                    # Books application directory
│   ├── migrations/           # Database migrations
│   ├── templates/            # HTML templates
│   ├── views.py              # View functions
│   ├── models.py             # Database models
│   ├── urls.py               # URL routing for books
│   └── ...
│
├── users/                    # Users application directory
│   ├── migrations/           # Database migrations
│   ├── templates/            # HTML templates
│   ├── views.py              # View functions
│   ├── models.py             # Database models
│   ├── urls.py               # URL routing for users
│   └── ...
│
├── manage.py                 # Django management script
└── requirements.txt          # Project dependencies

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.