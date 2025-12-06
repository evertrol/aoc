def test_version():
    """Verify that setuptools-scm did a proper job generating the version information"""

    from aoc import version

    for attr in ["version", "version_tuple", "__version__", "__semantic_version__"]:
        assert hasattr(version, attr)
