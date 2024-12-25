# Bot-to-Scrape-Scholarships-from-wemakescholars.com

This repository contains two Python scripts designed to scrape data from the **WeMakeScholars** platform. The scripts utilize Selenium to automate data extraction, allowing users to efficiently gather scholarship-related information and their respective links. Below is the detailed documentation.

---

## Features

### 1. **WeMakeScholarsLinks.py**
   - Scrapes scholarship links for specific countries.
   - Handles pagination and dynamic loading using Selenium.
   - Saves the extracted links into country-specific CSV files.

### 2. **WeMakeScholarsDATA.py**
   - Extracts detailed scholarship information for provided links.
   - Captures data such as:
     - Scholarship Title
     - Degree Type
     - Funding Type and Value
     - Scholarship Provider
     - Application Deadline
     - Eligible Courses
     - Eligible Nationalities
     - Institutions where the scholarship applies
     - Description and Eligibility Criteria
     - Scholarship Logo and Application URL
   - Saves data in structured CSV files categorized by degree type.

---

## Prerequisites

### Libraries and Dependencies
Install the required Python libraries using pip:
```bash
pip install selenium pandas
```

### Additional Requirements
- ChromeDriver: Ensure the compatible ChromeDriver version is installed.
- Pickled Cookies File: A `cookies.pkl` file containing pre-saved cookies for authentication with **WeMakeScholars**.

---

## Usage

### Step 1: Scraping Links
1. Open the `WeMakeScholarsLinks.py` script.
2. Update the `links` dictionary with countries and their respective WeMakeScholars URLs.
3. Run the script:
   ```bash
   python WeMakeScholarsLinks.py
   ```
4. Extracted links will be saved as CSV files in the specified directory.

### Step 2: Scraping Scholarship Data
1. Open the `WeMakeScholarsDATA.py` script.
2. Input the country and continent when prompted.
3. Ensure the folder paths for link and data files match your setup.
4. Run the script:
   ```bash
   python WeMakeScholarsDATA.py
   ```
5. The script processes each link, scraping detailed scholarship data and saving it to categorized CSV files.

---

## File Outputs

### Links Script (`WeMakeScholarsLinks.py`)
- Country-specific CSV files containing scholarship links:
  - Example: `aus.csv`

### Data Script (`WeMakeScholarsDATA.py`)
- CSV files categorized by degree type:
  - Example: `UK(Bachelors).csv`, `UK(Masters).csv`

---

## Code Highlights

### Handling Dynamic Pages
- **Pagination**: Automated through a "Show More" button click (`show_more()` method).
- **Scrolling**: Ensures all content is loaded by simulating page-down actions.

### Data Storage
- Each scraped dataset is appended to a CSV file. Headers are dynamically added if the file does not exist.

### Error Handling
- All data extraction methods have exception handling to manage missing elements gracefully.

---

## Limitations
- Scripts rely on the structure of **WeMakeScholars** web pages. Changes to the website may require updates.
- A valid `cookies.pkl` file is mandatory for successful execution.

---

## Conclusion
This project provides a streamlined solution to extract valuable scholarship data from **WeMakeScholars**. It leverages automation to minimize manual effort and maximize data accuracy. By running the scripts sequentially, users can build a comprehensive database of scholarship opportunities.

Feel free to extend or modify the scripts to fit additional use cases or target different regions.

--- 
