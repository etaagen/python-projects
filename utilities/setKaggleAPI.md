### Setting up a Kaggle API

Do this in your my_venv terminal

In the Terminal home directory: 
    mkdir -p ~/.kaggle 

Download a Kaggle API from the Settings tab
    https://www.kaggle.com/settings

Move the kaggle.json file to /.kaggle 
    mv ~/Downloads/kaggle.json ~/.kaggle/

Set file permissions
    chmod 600 ~/.kaggle/kaggle.json

Verify the set up 
    kaggle datasets list