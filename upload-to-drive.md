[Go Back](https://github.com/arm-on/dstools/)

# How to Move Files from a Server to Google Drive


- Install Amazon AWS on the server using [this tutorial](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html), and configure it using `aws configure`.

- Visit [this page](https://console.developers.google.com/apis/library/drive.googleapis.com/)

- Click "Enable". After some time (about a minute or so), you will be redirected to a page titled "Google Cloud Platform" at this [url](https://console.cloud.google.com/apis/api/drive.googleapis.com/overview?project=rapid-stage-329510).


- Go to the "OAuth consent screen" section. Write a dummy name for your app, and put your gmail as the user support email (and every other place an email is needed). Then, choose "External" as the "User Type", and click "Create". "Add a user" in the "Test users" section. Then, put the same gmail in the textbox again. Click "Save and Continue" at the end.


- Go to the "Credentials" section. Click "Create Credentials" from the top menu. Choose "OAuth client ID", In the first step, specify your "Application Type" as "Desktop app". You will see a message saying that "OAuth client created", and a button with the inside text "Download JSON". Click on it, and open the json file.

- Copy the "client id" and "client secret" from the JSON file. Edit the "settings.yaml" file accordingly. 

- Put "settings.yaml", and the Jupyter notebook in a folder (they should be in the same folder).

- The Jupyter notebook should contain the following things:


1. PyDrive Installation
```
!pip install PyDrive2
```
2. Include the Necessary Libraries
```
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)
```
3. Upload the file you want


- File name: "sample.zip"
- Google Drive ID: "abcdefghi"
- Location at the server: "/home/user/sample/sample.zip"

```
gfile = drive.CreateFile({'title':'sample.zip', 'mimeType':'application/zip',
        "parents": [{"kind": "drive#fileLink","id": "abcdefghi"}]})
gfile.SetContentFile('/home/user/sample/sample.zip')
gfile.Upload()
```