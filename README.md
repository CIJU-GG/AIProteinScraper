# AIProteinScraper

AIProteinScraper is a Python-based web scraping tool designed to extract and analyze protein-related data from online sources, with support for multiple proxy methods.

## Features

- Automated web scraping of protein-related information
- Multiple request methods: Bright Data API, Azure Proxy, Direct Requests
- Data parsing and structuring using local LLMs (Ollama)
- Interactive Streamlit UI for easy data exploration
- Uses Selenium and BeautifulSoup for data extraction

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/AIProteinScraper.git
   cd AIProteinScraper
   ```

2. Set up a virtual environment (recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   - Copy `sample.env` to `.env`
   - Update it with your credentials based on the chosen method (see Configuration section below)

5. Ensure you have the correct version of `chromedriver` installed and available in the project directory.

## Configuration

This project supports multiple methods for web scraping and inference. Choose the appropriate configuration based on your needs:

### Scraping Method 1: Bright Data API (Default)

For using the Bright Data scraping service:

1. Sign up for a [Bright Data](https://brightdata.com/) account
2. Get your Bright Data Scraping Browser webdriver URL
3. In your `.env` file, set:
   ```
   SBR_WEBDRIVER="your-brightdata-webdriver-url"
   ```

### Scraping Method 2: Azure Proxy

For using Azure Virtual Machine as proxy:

1. Set up an Azure VM with a proxy server like Squid
2. In your `.env` file, set:
   ```
   AZURE_PROXY_URL="http://your-azure-vm-ip:proxy-port"
   PROXY_USERNAME="your-proxy-username"  # If authentication is required
   PROXY_PASSWORD="your-proxy-password"  # If authentication is required
   ```

### Scraping Method 3: Direct Requests

For making direct requests without a proxy (use with caution as websites may block your IP):
- No additional configuration needed, but consider using rotating user agents

### Inference Method: Local Ollama

For local LLM inference with Ollama:

1. [Install Ollama](https://github.com/ollama/ollama) on your machine
2. Start the Ollama service:
   ```sh
   ollama serve
   ```
3. Pull the required model:
   ```sh
   ollama pull llama3
   ```

## Usage

1. Start the Streamlit application:

   ```sh
   streamlit run main.py
   ```

2. In the web interface:
   - Enter a protein name
   - Select your preferred scraping method
   - Click "Scrape Now" to start the data extraction process
   - Enter any specific parsing instructions in the text area
   - Click "Parse Content" to analyze the data

## Common Issues and Troubleshooting

### Connection Error with Ollama
If you see an error like "No connection could be made because the target machine actively refused it":
1. Ensure Ollama is running with `ollama serve`

### Proxy Connection Issues
If you encounter proxy connection problems:
1. Verify your proxy URL is correct
2. Check if your Azure VM firewall allows the connection
3. Try the direct request method as a last resort

## File Structure

- `main.py` - Entry point with Streamlit UI implementation
- `scrape.py` - Handles web scraping logic with multiple methods
- `parse.py` - Parses and structures data using local or cloud LLMs
- `protein.py` - Contains protein-specific data functions
- `requirements.txt` - Lists required Python libraries
- `sample.env` - Example environment variables setup

## Additional Features

- **Proxy Support:** The tool supports multiple proxy configurations, including Azure Proxy and Bright Data API, to bypass restrictions and ensure reliable scraping.
- **User-Agent Rotation:** Randomized user-agent headers to reduce the risk of detection.
- **Error Handling:** Comprehensive error handling for network and scraping issues.
- **Session Management:** Streamlit session state is used to manage scraped data efficiently.

## Future Enhancements

- **Unit Testing:** Add unit tests for all major functions to ensure code reliability.
- **Data Export:** Provide options to export parsed data in formats like CSV, JSON, or Excel.
- **Advanced Parsing:** Integrate more advanced parsing techniques using NLP models.
- **Cloud Deployment:** Deploy the application on cloud platforms like AWS or Azure for scalability.

## Contribution Guidelines

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with clear messages.
4. Submit a pull request for review.

For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

