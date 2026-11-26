#paso 1
email = 'alice.johnson@company.com'
#paso 2
print(f'Email: {email}')
#paso 3
at_position = email.find('@')
print(f'Position of @: {at_position}')
#paso 4
username = email[:at_position]
print(f'Username: {username}')
#paso 5
has_at = '@' in email
print(f'Has @ symbol: {has_at}')
#paso 6
has_com = '.com' in email
print(f'Has .com: {has_com}')
#paso 7
messy_name = '  sARaH dAVis  '
#paso 8
print(f'Original name: \'{messy_name}\'')
#paso 9
clean_name = messy_name.title()
#paso 10
clean_name = messy_name.strip().title()
print(f'Cleaned name: \'{clean_name}\'')
#paso 11


