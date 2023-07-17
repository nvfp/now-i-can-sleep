echo "::group::Set up NICS working directory"


echo "DEBUG: pwd: '$(pwd)'"
echo 'DEBUG: Running `ls`'
ls
echo "DEBUG: ls command completed"

echo 'DEBUG: Running `cd ..`'
cd ..

echo "DEBUG: pwd: '$(pwd)'"
echo 'DEBUG: Running `ls`'
ls
echo "DEBUG: ls command completed"

echo 'DEBUG: Running `mkdir __nics_work_dir__`'
mkdir __nics_work_dir__

echo 'DEBUG: Running `ls`'
ls
echo "DEBUG: ls command completed"

echo "DEBUG: Running 'cp $GH_REPO_NAME/$CONTAINER/ __nics_work_dir__/'"
cp -r $GH_REPO_NAME/$CONTAINER/ __nics_work_dir__/

echo 'DEBUG: Running `ls __nics_work_dir__`'
ls __nics_work_dir__
echo "DEBUG: ls command completed"


echo "::endgroup::"