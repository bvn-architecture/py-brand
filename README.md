# BVN Values

This is a _super_ simple package that contains the specific colours and words. 

## installation

The package is [here on pypi](https://pypi.org/project/bvn_values/) and [here on github](https://github.com/bvn-architecture/py-brand).

```pip install bvn_values```

## Things you can do with this

There are currently only two things this can do:

* `company_name` is a function that gives you the name of the company.
* `get_bvn_brand_colours` is a function that returns a dictionary of brand colours. 

That's it! (for now)


## contributing

This is being managed with [flit](https://flit.pypa.io/en/latest/index.html). 

1. make your changes
1. test them yourself. (no formal tests yet, so (⊙x⊙;) )
1. bump the version number. Given that this is a value module, just the z part of the x.y.z version number
1. run `flit publish`. You'll need to coordinate with ben to get write access to pypi though. (A problem for another day.)
