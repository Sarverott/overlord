
echo "### main ###"

git status

echo "### submodules ###"

git submodule foreach 'git status'


