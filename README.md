# Study_Pal

Study_Pal is a web application designed to help students collaborate and share resources. Users can create rooms, participate in discussions, and share messages. The application also includes user profiles and topics to organize discussions.

## Features

- User authentication (login, logout, register)
- Create and join rooms
- Post messages in rooms
- User profiles with bio/description
- Topics to organize discussions
- Search functionality for rooms and topics

## Technologies Used

- Django (Backend)
- HTML/CSS (Frontend)
- JavaScript (Frontend)
- SQLite (Database)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Study_Pal.git
    cd Study_Pal
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000/` to see the application.

## Project Structure

- `project/`: Contains the main Django project settings and URLs.
- `project/models.py`: Defines the database models for the application.
- `project/views.py`: Contains the view functions for handling requests and rendering templates.
- `project/templates/`: Contains the HTML templates for the application.
- `project/static/`: Contains the static files (CSS, JavaScript, images) for the application.

## Models

### User

The default Django `User` model is extended with a `Profile` model to include additional fields like `bio`.

### Room

- `host`: ForeignKey to `User`
- `topic`: ForeignKey to `Topic`
- `name`: CharField
- `description`: TextField
- `participants`: ManyToManyField to `User`
- `updated`: DateTimeField
- `created`: DateTimeField

### Message

- `user`: ForeignKey to `User`
- `room`: ForeignKey to `Room`
- `body`: TextField
- `updated`: DateTimeField
- `created`: DateTimeField

### Topic

- `name`: CharField

## Views

### Home

Displays a list of rooms and topics, with search functionality.

### Room

Displays the messages in a room and allows users to post new messages.

### UserProfile

Displays the user's profile, including their rooms and messages.

### TopicPage

Displays a list of topics, with search functionality.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License.