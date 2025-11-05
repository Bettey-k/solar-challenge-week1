# Solar Data Discovery Challenge

This repository contains the code and analysis for the Solar Data Discovery Challenge, focusing on analyzing solar farm data from Benin, Sierra Leone, and Togo.

## Project Structure

```
├── .github/
│   └── workflows/         # GitHub Actions workflows
├── data/                  # Data files (ignored by git)
├── notebooks/             # Jupyter notebooks for analysis
├── scripts/               # Utility scripts
├── src/                   # Source code
├── tests/                 # Test files
├── .gitignore             # Git ignore file
├── README.md              # This file
└── requirements.txt       # Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.8+
- Git
- Virtual environment (venv or conda)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/solar-challenge-week1.git
   cd solar-challenge-week1
   ```

2. **Create and activate a virtual environment**

   **Using venv:**
   ```bash
   python -m venv .venv
   # On Windows:
   .\.venv\Scripts\activate
   # On macOS/Linux:
   # source .venv/bin/activate
   ```

   **Using conda:**
   ```bash
   conda create -n solar-env python=3.9
   conda activate solar-env
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up pre-commit hooks (optional but recommended)**
   ```bash
   pre-commit install
   ```

## Development Workflow

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them with a descriptive message:
   ```bash
   git add .
   git commit -m "feat: add new analysis for solar data"
   ```

3. Push your changes to the remote repository:
   ```bash
   git push -u origin feature/your-feature-name
   ```

4. Create a pull request on GitHub to merge your changes into the main branch.

## Running Tests

Run the test suite using pytest:

```bash
pytest tests/
```

To run tests with coverage report:

```bash
pytest --cov=src tests/
```

## Code Style

This project uses:
- Black for code formatting
- isort for import sorting
- flake8 for linting

To format and check your code:

```bash
black .
isort .
flake8
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [10 Academy](https://www.10academy.org/) for providing this challenge
- [Solar Radiation Measurement Data](https://www.renewables.ninja/) for the dataset