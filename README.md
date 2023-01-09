# ogarantia-streamlit-card

Streamlit Component for a UI card - Adapted for Ogarantia applications.

Authors: [Wilder Lopes](https://github.com/wilderlopes) (wilder@ogarantia.com)
Based on the work by [@gamcoh](https://github.com/gamcoh) @Pernod Ricard

## Installation

### From pip

Install `ogarantia-streamlit-card` with pip
```bash
pip install ogarantia-streamlit-card
```

### From source

1. Build the react frontend

Go inside the frontend folder:

```
cd ogarantia_streamlit_card/frontend
```

Install npm packages (if you run into problems, just delete `package-lock.json`
and run the install command again):

```
npm install
```

Build the frontend:

```
npm run build
```

2. Build the python wheel

Go back to the project root and run (you might need to `pip install build` first):

```
python -m build .
```

This generates the folder `dist` that contains the python wheel. Finally,

```
pip install dist/*.whl
```

## Usage

Import the `card` function from `ogarantia-streamlit_card`
```py
from ogarantia_streamlit_card import card

hasClicked = card(
  title="Hello World!",
  text="Some description",
  image="https://get.ogre.run/images/ogarantia_logoBlue.png",
  url="https://github.com/Ogarantia/st-card"
)
```

## Push to PyPi
