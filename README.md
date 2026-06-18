# Shop API

A backend REST API for an e-commerce shop featuring asynchronous external API integration and background tasks.

Description:
This project is a RESTful API built with FastAPI that allows users to:
* Create and manage shop products
* Fetch products with dynamic price conversion (USD, EUR, RUB) on the fly using an external exchange rate API
* Create orders with automatic stock deduction
* Handle heavy notification processes asynchronously in the background

# Tech Stack:
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic (Pydantic Settings)
* HTTPX (Async HTTP client)
* Docker

# Features:
* Products
  * Create new products with USD prices and stock tracking
  * Get all products with dynamic, non-blocking currency conversion via external HTTP requests
* Orders
  * Place orders with stock verification and automatic inventory deduction
  * Asynchronous background execution for order processing notifications (simulated SMS gateway)

Project structure:
shop_api/
.env
docker-compose.yml
requirements.txt
app/
main.py
core/
config.py
database.py
orders/
orders_models.py
orders_schemas.py
orders_router.py
products/
products_models.py
products_schemas.py
products_router.py

# Run the Project

* Locally
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic-settings httpx
uvicorn app.main:app --reload

* Using Docker
Choose the directory where the file is downloaded:
docker-compose up --build

# API Documentation
After running the server: http://localhost:8000/docs

# Environment Variables
Create a .env file:
DATABASE_URL=postgresql://postgres:postgres@db:5432/fast_shop_db
