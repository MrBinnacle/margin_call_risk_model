from setuptools import setup, find_packages

setup(
    name="margin-call-sim",
    version="1.1.1",
    packages=find_packages(include=["margin_call_sim", "margin_call_sim.*"]),
    include_package_data=True,
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "streamlit",
        "pytest"
    ],
    entry_points={
        "console_scripts": [
            "margincall = margin_call_sim.cli:main"
        ]
    },
    author="MrBinnacle",
    author_email="contact@yourdomain.com",
    description="A narrative-driven financial margin risk simulator inspired by Margin Call (2011)",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MrBinnacle/margin_call_risk_model",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)

