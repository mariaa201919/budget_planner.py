def plan_budget(income, expenses):
    # Вычисление общих доходов и расходов
    total_income = sum(income.values())
    total_expenses = sum(expenses.values())

    # Вычисление свободных средств
    free_cash = total_income - total_expenses

    # Вычисление возможных категорий расходов
    categories = {}
    for category, amount in expenses.items():
        categories[category] = amount / total_expenses * free_cash

    # Вывод результата
    print(f"The total income is {total_income}")
    print(f"The total expenses is {total_expenses}")
    print(f"The free cash is {free_cash}")
    print("Possible spending categories:")
    for category, amount in categories.items():
        print(f"- {category}: {amount}")
        
# Пример использования функции
income = {'Sales': 100000, 'Investment': 50000}
expenses = {'Salary': 50000, 'Rent': 20000, 'Advertising': 10000}
plan_budget(income, expenses)
