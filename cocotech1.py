import random


def generate_sales_data():
    sales_data = []
    for day in range(1, 366):
        units_sold = random.randint(100, 1000)
        price = random.uniform(20, 30)
        amount = units_sold * price
        month = (day - 1) // 30 + 1
        quarter = (day - 1) // 90 + 1
        sales_data.append((day, month, quarter, units_sold, price, amount))
    return sales_data


def compute_statistics(sales_data, period_type, period_size):
    statistics = {}
    for day, month, quarter, units_sold, price, amount in sales_data:
        period = (day - 1) // period_size + 1
        if period not in statistics:
            statistics[period] = {'units_sold': 0, 'amount': 0}
        statistics[period]['units_sold'] += units_sold
        statistics[period]['amount'] += amount

    print(f"\n{period_type.capitalize()}ly Statistics:")
    for period, data in statistics.items():
        print(f"{period_type.capitalize()} {period}: Units Sold - {data['units_sold']}, Amount - {data['amount']}")

    max_period, max_amount = max(statistics.items(), key=lambda x: x[1]['amount'])
    print(f"\n{period_type.capitalize()} with Maximum Sales (Amount): {period_type} {max_period} - Amount: {max_amount['amount']}")

    max_period, max_units = max(statistics.items(), key=lambda x: x[1]['units_sold'])
    print(f"{period_type.capitalize()} with Maximum Sales (Units): {period_type} {max_period} - Units Sold: {max_units['units_sold']}")


sales_data = generate_sales_data()


compute_statistics(sales_data, 'month', 30)


compute_statistics(sales_data, 'quarter', 90)
