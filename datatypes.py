# Python Data Types Demonstration

print("\n--- Numeric Types ---")
integer_num = 10
float_num = 3.14
complex_num = 2 + 3j
print("Integer:", integer_num, type(integer_num))
print("Float:", float_num, type(float_num))
print("Complex:", complex_num, type(complex_num))

print("\n--- String ---")
string_val = "Hello, Python!"
print("String:", string_val, type(string_val))

print("\n--- List (mutable, ordered) ---")
list_val = [1, 2, 3, "apple", 4.5]
list_val.append("new item")  # shows mutability
print("List:", list_val, type(list_val))

print("\n--- Tuple (immutable, ordered) ---")
tuple_val = (10, 20, "banana")
print("Tuple:", tuple_val, type(tuple_val))

print("\n--- Set (unordered, unique elements) ---")
set_val = {1, 2, 2, 3, "grape"}
print("Set:", set_val, type(set_val))

print("\n--- Dictionary (key-value pairs) ---")
dict_val = {"name": "Vishnu", "age": 20, "course": "CSE"}
dict_val["college"] = "SVREC"  # shows mutability
print("Dictionary:", dict_val, type(dict_val))

print("\n--- Boolean ---")
bool_val = True
print("Boolean:", bool_val, type(bool_val))

print("\n--- NoneType ---")
none_val = None
print("NoneType:", none_val, type(none_val))
