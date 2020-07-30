
service_dict = {
    "bad" : 0.10,
    "good" : 0.2,
    "fair" : 0.15
}

bill_amount = float(input("Enter bill amount: "))
service = input("Level of service (bad, good, fair): ")


def calculator(amount, service):
    tip = amount * service_dict[service]
    total = amount + tip
    print(f"Tip amount: $%.2f" % tip)
    print("Total amount: $%.2f" % total)

calculator(bill_amount, service)