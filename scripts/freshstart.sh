#!/

echo "---### npm install --save ###---"
#npm install --save

if [ -d .venv ]; then
    echo "---### python3 -m venv venv ###---"
    #python3 -m .venv venv
    rm -rf ./.venv
fi


echo "---### source venv/bin/activate ###---"

python3 -m venv .venv

source .venv/bin/activate

pip install -r ./requirements.txt

python ./src/overlord/__init__.py
