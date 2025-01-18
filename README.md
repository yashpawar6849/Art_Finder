# ART Finder: Automated Research and Trigger Finder

**Objective:**

The objective of ART Finder is to streamline the research phase of ad creation by automating data gathering and analysis. This tool will:

* **Identify user pain points and triggers** from multiple data sources such as Google, YouTube, Reddit, Quora, and app reviews.
* **Analyze competitor ads and strategies** to uncover high-performing hooks, CTAs, and content formats.
* **Generate actionable insights and suggestions** to help marketers craft effective, user-centric ads.

**Key Features:**

* **Comprehensive Research Automation:**
    * Scrapes data from blogs, forums, social media, and app reviews.
    * Analyzes YouTube videos and competitor ads to identify trends, pain points, and effective solutions.
* **Actionable Insights Generation:**
    * Summarizes key triggers and user problems.
    * Suggests best-performing hooks, CTAs, and solutions tailored to the topic and audience.
* **Reference Dashboard:**
    * Provides direct links to scraped YouTube videos and competitor ads for easy validation and inspiration.
    * Visualizes insights with graphs, word clouds, and sentiment analysis.
* **User-Centric Interface:**
    * Simple input fields for topics and brand guidelines.
    * Intuitive dashboard showcasing insights and recommendations at a glance.

**Technologies Used:**

* **Datastax Astra DB:** High-performance, scalable database for storing and managing the vast amounts of data collected.
* **LangFlow:** Workflow orchestration platform for building and managing complex AI pipelines.
* **Mastral AI:** Cutting-edge language models for sentiment analysis, topic extraction, and text summarization.
* **Groq:** High-performance AI inference chip for accelerating the processing of large datasets.
* **Streamlit:** Rapid prototyping and deployment framework for building interactive web applications.

**Project Structure:**

* `data_collection/`: Scripts for scraping data from various sources.
* `data_processing/`: Scripts for cleaning, transforming, and enriching the collected data.
* `model_training/`: Scripts for training and evaluating the Mastral AI models.
* `inference/`: Scripts for deploying and running the models on the Groq chip.
* `app/`: Streamlit application for user interaction and visualization.
* `config/`: Configuration files for the application and the different components.

**Getting Started:**

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
