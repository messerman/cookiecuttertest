import sys

num_errors = 0

accounting_category = '{{cookiecutter.accounting_category}}'
if 'None' == accounting_category:
   print('ERROR: "None" is not a valid Accounting Category')
   num_errors += 1

creator_username = '{{cookiecutter.creator_username}}'
if 'None' == creator_username:
   print('ERROR: "creator_username" is a required field.')
   num_errors += 1

customer_name = '{{cookiecutter.customer_name}}'
if 'None' == customer_name:
   print('ERROR: "customer_name" is a required field.')
   num_errors += 1

sys.exit(0 if 0 == num_errors else 1)
