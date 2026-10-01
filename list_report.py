items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")

count = 0
for item in items:
    if len(item) > 4:
        count += 1

print("Items with more than 4 letters:", count)

longest = items[0]
for item in items:
    if len(item) > len(longest):
        longest = item

print("Longest item name:", longest)
