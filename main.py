# Lets get max number froma list

invoices =[6, 10, 20, 47, 69, 11, 50, 230, 20, 24, 39, 29, 45]

def biggest(numbers) :
  biggest_number = invoices[0]
  for number in invoices:
    if number > biggest_number:
       biggest_number = number
  return biggest_number
#Print List

print(biggest(invoices))

