import pandas as pd

# Load the CSV file
smartphone_data = pd.read_csv('smartphone_cleaned_v5.csv')

# Clean and ensure the 'price' column is numeric
# Strip unwanted characters, convert to numeric, and handle errors
smartphone_data['price'] = pd.to_numeric(smartphone_data['price'].replace(r'[^\d.]+', '', regex=True), errors='coerce')

# Drop rows where price is missing or not a valid number
smartphone_data.dropna(subset=['price'], inplace=True)


# Define the chatbot function
def chatbot_interaction():
    print("Welcome to the Smartphone Chatbot! I can help you find smartphones based on your preferences.")

    # Main loop to keep the chatbot running
    while True:
        # Ask the user for preferences and apply filters accordingly
        brand = input(
            "Which brand are you interested in? (e.g., Samsung, OnePlus, Realme, etc.). Type 'exit' to quit: ").lower()

        # If user types 'exit', break the loop and stop the program
        if brand == 'exit':
            print("Thank you for using the Smartphone Chatbot! Goodbye!")
            break

        # Ask for the maximum budget
        max_price = input(
            "What is your maximum budget for the smartphone? (Enter a number, e.g., 20000). Type 'exit' to quit: ")

        # If user types 'exit', break the loop and stop the program
        if max_price.lower() == 'exit':
            print("Thank you for using the Smartphone Chatbot! Goodbye!")
            break

        # Convert max_price to an integer if provided
        try:
            max_price = int(max_price)
        except ValueError:
            print("Invalid price entered, showing all results.")
            max_price = None

        # Apply filters based on user input
        filtered_data = smartphone_data.copy()

        if brand:
            filtered_data = filtered_data[filtered_data['brand_name'].str.lower() == brand]

        if max_price is not None:
            filtered_data = filtered_data[filtered_data['price'] <= max_price]

        # Check if there are results after filtering
        if filtered_data.empty:
            print("Sorry, no smartphones found with the given preferences.")
        else:
            print(f"Found {len(filtered_data)} smartphones matching your criteria:\n")
            for index, row in filtered_data.iterrows():
                print(
                    f"Brand: {row['brand_name']}, Model: {row['model']}, Price: {row['price']} INR, Rating: {row['rating']}%")
                print(
                    f"  - 5G Support: {'Yes' if row['has_5g'] else 'No'}, NFC: {'Yes' if row['has_nfc'] else 'No'}, Screen Size: {row['screen_size']} inches")
                print(
                    f"  - Processor: {row['processor_brand']} {row['num_cores']} cores at {row['processor_speed']} GHz, Refresh Rate: {row['refresh_rate']} Hz")
                print(
                    f"  - Rear Camera: {row['primary_camera_rear']} MP, Front Camera: {row['primary_camera_front']} MP")
                print("")

        # Ask the user if they want to search for a specific model
        search_model = input("Do you want to search for a specific smartphone model? (yes/no): ").lower()

        if search_model == 'yes':
            specific_model = input(
                "Enter the smartphone model you are looking for (e.g., Samsung Galaxy A11): ").lower()

            # Filter based on the model name
            model_search = filtered_data[filtered_data['model'].str.lower().str.contains(specific_model)]

            # Check if any specific model was found
            if not model_search.empty:
                for index, row in model_search.iterrows():
                    print(
                        f"Specific smartphone found:\nBrand: {row['brand_name']}, Model: {row['model']}, Price: {row['price']} INR, Rating: {row['rating']}%")
                    print(
                        f"  - 5G Support: {'Yes' if row['has_5g'] else 'No'}, NFC: {'Yes' if row['has_nfc'] else 'No'}, Screen Size: {row['screen_size']} inches")
                    print(
                        f"  - Processor: {row['processor_brand']} {row['num_cores']} cores at {row['processor_speed']} GHz, Refresh Rate: {row['refresh_rate']} Hz")
                    print(
                        f"  - Rear Camera: {row['primary_camera_rear']} MP, Front Camera: {row['primary_camera_front']} MP")
                    print("")
            else:
                print(f"Sorry, the model '{specific_model}' was not found within your search criteria.")

        # Continue the loop and ask for next input


# Run the chatbot function
chatbot_interaction()
