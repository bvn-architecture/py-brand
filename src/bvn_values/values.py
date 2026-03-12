company_name = "BVN"
website_url = "https://www.bvn.com.au"

abn = "46 010 724 339"
acn = "010 724 339"

social_media = {
    "instagram": "https://www.instagram.com/bvnarchitecture/",
    "linkedin": "https://au.linkedin.com/company/bvn-architecture",
}


def get_brand_colours() -> dict[str, dict]:
    """Return the BVN brand colour palette.

    Each colour is a dict with 'hex', 'rgb' (tuple), and 'cmyk' (tuple) values.
    Primary colours are listed first, followed by secondary colours.
    """
    return {
        # Primary
        "black": {"hex": "#000000", "rgb": (0, 0, 0), "cmyk": (60, 50, 50, 100)},
        "white": {"hex": "#ffffff", "rgb": (255, 255, 255), "cmyk": (0, 0, 0, 0)},
        "grey": {"hex": "#b3b3b3", "rgb": (179, 179, 179), "cmyk": (0, 0, 0, 30)},
        "light-blue": {"hex": "#3fdadf", "rgb": (63, 218, 223), "cmyk": (72, 2, 0, 13)},
        "purple": {"hex": "#6d67bd", "rgb": (109, 103, 189), "cmyk": (42, 46, 0, 26)},
        "light-green": {"hex": "#e0f532", "rgb": (224, 245, 50), "cmyk": (9, 0, 80, 4)},
        # Secondary
        "light-orange": {"hex": "#ffa600", "rgb": (255, 166, 0), "cmyk": (0, 35, 100, 0)},
        "red": {"hex": "#96131b", "rgb": (150, 19, 27), "cmyk": (0, 87, 82, 41)},
        "dark-blue": {"hex": "#13519c", "rgb": (19, 81, 156), "cmyk": (88, 48, 0, 39)},
        "medium-green": {"hex": "#99ef4c", "rgb": (153, 239, 76), "cmyk": (36, 0, 68, 6)},
        "orange": {"hex": "#ed5933", "rgb": (237, 89, 51), "cmyk": (0, 62, 78, 7)},
        "light-yellow": {"hex": "#f7fccc", "rgb": (247, 252, 204), "cmyk": (2, 0, 19, 1)},
        "blue": {"hex": "#0093ee", "rgb": (0, 147, 238), "cmyk": (100, 38, 0, 7)},
        "sea-green": {"hex": "#bfe9d0", "rgb": (191, 233, 208), "cmyk": (18, 0, 11, 9)},
        "yellow": {"hex": "#fcdb00", "rgb": (252, 219, 0), "cmyk": (0, 13, 100, 1)},
    }
