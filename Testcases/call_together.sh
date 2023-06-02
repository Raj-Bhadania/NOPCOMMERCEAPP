#!/usr/bin/env sh

CURRENT_DIR=$(pwd)

echo "Current Directory: $CURRENT_DIR"

test_files=$(find "$CURRENT_DIR" -name "*Test*.py")

for file in $test_files; do
  echo "Running test case: $file"
  pytest "$file" -v
done
