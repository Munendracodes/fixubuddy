# 💊 Pharmacy Management System

A backend application built with **FastAPI** and **MySQL** to manage a medical store's operations such as inventory management, billing, and automated stock alerts.

---

## 🚀 Features

- Add, update, delete medicines with stock and batch details
- Associate medicines with drug compositions (e.g., Paracetamol, Caffeine)
- Reduce stock automatically when medicine is sold
- Search medicines by name, category, or drug composition
- Auto-alert for low-stock medicines (via email)
- Email notifications to customers on billing
- Pagination support for listing medicines
- Containerized using Docker for production deployment

---

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Email**: SMTP + FastAPI BackgroundTasks
- **Environment**: Python `.env` + `python-dotenv`
- **Containerization**: Docker + Docker Compose

---

## 📂 Project Structure

