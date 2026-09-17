#!/bin/bash
# Auto label helper
echo "Label bug if error found, feature if add found"
if [[ "$1" == *error* ]]; then echo bug; fi
if [[ "$1" == *add* ]]; then echo feature; fi
