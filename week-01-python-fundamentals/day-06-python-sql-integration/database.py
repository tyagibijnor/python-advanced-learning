import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv

# Load environment variables from this directory's .env file
ENV_FILE = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=ENV_FILE, override=False)


def get_db_connection():
    """Create and return a MySQL database connection."""

    required_variables = [
        "DB_HOST",
        "DB_PORT",
        "DB_USER",
        "DB_PASSWORD",
        "DB_NAME",
    ]

    missing_variables = [
        variable for variable in required_variables if not os.getenv(variable)
    ]

    if missing_variables:
        raise RuntimeError(
            f"Missing database environment variables: "
            f"{', '.join(missing_variables)}"
        )

    try:
        db_port = int(os.getenv("DB_PORT"))
    except ValueError as exc:
        raise ValueError("DB_PORT must be a valid integer") from exc

    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=db_port,
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        connection_timeout=5,
    )

    return connection


def create_employee(name, email, department, salary):
    """Insert a new employee and return the generated employee ID."""

    connection = get_db_connection()
    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO employees (name, email, department, salary)
            VALUES (%s, %s, %s, %s)
        """

        values = (name, email, department, salary)

        cursor.execute(query, values)
        connection.commit()

        return cursor.lastrowid

    except Exception:
        connection.rollback()
        raise

    finally:
        if cursor is not None:
            cursor.close()

        connection.close()


def get_employee_by_id(employee_id):
    """Fetch an employee by ID. Return None if not found."""

    connection = get_db_connection()
    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT employee_id, name, email, department, salary, created_at
            FROM employees
            WHERE employee_id = %s
        """

        cursor.execute(query, (employee_id,))

        return cursor.fetchone()

    finally:
        if cursor is not None:
            cursor.close()

        connection.close()


def get_all_employees():
    """Fetch all employees from the database."""

    connection = get_db_connection()
    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT employee_id, name, email, department, salary, created_at
            FROM employees
            ORDER BY employee_id
        """

        cursor.execute(query)

        return cursor.fetchall()

    finally:
        if cursor is not None:
            cursor.close()

        connection.close()


def update_employee(employee_id, department, salary):
    """Update an employee's department and salary."""

    connection = get_db_connection()
    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            UPDATE employees
            SET department = %s, salary = %s
            WHERE employee_id = %s
        """

        values = (department, salary, employee_id)

        cursor.execute(query, values)
        connection.commit()

        return cursor.rowcount

    except Exception:
        connection.rollback()
        raise

    finally:
        if cursor is not None:
            cursor.close()

        connection.close()


def delete_employee(employee_id):
    """Delete an employee by ID and return affected rows."""

    connection = get_db_connection()
    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            DELETE FROM employees
            WHERE employee_id = %s
        """

        cursor.execute(query, (employee_id,))
        connection.commit()

        return cursor.rowcount

    except Exception:
        connection.rollback()
        raise

    finally:
        if cursor is not None:
            cursor.close()

        connection.close()
