# **Deployment**

## **Table of Contents**

* [**Deployment**](#deployment)
  * [**Table of Contents**](#table-of-contents)
  * [**Initial Deployment**](#initial-deployment)
    * [**Create repository**](#create-repository)
    * [**Setting up the Workspace** (To be done locally via the console of your chosen editor)](#setting-up-the-workspace-to-be-done-locally-via-the-console-of-your-chosen-editor)
    * [**Create Heroku App**](#create-heroku-app)
    * [**AWS S3 Bucket**](#aws-s3-bucket) 
    * [**Creating Environmental Variables Locally**](#creating-environmental-variables-locally)
    * [**Setting up setting.py File**](#setting-up-settingpy-file)
    * [Set up Heroku for use via the console](#set-up-heroku-for-use-via-the-console)
  * [Cloning on a Local machine or Via Gitpod Terminal](#cloning-on-a-local-machine-or-via-gitpod-terminal)

## **Initial Deployment**

Below are the steps I took to deploy the site to Heroku and any console commands required to initiate it.

### **Create repository**

1. Create a new repository in GitHub and clone it locally following [these instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
    * ***Note*** - If you are cloning my project, then you can skip all pip installs below and just run the following command in the terminal to install all the required libraries/packages at once:
       * ```pip install -r requirements.txt```
    * ***IMPORTANT*** -  If developing locally on your device, ensure you set up/activate the virtual environment ([see below](#setting-up-the-workspace-to-be-done-locally-via-the-console-of-your-chosen-editor)) before installing/generating the requirements.txt file; failure to do this will pollute your machine and put other projects at risk

### **Setting up the Workspace** (To be done locally via the console of your chosen editor)

1. Create a virtual environment on your machine (Can be skipped if using gitpod):
    * python -m venv .venv
1. To ensure the virtual environment is not tracked by version control, add .venv to the .gitignore file.
1. Install Django with version 4.2:
    * ```pip install django==4.2```
1. Install gunicorn:
    * ```pip install gunicorn```
1. Install supporting libraries:
    * ```pip install dj_database_url```
    * ```pip install psycopg2-binary```
1. Create requirements.txt:
    * ```pip freeze --local > requirements.txt```
1. Create an empty folder for your project in your chosen location.
1. Create a project in the above folder:
    * ```django-admin startproject <PROJECT_NAME>``` (in the case of this project, the project name was "gameshark")
1. Create an app within the project:
    * ```python manage.py startapp APP_NAME``` (in the case of this project, the app name was "gameshark")
1. Add a new app to the list of installed apps in setting.py
1. Migrate changes:
    * ```python manage.py migrate```
1. Test server works locally:
    * ```python manage.py runserver```  (You should see the default Django success page)

### **Create Heroku App**

The below works on the assumption that you already have an account with [Heroku](https://id.heroku.com/login) and are already signed in.

1. Create a new Heroku app:
    * Click "New" in the top right-hand corner of the landing page, then click "Create new app."
1. Give the app a unique name:
    * Will form part of the URL (in the case of this project, I called the Heroku app Gameshark)
1. Select the nearest location:
    * For me, eu-north-1.
1. Add Database to the Heroku app:
    * Navigate to the Resources tab of the app dashboard. Under the heading "Add ons," search for "Heroku Postgres" and click on it when it appears.
    * Select "Hobby Dev - Free" from the "plan name" drop-down menu and click "Submit Order Form."
1. From your editor, go to your projects settings.py file and copy the SECRET_KEY variable. Add this to the same name variable under the Heroku App's config vars.
    * left box under config vars (variable KEY) = SECRET_KEY
    * right box under config vars (variable VALUE) = Value copied from settings.py in project.

### **AWS S3 Bucket**

### AWS Cloud Service

GameShark uses Amazon Web Services (AWS) to store static and media files securely in the cloud, ensuring fast and reliable access for our users.

**To integrate AWS, follow steps:**

#### **1. Create and Configure an S3 Bucket**

1.  **Access AWS:**
    
    -   Go to [aws.amazon.com](https://aws.amazon.com/) and log in to your AWS Management Console.
2.  **Create an S3 Bucket:**
    
    -   Search for "S3" in the AWS Management Console and create a new bucket.
    -   Name the bucket to match your Heroku app name and select the region closest to your target audience.
3.  **Set Public Access and Ownership:**
    
    -   Uncheck the "Block all public access" option and acknowledge that the bucket will be public (required for compatibility with Heroku).
    -   Under "Object Ownership," ensure "ACLs enabled" and "Bucket owner preferred" are selected.
4.  **Enable Static Website Hosting:**
    
    -   In the "Properties" tab, enable static website hosting.
    -   Set `index.html` as the index document and `error.html` as the error document, then click "Save."
5.  **Configure CORS (Cross-Origin Resource Sharing):**
    
    -   In the "Permissions" tab, add the following CORS configuration:
    
    json
    
    Copy code
    
    `[
      {
        "AllowedHeaders": ["Authorization"],
        "AllowedMethods": ["GET"],
        "AllowedOrigins": ["*"],
        "ExposeHeaders": []
      }
    ]` 
    
    -   Copy your bucket's **ARN** (Amazon Resource Name).

6.  **Add a Bucket Policy:**
    
    -   Go to the "Bucket Policy" tab and click on the "Policy Generator" link.
    -   Configure the policy:
        -   **Policy Type:** S3 Bucket Policy
        -   **Effect:** Allow
        -   **Principal:** *
        -   **Actions:** `s3:GetObject`
        -   **ARN:** Paste your bucket's ARN
    -   Click "Add Statement" and "Generate Policy."
    -   Copy the generated policy and paste it into the "Bucket Policy Editor":
    
    json
    
    Copy code
    
    ```{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": "*",
          "Action": "s3:GetObject",
          "Resource": "arn:aws:s3:::your-bucket-name/*"
        }
      ]
    }```
    
    -   Ensure the `Resource` field ends with `/*` and click "Save."
7.  **Adjust Access Control List (ACL):**
    
    -   In the "Access Control List" (ACL) section, click "Edit" and enable "List" for Everyone (public access). Accept the warning prompt.
    -   If the edit option is disabled, ensure the "Object Ownership" settings have ACLs enabled.

#### **2. Configure IAM (Identity and Access Management):**

1.  **Create a User Group:**
    
    -   Navigate to the IAM service and select "User Groups."
    -   Click "Create New Group," and name it appropriately (e.g., `group-gameshark`).
2.  **Attach Policies to the Group:**
    
    -   Select the newly created group and go to the "Permissions" tab.
    -   Click "Add Permissions" > "Attach Policies."
    -   In the "JSON" tab, click "Import Managed Policy" and search for `AmazonS3FullAccess`.
    -   Import the policy and modify it to limit access to your specific bucket:
    
    json
    
    Copy code
    
    ```{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": "s3:*",
          "Resource": [
            "arn:aws:s3:::your-bucket-name",
            "arn:aws:s3:::your-bucket-name/*"
          ]
        }
      ]
    }```
    
    -   Click "Review Policy" and name it (e.g., `policy-gameshark`), then click "Create Policy."
3.  **Add Users and Assign Permissions:**
    
    -   Go back to "User Groups," select your group, and click "Attach Policy."
    -   Select your custom policy (e.g., `policy-gameshark`) and attach it.
    -   Click "Add User" and name it appropriately (e.g., `user-gameshark`).
    -   Select "Programmatic Access" and add the user to your group.
    -   Download the CSV file containing the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

#### **3. Final AWS Setup and Heroku Integration:**

1.  **Update Heroku Configurations:**
    
    -   Remove `DISABLE_COLLECTSTATIC` from Heroku Config Vars to enable AWS management of static files.
2.  **Create Media Directory:**
    
    -   Within your S3 bucket, create a new folder named `media`.
    -   Upload your media files into this folder and set "Public read access."
3.  **Security Reminder:**
    
    -   Ensure all sensitive information (like AWS credentials) is securely stored and not hard-coded into your source code.

----------

***Summary***

These steps integrate AWS S3 with your Heroku-hosted application, enabling efficient management of static and media files in a secure and scalable cloud environment. Proper configuration ensures that your content is readily accessible while adhering to best practices in cloud security and management.

1. Link S3 Bucket to Django Project by adding the following to the settings.py file:

    ``` python
        # its important to keep the AWS keys secret so we use environment variables which will be added to Heroku later
        # Cache control
        AWS_S3_OBJECT_PARAMETERS = {
           'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
           'CacheControl': 'max-age=94608000',
        }
        # Bucket config
        AWS_STORAGE_BUCKET_NAME = '{Bucket name}' # name of your bucket
        AWS_S3_REGION_NAME = '{Region name}' # region of your bucket
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

        # Static and media files
        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
        STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'

        # Override static and media URLs in production
        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```

1. Add allowed hosts to settings.py:
    * ``` ALLOWED_HOSTS = ["PROJECT_NAME.herokuapp.com", "localhost", "127.0.0.1"] ```

1. Create Procfile at the top level of the file structure and insert the following:
    * ``` web: gunicorn PROJECT_NAME.wsgi ```

1. Make an initial commit and push the code to the GitHub Repository.
    * ```git add .```
    * ```git commit -m "Initial deployment"```
    * ```git push```

1. Add AWS Keys from step 7 above to Heroku Config Vars.
1. Add the ```USE_AWS``` variable to Heroku Config Vars and set it to True.
1. Create a file call "Custom_storages.py" in the root of the project and add the following code:

    ```python
        # this file is used to tell Django where to store static and media files when COLLECT_STATIC is run (when deploying to heroku)
        from django.conf import settings
        from storages.backends.s3boto3 import S3Boto3Storage

        class StaticStorage(S3Boto3Storage):
            location = settings.STATICFILES_LOCATION

        class MediaStorage(S3Boto3Storage):
            location = settings.MEDIAFILES_LOCATION
    ```

### Set up Heroku for use via the console

1. Click on Account Settings (under the avatar menu)
1. Scroll down to the API Key section and click Reveal. Copy the API key.
1. Log in to Heroku via the console and enter your details.
    * heroku login-i
    * When prompted, enter your Heroku username
    * Enter copied API key as the password

1. Get your app name from Heroku
    * ```heroku apps```
1. Set Heroku remote
    * ```heroku git:remote -a <app_name>```
1. Add, Commit, Pust to GitHub:
    * ```git add . && git commit -m "Deploy to Heroku via CLI"```
1. Push to GitHub and Heroku
    * ```git push origin main```
    * ```git push heroku main```

## Cloning on a Local machine or Via Gitpod Terminal

1. Navigate to the [GitHub repository](https://github.com/dhardi/gameshark), and follow [these steps to clone the project](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) into your IDE of choice.

   * **Gitpod** only **requires** you to have the **web extension** installed and **click** the **green Gitpod button** from the repositories main page. If you are **using Gitpod**, please **skip step 2** below as you do not require a virtual environment to protect your machine.  
  
1. **Create** the **virtual environment** with the terminal command **```python3 -m venv venv```.** Once complete add the "venv" file to you're ".gitignore" file and use the terminal command **```venv\Scripts\activate.bat``` to activate it.**

   * ***IMPORTANT*** If developing locally on your device, ensure you **set up/activate the virtual environment before installing/generating the requirements.txt file**; failure to do this will pollute your machine and put other projects at risk.

1. **Install the requirements** listed in requirements.txt using the terminal command  **```pip3 install -r requirements.txt```**
   * Kindly note that since I developed the project from scratch and installed the required libraries as I progressed **I have already included a requirements.txt for this app** by using the terminal command **```pip3 freeze > requirements.txt```** to generate it.

1. **[Create your own Heroku app](#create-heroku-app)**, and update allowed hosts in settings.py.

1. **[Create your own AWS bucket](#AWS-S3-Bucket)**, and update AWS settings for name and region of the bucket in settings.py.

1. **[Create your .env file](#creating-environmental-variables-locally)**.

1. **Run server locally** with ``` python mange.py runserver ```

[Back to Readme](README.md)