## Springboard Capstone Project One Proposal – Amazon Fine Food Review Predictions

Introduction
======
There are a number of difficulties when predictive models are applied to human languages, such as semantic analysis, sentence breaking, word segmentation, and question answering. This field is called natural language processing (NLP) and this project will focus on one aspect of it, semantic analysis.  The dataset will be taken from https://www.kaggle.com/snap/amazon-fine-food-reviews, which is data of fine food reviews by amazon users hosted on kaggle.  The data roughly contains 500k rows of users who are providing food reviews.  The review consists of the number of stars the user gave (between one and five, with five being the highest rating), the actual text of the review, and number of people who indicated that the review was helpful/not helpful.  

Approach
======
After obtaining the Amazon Fine Food Review data, it will be cleaned after some exploratory analysis is done.  There can be some missing data or long reviews which users typed in accidentally.  These anomalies will be studied through visualizations and deleted from the main dataset as needed.  Other features may be engineered during this process if the possibility of enhancements seems feasible.  Once the data is cleaned and explored, a convolutional neural network (CNN) is fitted on the data and performance is measured.  

Client
======
A potential audience for this project is companies who utilizes ratings by users as part of the overall product ratings.   Given the same review submitted by different users, the ratings could vary widely due to different standards employed by different users.  Once the CNN is trained, it can possibly give an unbiased rating based on texts alone to potential customers of products.

Deliverables
======
The trained CNN will be a major part of the project, as well as the codebase, paper, and slidedeck. 
