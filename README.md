# Similarweb Advanced Scraper

> Similarweb Advanced Scraper automates the extraction of in-depth traffic and audience data from Similarweb, empowering marketers, analysts, and researchers to gain competitive insights and make data-driven decisions.
> It streamlines website performance analysis and competitor benchmarking across multiple industries.


<p align="center">
  <a href="https://bitbash.def" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Similarweb Advanced Scraper</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

This project provides an automated solution for collecting web analytics and audience insights from Similarweb.
It’s designed for businesses and researchers looking to analyze traffic sources, user demographics, and engagement metrics across domains.

### Why It Matters

- Helps identify market trends and benchmark against competitors.
- Provides automated access to web traffic, SEO metrics, and audience data.
- Eliminates manual data collection by aggregating insights from multiple websites.
- Offers flexible export options for analytics tools and dashboards.

## Features

| Feature | Description |
|----------|-------------|
| Easy Input Configuration | Accepts website lists in text, JSON, or CSV formats for scalable analysis. |
| Data Extraction | Gathers traffic, engagement, and audience insights efficiently. |
| Comprehensive Insights | Fetches visits, sources, demographics, and SEO metrics per domain. |
| Customizable Output | Exports results in JSON, CSV, or Excel for smooth integration. |
| Scheduling and Automation | Enables automatic updates for periodic tracking. |
| Error Handling and Retry | Automatically retries failed pages without stopping execution. |
| Data Privacy | Ensures all gathered data remains secure and confidential. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|-------------|------------------|
| domain | Website domain analyzed. |
| interests | Related interests and top categories of audience. |
| competitors | List of competing domains and similarity metrics. |
| searchesSource | Organic and paid keyword metrics and shares. |
| incomingReferrals | Top referral sites and referral categories. |
| adsSource | Top advertising sites and ad network stats. |
| socialNetworksSource | Distribution of traffic from social networks. |
| technologies | Technologies used by the website. |
| recentAds | Recently active display ads with preview images. |
| overview | General overview including company info and visit summary. |
| demographics | Gender and age distribution data. |
| geography | Geographic traffic distribution by country. |
| trafficSources | Traffic breakdown across channels. |
| ranking | Global, country, and category ranks. |
| traffic | Historical visit data and metrics. |

---

## Example Output


    {
      "domain": "twitter.com",
      "overview": {
        "companyName": "Twitter",
        "visitsTotalCount": 6141624959,
        "pagesPerVisit": 10.09,
        "visitsAvgDurationFormatted": "00:10:52",
        "bounceRate": 0.319
      },
      "competitors": {
        "topSimilarityCompetitors": [
          { "domain": "instagram.com", "visitsTotalCount": 6674146453 },
          { "domain": "facebook.com", "visitsTotalCount": 16717821583 },
          { "domain": "linkedin.com", "visitsTotalCount": 1811660548 }
        ]
      },
      "demographics": {
        "ageDistribution": [
          { "minAge": 25, "maxAge": 34, "value": 0.295 },
          { "minAge": 18, "maxAge": 24, "value": 0.287 }
        ],
        "genderDistribution": { "male": 0.665, "female": 0.335 }
      },
      "geography": {
        "topCountriesTraffics": [
          { "countryAlpha2Code": "US", "visitsShare": 0.236 },
          { "countryAlpha2Code": "JP", "visitsShare": 0.159 }
        ]
      }
    }

---

## Directory Structure Tree


    similarweb-advanced-scraper/
    ├── src/
    │   ├── main.py
    │   ├── extractors/
    │   │   ├── traffic_parser.py
    │   │   ├── demographics_parser.py
    │   │   └── competitors_parser.py
    │   ├── utils/
    │   │   ├── logger.py
    │   │   └── retry_handler.py
    │   └── config/
    │       └── settings.json
    ├── data/
    │   ├── input_sample.json
    │   ├── output_example.json
    │   └── cache/
    ├── requirements.txt
    └── README.md

---

## Use Cases

- **Digital marketers** use it to compare competitor traffic and uncover new audience opportunities.
- **SEO analysts** extract keyword data to improve visibility and refine targeting strategies.
- **Market researchers** gather industry benchmarks for investment or campaign analysis.
- **Business intelligence teams** feed insights directly into dashboards for live performance tracking.
- **Investors** integrate domain performance data into predictive models for brand evaluation.

---

## FAQs

**Q: Does this scraper still work with Similarweb’s login requirement?**
A: No, Similarweb now requires login for traffic data. Please use the maintained version here: [curious_coder/similarweb-scraper](https://apify.com/curious_coder/similarweb-scraper).

**Q: How are failed URLs handled?**
A: Failed pages are automatically retried, ensuring no domain is skipped during the run.

**Q: Can I schedule recurring data collection?**
A: Yes, you can automate it with scheduling settings for daily, weekly, or monthly runs.

**Q: What formats are supported for input and output?**
A: Inputs can be provided as text, JSON, or CSV; outputs can be saved as JSON, CSV, or Excel files.

---

## Performance Benchmarks and Results

**Primary Metric:** Average scrape time per domain — ~4.8 seconds.
**Reliability Metric:** Over 98% success rate in consistent data extraction runs.
**Efficiency Metric:** Handles up to 500 domains per session without throttling.
**Quality Metric:** Provides over 90% data completeness, including demographic and traffic data.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
