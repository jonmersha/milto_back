# Miltoo Ride System - Django Backend

This is the REST API backend for the Miltoo Ride System, built with Django and Django Rest Framework.

## Setup Instructions

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run Migrations**:
    ```bash
    python manage.py makemigrations miltoo
    python manage.py migrate
    ```

3.  **Create Superuser** (Optional):
    ```bash
    python manage.py createsuperuser
    ```

4.  **Run the Server**:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

-   `GET /api/users/`: List all users
-   `POST /api/users/`: Create a user profile
-   `GET /api/rides/`: List available rides
-   `POST /api/rides/`: Create a new ride
-   `GET /api/ride-requests/`: List ride requests
-   `POST /api/ride-requests/`: Create a ride request
-   `POST /api/alerts/`: Send SOS alerts

## Configuration

The backend is configured to allow all CORS origins by default for development. For production, update `CORS_ALLOWED_ORIGINS` in `core/settings.py`.
