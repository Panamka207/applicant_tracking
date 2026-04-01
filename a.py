tables = {
    'applicants': 'self.tableApplicants',
    'applications': 'self.tableApplications',
    'departaments': 'self.tableDepartments',
    'specialties': 'self.tableDirections'
}

for key in tables:
    print(key)  # Что выведется?

for key, value in tables.items():
    print(key, value)  # Что выведется?
