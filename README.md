# Flask Student CRUD API

A RESTful API built with Flask for performing CRUD (Create, Read, Update, Delete) operations on student records.

## Features

- Create, read, update, and delete student records
- Pagination support for listing students
- Comprehensive error handling
- Input validation
- RESTful design principles

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/students` | Get all students (with pagination) |
| GET | `/students/<id>` | Get a specific student by ID |
| POST | `/students` | Create a new student |
| PUT | `/students/<id>` | Update an existing student |
| DELETE | `/students/<id>` | Delete a student |

### Query Parameters for GET /students

- `page` (optional): Page number (default: 1)
- `limit` (optional): Number of students per page (default: 10)

### Student Data Model

```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 20,
    "gender": "male"
}