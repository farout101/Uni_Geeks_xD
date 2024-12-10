# Uni_Geeks

Uni_Geeks is a web application designed to help students collaborate and share resources. Users can create rooms, participate in discussions, and share messages. The application also includes user profiles and topics to organize discussions.

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
    git clone https://github.com/farout101/Uni_Geeks.git
    cd Uni_Geeks
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

## API Implementation

I am planning to develop a comprehensive RESTful API using Django REST Framework (DRF) to enhance the functionality and accessibility of Uni_Geeks. The API will include the following endpoints:

### Authentication

- `POST /api/auth/login/`: Authenticate a user and return a token.
- `POST /api/auth/register/`: Register a new user.
- `POST /api/auth/logout/`: Log out the authenticated user.

### User

- `GET /api/users/`: Retrieve a list of users.
- `GET /api/users/{id}/`: Retrieve a specific user by ID.
- `PUT /api/users/{id}/`: Update a specific user by ID.
- `DELETE /api/users/{id}/`: Delete a specific user by ID.

### Room

- `GET /api/rooms/`: Retrieve a list of rooms.
- `POST /api/rooms/`: Create a new room.
- `GET /api/rooms/{id}/`: Retrieve a specific room by ID.
- `PUT /api/rooms/{id}/`: Update a specific room by ID.
- `DELETE /api/rooms/{id}/`: Delete a specific room by ID.

### Message

- `GET /api/messages/`: Retrieve a list of messages.
- `POST /api/messages/`: Create a new message.
- `GET /api/messages/{id}/`: Retrieve a specific message by ID.
- `PUT /api/messages/{id}/`: Update a specific message by ID.
- `DELETE /api/messages/{id}/`: Delete a specific message by ID.

### Topic

- `GET /api/topics/`: Retrieve a list of topics.
- `POST /api/topics/`: Create a new topic.
- `GET /api/topics/{id}/`: Retrieve a specific topic by ID.
- `PUT /api/topics/{id}/`: Update a specific topic by ID.
- `DELETE /api/topics/{id}/`: Delete a specific topic by ID.

These endpoints will allow developers to integrate Uni_Geeks with other applications and services, providing a seamless experience for users. Stay tuned for updates as I continue to develop and enhance the API.

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