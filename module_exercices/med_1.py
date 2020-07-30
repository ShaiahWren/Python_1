

service_dict = {
    "bad" : 0.10,
    "good" : 0.2,
    "fair" : 0.15
}

bill_amount = float(input("Enter bill amount: "))
service = input("Level of service (bad, good, fair): ")
split_ways = int(input("Split how many ways: "))


def calculator(amount, service, split):
    tip = amount * service_dict[service]
    total = amount + tip
    split_amount = total / split
    print(f"Tip amount: $%.2f" % tip)
    print("Total amount: $%.2f" % total)
    print("Amount per person: $%.2f" % split_amount)

calculator(bill_amount, service, split_ways)


