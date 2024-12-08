# Library Management System (Flask)

This project implements a simple Library Management System using Flask, where users can manage books and members, with CRUD operations and token-based authentication.

## How to Run the Project

1. **Clone the Repository**:
  git clone https://github.com/DnyaneshwariPatalee/library-management-system-flask.git cd library-management-system-flask

2. **Set Up a Virtual Environment** (optional but recommended):
- Install `virtualenv` if you don't have it:
  ```
  pip install virtualenv
  ```
- Create and activate a virtual environment:
  ```
  virtualenv venv
  source venv/bin/activate   # On Windows use `venv\Scripts\activate`
  ```

3. **Install Dependencies**:
- Ensure you have Flask installed:
  ```
  pip install Flask
  ```

4. **Run the Application**:
- Run the Flask application:
  ```
  python app.py
  ```
- The app will be available at `http://127.0.0.1:5000`.

5. **Login**:
- Send a `POST` request to `/login` with the username `admin` and password `admin` to obtain an authentication token.

6. **Use the API**:
- Use Postman or another API testing tool to interact with the available endpoints:
  - `/login` (POST) - Authenticate and get the token.
  - `/books` (GET, POST) - Get or add books.
  - `/books/<book_id>` (GET, PUT, DELETE) - View, update, or delete a book.
  - `/members` (GET, POST) - Get or add members.
  - `/members/<member_id>` (GET, PUT, DELETE) - View, update, or delete a member.

## Design Choices

1. **Token-based Authentication**:
- The application uses a simple token-based authentication system. Users must authenticate with a username and password, and then receive a token which must be sent in the `Authorization` header for all subsequent requests.

2. **In-Memory Data Storage**:
- The data (books and members) is stored in memory, meaning it will be lost when the application stops. In a production environment, you might want to use a database.

3. **Simple Flask Application**:
- The app is built using Flask to demonstrate basic CRUD operations with authentication. It's designed to be simple, scalable, and easy to understand.

## Assumptions & Limitations

1. **No Persistent Storage**:
- The application uses in-memory storage (i.e., Python lists) for books and members. This means the data will be lost when the server is restarted. A persistent database like SQLite, MySQL, or MongoDB would be needed for production use.

2. **No User Registration**:
- Currently, the system has a hard-coded `admin` username and password. There is no support for user registration or password reset functionality.

3. **No Rate Limiting**:
- The application doesn't implement rate limiting or protection against brute-force attacks, which would be important for a production environment.

4. **Limited Error Handling**:
- The app provides basic error messages (e.g., "Unauthorized", "Book not found"), but it doesn't have detailed error handling or validation for invalid input data.

5. **No Frontend**:
- The application does not include a frontend UI; it is an API-only implementation. A frontend can be built on top of this API for better interaction.

## Future Improvements

1. **Database Integration**:
- Switch from in-memory storage to a database for persistent data.

2. **User Registration and Roles**:
- Implement user registration, password hashing, and support for different user roles (e.g., admin, member).

3. **Input Validation**:
- Add proper input validation and error handling for better user experience.

4. **Rate Limiting**:
- Implement rate limiting and other security features to protect the API.

---

Feel free to contribute, report issues, or suggest improvements!
