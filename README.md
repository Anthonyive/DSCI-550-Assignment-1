# DSCI-550-Assignment-1

![GitHub watchers](https://img.shields.io/github/watchers/Anthonyive/DSCI-550-Assignment-1?style=social)![GitHub Repo stars](https://img.shields.io/github/stars/Anthonyive/DSCI-550-Assignment-1?style=social) ![GitHub forks](https://img.shields.io/github/forks/Anthonyive/DSCI-550-Assignment-1?style=social)

[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=flat-square&logo=Jupyter)](https://jupyter.org/try) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=flat-square)](https://www.python.org/)

![commit activity](https://img.shields.io/github/commit-activity/m/Anthonyive/DSCI-550-Assignment-1?style=flat-square) ![repo size](https://img.shields.io/github/repo-size/Anthonyive/DSCI-550-Assignment-1?style=flat-square)

^ Badges will be available once the repo changes to public.

![title-img](https://www.yeahhub.com/wp-content/uploads/2018/08/phishing-report.png)

## Prerequisite

1. Python virtual environment has been set up using `pipenv`. You need `pipenv` installed ([learn more about installation and usage](https://pipenv-fork.readthedocs.io/en/latest/)).
2. Even though we have converted the data into json files using Tika, you ßmay want to do it yourself. To learn more, check out the notes we have written below and its [documentations.](http://tika.apache.org/1.25/gettingstarted.html)
3. There are several other packages/tools you may want to use along the way. You should check out the [instruction about this assignment](docs/DSCI550_Spring2021_HW_BIGDATA_PHISHING.pdf)

## Build Instructions

0. First of foremost, build up the `pipenv` environment by running `pipenv install` command in this working directory. We are using Jupyter notebooks for all of our coding, so you may want to install the ipykernel as well. To do so:

   ```bash
   $ pipenv shell # this take you to the virtual environment
   $ python -m ipykernel install --user --name=<my-virtualenv-name> # change the kernel name as you see fit
   $ jupyter lab # run a jupyterlab instance on your localhost
   ```

1. **[Task 4]** Download [fraudulent emails datasets](https://www.kaggle.com/rtatman/fraudulent-email-corpus) from Kaggle and put it into the [data](data) directory.

   Convert tika output to json:

   ```bash
   java -jar tika-app-2.0.0-ALPHA.jar -J -t -r data/fradulent_emails.txt >
   data/fradulent_emails_t.json
   ```

   Explanation ([learn more](http://tika.apache.org/1.25/gettingstarted.html)): 

   - `-J` is recursive JSON.
     - *[doc]* -J  or --jsonRecursive Output metadata and content from all embedded files (choose content type with -x, -h, -t or -m; default is -x)
   - `-t` is output plain text content.
     - *[doc]*  -t  or --text          Output plain text content
   - `-r` is pretty print.

   We have converted all flag options, but we mainly used `-t` option.

2. **[Task 5]** Jupyter notebooks in [Task 5](notebooks/Task5)

   Just run through each cell in the notebooks, they either generate a new feature JSON file or upload each of the features to the Firebase, where our team store the data to. As long as you are using the virtual environment kernel we mentioned in the 0 step of Build Instructions, you should have the packages you need in your virtual environment.

3. **[Task 6]** Jupyter notebooks in [Task 6](notebooks/Task6)

   Just run through each cell in the three notebooks, each notebook handles one dataset. We used firebase to store our data but we have accommodate the grader to have a local version by using json dump.

4. **[Task 7]** Export PDF files in [visualization directory](visualizations/tika-similarity). We offer circle packing and dynamic circle packing clustering visualizations.

   Also, we have saved all the `circle.json` and `cluster.json` from each similarity metrics. 

   To re-run the visualization:

   - Step 0: copy [circle-packing-for-all.py](visualizations/tika-similarity/src/circle-packing-for-all.py) to the compiled [`tika-similarity` repo](https://github.com/chrismattmann/tika-similarity.git).

   - ```bash
     $ python3 circle-packing-for-all.py --inputCSV <path-to-tika-output-csv> --cluster 2
     ```

   - The above step generates `circle.json` and `cluster.json` files.

   - ```bash
     $ python3 -m http.server 8000
     ```

   - The above step starts a localhost server at port 8000. Then open [dynamic circle packing](http://localhost:8000/dynamic-circlepacking.html) or [circle packing](http://localhost:8000/circlepacking.html) to see the visualizations.

   Sample visualizations (edit-distance, dynamic circle packing): [edit-distance-viz](visualizations/tika-similarity/dynamic-circle-packing/edit-distance.pdf)

   Sample visualizations (cosine, circle packing): [cosine-viz](visualizations/tika-similarity/circle-packing/cosine.pdf)

5. **[Task 8]** TSV generation: Jupyter notebook [here](notebooks/Task7-TikaSimilarity/TSV generation & data for tika-smilarity.ipynb)

   Output in the [data directory](data/additional-features/additional_features.tsv)

## Notes

1. Python virtual environment has been set up using `pipenv`. You need `pipenv` installed ([learn more](https://pipenv-fork.readthedocs.io/en/latest/)). Then run:

   ```bash
   pipenv install
   ```

   `pipenv` will install all python packages in the virtual environment. In the future, use

   ```bash
   pipenv install <wanted-package>
   ```

   to install a python package and it will keep track of what packages used in our project.

2. `fradulent_emails.txt` has been converted to read-only. To modify the data, run this command in the data directory:

   ```bash
   new_file_name="<your-new-file-name>" bash -c 'cp fradulent_emails.txt ${new_file_name}; chmod 0644 ${new_file_name}'
   ```

   The command will make a copy of the data that can be read and written.

## About

This is the assignment 1 from DSCI 550 Spring 2021 at USC Viterbi School of Engineering. This repo is collaborated by a group of six.

Team members: Zixi Jiang, Peizhen Li, Xiaoyu Wang, Xiuwen Zhang, Yuchen Zhang, Nat Zheng
