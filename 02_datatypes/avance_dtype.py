from datetime import datetime

brewing_time = datetime.utcnow()
print("Brewing started at:", brewing_time.strftime('%Y-%m-%d %H:%M:%S'))


from collections import namedtuple
chaiProfile = namedtuple('ChaiProfile', ['sugar_level', 'milk_type', 'spice_level'])
my_chai = chaiProfile(sugar_level='medium', milk_type='whole', spice_level='high')
print("Chai Profile:", my_chai)