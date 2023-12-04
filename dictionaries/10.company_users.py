line = input()
companies = {}
while line != 'End':
    company, emp_id = line.split(' -> ')
    if company not in companies:
        companies[company] = []
    if emp_id not in companies[company]:
        companies[company].append(emp_id)
    line = input()

for company, emp_id in companies.items():
    print(company)
    for employee in emp_id:
        print(f"-- {employee}")
