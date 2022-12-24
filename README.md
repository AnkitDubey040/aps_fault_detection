# Air Pressure Sensor - Fault Detection 

![1_pT9vCxg2Cn7R5DSnHNUDZw](https://user-images.githubusercontent.com/87509236/208734015-5d3a863b-3080-44f7-81a7-b1b5c63e11ad.jpeg)


### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```

Git Version
```
git --version
```

To download your dataset : 
```
wget https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv
```


Git Commands : 

Say you are starting a project want to coonect git repo with the source code 

```
git init
```
This will initialize git to project folder 

To clone existing repo : 
```
git clone <github url> 
```
Note : clone\download github in your system

Add changes in file to git staging area 
```
git add filename 
```
or to add all files : 

```
git add . 
```
To create commit :
```
git commit -m "message"
```
```
git push origin main
```
or for forcefull changes: 
```
git push -f origin main
```

 Note : Origin contains url to the github repo 

 To pull changes from github repo :

```
git pull origin
```
For batch Prediction :
```
python batch_prediction_main.py
```

For instace Prediction and running training pipeline:
```
python train_instance_pred_main.py
```
Linux shell script to run docker : 
```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```
