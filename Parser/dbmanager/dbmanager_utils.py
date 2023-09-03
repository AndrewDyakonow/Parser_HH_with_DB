
def get_avg_salary(salary_from, salary_to):
    """Получить среднюю зарплату"""
    if salary_to is not None:
        return salary_to
    elif salary_from is not None:
        return salary_from
    else:
        return None
