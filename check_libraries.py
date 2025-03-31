import importlib
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

def check_library(package_name, import_name=None):
    """Check if a package is installed; if not, log an error."""
    # Use a fallback for scikit-learn to use the proper import name "sklearn"
    module_name = import_name if import_name else package_name
    try:
        mod = importlib.import_module(module_name)
        version = getattr(mod, '__version__', 'unknown')
        logger.info(f"[INSTALLED] {package_name} is installed (version: {version})")
    except ImportError:
        logger.error(f"[MISSING] {package_name} is NOT installed: No module named '{module_name}'")

if __name__ == "__main__":
    logger.info("Starting library check...")

    # Check libraries: For scikit-learn, specify "sklearn" as the import name.
    libraries = [
        ("numpy", None),
        ("pandas", None),
        ("matplotlib", None),
        ("scikit-learn", "sklearn"),  # Use "sklearn" for import
        ("torch", None),
        ("xgboost", None),
        ("transformers", None),
        ("huggingface_hub", None),
        ("sentencepiece", None),
        ("beautifulsoup4", "bs4"),
        ("requests", None),
        ("flask", None),
        ("fastapi", None),
        ("uvicorn", None),
        ("streamlit", None),
        ("openai", None),
        ("tweepy", None),
        ("langchain", None),
        ("plotly", None),
        ("statsmodels", None),
        ("pulp", None),
        ("nltk", None),
        ("vaderSentiment", None),
        ("regex", None),
        ("tqdm", None),
    ]

    for package, import_name in libraries:
        check_library(package, import_name)

    logger.info("Library check complete.")
