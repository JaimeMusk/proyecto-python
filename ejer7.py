
#lista de variables#
strings = ["15", "100", "55", "42"]
integers = [15, 100, 55 ,42]
floats = [1.1, 2.2, 3.3, 4.4]
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#def#
print(f"""
The variable strings is a {type(strings)}.
It contains the elements: {strings}
The element {strings[0]} is a {type(strings[0])}.
""")

print(f"""
The variable integers is a {type(integers)}.
It contains the elements: {integers}
The element {integers[0]} is a {type(integers[0])}.
""")

print(f"""
The variable floats is a {type(floats)}.
It contains the elements: {floats}
The element {floats[0]} is a {type(floats[0])}.
""")

print(f"""
The variable lists is a {type(lists)}.
It contains the elements: {lists}
The element {lists[0]} is a {type(lists[0])}.
""")

print("Now sorting strings and integers...")
strings = sorted(strings)
integers = sorted(integers)
print(f"Sorted strings: {strings}")
print(f"Sorted integers: {integers}")
#comment#
print("Strings are sorted alphabetically while integers are sorted numerically!")