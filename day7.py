print("配置管理器")
print("alalla")
print("test")
class ConfigManager:
    """配置管理器"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_config()
        return cls._instance
    def _init_config(self):
        self.config = {"appname": "MyApp", "theme" : "light" , "version": "1.0.0"}
        print("配置管理器初始化完成")
    def get(self, key):
        return self.config.get(key)
    def set(self, key, value):
        self.config[key] = value
        print(f"配置项 {key} 已更新为 {value}")

config_a = ConfigManager()
config_b = ConfigManager()
print(config_a is config_b)  # True

print(config_a.get("appname"))  # MyApp
print(config_a.get("theme"))  # light
config_b.set("theme", "dark")
print(config_a.get("theme"))  # dark


class Sedan:
    def __init__(self,model):
        self.model = model
    def display_info(self):
        print(f"这是一个{self.model}轿车")
class SUV:
    def __init__(self,model):
        self.model = model
    def display_info(self):
        print(f"这是一个{self.model} SUV")
class Truck:
    def __init__(self,model):
        self.model = model
    def display_info(self):
        print(f"这是一个{self.model}卡车")
class CarFactory:
    @staticmethod
    def create_car(model):
        if model == "sedan":
            return Sedan(model)
        elif model == "suv":
            return SUV(model)
        elif model == "truck":
            return Truck(model)
        else:
            print("未知的汽车类型")
car1 = CarFactory.create_car("sedan")
car1.display_info()
car2 = CarFactory.create_car("suv")
car2.display_info()
car3 = CarFactory.create_car("truck")
car3.display_info()


class Error(Exception):
  """Base class for exceptions in this module."""
  pass 
class InputError(Error):
  """Exception raised for errors in the input.
  Attributes:
    expression -- input expression in which the error occurred
    message -- explanation of the error
  """  
  def __init__(self, expression, message):
    self.expression = expression
    self.message = message 
class TransitionError(Error):
  def __init__(self, previous, next, message):
    self.previous = previous
    self.next = next
    self.message = message
  def __str__(self):
    return f"{self.previous} -> {self.next}: {self.message}"
  #raise TransitionError(32,22, "The value must be > 0")

