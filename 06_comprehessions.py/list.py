menu  = [
    'Home',
    'About',
    'Services',
    'Contact',
    'Blog'
]

iced_tea = [item for item in menu if 'e' in item.lower()]

print(iced_tea)  # Output: ['Home', 'Services', 'Contact', 'Blog']