```
cd [working directory]
virtualenv -p python3 env
source env/bin/activate
git clone https://github.com/XaviP/recording_matcher_backend.git
cd recording_matcher_backend
pip install -r requirements.txt
sudo -u postgres psql
  CREATE DATABASE recording_matcher_db;
  CREATE USER recording_matcher_user WITH PASSWORD 'p455w0rd';
  ALTER ROLE recording_matcher_user SET client_encoding TO 'utf8';
  ALTER ROLE recording_matcher_user SET default_transaction_isolation TO 'read committed';
  ALTER ROLE recording_matcher_user SET timezone TO 'UTC';
  GRANT ALL PRIVILEGES ON DATABASE recording_matcher_db TO recording_matcher_user;
  \q
python manage.py migrate
python manage.py import_sound_recordings
python manage.py runserver
```
