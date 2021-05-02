set -e

if command -v cdk; then
  echo "Using command: cdk."
  cdk "$@"
  exit 0
fi

if command -v /usr/bin/cdk; then
  echo "Using command: /usr/bin/cdk."
  /usr/bin/cdk "$@"
  exit 0
fi

if command -v ./node_modules/aws-cdk/bin/cdk; then
  echo "Using command: ./node_modules/aws-cdk/bin/cdk."
  ./node_modules/aws-cdk/bin/cdk "$@"
  exit 0
fi

echo "Error. No cdk tool found. Did you run npm install aws-cdk?"
exit 1
