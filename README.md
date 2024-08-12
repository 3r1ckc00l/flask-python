# Flask Python - micro service

## Install python first on your localhost (check with python --version)

```
$brew install python
$brew install pyenv
$pip3 install virtualenv << install virtual ENV machine
```

## Running Flask
```
$python3 -m venv myenv << create virtual ENV machine (name: myenv) on folder project
$source myenv/bin/activate << activate virtual ENV
$pip3 install flask flask-sqlalchemy << install flask and sqlalchemy on ENV machine
$python3 app.py << running python on the ENV machine & if error python founded please remove the virtual ENV folder (rm -rf myenv) 
```
