# "Счётчик вызовов"
calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
     count_calls()
     line_length = len(string)
     up_string = string.upper()
     low_string = string.lower()
     return (line_length, up_string, low_string)
def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in (item.upper() for item in list_to_search)

print(string_info('Hello world'))
print(is_contains('urban', ["Ira", "Nina", "Tanya", "Urban"]))
print('Количество вызовов:', calls)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print('Количество вызовов:', calls)