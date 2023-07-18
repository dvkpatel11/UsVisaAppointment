python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
playwright install


# for development
pip install -r dev-configs/requirements.txt
#install file watchers abd import dev-configs/watchers.xml
