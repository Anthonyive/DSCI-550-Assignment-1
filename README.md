# DSCI-550-Assignment-1

This is the assignment 1 from DSCI 550 Spring 2021 at USC Viterbi School of Engineering. This repo is collaborated by a group of six.

Team members: Zixi Jiang, Peizhen Li, Xiaoyu Wang, Yuchen Zhang



### Notes

1. To run Apache Tika with GUI:

   ```bash
   java -jar tika-app-2.0.0-ALPHA.jar
   ```

   To run Apache Tika without GUI (neccessary for large data):

   ```bash
   java -jar tika-app-2.0.0-ALPHA.jar -J <file-name>
   ```

2. `fradulent_emails.txt` has been converted to read-only. To modify the data, run this command in the data directory:

   ```bash
   new_file_name="<your-new-file-name>" bash -c 'cp fradulent_emails.txt ${new_file_name}; chmod 0644 ${new_file_name}'
   ```

   The command will make a copy of the data that can be read and written.