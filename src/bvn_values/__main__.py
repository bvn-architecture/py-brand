from .values import get_brand_colours, company_name
from .studios import studios


def say_hi():
    print(
        f"""
        ______     ___   _ 
        | __ ) \\   / / \\ | |
        |  _ \\\\ \\ / /|  \\| |
        | |_) |\\ V / | |\\  |
        |____/  \\_/  |_| \\_|

       Brand colours and studios for {company_name}.
    """
    )
    print("Colours:")
    for name, colour in get_brand_colours().items():
        print(f"  {name}: {colour['hex']}")

    print("\nStudios:")
    for key, studio in studios.items():
        print(f"  {studio['name']}: {studio['phone']}")


if __name__ == "__main__":
    say_hi()
