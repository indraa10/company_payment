# Contents of /cheque-management-app/cheque-management-app/backend/README.md

# Cheque Management App - Backend

This is the backend component of the Cheque Management application. It is built using Python and Flask, and it interacts with a SQLite database to store and manage cheque details.

## Project Structure

- **app.py**: The main entry point for the Flask application. It sets up the server and defines the API endpoints for managing cheque data.
- **models.py**: Contains the data models for the application, including the Cheque model that defines the structure of cheque records.
- **database.db**: The SQLite database file where cheque records are stored.
- **requirements.txt**: Lists the Python dependencies required to run the backend application.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd cheque-management-app/backend
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```
   python app.py
   ```

The backend will start running on `http://127.0.0.1:5000`.

## API Endpoints

- **POST /cheques**: Add a new cheque record.
- **GET /cheques**: Retrieve all cheque records.
- **GET /cheques/<id>**: Retrieve a specific cheque record by ID.
- **PUT /cheques/<id>**: Update a specific cheque record by ID.
- **DELETE /cheques/<id>**: Delete a specific cheque record by ID.

## Database Schema

The database contains a single table for cheque records with the following fields:

- `id`: Integer, primary key
- `given_date`: Date
- `bank`: String
- `cheque_number`: String
- `amount`: Float
- `shop_name`: String
- `salesman_name`: String
- `clear_date`: Date (nullable)
- `remarks`: String (nullable)

## License

This project is licensed under the MIT License. See the LICENSE file for more details.