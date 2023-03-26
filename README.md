# Brand Generator

## Project structure

- model_training.ipynb - Google Colab Notebook for model training
- generate_brand.py - script to generate brands using a trained model to csv file
- latin_model/ and pokemon_model/ - trained models

## Installation to python virtual environment

```
pip install -r requirements.txt
```

## Basic usage

Generating 50 brands and save to csv file:

```
from generate_brand import generate_brand_name, save_csv

csv_brands = generate_brand_name(50)
save_csv(csv_brands, 'result.csv')
```