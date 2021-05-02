set -e

if command -v cdk &> /dev/null; then
  echo "Using command: cdk."
  custom_cdk="cdk"
fi

if command -v /usr/bin/cdk &> /dev/null; then
  echo "Using command: /usr/bin/cdk."
  custom_cdk="/usr/bin/cdk"
fi

if command -v ./node_modules/aws-cdk/bin/cdk &> /dev/null; then
  echo "Using command: ./node_modules/aws-cdk/bin/cdk."
  custom_cdk="./node_modules/aws-cdk/bin/cdk"
fi

eval "$custom_cdk" "$@"
