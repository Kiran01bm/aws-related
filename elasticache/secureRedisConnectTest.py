import redis

r = redis.StrictRedis(
host='redis.dev.example.com',
port=6379,
password='redispassword',
ssl=True,
)

r.set('foo', 'bar')
response = r.get('foo')
print response

"""
curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py --user
export PATH=$PATH:/home/myself/.local/bin
pip install redis
"""

"""
Deploying Lambda with Custom Packge Installs

sudo pip install virtualenv
virtualenv -p /usr/bin/python redistest
pip install redis
vi lambda_function.py
mv lambda_function.py redistest/lib/python2.7/site-packages
cd redistest/lib/python2.7/site-packages
zip -r9 lambda_function.zip *
"""
