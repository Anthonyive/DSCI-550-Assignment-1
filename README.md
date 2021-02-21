# DSCI-550-Assignment-1

This is the assignment 1 from DSCI 550 Spring 2021 at USC Viterbi School of Engineering. This repo is collaborated by a group of six.

Team members: Zixi Jiang, Peizhen Li, Xiaoyu Wang, Xiuwen Zhang, Yuchen Zhang, Nat Zheng

### Tasks

1. Download and install Apache Tika
   1. Chapter 2 in your book covers some of the basics of building the code, and additionally, see http://tika.apache.org/1.25/gettingstarted.html
   2. Install Tika-Python, you can pip install tika to get started.
      1. Read up on Tika Python here: http://github.com/chrismattmann/tika-python
2. Download and install D3.js
   1. Visit http://d3js.org/
   2. Review Mike Bostock’s Visual Gallery Wiki
      1. https://github.com/mbostock/d3/wiki/Tutorials
3. Download the Fraudulent emails dataset from Kaggle
   1. https://www.kaggle.com/rtatman/fraudulent-email-corpus
   2. Make a copy of the original dataset (because you are going to modify/add to it in this assignment)
4. Begin by converting the original dataset format into JSON
   1. Use Tika
   2. After converting the email dataset into JSON, ensure that each email is a separate JSON that will ensure easy processing and aggregation later
5. Add and expand the dataset with the following features
   1. Attack Type (aka “Ask”) – may contain more than one
      1. Reconnaissance
      2. Social Engineering
      3. Malware
      4. Credential Phishing
   2. Attacker Stylometrics
      1. Attacker title (e.g., Prince, Colonel, Nonprofit worker)
      2. Urgency of the attack email (word strength, “urgent”, “now”)
      3. Date/time of the email attack
      4. Attacker offering (Money? Services?)
      5. Attacker location
         1. Resolve the location using the geoNames.txt dataset and compare the location referenced of the attacker either in the text, or via the Attacker’s IP
         2. Add relevant geoNames.txt features including information about the locality
      6. Attacker relationship (how do they claim to know the victim, 1) met online? 2) friend of a friend?, 3) met the victim in person before)
      7. Attacker email sentiment
         1. You will use the USC Data Science Sentiment analyzer capability to perform this, see here: https://github.com/USCDataScience/SentimentAnalysisParser
      8. Attacker language style
         1. Many misspellings (test different thresholds)
         2. Random capitalization (test different thresholds)
      9. Attacker estimated age
         1. You will use the USC Data Science AgePredictor, here: https://github.com/USCDataScience/AgePredictor
      10. Attacker IP known as Phisher?
          1. See: ​https://scamalytics.com/ip as an example of how to look this up
6. Identify at least three other datasets, each of different top level MIME type (can’t all be e.g., text/*)
   1. Check out places including: https://catalog.data.gov/dataset (Data.gov)
   2. For each dataset, develop a Python program to join the data to your new Fraudulent Emails dataset
      1. For each non text/* dataset, be prepared to describe how you featurized the dataset
   3. Each dataset that you join must contribute at least three features (in addition to the features you are adding described in part 5)
   4. For each feature you add, be prepared to discuss what types of queries it will allow you to answer and also how you computed the feature
7. Download and install Tika-Similarity
   1. Read the documentation
   2. You can find Tika Similarity here (http://github.com/chrismattmann/tika-similarity)
   3. Compare Jaccard similarity, edit-distance, and cosine similarity
      1. Compare and contrast clusters from Jaccard, Cosine Distance, and Edit Similarity – do you see any differences? Why?
   4. How do the resultant clusters generated highlight the features you extracted? Be prepared to identify this in your report
8. Package your data up by combining all of your new JSONs with additional features into a single TSV (tab separated values) file where the columns represent the features and the rows are the instances of email attack.
9. (**EXTRA CREDIT**) Add some new D3.js visualizations to Tika Similarity
   1. Currently Tika Similarity only supports Dendrogram, Circle Packing, and combinations of those to view clusters, and relative similarities between datasets
   2. Consider adding
      1. Feature related visualizations, e.g., time series, bar charts, plots
      2. Add functionality in a generic way that is not specific to your dataset
      3. See gallery here: https://github.com/d3/d3/wiki/Gallery
      4. Contributions will be reviewed as Pull Requests in a first come, first serve basis (check existing PRs and make sure you aren’t duplicating what some other group has done)

### Notes

1. Python virtual environment has been set up using `pipenv`. You need `pipenv` installed ([learn more](https://pipenv-fork.readthedocs.io/en/latest/)). Then run:

   ```bash
   pipenv install
   ```

   `pipenv` will install all python packages in the virtual environment. In the future, use

   ```bash
   pipenv install <wanted-package>
   ```

   to install a python package and it will keep track of what packages used in our project.

2. To run Apache Tika with GUI:

   ```bash
   java -jar tika-app-2.0.0-ALPHA.jar
   ```

   To run Apache Tika without GUI (neccessary for large data):

   ```bash
   java -jar tika-app-2.0.0-ALPHA.jar -J <file-name>
   ```

3. `fradulent_emails.txt` has been converted to read-only. To modify the data, run this command in the data directory:

   ```bash
   new_file_name="<your-new-file-name>" bash -c 'cp fradulent_emails.txt ${new_file_name}; chmod 0644 ${new_file_name}'
   ```

   The command will make a copy of the data that can be read and written.
   
4. Convert tika output to json:

   ```bash
   java -jar tika-app-2.0.0-ALPHA.jar -J -t -r data/fradulent_emails.txt >
   data/fradulent_emails_t.json
   ```

   Explanation ([learn more](http://tika.apache.org/1.25/gettingstarted.html)): 

   - `-J` is recursive JSON.
     - [doc] -J  or --jsonRecursive Output metadata and content from all embedded files (choose content type with -x, -h, -t or -m; default is -x)
   - `-t` is output plain text content.
     - [doc]  -t  or --text          Output plain text content
   - `-r` is pretty print.

