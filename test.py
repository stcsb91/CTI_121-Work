import pytest
from employee_data import Employee

@pytest.fixture
def sample_employee():
    return Employee("Sam", "Starrbaum", 70000)

def test_give_default_raise(sample_employee):
    sample_employee.give_raise()
    assert sample_employee.annual_salary == 75000

def test_give_custom_raise(sample_employee):
    sample_employee.give_raise(10000)
    assert sample_employee.annual_salary == 80000