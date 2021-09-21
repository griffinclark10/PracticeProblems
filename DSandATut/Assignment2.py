#In this assignment, you will recreate Python dictionaries from scratch using data structure called hash table. 
#Dictionaries in Python are used to store key-value pairs. Keys are used to store and retrieve values. For example, 
# here's a dictionary for storing and retrieving phone numbers using people's names.

MAX_HASH_TABLE_SIZE = 4096

phone_numbers = {
  'Aakash' : '9489484949',
  'Hemanth' : '9595949494',
  'Siddhant' : '9231325312'
}
phone_numbers['Vishal'] = '8787878787'
phone_numbers['Aakash'] = '7878787878'

def get_index(data_list, a_string):
    result = 0
    for a_character in a_string:
        a_number = ord(a_character)
        result += a_number
    return result % len(data_list)

def get_valid_index(data_list, key):
    idx = get_index(data_list, key)
    while True:
        kv = data_list[idx]
        if kv is None:
            return idx
        k, v = kv
        if k == key:
            return idx
        idx += 1
        if idx == len(data_list):
            idx = 0


# for name in phone_numbers:
#     print('Name:', name, ', Phone Number:', phone_numbers[name])

class HashTable:
    def __init__(self, max_size = MAX_HASH_TABLE_SIZE):
        self.data_list = [None]*max_size

    def insert(self, key, value):
        """Insert a new key-value pair"""
        idx = get_valid_index(self.data_list, key)
        self.data_list[idx] = (key, value)
        
    
    def find(self, key):
        """Find the value associated with a key"""
        idx = get_valid_index(self.data_list, key)
        kv = self.data_list[idx]
        if kv is None:
            return None
        else:
            key, value = kv
            return value
    
    def update(self, key, value):
        """Change the value associated with a key"""
        self.data_list[get_index(self.data_list, key)] = (key, value)
        
    
    def list_all(self):
        """List all the keys"""
        return [kv[0] for kv in self.data_list if kv is not None]

probing_table = HashTable(max_size=1024)

# Insert a value
probing_table.insert('listen', 99)
# Check the value
print(probing_table.find('listen') == 99)
probing_table.insert('silent', 200)
print(probing_table.find('listen') == 99 and probing_table.find('silent') == 200)
probing_table.insert('listen', 101)
# Check the value
print(probing_table.find('listen') == 101)
print(probing_table.list_all() == ['listen', 'silent'])


# data_list = [None]*MAX_HASH_TABLE_SIZE



# #insert a key value pair
# key, value  = 'Aakash', '7878787878'
# idx = get_index(data_list, key)
# data_list[idx] = (key, value)
# #or
# data_list[get_index(data_list, 'Hemanth')] = ('Hemanth', '5064762939')

# #find
# idx = get_index(data_list, 'Hemanth')
# key, value = data_list[idx]

# #list
# pairs = [kv[0] for kv in data_list if kv is not None]
# print(pairs)

# key, value = 'hsakaA', '6969696969'
# data_list[get_index(data_list, key)] = (key, value)
# idx1 = get_index(data_list, 'hsakaA')
# idx2 = get_index(data_list, 'Aakash')
# print("id1: ", data_list[idx1], ", id2: ", data_list[idx2])