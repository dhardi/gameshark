# Deployment

## Table of Contents
- [Initial Deployment](#initial-deployment)
- [Create repository](#create-repository)
- [Setting up the Workspace (To be done locally via the console of your chosen editor)](#setting-up-the-workspace-to-be-done-locally-via-the-console-of-your-chosen-editor)
- [Create Heroku App](#create-heroku-app)
- [AWS S3 Bucket](#aws-s3-bucket)
- [Creating Environmental Variables Locally](#creating-environmental-variables-locally)
- [Setting up settings.py File](#setting-up-settingspy-file)
- [Set up Heroku for use via the console](#set-up-heroku-for-use-via-the-console)
- [Cloning on a Local machine or Via Gitpod Terminal](#cloning-on-a-local-machine-or-via-gitpod-terminal)

## Initial Deployment
Below are the steps I took to deploy the site to Heroku and any console commands required to initiate it.

## Create repository
Create a new repository in GitHub and clone it locally following these instructions.  
**Note** - If you are cloning my project, then you can skip all pip installs below and just run the following command in the terminal to install all the required libraries/packages at once:

**bash**
pip install -r requirements.txt

**IMPORTANT** - If developing locally on your device, ensure you set up/activate the virtual environment (see below) before installing/generating the `requirements.txt` file; failure to do this will pollute your machine and put other projects at risk.

## Setting up the Workspace (To be done locally via the console of your chosen editor)
1. Create a virtual environment on your machine (Can be skipped if using Gitpod):
    ```bash
    python -m venv .venv
    ```
2. To ensure the virtual environment is not tracked by version control, add `.env` to the `.gitignore` file.
3. Install Django with version 3.2:
    ```bash
    pip install django==3.2.14
    ```
4. Install Gunicorn:
    ```bash
    pip install gunicorn
    ```
5. Install supporting libraries:
    ```bash
    pip install dj_database_url
    pip install psycopg2-binary
    ```
6. Create `requirements.txt`:
    ```bash
    pip freeze --local > requirements.txt
    ```
7. Create an empty folder for your project in your chosen location.
8. Create a project in the above folder:
    ```bash
    django-admin startproject <PROJECT_NAME>
    ```
   (In the case of this project, the project name was "Gameshark")
9. Create an app within the project:
    ```bash
    python manage.py startapp APP_NAME
    ```
   (In the case of this project, the app name was "gameshark")
10. Add a new app to the list of installed apps in `settings.py`.
11. Migrate changes:
    ```bash
    python manage.py migrate
    ```
12. Test server works locally:
    ```bash
    python manage.py runserver
    ```
   (You should see the default Django success page)

## Create Heroku App
The below works on the assumption that you already have an account with Heroku and are already signed in.

1. Create a new Heroku app:
   - Click "New" in the top right-hand corner of the landing page, then click "Create new app."
2. Give the app a unique name:
   - Will form part of the URL (in the case of this project, I called the Heroku app `gameshark`).
3. Select the nearest location:
   - For me, this was Europe.
4. Add Database to the Heroku app:
   - Navigate to the Resources tab of the app dashboard. Under the heading "Add ons," search for "Heroku Postgres" and click on it when it appears.
   - Select "Hobby Dev - Free" from the "plan name" drop-down menu and click "Submit Order Form."
5. From your editor, go to your project's `settings.py` file and copy the `SECRET_KEY` variable. Add this to the same name variable under the Heroku App's config vars.
   - left box under config vars (variable KEY) = `SECRET_KEY`
   - right box under config vars (variable VALUE) = Value copied from `settings.py` in the project.

## AWS S3 Bucket
The below works on the assumption that you already have an account with AWS and are already signed in.

1. Create a new S3 bucket:
   - Click "Services" in the top left-hand corner of the landing page, click on "Storage" then click "S3."
   - Click "Create bucket."
   - Give the bucket a unique name:
     - Will form part of the URL (in the case of this project, I called the S3 bucket `gameshark`).
   - Select the nearest location:
     - For me, this was EU (Frankfurt) `eu-central-1`.
   - Under the "Object Ownership" section, select "ACLS enabled."
   - Under the "Block Public Access settings for this bucket" section, untick "Block all public access" and tick the box to acknowledge that this will make the bucket public.
   - Click "Create bucket."

2. Amend Bucket settings:

   **Bucket Properties:**
   - Click on the bucket name to open the bucket.
   - Click on the "Properties" tab.
   - Under the "Static website hosting" section, click "Edit."
   - Under the "Static website hosting" section select "Enable."
   - Under the "Hosting type" section ensure "Host a static website" is selected.
   - Under the "Index document" section enter `index.html`.
   - Click "Save changes."

   **Bucket Permissions:**
   - Click on the "Permissions" tab.
   - Scroll down to the "CORS configuration" section and click edit.
   - Enter the following snippet into the text box:
     ```json
     [
         {
             "AllowedHeaders": [
             "Authorization"
             ],
             "AllowedMethods": [
             "GET"
             ],
             "AllowedOrigins": [
             "*"
             ],
             "ExposeHeaders": []
         }
     ]
     ```
   - Click "Save changes."
   - Scroll back up to the "Bucket Policy" section and click "Edit."
   - Take note of the "Bucket ARN," click on the "Policy Generator" button to open the AWS policy generator in a new tab.
   - In the newly opened tab under Step 1 "Select Policy Type," select "S3 Bucket Policy." from the drop-down menu.
   - Under Step 2 "Add Statement(s)" enter `"*"` in the "Principal" text box.
   - From the "s3:Action" drop-down menu select "s3:GetObject."
   - Enter the "ARN" noted from the bucket policy page into the "Amazon Resource Name (ARN)" text box.
   - Click "Add Statement."
   - Under Step 3 "Generate Policy" click "Generate Policy."
   - Copy the resultant policy and paste it into the bucket policy text box on the previous tab.
   - In the same text box add `"/*"` to the end of the resource key to allow access to all resources in this bucket.
   - Click "Save changes."
   - When back on the bucket's permissions tab, scroll down to the "Access Control List" section and click "Edit."
   - Enable "List" for "Everyone (public access)", tick the box to accept that "I understand the effects of these changes on my objects and buckets." and click "Save changes."

3. Create AWS static files User and assign to S3 Bucket:

   **Create "User Group":**
   - Click "Services" in the top left-hand corner of the landing page, from the left side of the menu click on "Security, Identity, & Compliance" and select "IAM" from the right side of the menu.
   - Under "Access management" click "User Groups."
   - Click "Create Group."
   - Enter a user name (in the case of this project, I called the user group `gameshark`).
   - Scroll to the bottom of the page and click "Create Group."

   **Create permissions policy for the new user group:**
   - Click "Policies" in the left-hand menu.
   - Click "Create Policy."
   - Click "Import managed policy."
   - Search for `AmazonS3FullAccess`, select this policy, and click "Import."
   - Click "JSON" under "Policy Document" to see the imported policy.
   - Copy the bucket ARN from the bucket policy page and paste it into the "Resource" section of the JSON snippet. Be sure to remove the "/*" at the end of the ARN to allow access to the bucket only.
   - The resultant policy should look something like this:
     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Principal": "*",
           "Action": "s3:GetObject",
           "Resource": "arn:aws:s3:::gameshark/*"
         }
       ]
     }
     ```
   - Click "Review Policy."
   - Add a name for the policy (in the case of this project, I called it `allow-access-to-gameshark`), and click "Create Policy."

   **Attach Permissions to the User Group:**
   - Click "User Groups" in the left-hand menu.

