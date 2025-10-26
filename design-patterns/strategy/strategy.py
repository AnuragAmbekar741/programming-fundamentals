from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    """
    Abstract base class that defines the interface for all payment strategies
    Each strategy will have pay() method
    """
    @abstractmethod
    def pay(self,amount:float)->bool:
        pass

class CreditCardPayment(PaymentStrategy):

    def __init__(self,card_number:str,cvv:str) -> None:
        self.card_number = card_number
        self.cvv = cvv

    def pay(self,amount:float)->bool:
        print(f"\n Processing Credit Card Payment")
        print(f" Amount: ${amount:.2f}")
        print(f" Card: ****{self.card_number[-4:]}")
        print(f" Validating card details...")
        print(f" Charging card...")
        print(f" Payment successful!")
        return True

class DebitCardPayment(PaymentStrategy):
    """Concrete strategy for Debit card payments"""
    def __init__(self,card_number,cvv) -> None:
        self.card_number = card_number
        self.cvv = cvv

    def pay(self,amount:float)->bool:
        print(f"\n Processing Credit Card Payment")
        print(f" Amount: ${amount:.2f}")
        print(f" Card: ****{self.card_number[-4:]}")
        print(f" Validating card details...")
        print(f" Charging card...")
        print(f" Payment successful!")
        return True

class PayPalPayment(PaymentStrategy):
    """Concrete strategy for PayPal payments"""

    def __init__(self, email: str):
        self.email = email
    
    def pay(self, amount: float) -> bool:
        print(f"\nProcessing PayPal Payment")
        print(f"Amount: ${amount:.2f}")
        print(f"Account: {self.email}")
        print(f"Redirecting to PayPal...")
        print(f"Authenticating...")
        print(f"Confirming payment...")
        print(f"Payment successful!")
        return True


class CryptoPayment(PaymentStrategy):
    """Concrete strategy for cryptocurrency payments"""

    def __init__(self, wallet_address: str, crypto_type: str = "Bitcoin"):
        self.wallet_address = wallet_address
        self.crypto_type = crypto_type

    def pay(self, amount: float) -> bool:
        print(f"\nProcessing {self.crypto_type} Payment")
        print(f"Amount: ${amount:.2f}")
        print(f"Wallet: {self.wallet_address[:8]}...{self.wallet_address[-8:]}")
        print(f"Connecting to blockchain...")
        print(f"Creating transaction...")
        print(f"Waiting for confirmation...")
        print(f"Payment successful!")
        return True

class ShoppingCart:
    """
    Context class yo use payment strategy
    """

    def __init__(self):
        self.items = []
        self.payment_strategy = None

    def add_item(self,item:str,price:float):
        """Add an item to the cart"""
        self.items.append({"item":item,"price":price})
        print(f"✓ Added {item} (${price:.2f}) to cart")

    def get_total(self):
        return sum( item["price"] for item in self.items)

    def set_payment_strategy(self,strategy:PaymentStrategy):
        self.payment_strategy = strategy
        print(f"\n💡 Payment method set: {strategy.__class__.__name__}")

    def checkout(self):
        """Process the payment using the selected strategy"""
        if not self.payment_strategy:
            print("❌ Error: Please select a payment method!")
            return False
        
        total = self.get_total()
        print(f"\n🛒 Cart Total: ${total:.2f}")
        print(f"   Items: {len(self.items)}")
        
        # Delegate to the strategy
        return self.payment_strategy.pay(total)


# ================== DEMO / CLIENT CODE ==================
def demonstrate_strategy_pattern():
    """
    Demonstrates how the Strategy Pattern works in practice.
    """
    
    print("=" * 60)
    print("STRATEGY PATTERN DEMO: E-Commerce Payment System")
    print("=" * 60)
    
    # Create a shopping cart
    cart = ShoppingCart()
    
    # Add some items
    print("\n📦 Adding items to cart...")
    cart.add_item("Laptop", 999.99)
    cart.add_item("Mouse", 29.99)
    cart.add_item("Keyboard", 79.99)
    
    # ===== Scenario 1: Pay with Credit Card =====
    print("\n" + "=" * 60)
    print("SCENARIO 1: Customer chooses Credit Card")
    print("=" * 60)
    
    credit_card = CreditCardPayment("1234567812345678", "123")
    cart.set_payment_strategy(credit_card)
    cart.checkout()
    
    # ===== Scenario 2: Customer changes mind, pays with PayPal =====
    print("\n" + "=" * 60)
    print("SCENARIO 2: Customer switches to PayPal")
    print("=" * 60)
    
    paypal = PayPalPayment("customer@email.com")
    cart.set_payment_strategy(paypal)  # Easy to change strategy!
    cart.checkout()
    
    # ===== Scenario 3: Another customer uses Crypto =====
    print("\n" + "=" * 60)
    print("SCENARIO 3: New customer uses Cryptocurrency")
    print("=" * 60)
    
    cart2 = ShoppingCart()
    cart2.add_item("Gaming Chair", 299.99)
    
    crypto = CryptoPayment("1A2B3C4D5E6F7G8H9I0J", "Bitcoin")
    cart2.set_payment_strategy(crypto)
    cart2.checkout()
    
    print("\n" + "=" * 60)
    print("✅ DEMO COMPLETE")
    print("=" * 60)
    print("\nKey Takeaways:")
    print("1. Each payment method is a separate, interchangeable strategy")
    print("2. The cart doesn't need to know HOW each payment works")
    print("3. We can add new payment methods without changing existing code")
    print("4. Strategies can be switched at runtime")
    print("=" * 65)


if __name__ == "__main__":
    demonstrate_strategy_pattern()

