echo
echo
echo '-----------' delete data.json from s3 '-----------'
aws s3 rm s3://data-testlambdas3/data.json

echo
echo
echo '-----------' delete stack '-----------'
aws cloudformation --region us-west-2 delete-stack --stack-name testlambda
