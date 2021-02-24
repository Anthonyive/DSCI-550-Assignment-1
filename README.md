# DSCI-550-Assignment-1

![GitHub watchers](https://img.shields.io/github/watchers/Anthonyive/DSCI-550-Assignment-1?style=social)
![GitHub Repo stars](https://img.shields.io/github/stars/Anthonyive/DSCI-550-Assignment-1?style=social)
![GitHub forks](https://img.shields.io/github/forks/Anthonyive/DSCI-550-Assignment-1?style=social)

![last commit](https://img.shields.io/github/last-commit/Anthonyive/DSCI-550-Assignment-1?style=flat-square)
![commit activity](https://img.shields.io/github/commit-activity/m/Anthonyive/DSCI-550-Assignment-1?style=flat-square)
![code size](https://img.shields.io/github/languages/code-size/Anthonyive/DSCI-550-Assignment-1?style=flat-square)
![repo size](https://img.shields.io/github/repo-size/Anthonyive/DSCI-550-Assignment-1?style=flat-square)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=flat-square)](https://www.python.org/)
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=flat-square&logo=Jupyter)](https://jupyter.org/try)

![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/Anthonyive/DSCI-550-Assignment-1?style=flat-square)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/Anthonyive/DSCI-550-Assignment-1/tensorflow?style=flat-square)

^ Badges will be available once the repo changes to public.

This is the assignment 1 from DSCI 550 Spring 2021 at USC Viterbi School of Engineering. This repo is collaborated by a group of six.

Team members: Zixi Jiang, Peizhen Li, Xiaoyu Wang, Xiuwen Zhang, Yuchen Zhang, Nat Zheng

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
