import pytest
from AES import encrypt

@pytest.mark.parametrize("size", [10, 100, 1000, 10000, 100000, 1000000])
def test_encrypt_benchmark(benchmark, size):
    key = "This is a key123"
    text = "a" * size

    # Benchmark the encrypt function
    result = benchmark(encrypt, key, text)

    # Optionally, you can add assertions to verify the result
    assert isinstance(result, str)
    assert len(result) > 0