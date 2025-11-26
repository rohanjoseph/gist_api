# Gist API Django Project

This project is a Django-based web application that interacts with the GitHub Gist API and displays public gists. It is structured as a typical Django project with two main apps: `gistapp` (the main project configuration) and `dataWare` (the app containing core logic and views).

## Features

- Fetches and displays public gists from the GitHub API.
- Renders data using Django templates.
- Organized with Django best practices for apps, templates, and static files.

## Project Structure

```
gist_api/
├── .gitignore
├── db.sqlite3
├── manage.py
├── gistapp/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
├── dataWare/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── __pycache__/
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── __pycache__/
│   └── templates/
│       └── index.html
└── env/
    └── ... (virtual environment)
```

## Key Files

- [`gistapp/settings.py`](gistapp/settings.py): Django project settings.
- [`dataWare/views.py`](dataWare/views.py): Contains views for fetching GitHub gists and rendering templates.
- [`dataWare/templates/index.html`](dataWare/templates/index.html): Main HTML template.
- [`dataWare/urls.py`](dataWare/urls.py): URL configuration for the `dataWare` app.
- [`gistapp/urls.py`](gistapp/urls.py): Root URL configuration.

## Setup & Usage

1. **Clone the repository** and navigate to the project directory.
2. **Create and activate a virtual environment** (if not already present):
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```
3. **Install dependencies**:
    ```sh
    pip install django requests
    ```
4. **Run migrations**:
    ```sh
    python manage.py migrate
    ```
5. **Start the development server**:
    ```sh
    python manage.py runserver
    ```
6. **Access the app** at [http://localhost:8000/](http://localhost:8000/).

## API Endpoints

- `/` : Renders the main index page.
- `/data/` : Fetches and returns public gists from GitHub as JSON.

## Notes

- The project uses a local SQLite database (`db.sqlite3`), which is ignored in version control via `.gitignore`.
- The virtual environment directory (`env/`) is also ignored.

## License

This project is for educational/demo purposes.
