echo
echo
echo '-----------' zipping '-----------'
zip -r dag_exercise.zip dag_exercise.py graph_utils.py

echo
echo
echo '-----------' create bucket for code and upload '-----------'

BUCKET_NOT_EXISTS=$(`which aws` s3api head-bucket --bucket testlambdas3 2>&1)

if [ ! -z "${BUCKET_NOT_EXISTS}" ]; then
  $(which aws) s3 mb s3://testlambdas3 --region us-west-2
fi

$(which aws) s3 cp dag_exercise.zip s3://testlambdas3

echo
echo
echo '-----------' packaging '-----------'
$(which aws) cloudformation package --region us-west-2 --template-file ./template.yaml --output-template-file ./serverless.yaml --s3-bucket tests3bucket --s3-prefix test-code-deploy

echo
echo
echo '-----------' deploying '-----------'
$(which aws) cloudformation deploy --region us-west-2 --template-file ./template.yaml --stack-name testlambda --capabilities CAPABILITY_NAMED_IAM

echo
echo
echo '-----------' uploading data '-----------'
RESP_DATA_BUCKET_EXISTS=$($(which aws) s3api head-bucket --bucket data-testlambdas3 2>&1)
if [ -z "${RESP_DATA_BUCKET_EXISTS}" ]; then
  $(which aws) s3 cp data.json s3://data-testlambdas3
fi
