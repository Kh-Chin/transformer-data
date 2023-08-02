# Job Description Generator

As a final year project for my bachelor thesis, I built a text generator using deep learning models.

The aim is to help HR departments automate their process of writing job description when hiring.

Here are the process of the project:
1) Built an web scrapper with Python to scrap job description and related job information from Linkedin.
2) Cleaned and preprocessed the scraped data, including deduplicating and text preprocessing.
3) Built a GPT-2 model with HuggingFace module.
4) Constructed the data pipeline, including the model input and output layer.
5) Fine-tuned the model with job description data.
6) Evaluated the model with some NLP metrics (BLEU, METEOR, etc).
7) Built a Django website for user to interact with the model, with some post-processing layers.

# Website design
![alt text](https://github.com/Kh-Chin/transformer-data/blob/main/README_media/website_design_1.png)

![alt text](https://github.com/Kh-Chin/transformer-data/blob/main/README_media/website_design_2.png)

![alt text](https://github.com/Kh-Chin/transformer-data/blob/main/README_media/website_design_3.png)

# Sample output
![alt text](https://github.com/Kh-Chin/transformer-data/blob/main/README_media/sample_job_description_1.png)

![alt text](https://github.com/Kh-Chin/transformer-data/blob/main/README_media/sample_job_description_2.png)