# BVN Values

[![PyPI version](https://badge.fury.io/py/bvn_values.svg)](https://badge.fury.io/py/bvn_values)

A Python package containing BVN brand values: colours, studio addresses, and company information.

## Installation

The package is on [PyPI](https://pypi.org/project/bvn_values/) and [GitHub](https://github.com/bvn-architecture/py-brand).

```
pip install bvn_values
```

## Usage

### Company info

```python
from bvn_values import company_name, website_url, abn, acn, social_media

print(company_name)  # "BVN"
print(website_url)   # "https://www.bvn.com.au"
print(abn)           # "46 010 724 339"
print(acn)           # "010 724 339"
print(social_media)  # {"instagram": "...", "linkedin": "..."}
```

### Brand colours

Colours match the official palette at [brand.bvn.com.au](https://brand.bvn.com.au/), with hex, RGB, and CMYK values.

```python
from bvn_values import get_brand_colours

colours = get_brand_colours()
print(colours["purple"]["hex"])   # "#6d67bd"
print(colours["purple"]["rgb"])   # (109, 103, 189)
print(colours["purple"]["cmyk"])  # (42, 46, 0, 26)
```

### Studios

```python
from bvn_values import studios, get_studio_html

# Access studio data
sydney = studios["sydney"]
print(sydney["phone"])        # "+61 2 8297 7200"
print(sydney["email"])        # "sydney@bvn.com.au"
print(sydney["timezone"])     # "Australia/Sydney"
print(sydney["coordinates"])  # {"latitude": -33.8718, "longitude": 151.2085}

# Generate an HTML address snippet
html = get_studio_html("sydney")
print(html)
```

Available studios: `brisbane`, `sydney`, `london`, `new_york`.

## CLI

```
python -m bvn_values
```

## Contributing

1. Make your changes
1. Update the version in `src/bvn_values/__init__.py`
1. Commit and push
1. Create a git tag: `git tag v0.2.0 && git push origin v0.2.0`
1. The GitHub Action will build and publish to PyPI automatically

### First-time PyPI setup

This package uses [Trusted Publishers](https://docs.pypi.org/trusted-publishers/) for PyPI authentication (no API tokens needed).

A repository maintainer needs to configure the publisher on PyPI once:

1. Go to the [bvn_values publishing settings on PyPI](https://pypi.org/manage/project/bvn_values/settings/publishing/)
2. Add a new publisher with:
   - Owner: `bvn-architecture`
   - Repository: `py-brand`
   - Workflow: `publish.yml`
   - Environment: `pypi`
