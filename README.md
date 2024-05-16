# My FastAPI App

This is a Python application built with FastAPI that serves as a REST API for managing movies. It interacts with a MySQL database running on localhost.

## Project Structure

The project has the following structure:

```
my-fastapi-app
├── app
│   ├── main.py
│   ├── models
│   │   └── movie.py
│   ├── schemas
│   │   └── movie.py
│   └── database
│       └── connection.py
├── .env
├── requirements.txt
└── README.md
```

- `app/main.py`: This file is the entry point of the application. It sets up the FastAPI app, defines the routes, and starts the server to listen on a specified port.

- `app/models/movie.py`: This file defines the `Movie` model class, which represents the structure of a movie in the database. It contains attributes such as `name`, `year`, and `actors`.

- `app/schemas/movie.py`: This file defines the `MovieCreate` and `MovieUpdate` schemas, which are used for validating the request payload when creating or updating a movie.

- `app/database/connection.py`: This file contains the logic for establishing a connection to the MySQL database on localhost. It provides functions to execute queries and interact with the `movies` table.

- `.env`: This file is used to store environment variables. It may contain configuration settings such as the database connection details.

- `requirements.txt`: This file lists the Python dependencies required for the project. It includes the FastAPI library and any other packages needed for the application.

## Getting Started

To set up and run the application, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/my-fastapi-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd my-fastapi-app
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database connection details in the `.env` file.

5. Start the FastAPI server:

   ```bash
   uvicorn app.main:app --reload
   ```

6. The API is now ready to accept requests. You can access it at `http://localhost:8000`.

## API Endpoints

The following endpoints are available:

- `GET /movies`: Retrieves a list of all movies.
- `GET /movies/{movie_id}`: Retrieves a specific movie by ID.
- `POST /movies`: Creates a new movie.
- `PUT /movies/{movie_id}`: Updates an existing movie by ID.
- `DELETE /movies/{movie_id}`: Deletes a movie by ID.

Please refer to the source code in the `app` directory for more details on the implementation of these endpoints.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.