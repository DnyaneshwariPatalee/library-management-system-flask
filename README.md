# Library Management System (Flask)

This project implements a simple **Library Management System** using **Flask**, where users can manage books and members, with CRUD operations and token-based authentication.

## How to Run the Project

### 1. **Clone the Repository**:
   Clone this repository to your local machine:
   git clone https://github.com/DnyaneshwariPatalee/library-management-system-flask.git
   cd library-management-system-flask

### 2. **Set Up a Virtual Environment** (optional but recommended):
   To avoid any version conflicts, it's best to use a virtual environment.

   - Install `virtualenv` if you don’t have it already:
     ```bash
     pip install virtualenv
     ```

   - Create and activate a virtual environment:
     ```bash
     virtualenv venv
     source venv/bin/activate   # On Windows use `venv\Scripts\activate`
     ```

   - Install the necessary dependencies (Flask):
     ```bash
     pip install Flask
     ```

### 3. **Run the Application**:
   - Run the Flask application:
     ```bash
     python app.py
     ```
   - The app will be available at `http://127.0.0.1:5000`.

### 4. **Login**:
   - Open **Postman** (or another API testing tool).
   - To get an authentication token, send a `POST` request to `/login` with the following details:
     - **URL**: `http://127.0.0.1:5000/login`
     - **Method**: `POST`
     - **Headers**:
       - `Content-Type`: `application/json`
     - **Body** (raw JSON):
       ```json
       {
           "username": "admin",
           "password": "admin"
       }
       ```
   - **Response** (on successful login):
     ```json
     {
         "message": "Login successful",
         "token": "your_generated_token_here"
     }
     ```

### 5. **Use the API**:
   - For all subsequent API requests, you must include the token in the `Authorization` header.
     - Example: Add the following header to your requests:
       - **Authorization**: `Bearer <your_token_here>`
   - Example of a **POST request to add a book**:
     - **URL**: `http://127.0.0.1:5000/books`
     - **Method**: `POST`
     - **Headers**:
       - `Authorization`: `Bearer <your_token_here>`
       - `Content-Type`: `application/json`
     - **Body** (raw JSON):
       ```json
       {
           "title": "Learn Flask",
           "author": "John Doe",
           "year": 2024
       }
       ```

   - Example of a **GET request to fetch all books**:
     - **URL**: `http://127.0.0.1:5000/books`
     - **Method**: `GET`
     - **Headers**:
       - `Authorization`: `Bearer <your_token_here>`
       - `Content-Type`: `application/json`
     - **Response**:
       ```json
       [
           {
               "id": "unique_book_id_1",
               "title": "Learn Flask",
               "author": "John Doe",
               "year": 2024
           },
           ...
       ]
       ```

## Design Choices Made

1. **Token-based Authentication**: 
   - Used token-based authentication to secure the API routes. Tokens are generated upon successful login and required for accessing protected routes.
   
2. **In-memory Data Storage**:
   - The application uses in-memory storage (i.e., lists for books and members) for simplicity. In a production environment, you would typically use a database like MySQL, PostgreSQL, or MongoDB.

3. **Flask Framework**:
   - Flask was chosen due to its simplicity and flexibility for building small and lightweight APIs.

4. **Pagination**:
   - Pagination is implemented on the `/books` route to limit the number of books returned in one response, reducing load and improving performance.

## Assumptions and Limitations

1. **Assumptions**:
   - The system assumes a basic setup with an in-memory database. In real-world applications, a persistent database is necessary.
   
2. **Limitations**:
   - The project currently supports only a single user (`admin`) for authentication.
   - No persistent storage (database) is used, which means data is lost when the server is restarted.
   - Error handling and validation are basic; there are no detailed checks for malformed input.
   - There is no rate-limiting or advanced security measures like encryption.
   - Pagination parameters are simple, and there's no sorting or filtering by advanced fields such as `year`.

## API Endpoints

### 1. **Login**:
   - **POST** `/login`
   - **Body** (raw JSON):
     ```json
     {
         "username": "admin",
         "password": "admin"
     }
     ```
   - **Response**:
     ```json
     {
         "message": "Login successful",
         "token": "your_generated_token_here"
     }
     ```

### 2. **Books**:
   - **GET** `/books` (Fetch all books with optional search and pagination)
     - **Query Parameters**:
       - `q`: Search query (optional, to filter by title or author)
       - `page`: Page number (optional, default is 1)
       - `per_page`: Number of items per page (optional, default is 5)
   
   - **POST** `/books` (Add a new book)
     - **Body** (raw JSON):
       ```json
       {
           "title": "Book Title",
           "author": "Author Name",
           "year": 2024
       }
       ```
   
   - **GET** `/books/<book_id>` (Fetch details of a specific book)
   
   - **PUT** `/books/<book_id>` (Update details of a specific book)
     - **Body** (raw JSON):
       ```json
       {
           "title": "Updated Title",
           "author": "Updated Author",
           "year": 2025
       }
       ```
   
   - **DELETE** `/books/<book_id>` (Delete a specific book)

### 3. **Members**:
   - **GET** `/members` (Fetch all members)
   
   - **POST** `/members` (Add a new member)
     - **Body** (raw JSON):
       ```json
       {
           "name": "Member Name",
           "email": "member@example.com"
       }
       ```
   
   - **GET** `/members/<member_id>` (Fetch details of a specific member)
   
   - **PUT** `/members/<member_id>` (Update details of a specific member)
   
   - **DELETE** `/members/<member_id>` (Delete a specific member)

### 4. **Logout**:
   - **POST** `/logout` (Logout and invalidate the token)

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
