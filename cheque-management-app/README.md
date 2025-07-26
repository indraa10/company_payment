# Cheque Management Application

This project is a Cheque Management Application that consists of a frontend built with React and a backend developed using Python with Flask. The application allows users to input and manage cheque details.

## Project Structure

```
cheque-management-app
├── frontend
│   ├── src
│   │   ├── components
│   │   │   └── ChequeForm.tsx
│   │   ├── App.tsx
│   │   ├── index.tsx
│   │   └── types
│   │       └── cheque.ts
│   ├── public
│   │   └── index.html
│   ├── package.json
│   ├── tsconfig.json
│   └── README.md
├── backend
│   ├── app.py
│   ├── models.py
│   ├── database.db
│   ├── requirements.txt
│   └── README.md
└── README.md
```

## Frontend

The frontend is a React application that allows users to input cheque details. It includes:

- **ChequeForm Component**: A form for entering cheque details such as date, bank, cheque number, amount, shop name, salesman name, clear date, and remarks for bounced cheques.
- **App Component**: The main application component that renders the ChequeForm.
- **TypeScript Support**: Type definitions for cheque-related data.

### Getting Started

1. Navigate to the `frontend` directory.
2. Install dependencies using `npm install`.
3. Start the development server with `npm start`.

## Backend

The backend is a Flask application that handles the processing and storage of cheque information. It includes:

- **Flask App**: The main entry point for the application.
- **Database Models**: Definitions for cheque records stored in an SQLite database.
- **API Endpoints**: Routes for handling cheque data submissions.

### Getting Started

1. Navigate to the `backend` directory.
2. Install dependencies listed in `requirements.txt` using `pip install -r requirements.txt`.
3. Run the Flask application with `python app.py`.

## License

This project is licensed under the MIT License. See the LICENSE file for details.