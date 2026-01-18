# 🕸️ LinkSpider

**LinkSpider** is a high-performance, logic-based web crawler written in Python. Unlike traditional crawlers that rely on heavy libraries, LinkSpider uses a custom **"Stopper-Logic"** algorithm to extract and fragment URLs directly from raw HTML.

## Why LinkSpider?

Most crawlers use libraries like BeautifulSoup which can be slow and memory-intensive. LinkSpider is built for speed and precision using:
- **Recursive Path Fragmentation:** Breaks URLs into sub-paths (Domain -> Path -> Query) to ensure no hidden directory is missed.
- ** Stopper-Logic Extraction:** A custom algorithm that identifies URL boundaries using multi-delimiter detection (`>`, `"`, `'`, `\`, `&`, and spaces).
- **Zero-Dependency Extraction:** The core search engine uses zero external libraries.

## 🚀 Features
- **Smart Memory:** Uses `set()` based visited-link tracking to prevent infinite loops.
- **Path Deep-Dive:** Automatically generates and crawls sub-directories of discovered links.
- **Robust Error Handling:** Built-in timeout and connection error management to keep the spider crawling.

## 🛠️ How it Works

1. **LinkSearcher:** Scans raw HTML for `https://` patterns and determines the exact end of the URL using the nearest "stopper" character.
2. **UrlPBPaths:** Deconstructs found URLs into multiple crawlable stages (Base, Path, Parameters).
3. **SpiderCrawl:** Orchestrates the queue and manages the depth of the crawl.

## 📦 Installation & Usage

```bash
git clone https://github.com
cd LinkSpider
python spider.py
