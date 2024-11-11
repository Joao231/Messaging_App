# Chat Application

This is a chat application built using Flask, MongoDB, and WebSocket for real-time communication. The application allows users to register, create groups, and send direct messages.

## Features

- **User Registration**: Users can register with a unique username, allowing them to participate in chat rooms and send messages.

- **Group Creation**: Users can create chat groups, enabling multiple users to communicate in a shared space.

- **Real-Time Messaging**: Utilizes WebSocket for instant message delivery, allowing users to send and receive messages in real-time without refreshing the page.

- **Direct Messaging**: Users can send direct messages to each other, facilitating private conversations.

- **Message History**: The application stores messages in a MongoDB database, allowing users to retrieve and view past conversations.

- **Real-Time User Presence**: The application provides real-time updates on user presence within chat rooms, fostering a more dynamic and engaging user experience.

- **Modular Architecture**: The application is structured using Flask blueprints, promoting a clean and organized codebase for easier maintenance and scalability.

## Why This Implementation?

The choice of technologies and architecture for this chat application was driven by several factors:

1. **Flask**: Flask is a lightweight and flexible web framework that allows for rapid development. Its simplicity makes it easy to set up and scale as needed, which is ideal for a chat application where quick iterations and changes are often required.

2. **MongoDB**: MongoDB is a NoSQL database that provides flexibility in data storage. It allows for easy handling of dynamic data structures, which is beneficial for a chat application where user messages and group information can vary widely.

3. **WebSocket**: Using WebSocket enables real-time communication between the server and clients. This is crucial for a chat application, as it allows messages to be sent and received instantly without the need for constant polling.

4. **Modular Design**: The application is structured using blueprints for user and group management, promoting a clean and organized codebase. This modular approach makes it easier to maintain and extend the application in the future.

5. **Docker**: Docker is used to containerize the application, ensuring that it runs consistently across different environments. This simplifies deployment and makes it easier to manage dependencies.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.13
- MongoDB (for local setup)
- Docker and Docker Compose (for Docker setup)

## Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a `.env` file** (optional but recommended):
   Create a `.env` file in the root of your project directory with the following content:

   ```env
   MONGO_URI=mongodb://mongo:27017/chat_db
   SECRET_KEY=your_secret_key
   ```

   Replace `your_secret_key` with a secure key of your choice.

## Running the Application Locally

### Using Python and MongoDB

1. **Set up a virtual environment** (optional but recommended):

   ```bash
   python3.13 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

   Make sure your `requirements.txt` includes the necessary packages, such as:

   ```
   Flask
   Flask-PyMongo
   Flask-SocketIO
   python-dotenv
   requests
   ```

3. **Start MongoDB**:
   Ensure that MongoDB is running on your local machine. You can start MongoDB using:

4. **Run the Flask application**:

   ```bash
   python3 main.py
   ```

   The application will start running on `http://localhost:8000`.

5. **Test the application**:
   You can test the application by running the provided Python client files. Open two terminal windows and follow these steps:

   **Run the first client**:
   In the first terminal, run:

   ```bash
   python python_client_1.py
   ```

   **Run the second client**:
   In the second terminal, run:

   ```bash
   python python_client_2.py
   ```

   Make sure to adjust the client files if necessary to use different usernames or rooms.

## Running the Application with Docker

1. **Build and run the application**:
   You can use Docker Compose to build and run the application along with MongoDB. Run the following command in the root of your project directory:

   ```bash
   docker-compose up --build
   ```

   This command will:

   - Build the Docker images defined in your `docker-compose.yml` file.
   - Start the Flask application and MongoDB as defined in the services.

2. **Test the application**:
   You can test the application by running the provided Python client files. Open two terminal windows and follow these steps:

   **Run the first client**:
   In the first terminal, run:

   ```bash
   python python_client_1.py
   ```

   **Run the second client**:
   In the second terminal, run:

   ```bash
   python python_client_2.py
   ```

   Make sure to adjust the client files if necessary to use different usernames or rooms.

## Stopping the Application

- **For Local Setup**: To stop the application, press `CTRL + C` in the terminal where the Flask application is running.
- **For Docker Setup**: To stop the application, press `CTRL + C` in the terminal where Docker Compose is running. You can also run:
  ```bash
  docker-compose down
  ```

## Future Improvements

In the future, I plan to implement the following enhancements to make the application more robust and production-ready:

1. **Production-Ready Server**: Implement necessary changes to ensure the server is fully optimized for production, including performance tuning, security enhancements, and proper error handling.

2. **Frontend Development**: Develop a user-friendly frontend interface that allows users to interact with the chat application seamlessly. This will enhance the user experience and make it easier to send and receive messages.

3. **Improved Authentication**: Enhance the authentication mechanism to provide better security features, such as token-based authentication, password hashing, and user role management.
