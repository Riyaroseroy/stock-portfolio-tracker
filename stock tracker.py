# 1. Make a new folder named 'stock-proj

# 2. Move your Python file (with quotes!) into that new folder# 1. Define hardcoded stock prices
# This dictionary maps stock symbols (keys) to their prices (values).
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 310.50,
    "GOOG": 135.75,
    "AMZN": 130.00
}

def track_portfolio():
    """
    Main function to run the portfolio tracker.
    """
    
    # 2. Initialize variables
    portfolio = []  # A list to store the stocks the user enters
    total_investment_value = 0.0

    print("--- Simple Stock Portfolio Tracker ---")
    print(f"Available stocks: {', '.join(STOCK_PRICES.keys())}")
    print("Enter 'done' for the stock symbol when you are finished.")
    print("-" * 40)

    # 3. Get user input in a loop
    while True:
        # Get stock symbol
        symbol = input("Enter stock symbol: ").strip().upper()

        if symbol == 'DONE':
            break  # Exit the loop if user is finished

        # --- Validation 1: Check if stock exists in our price list ---
        if symbol not in STOCK_PRICES:
            print(f"Error: Stock '{symbol}' not found in our price list. Please try again.")
            print("-" * 40)
            continue  # Ask for a new symbol

        # Get stock quantity
        try:
            quantity_str = input(f"Enter quantity for {symbol}: ")
            quantity = int(quantity_str)
            
            # --- Validation 2: Check for positive quantity ---
            if quantity <= 0:
                print("Error: Quantity must be a positive number.")
                print("-" * 40)
                continue

        except ValueError:
            # --- Validation 3: Check if quantity was a number ---
            print("Error: Invalid quantity. Please enter a whole number.")
            print("-" * 40)
            continue

        # 4. Perform calculations
        price = STOCK_PRICES[symbol]
        stock_value = price * quantity
        
        # Add to our totals
        total_investment_value += stock_value
        portfolio.append((symbol, quantity, stock_value))

        print(f"Added {quantity} shares of {symbol}. Current total: ${total_investment_value:.2f}")
        print("-" * 40)

    # 5. Display final results
    print("\n--- Your Portfolio Summary ---")
    if not portfolio:
        print("Your portfolio is empty.")
    else:
        for (sym, qty, val) in portfolio:
            print(f"  * {sym}: {qty} shares = ${val:.2f}")
        
        print("-" * 30)
        print(f"**Total Portfolio Value: ${total_investment_value:.2f}**")

    # 6. Optional: Save to file
    print("-" * 40)
    save_choice = input("Do you want to save this summary to 'portfolio.txt'? (yes/no): ").strip().lower()

    if save_choice.startswith('y'):
        try:
            with open("portfolio.txt", "w") as f:
                f.write("--- Portfolio Summary ---\n")
                for (sym, qty, val) in portfolio:
                    f.write(f"  * {sym}: {qty} shares = ${val:.2f}\n")
                f.write("-" * 30 + "\n")
                f.write(f"**Total Portfolio Value: ${total_investment_value:.2f}**\n")
            print("Successfully saved to 'portfolio.txt'.")
        except IOError as e:
            print(f"Error: Could not save file. {e}")
    else:
        print("Summary not saved. Goodbye!")

# Run the main function
if __name__ == "__main__":
    track_portfolio()