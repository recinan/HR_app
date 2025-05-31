# HR App

This project is a web-based recruitment management system developed to digitalize internal hiring processes. The backend was built using Django Rest Framework (DRF).

## 🚀 Features

- JWT-based authentication system
- Role-based authorization (Applicant, Committee Member, Administrator)
- Application submission with file upload/download support
- Candidate evaluation and scoring by committee members
- Automated email notifications (e.g., application status updates)
- Swagger UI for API documentation and testing

## 🛠️ Technologies Used

- **Python**
- **Django**
- **Django REST Framework**
- **PostgreSQL**
- **JWT (djangorestframework-simplejwt)**
- **Swagger UI (drf-yasg)**
- **SMTP / Celery / Redis** (if used – feel free to modify)

## 🔐 Authentication & Authorization

- JWT is used for user authentication.
- Users are assigned roles with specific permissions:
  - **Applicant:** Can submit applications and upload documents
  - **Committee Member:** Can view and evaluate applications
  - **Administrator:** Can manage job postings and system settings

## 📄 API Documentation

All endpoints are documented and accessible via Swagger UI:


