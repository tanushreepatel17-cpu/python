#Remove Duplicates from List

duplicate = [10, 20, 10, 30, 40, 40, 20, 50]

## Method to remove duplicates while preserving order
unique_list = list(dict.fromkeys(duplicate))
print(f"unique_list: {unique_list}")