def main():
    cost_per_item = 19.99
    print (f"cost_per_item = ${cost_per_item}") 
 
    quantity = 5 
    print (f"quantity = {quantity}") 

    # YOUR CODE TO CALCULATE THE TOTALS GOES HERE

    subtotal_cost = (cost_per_item * quantity)
    print(f'subtotal_cost = ${subtotal_cost:0.2f}')

    tax = 0.13 * subtotal_cost
    print (f"tax = ${tax:0.2f}")

# YOUR CODE TO PRINT THE TOTALS GOES HERE

    total_cost = subtotal_cost + tax
    print (f"total_cost = ${total_cost:0.2f}")

if __name__ == "__main__":
    main()