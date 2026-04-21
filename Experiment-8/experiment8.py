import re

text = "My phone number is 9876543210 and email is test123@gmail.com"

match_result = re.match(r"my", text)
if match_result:
    print("Match found at beginning:", match_result.group())

search_result = re.search(r"\d{10}", text)
if search_result:
    print("Phone number found:", search_result.group())

findall_result = re.findall(r"\d", text)
print("All digits:", findall_result)

print("Digits using finditer:")
for match in re.finditer(r"\d", text):
    print(match.group(), "at position", match.start())

sub_result = re.sub(r"\d", "*", text)
print("After substitution:", sub_result)

split_result = re.split(r"\s", text)
print("Split by space:", split_result)

date = input("Enter date (dd/mm/yyyy): ")
pattern = r"^\d{2}/\d{2}/\d{4}$"

if re.fullmatch(pattern, date):
    print("Valid date format")
else:
    print("Invalid date format")