import unittest
from uuid import uuid4

from database import (
    create_employee,
    get_db_connection,
    get_employee_by_id,
    get_all_employees,
    update_employee,
    delete_employee,
)


# Base class for database integration tests
class TestDatabaseConnection(unittest.TestCase):

    def test_database_connection(self):
        # Create database connection
        connection = get_db_connection()

        # Register connection cleanup
        self.addCleanup(connection.close)

        # Verify database connection
        self.assertTrue(connection.is_connected())

        # Create database cursor
        cursor = connection.cursor()
        self.addCleanup(cursor.close)

        # Execute SQL query
        cursor.execute("SELECT DATABASE(), CURRENT_USER()")

        # Retrieve one result row
        database_name, current_user = cursor.fetchone()

        # Verify database and authenticated user
        self.assertEqual(database_name, "employee_db")
        self.assertEqual(current_user, "employee_app@localhost")

    def test_create_employee(self):
        email = f"test-{uuid4().hex}@example.com"
        employee_id = create_employee(
            "Test Employee",
            email,
            "Engineering",
            65000.00,
        )
        # Automatically delete test data after the test
        self.addCleanup(self.cleanup_employee, employee_id)

        self.assertIsInstance(employee_id, int)
        self.assertGreater(employee_id, 0)

    def delete_employee(self, employee_id):
        connection = get_db_connection()
        cursor = None

        try:
            cursor = connection.cursor()
            cursor.execute(
                "DELETE FROM employees WHERE employee_id = %s",
                (employee_id,),
            )
            connection.commit()

        finally:
            if cursor is not None:
                cursor.close()

            connection.close()

    def test_get_employee_by_id(self):
        email = f"read-{uuid4().hex}@example.com"
        employee_id = create_employee(
            "Read Test Employee",
            email,
            "Engineering",
            70000.00,
        )
        self.addCleanup(self.cleanup_employee, employee_id)
        employee = get_employee_by_id(employee_id)

        self.assertIsNotNone(employee)
        self.assertEqual(employee["employee_id"], employee_id)
        self.assertEqual(employee["name"], "Read Test Employee")
        self.assertEqual(employee["email"], email)
        self.assertEqual(employee["department"], "Engineering")
        self.assertEqual(float(employee["salary"]), 70000.00)

    def test_get_all_employees(self):
        email = f"all-{uuid4().hex}@example.com"
        employee_id = create_employee(
            "All Test Employee",
            email,
            "Engineering",
            75000.00,
        )

        self.addCleanup(self.cleanup_employee, employee_id)
        employees = get_all_employees()

        self.assertIsInstance(employees, list)
        employee_ids = [employee["employee_id"] for employee in employees]
        self.assertIn(employee_id, employee_ids)

    def test_update_employee(self):
        email = f"update-{uuid4().hex}@example.com"

        employee_id = create_employee(
            "Update Test Employee",
            email,
            "Engineering",
            65000.00,
        )

        self.addCleanup(self.cleanup_employee, employee_id)
        affected_rows = update_employee(
            employee_id,
            "Data Science",
            85000.00,
        )
        employee = get_employee_by_id(employee_id)
        self.assertEqual(affected_rows, 1)
        self.assertEqual(employee["department"], "Data Science")
        self.assertEqual(float(employee["salary"]), 85000.00)

    def cleanup_employee(self, employee_id):
        connection = get_db_connection()
        cursor = None

        try:
            cursor = connection.cursor()
            cursor.execute(
                "DELETE FROM employees WHERE employee_id = %s",
                (employee_id,),
            )
            connection.commit()

        except Exception:
            connection.rollback()
            raise

        finally:
            if cursor is not None:
                cursor.close()

            connection.close()

    def test_delete_employee(self):
        email = f"delete-{uuid4().hex}@example.com"
        employee_id = create_employee(
            "Delete Test Employee",
            email,
            "Engineering",
            65000.00,
        )

        self.addCleanup(self.cleanup_employee, employee_id)
        affected_rows = delete_employee(employee_id)
        employee = get_employee_by_id(employee_id)

        self.assertEqual(affected_rows, 1)
        self.assertIsNone(employee)

    def test_delete_non_existing_employee(self):
        email = f"missing-{uuid4().hex}@example.com"

        employee_id = create_employee(
            "Missing Test Employee",
            email,
            "Engineering",
            55000.00,
        )

        self.addCleanup(self.cleanup_employee, employee_id)

        # First deletion should succeed.
        first_delete = delete_employee(employee_id)

        # Second deletion should find no matching record.
        second_delete = delete_employee(employee_id)

        self.assertEqual(first_delete, 1)
        self.assertEqual(second_delete, 0)


if __name__ == "__main__":
    unittest.main()
