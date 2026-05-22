from core.models import Pvi

def main():
    pvi1 = Pvi(1500.00, 15.25)
    print("Hello world! You have a PVI at: " + pvi1.get_report())
    pass

if __name__ == "__main__":
    main()