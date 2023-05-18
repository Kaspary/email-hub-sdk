import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="email-hub-sdk",
    version="0.0.1",
    author="João Pedro Kaspary",
    author_email="jpkasparydev@gmail.com",
    description="Package for implement an interface to send email with different server.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kaspary/email-hub-sdk",
    project_urls={"Bug Tracker": "https://github.com/Kaspary/email-hub-sdk/issues"},
    license="UNLICENSED",
    packages=["email_hub_sdk"],
    install_requires=[],
)
