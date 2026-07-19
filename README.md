# Personal Finance Tracker

A Django-based web application to manage personal finances with
authentication, income and expense tracking, reports, and charts.

## Features

-   User Registration, Login & Logout
-   Dashboard with financial summary
-   Income CRUD
-   Expense CRUD
-   Search by title
-   Filter by category
-   Pagination
-   Reports with Chart.js
-   Responsive Bootstrap UI

## Tech Stack

-   Python 3
-   Django 5
-   SQLite3
-   HTML5
-   CSS3
-   Bootstrap 5
-   JavaScript
-   Chart.js

## Project Structure

``` text
finance_tracker/
├── accounts/
├── dashboard/
├── income/
├── expense/
├── reports/
├── finance_tracker/
├── templates/
├── static/
│   ├── css/
│   └── js/
├── manage.py
└── db.sqlite3
```

## Installation

``` bash
git clone <repository-url>
cd finance_tracker
python -m venv venv
```

Activate the virtual environment and install dependencies:

``` bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

## Main Modules

### Accounts

Authentication using Django's built-in authentication system.

### Dashboard

-   Total Income
-   Total Expense
-   Balance
-   Savings Percentage
-   Income vs Expense Chart

### Income

-   Add
-   Edit
-   Delete
-   Search
-   Filter
-   Pagination

### Expense

-   Add
-   Edit
-   Delete
-   Search
-   Filter
-   Pagination

### Reports

-   Financial Summary
-   Expense Category Pie Chart

## Django Concepts Used

-   Models
-   Views
-   Templates
-   URL Routing
-   ModelForms
-   Authentication
-   ORM
-   Aggregation (`Sum`)
-   Pagination
-   Messages Framework
-   Static Files

## Security

-   Login Required
-   CSRF Protection
-   User-specific data filtering
-   Django ORM

## Future Enhancements

-   Monthly Reports
-   Excel/PDF Export
-   Budget Planning
-   REST API
-   PostgreSQL
-   Docker

## License

This project is intended for learning, portfolio, and demonstration
purposes.
