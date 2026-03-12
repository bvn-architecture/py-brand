studios = {
    "brisbane": {
        "name": "Brisbane",
        "address": {
            "building": "The Annex",
            "level": "Level 3",
            "street": "12 Creek Street",
            "city": "Brisbane",
            "state": "QLD",
            "postcode": "4000",
            "country": "Australia",
        },
        "phone": "+61 7 3852 2525",
        "email": "brisbane@bvn.com.au",
        "timezone": "Australia/Brisbane",
        "coordinates": {"latitude": -27.4679, "longitude": 153.0258},
    },
    "sydney": {
        "name": "Sydney",
        "address": {
            "level": "Level 11",
            "street": "255 Pitt Street",
            "city": "Sydney",
            "state": "NSW",
            "postcode": "2000",
            "country": "Australia",
        },
        "phone": "+61 2 8297 7200",
        "email": "sydney@bvn.com.au",
        "timezone": "Australia/Sydney",
        "coordinates": {"latitude": -33.8718, "longitude": 151.2085},
    },
    "london": {
        "name": "London",
        "address": {
            "building": "White Collar Factory",
            "street": "1 Old Street Yard",
            "city": "London",
            "postcode": "EC1Y 8AF",
            "country": "United Kingdom",
        },
        "phone": "+44 20 4570 4086",
        "email": "london@bvn.com.au",
        "timezone": "Europe/London",
        "coordinates": {"latitude": 51.5255, "longitude": -0.0873},
    },
    "new_york": {
        "name": "New York",
        "address": {
            "building": "Neuehouse",
            "street": "110 E 25th Street",
            "city": "New York",
            "state": "NY",
            "postcode": "10010",
            "country": "United States",
        },
        "phone": "+1 (347) 622 7345",
        "email": "newyork@bvn.com.au",
        "timezone": "America/New_York",
        "coordinates": {"latitude": 40.7411, "longitude": -73.9876},
    },
}


def get_studio_html(studio_key: str) -> str:
    """Return an HTML <address> snippet for the given studio.

    Args:
        studio_key: Key from the studios dict (e.g. "sydney", "london").

    Raises:
        KeyError: If studio_key is not found in studios.
    """
    studio = studios[studio_key]
    addr = studio["address"]

    lines = []
    if "building" in addr:
        lines.append(addr["building"])
    if "level" in addr:
        lines.append(addr["level"])
    lines.append(addr["street"])

    city_parts = [addr["city"]]
    if "state" in addr:
        city_parts.append(addr["state"])
    city_parts.append(addr["postcode"])
    lines.append(" ".join(city_parts))

    lines.append(addr["country"])

    address_body = "<br>\n  ".join(lines)
    phone = studio["phone"]
    email = studio["email"]
    phone_digits = "".join(c for c in phone if c in "+0123456789")

    return (
        f'<address>\n'
        f'  <strong>BVN {studio["name"]}</strong><br>\n'
        f'  {address_body}<br>\n'
        f'  <a href="tel:{phone_digits}">{phone}</a><br>\n'
        f'  <a href="mailto:{email}">{email}</a>\n'
        f'</address>'
    )
