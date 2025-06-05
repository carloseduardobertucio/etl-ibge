

A simple Python project that extracts data about Brazilian states and cities from IBGE's API.

## What it does

- Extracts data about all Brazilian states
- Extracts data about all cities in each state
- Saves the data in CSV format

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## How to use

Run the extraction script:
```bash
python src/extract.py
```

The data will be saved in the `data/raw` directory.

## Data Source

This project uses data from IBGE's API:
- States: https://servicodados.ibge.gov.br/api/v1/localidades/estados
- Cities: https://servicodados.ibge.gov.br/api/v1/localidades/estados/{id}/municipios 
