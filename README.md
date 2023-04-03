# Setup virtual environment
cd /path/to/crawl-craftpix
virtualenv venv
. venv/bin/activate

Step 1: Installing Google Chrome
Use the below steps to install the latest Google Chrome browser on Ubuntu and Debian systems.

First of all, download the latest Gooogle Chrome Debian package on your system.
```
wget -nc https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

Now, execute the following commands to install Google Chrome from the locally downloaded file.
```
apt update 
apt install -f ./google-chrome-stable_current_amd64.deb 
```
Press ‘y’ for all the confirmations asked by the installer.

This will complete the Google Chrome on your Ubuntu or Debian system. This will also create an Apt PPA file for further upgrades.

Step 2: Installing Selenium and Webdriver for Python
We will use a virtual environment for running Python scripts. Follow the below steps to create Python virtual environment and install the required python modules.

Create a directory to store Python scripts. Then switch to the newly-created directory.
```
mkdir tests && cd tests 
```
Set up the Python virtual environment and activate it.
```
python3 -m venv venv 
source venv/bin/activate 
```
Once the environment is activated, You will find the updated prompt as shown below screenshot:

Create Python Environment for Selenium on Ubuntu
Now use PIP to install the selenium and webdriver-manager Python modules under the virtual environment.
```
pip install selenium webdriver-manager 
```



Cách 2:
```
wget https://chromedriver.storage.googleapis.com/111.0.5563.64/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
```

trong code
```
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(executable_path='/path/to/chromedriver'), options=options)
```