from setuptools import setup, find_packages

setup(
    name="raspberry_pi_monitor",               # this is what people type in pip install
    version="1.0.0",
    author="Shreyash Narayan S",
    author_email="sshreyashnarayan@gmail.com",
    description="A simple Raspberry Pi performance monitor",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Shreyash0124/pi_monitor",  # optional
    packages=find_packages(),
    install_requires=["psutil"],
    python_requires=">=3.6",
)
