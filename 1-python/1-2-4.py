# enter grocery item and quantity 

grocery_list = []
while True: 
    grocer_item = input("Enter grocery item (or 'done' to finish): ")
    if grocer_item.lower() == 'done':
        break
    quantity = int(input("Enter quantity: "))
    grocery_list.append({"item": grocer_item, "quantity": quantity})   
    print(f"Added {quantity} of {grocer_item} to the grocery list.")

print(grocery_list)

# grocery_item = {}
# grocery_item["name"] = input("Enter grocery item: ")
# grocery_item["quantity"] = int(input("Enter qunatity: "))
# print(grocery_item["name"])

