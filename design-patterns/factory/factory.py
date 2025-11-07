from abc import ABC, abstractmethod

# ================== PRODUCT INTERFACE ==================
class Vehicle(ABC):
    """
    Abstract base class (Product) that defines the interface
    All vehicles must implement these methods
    """
    @abstractmethod
    def start(self):
        """Start the vehicle"""
        pass
    
    @abstractmethod
    def stop(self):
        """Stop the vehicle"""
        pass
    
    @abstractmethod
    def get_info(self):
        """Get vehicle information"""
        pass


# ================== CONCRETE PRODUCTS ==================
class Car(Vehicle):
    """Concrete product: Car"""
    
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self.type = "Car"
    
    def start(self):
        print(f"🚗 {self.brand} {self.model} engine started!")
    
    def stop(self):
        print(f"🚗 {self.brand} {self.model} engine stopped.")
    
    def get_info(self):
        return f"{self.brand} {self.model} ({self.type})"


class Motorcycle(Vehicle):
    """Concrete product: Motorcycle"""
    
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self.type = "Motorcycle"
    
    def start(self):
        print(f"🏍️  {self.brand} {self.model} engine revved!")
    
    def stop(self):
        print(f"🏍️  {self.brand} {self.model} engine stopped.")
    
    def get_info(self):
        return f"{self.brand} {self.model} ({self.type})"


class Truck(Vehicle):
    """Concrete product: Truck"""
    
    def __init__(self, brand: str, model: str, capacity: str):
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.type = "Truck"
    
    def start(self):
        print(f"🚚 {self.brand} {self.model} engine started!")
        print(f"   Load capacity: {self.capacity}")
    
    def stop(self):
        print(f"🚚 {self.brand} {self.model} engine stopped.")
    
    def get_info(self):
        return f"{self.brand} {self.model} ({self.type}) - Capacity: {self.capacity}"


# ================== FACTORY CLASS ==================
class VehicleFactory:
    """
    Factory class that creates Vehicle objects
    Client code uses this factory instead of creating vehicles directly
    """
    
    @staticmethod
    def create_vehicle(vehicle_type: str, **kwargs) -> Vehicle:
        """
        Factory method that creates and returns a Vehicle object
        
        Args:
            vehicle_type: Type of vehicle ("car", "motorcycle", "truck")
            **kwargs: Additional parameters for vehicle creation
        
        Returns:
            Vehicle object (Car, Motorcycle, or Truck)
        """
        vehicle_type = vehicle_type.lower()
        
        if vehicle_type == "car":
            return Car(
                brand=kwargs.get("brand", "Generic"),
                model=kwargs.get("model", "Model")
            )
        
        elif vehicle_type == "motorcycle":
            return Motorcycle(
                brand=kwargs.get("brand", "Generic"),
                model=kwargs.get("model", "Model")
            )
        
        elif vehicle_type == "truck":
            return Truck(
                brand=kwargs.get("brand", "Generic"),
                model=kwargs.get("model", "Model"),
                capacity=kwargs.get("capacity", "5 tons")
            )
        
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")


# ================== DEMO / CLIENT CODE ==================
def demonstrate_factory_pattern():
    """
    Demonstrates how the Factory Pattern works in practice.
    """
    
    print("=" * 60)
    print("FACTORY PATTERN DEMO: Vehicle Manufacturing System")
    print("=" * 60)
    
    factory = VehicleFactory()
    
    # ===== Scenario 1: Create a Car =====
    print("\n" + "=" * 60)
    print("SCENARIO 1: Customer orders a Car")
    print("=" * 60)
    
    car = factory.create_vehicle(
        "car",
        brand="Toyota",
        model="Camry"
    )
    print(f"✅ Created: {car.get_info()}")
    car.start()
    car.stop()
    
    # ===== Scenario 2: Create a Motorcycle =====
    print("\n" + "=" * 60)
    print("SCENARIO 2: Customer orders a Motorcycle")
    print("=" * 60)
    
    motorcycle = factory.create_vehicle(
        "motorcycle",
        brand="Harley-Davidson",
        model="Sportster"
    )
    print(f"✅ Created: {motorcycle.get_info()}")
    motorcycle.start()
    motorcycle.stop()
    
    # ===== Scenario 3: Create a Truck =====
    print("\n" + "=" * 60)
    print("SCENARIO 3: Customer orders a Truck")
    print("=" * 60)
    
    truck = factory.create_vehicle(
        "truck",
        brand="Ford",
        model="F-150",
        capacity="10 tons"
    )
    print(f"✅ Created: {truck.get_info()}")
    truck.start()
    truck.stop()
    
    # ===== Scenario 4: Dynamic creation based on user input =====
    print("\n" + "=" * 60)
    print("SCENARIO 4: Dynamic Vehicle Creation")
    print("=" * 60)
    
    orders = [
        ("car", {"brand": "Honda", "model": "Civic"}),
        ("motorcycle", {"brand": "Yamaha", "model": "R1"}),
        ("truck", {"brand": "Chevrolet", "model": "Silverado", "capacity": "8 tons"})
    ]
    
    vehicles = []
    for vehicle_type, params in orders:
        vehicle = factory.create_vehicle(vehicle_type, **params)
        vehicles.append(vehicle)
        print(f"✅ Created: {vehicle.get_info()}")
    
    print("\n📋 All vehicles created:")
    for vehicle in vehicles:
        print(f"   - {vehicle.get_info()}")
    
    print("\n" + "=" * 60)
    print("✅ DEMO COMPLETE")
    print("=" * 60)
    print("\nKey Takeaways:")
    print("1. Client code doesn't need to know HOW vehicles are created")
    print("2. All creation logic is centralized in the Factory")
    print("3. Easy to add new vehicle types without changing client code")
    print("4. Factory handles object creation complexity")
    print("=" * 65)