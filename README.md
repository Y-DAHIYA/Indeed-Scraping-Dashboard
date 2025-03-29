## Project Overview
This project involves scraping job postings from **Indeed** using **BeautifulSoup** and **Requests**, leveraging an API for proxy management to avoid blocks. The scraped data is then stored in **SQL**, cleaned using **Python**, and visualized in **Power BI**.

## Tools & Technologies Used
- **Python** (BeautifulSoup, Requests, Pandas)
- **Proxy API** (For bypassing restrictions)
- **SQL** (Storing and managing job data)
- **Power BI** (Visualization and dashboard creation)

## Data Collected
The following fields are extracted:
- **Job Title**
- **Job URL**
- **Company Name**
- **Country** (Only India)

## Data Cleaning Process
1. Removed duplicate job postings.
2. Handled missing values in salary and rating columns (set to 'Not Disclosed' and 'Not Rated').
3. Standardized company names for consistency.
4. Removed extra spaces and special characters.

## Power BI Dashboard
### **Cards (KPIs):**
- **Total Job Postings** → Total number of jobs scraped.
- **Top Job Titles** → Count of distinct job titles.
- **Top Hiring Company** → The company with the most job postings.
- **Unique Companies Hiring** → Number of distinct companies posting jobs.

### **Charts:**
1. **Bar Chart** → Count of companies by job title.
2. **Pie Chart** → Distribution of job postings by company.
3. **Table** → Job title, company, and job URL.

### **Slicers:**
- **Company Name** → Filter job postings by company.
- **Job Title** → Filter data based on job roles.

### **Design Elements:**
- **Background Color:** Soft Blue

## Challenges Faced & Solutions
1. **IP Blocks & Captchas:**
   - Used a proxy API to prevent blocking.
2. **Incomplete Data:**
   - Salary and rating fields were often missing, so default values were assigned.
3. **Data Cleaning Issues:**
   - Standardized company names and job titles to avoid duplication.
4. **Visualization Clarity:**
   - Used slicers and filters for better insights.

## How to Run the Project
1. Install required Python libraries:
   ```bash
   pip install beautifulsoup4 requests pandas
   ```
2. Run the scraper script to collect data.
3. Store the scraped data in SQL.
4. Clean the data using Python.
5. Import cleaned data into Power BI and build visualizations.

## Dashboard Screenshot
![Image](https://github.com/user-attachments/assets/8e1c9fe9-ff71-42fd-b4aa-74926ae5939e)

## Contributor:
**YASH**

---
This project provides insights into job market trends by analyzing hiring patterns on Indeed. 🚀

