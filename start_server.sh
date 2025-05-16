source /Users/omarpalmer-lopez/Documents/personal-site/site_env/bin/activate
cd /Users/omarpalmer-lopez/Documents/personal-site
gunicorn -b 0.0.0.0:9100 main:app