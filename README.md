# Daily Expenses Sharing Application

## Project Overview

This Django-based backend service is designed for a daily expenses sharing application. It enables users to manage their expenses and split them using three methods: equal splits, exact amounts, and percentages. The application provides endpoints for user management, expense management, and balance sheet generation.

## Features

- **User Management**: Handle user details including email, name, and mobile number.
- **Expense Management**:
  - **Equal Splits**: Split expenses equally among all participants.
  - **Exact Amounts**: Specify exact amounts each participant owes.
  - **Percentage-Based Splits**: Specify percentage contributions ensuring they sum up to 100%.
- **Balance Sheet**: Generate and download balance sheets showing individual and overall expenses.

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Setup

1. **Clone the Repository**

   ```bash
   git clone <https://github.com/Abhi19990628/Daily-Expenses-Sharing-Application.git>
   cd expensesharing

2. **Create and Activate a Virtual Environment**

```bash
  python -m venv my_env
  my_env\Scripts\activate  # On Windows
  source my_env/bin/activat # on linux

3. **Install Dependencies**

Create a requirements.txt file in the root directory with the following content:**

Django>=3.2,<4.0
djangorestframework>=3.12.0,<4.0


4. **Apply Migrations**
python manage.py migrate


5. **Run the Development Server**
python manage.py runserver
