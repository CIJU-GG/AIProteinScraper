# AIProteinScraper

AIProteinScraper is a Python-based web scraping tool designed to extract and analyze protein-related data from online sources.

## Features

- Automated web scraping of protein-related information
- Data parsing and structuring using ollama
- Easy setup with environment variables
- Uses Selenium and BeautifulSoup for data extraction

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/AIProteinScraper.git
   cd AIProteinScraper
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   - Copy the `.env` file from `sample.env` and update it with necessary credentials.

4. Ensure you have the correct version of `chromedriver` installed and configured.

## Usage

Run the main script:

```sh
python main.py
```

## File Structure

- `main.py` - Entry point of the scraper
- `scrape.py` - Handles web scraping logic
- `parse.py` - Parses and structures extracted data
- `protein.py` - Contains protein-specific data functions
- `requirements.txt` - Lists required Python libraries
- `sample.env` - Example environment variables setup

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License.

