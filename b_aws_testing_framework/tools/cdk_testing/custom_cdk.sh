set -e

if command -v cdk &> /dev/null; then
  echo "Using command: cdk."
  cdk "$@"
fi

if command -v /usr/bin/cdk &> /dev/null; then
  echo "Using command: /usr/bin/cdk."
  /usr/bin/cdk "$@"
fi

if command -v ./node_modules/aws-cdk/bin/cdk &> /dev/null; then
  echo "Using command: ./node_modules/aws-cdk/bin/cdk."
  ./node_modules/aws-cdk/bin/cdk "$@"
fi
