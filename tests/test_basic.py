def test_version():
    """Verify that setuptools-scm did a proper job generating the version information"""

    from aoc import version
    print(version.version)
