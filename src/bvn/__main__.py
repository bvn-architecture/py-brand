from colours import bvn_brand_colours


def say_hi():
    print(
        """
        ______     ___   _ 
        | __ ) \   / / \ | |
        |  _ \\ \ / /|  \| |
        | |_) |\ V / | |\  |
        |____/  \_/  |_| \_|
                        
       Brand colours, for now.
    """
    )
    for name, hex in bvn_brand_colours.items():
        print(f"{name}: {hex}")


if __name__ == "__main__":
    say_hi()
