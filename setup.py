import setuptools

with open('README.md') as readme_file:
    readme = readme_file.read()


setuptools.setup(
    name="ogarantia-streamlit-card",
    version="0.0.2",
    author="Wilder Lopes",
    author_email="wilder@ogarantia.com",
    description="A streamlit component to make UI cards, adapted for Ogarantia applications from `streamlit-card` by gamcoh (cohengamliel8@gmail.com)",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Ogarantia/st-card.git",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords="card streamlit streamlit-component",
    python_requires=">=3.8",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
