# HR App

This project is a web-based HR App that provides simplicity for hiring process. The backend was built using Django Rest Framework.

## 🚀 Features

- JWT-based authentication system
- Role-based authorization
- Application submission with file upload/download support
- Candidate evaluation and scoring by committee members
- Automated email notifications (e.g., application status updates)
- Swagger UI for API documentation and testing

## 🛠️ Technologies Used

- **Python**
- **Django**
- **Django REST Framework**
- **PostgreSQL**
- **JWT**
- **Swagger UI**
- **SMTP** 

## 🔐 Authentication & Authorization

- JWT is used for user authentication.
- Users are assigned roles with specific permissions:
  - **Candidate:** Can submit applications and upload/download documents
  - **Evaluator** Can view, upload/download documents and evaluate applications
  - **Admin:** Can manage job postings and system settings

## 📄 API Documentation

All endpoints are documented and accessible via Swagger UI:


