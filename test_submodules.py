# This file should use provided functionality from the submodules
# Submodule1 and
# Submodule2

class MainModule:
    name: str = "MainModule"

    def say_hello(self):
        print("Hello, I'm the " + self.name + ".")

if __name__ == "__main__":
    # Instantiate classes from different modules
    main_module = MainModule()

    # Hello from all modules
    main_module.say_hello()
