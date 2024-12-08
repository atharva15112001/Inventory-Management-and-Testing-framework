from PIL import Image
import requests
import math
import pandas as pd

# Logging Setup
# We can use the logging module to log information about our code.
# This will do the same thing for us as print statements or using the debugger, again in a different way. 
# Logging can be made more elaborate, but we can start with just the basics - basically a print statement for logs only. 
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='testing.log', encoding='utf-8', level=logging.DEBUG)
#logging.debug('This will get logged')

# Note: the arrow and variable type thing at the end of function definitions is a type hint.
# It's not required, and it won't be enforced when code runs, it is basically a more formalized comment. 

class myProduct():

    def __init__(self, name, category, subcat, imageURL, prodURL, rating, numRate, discPrice, price) -> None:
        """
        Initialize a product object. Each product has a name, category, subcategory, image URL, product URL, rating, number of ratings, discount price, and price.

        Note that the price and ratings should be converted to floats and integers respectively. Error handling is good here. 

        Args:
            name (str): The name of the product.
            category (str): The category of the product.
            subcat (str): The subcategory of the product.
            imageURL (str): The URL of the product image.
            prodURL (str): The URL of the product.
            rating (float): The rating of the product.
            numRate (int): The number of ratings.
            discPrice (str): The discount price of the product.
            price (str): The base price of the product.
        """
        self.name = name
        self.category = category
        self.subcat = subcat
        self.imageURL = imageURL
        self.prodURL = prodURL
        
        # Convert rating to float and ensure valid input
        try:
            self.rating = float(rating)
        except ValueError:
            self.rating = 0.0  # Default to 0 if conversion fails
            logger.error(f"Invalid rating value for product {name}. Defaulted to 0.0.")
        
        # Convert numRate to int and ensure valid input
        try:
            self.numRate = int(numRate)
        except ValueError:
            self.numRate = 0  # Default to 0 if conversion fails
            logger.error(f"Invalid numRate value for product {name}. Defaulted to 0.")
        
        # Convert discPrice to float and ensure valid input
        try:
            self.discPrice = float(discPrice)
        except ValueError:
            self.discPrice = 0.0  # Default to 0 if conversion fails
            logger.error(f"Invalid discount price value for product {name}. Defaulted to 0.0.")
        
        # Convert price to float and ensure valid input
        try:
            self.price = float(price)
        except ValueError:
            self.price = 0.0  # Default to 0 if conversion fails
            logger.error(f"Invalid price value for product {name}. Defaulted to 0.0.")

    def __repr__(self):
        """
        This method will define how the product object is represented when printed.
        """
        return f"Product({self.name}, {self.category}, {self.subcat}, {self.rating}, {self.numRate}, {self.discPrice}, {self.price})"

    def __str__(self) -> str:
        """
        Returns:
            str: A string representation of the product.
        """
        return (f"Product Name: {self.name}\n"
            f"Category: {self.category} | Subcategory: {self.subcat}\n"
            f"Rating: {self.rating} ({self.numRate} ratings)\n"
            f"Discount Price: ${self.discPrice} | Regular Price: ${self.price}\n"
            f"Product URL: {self.prodURL}\n"
            f"Image URL: {self.imageURL}")

    def get_rating(self) -> float:
        """
        Get the rating of the product.

        Returns:
            float: The rating of the product.
        """
        return self.rating
    def add_rating(self, rating, numberRate=1) -> float:
        """
        Add more ratings to the product. Update the rating based on the new rating and the number of ratings added.
        Note that you'll need to recalculate the weighted average of the ratings, based on the original number of ratings and their mean, and the new rating and the number of new ratings with their mean,
        Also update the number of ratings.

        Args:
            rating (float): The mean of the new ratings to add.
            numberRate (int, optional): The number of ratings the above value is based on. Defaults to 1.

        Returns:
            float: The new rating.
        """
        try:
            # Ensure the rating is a float and numberRate is an int
            rating = float(rating)  # Convert the rating to float
            numberRate = int(numberRate)  # Ensure numberRate is an integer

            # Calculate the new weighted average rating
            total_ratings = self.numRate + numberRate
            self.rating = ((self.rating * self.numRate) + (rating * numberRate)) / total_ratings

            # Update the total number of ratings
            self.numRate = total_ratings

            return self.rating  # Return the new rating

        except ValueError:
         # Handle the error if rating or numberRate is invalid
         logger.error(f"Invalid value for rating: {rating} or numberRate: {numberRate}")
        return self.rating  # Return the current rating if there's an error
    
    def get_purchase_price(self) -> float:
        """
        Get the purchase price - if there is a discount price set, return that, otherwise return the base price.

        Returns:
            float: The purchase price of the product.
        """
        if self.discPrice > 0:  # If a valid discount price exists
            return self.discPrice
        else:
            return self.price  # Otherwise, return the base price

    def get_base_price(self) -> float:
     """
     Get the base price of the product (without any discounts).

    Returns:
        float: The base price of the product.
    """
     return self.price  # Return the base price of the product


    def set_discount_percent(self, discount) -> float:
        """
        Update the discount price based on a percentage discount. Calculate this discount based on the percentage of the base price.
        Truncate (i.e. do not round) the price to two decimal places - the cent value. 

        Args:
            discount (float): The percentage discount to apply.

        Returns:
            float: The new discount price.
        """
            # Calculate the discount price based on the base price and the discount percentage
        new_discount_price = self.price * (1 - discount / 100)
        
        # Truncate to two decimal places
        truncated_price = int(new_discount_price * 100) / 100.0
        
        # Update the discount price
        self.discPrice = truncated_price
        
        return self.discPrice  # Return the new discount price

    def set_disc_price(self, newPrice) -> float:
        
        """
        Set the discount price to a specific value.

        Args:
            newPrice (float): The new discount price.

        Returns:
            float: The new discount price.
        """
        try:
            # Ensure newPrice is a valid float and not negative
            newPrice = float(newPrice)
            if newPrice < 0:
                raise ValueError("Discount price cannot be negative.")
            
            # Set the new discount price
            self.discPrice = newPrice

            return self.discPrice  # Return the updated discount price

        except ValueError:
            logger.error(f"Invalid value for newPrice: {newPrice}. Setting discount price failed.")
            return self.discPrice  # Return the current discount price if there's an error

    def displayIMG(self):
        try:
            im = Image.open(requests.get(self.imageURL, stream=True).raw)
            return im
        except Exception as e:
            logger.error(f"Failed to display image for {self.name}: {e}")
        
        return None
    # Override the operaters that you need for the functionality here. 

    def __lt__(self, other) -> bool:
        """
        Compare two products based on their price.
        """
        """
        Args:
            other (myProduct): Another product object to compare with.
        Returns:
            bool: True if the price of self is less than the price of other, False otherwise.
        """
        return self.price < other.price

             

    def __eq__(self, other) -> bool:
        """
        Check if two products are equal. Equal products have the same name.
        """
        """
        Check if two products are equal. Equal products have the same name.

        Args:
        other (myProduct): Another product object to compare with.

        Returns:
        bool: True if the products have the same name, False otherwise.
        """
        return self.name == other.name
    
    # If you need any other helper methods, add them here.
    # Remember, the tests will only call the methods that are specified, so you're free
    # to add any other methods you want to organize your code, but they'll need to be called by
    # the other methods to be included in the tests.

class myInventory():

    def __init__(self, inv_name="My Inventory", file_path=None) -> None:
        # Think about the best data structure to use to store the product objects. 
        # Consider how it will typically be accessed and what operations will be performed on it.
        # As long as you meet what the the other methods expect, you can use any data structure, but some may be easier or quicker. 
        """
        Initialize the inventory with a name and optionally load products from a CSV file.

        Args:
            inv_name (str): The name of the inventory.
            file_path (str): Optional file path to load products from a CSV file.
        """
        # Initialize the inventory name
        self.inv_name = inv_name

        # Create a list to store product objects
        self.products = {}
        
        if file_path:
            self.read_file(file_path)
        

    def read_file(self, path) -> int:
        """
        Read in a CSV file and populate the inventory with the products in the file. Each product should have a stock of 10, unless otherwise specified.
        Note that the CSV file will have the following columns: name, main_category, sub_category, image, link, ratings, no_of_ratings, discount_price, actual_price.
        Duplicate names should not be allowed in the inventory, if a duplicate attempts to be added, the function should ignore it.
        Also, the ratings and no_of_ratings should be converted to floats and integers respectively.
        Additionally, the discount_price and actual_price should be converted to floats, and any non-numeric characters should be removed.
        
        Args:
            path (str): The path to the CSV file.
        
        Returns:
            int: The number of products in the inventory.
        """

        data = pd.read_csv(path)

        for _, row in data.iterrows():
            try:
                # Handle discount_price
                if isinstance(row['discount_price'], str):
                    discount_price = ''.join(c for c in row['discount_price'] if c.isdigit() or c == '.')
                    discount_price = float(discount_price) if discount_price else 0.0  # Default to 0.0 if empty or invalid
                else:
                    discount_price = float(row['discount_price']) if not pd.isna(row['discount_price']) else 0.0

                # Handle actual_price
                if isinstance(row['actual_price'], str):
                    actual_price = ''.join(c for c in row['actual_price'] if c.isdigit() or c == '.')
                    actual_price = float(actual_price) if actual_price else 0.0  # Default to 0.0 if empty or invalid
                else:
                    actual_price = float(row['actual_price']) if not pd.isna(row['actual_price']) else 0.0

                # Handle no_of_ratings
                if isinstance(row['no_of_ratings'], str):
                    no_of_ratings_str = ''.join(c for c in row['no_of_ratings'] if c.isdigit())
                    no_of_ratings = int(no_of_ratings_str) if no_of_ratings_str else 0  # Default to 0 if empty or invalid
                elif isinstance(row['no_of_ratings'], float) and math.isnan(row['no_of_ratings']):
                    no_of_ratings = 0
                else:
                    no_of_ratings = int(row['no_of_ratings'])

                # Handle ratings
                if isinstance(row['ratings'], str):
                    rating = ''.join(c for c in row['ratings'] if c.isdigit() or c == '.')
                    rating = float(rating) if rating else 0.0  # Default to 0.0 if empty or invalid
                elif isinstance(row['ratings'], float) and math.isnan(row['ratings']):
                    rating = 0.0  # Default to 0.0 if NaN
                else:
                    rating = float(row['ratings'])

                # Create the product object
                product = myProduct(
                    name=row['name'],
                    category=row['main_category'],
                    subcat=row['sub_category'],
                    imageURL=row['image'],
                    prodURL=row['link'],
                    rating=rating,
                    numRate=no_of_ratings,
                    discPrice=discount_price,
                    price=actual_price
                )

                # Add product to the inventory
                if product.name not in self.products:
                    self.products[product.name] = {"product": product, "stock": 10}
                else:
                    continue

            except (ValueError, TypeError) as e:
                print(f"Row '{row['name']}' encountered an error, but handled: {e}")
                continue

        return len(self.products)





    
    def __len__(self) -> int:
        """
        Get the number of products in the inventory.
        """
        return len(self.products)

    def getProduct(self, product_name) -> myProduct:
        """
        Get a product from the inventory.

        Args:
            product (str): The name of the product.

        Returns:
            myProduct: The product object.
        """
        return self.products.get(product_name, {}).get("product", None)
        

    def adjust_stock(self, product, stock) -> None:
        """
        Adjusts the stock of a product to a new value.

        Args:
            product (str): The name of the product.
            stock (int): The new stock value.
        """
        if product in self.products:
            self.products[product]["stock"] = stock

    def getCategory(self, category=None) -> list:
        """
        Get a subset of the inventory based on a category.

        Args:
            category (str, optional): The category to filter by. Defaults to None.

        Returns:
            list: A list of myProduct objects.
        """
        if category:
            return [product_info["product"] for product_info in self.products.values() if product_info["product"].category == category]
        return list(self.products.values())

    def getPrices(self, min_price, max_price) -> list:
        """
        Get a subset of the inventory based on a price range.

        Args:
            max_price (float): The maximum price.
            min_price (float): The minimum price.

        Returns:
            list: A list of myProduct objects.
        """
        return [product_info["product"] for product_info in self.products.values() if min_price <= product_info["product"].price <= max_price]

    def itemRating(self, product_name) -> float:
        """
        Get the rating of a product.

        Args:
            product_name (str): The name of the product.

        Returns:
            float: The rating of the product.
        """
        product = self.getProduct(product_name)
        if product:
            return product.get_rating()
        return None
    
    def do_purchase(self, product_quantity_tuple_list) -> float:
        """
        Perform a purchase of multiple products.

        If the quantity of a product is not available, the purchase should get as many as possible, and the total price should be calculated based on the available quantity.

        Args:
            product_quantity_tuple_list (list): A list of tuples, where each tuple contains a myProduct item name and an integer representing the quantity purchased.

        Returns:
            float: The total price of all the purchased products, calculated using the get_purchase_price function.
            items_purchased (list): A list of tuples, where each tuple contains the name of the product, the quantity purchased, and the total price for that product.
        """
        total_price = 0
        items_purchased = []

        for product_name, quantity in product_quantity_tuple_list:
            product_info = self.products.get(product_name)
            if product_info:
                product = product_info["product"]
                stock = product_info["stock"]
                purchased_quantity = min(quantity, stock)
                price_for_product = purchased_quantity * product.get_purchase_price()
                total_price += price_for_product
                product_info["stock"] -= purchased_quantity
                items_purchased.append((product_name, purchased_quantity, price_for_product))

        return total_price, items_purchased
    
    def addReviews(self, product_name, rating, numberRate=1) -> float:
        """
        Add a review to a product.

        Args:
            product_name (str): The name of the product.
            rating (float): The rating to add.
            numberRate (int, optional): The number of ratings the rating is based on. Defaults to 1.

        Returns:
            float: The new rating of the product.
        """
        product = self.getProduct(product_name)
        if product:
            return product.add_rating(rating, numberRate)
        return None
    
    def __eq__(self, other) -> bool:
        """
        Check if two inventories are equal. Equal inventories have the same products.

        Args:
            other (myInventory): The other inventory to compare to.
        """
        return set(self.products.keys()) == set(other.products.keys())
    
    def __str__(self) -> str:
        """
        String representation of the inventory.
        """
        return f"Inventory: {self.inv_name}, Number of Products: {len(self)}"
    
    def __len__(self) -> int:
        """
        Get the number of products in the inventory.

        Returns:
            int: The number of products in the inventory.
        """
        return len(self.products)
    
    def __add__(self, other) -> 'myInventory':
        """
        Combine two inventories into one.

        Args:
            other (myInventory): The other inventory to combine with.

        Returns:
            myInventory: The combined inventory.
        """
        
        combined_inventory = myInventory(inv_name=f"{self.inv_name} + {other.inv_name}")

        # Add products from self
        for product_name, product_info in self.products.items():
            combined_inventory.products[product_name] = product_info

        # Add products from the other inventory, avoid duplicates
        for product_name, product_info in other.products.items():
            if product_name not in combined_inventory.products:
                combined_inventory.products[product_name] = product_info

        return combined_inventory
    


    def __radd__(self, other) -> 'myInventory':
    
        pass
    
    # If you need any other helper methods, add them here.

    
