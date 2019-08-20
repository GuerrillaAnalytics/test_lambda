aws lambda invoke --function-name my_lambda_function  --log-type Tail  --query 'LogResult' --output text --payload '{"pi": "foo", "e":"bar"}' --profile personal | base64 -d
