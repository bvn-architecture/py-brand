from .values import get_bvn_brand_colours, company_name


def say_hi():
    print(
        f"""
        ______     ___   _ 
        | __ ) \   / / \ | |
        |  _ \\ \ / /|  \| |
        | |_) |\ V / | |\  |
        |____/  \_/  |_| \_|
                        
       Brand colours, for {company_name}, for now.
    """
    )
    for name, hex in get_bvn_brand_colours().items():
        print(f"{name}: {hex}")


if __name__ == "__main__":
    say_hi()
