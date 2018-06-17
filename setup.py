import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SpoofMailer",
    version="0.0.2",
    author="Dipanker shah",
    author_email="Dipankarshah143@gmail.com",
    description="By ussing SpoofMailer you can send unlimited spoof email or make your own mailing server API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dipankershah/spoof_mailer_pro",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)