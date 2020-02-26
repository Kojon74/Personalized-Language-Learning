# Personalized-Language-Learning

Enter any URL and create a customized Quizlet with translations of words from the URL to a language of your choice to help you learn a new language!

How to use translate section:

https://www.youtube.com/watch?v=EdNWgZ4cOWo

1.  Install Google Cloud SDK file and make sure its added to PATH. You can check by entering in command line:
  
      echo $PATH
    
    Now you should be able to run in terminal:

      gcloud init
      
      gcloud auth login
      
2.  In command line run:

      pip install --upgrade google-cloud-translate
      
3.  In command line run:

      export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/json/file"
      
      Example:
      
      export GOOGLE_APPLICATION_CREDENTIALS="/home/kenjohnson/Documants/Work/TranslationAPI/Google.json"
      
4.  Then run!

      python3 <filename>
