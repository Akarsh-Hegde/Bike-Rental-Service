# Bike Rental Service

Welcome to the Bike Rental Service project! This project is designed to provide a simple and efficient bike rental service. It utilizes Python for the backend, Streamlit web framework for the frontend, and MySQL for the backend database.

## Features

- User-friendly interface for bike rental
- Seamless integration with MySQL for data storage
- Easy-to-use web application powered by Streamlit

## Getting Started

Follow these steps to clone the repository and start the project on your local machine.

### Prerequisites

Make sure you have the following installed on your machine:

- Python (3.6 or later)
- pip (Python package installer)
- MySQL

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Akarsh-Hegde/bike-rental-service.git
    ```

2. Navigate to the project directory:

    ```bash
    cd bike-rental-service
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. Create a MySQL database and update the configuration in `BikeRentalBackend.py` and `Setup.py` with your database credentials:

    ```python
    # BikeRentalBackend.py

    DB_CONFIG = {
        'host': 'your_mysql_host',
        'user': 'your_mysql_user',
        'password': 'your_mysql_password',
        'database': 'your_database_name'
    }
    ```

### Running the Application

1. Run the following command to start the Streamlit web application:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to [http://localhost:8501](http://localhost:8501) to access the Bike Rental Service.

