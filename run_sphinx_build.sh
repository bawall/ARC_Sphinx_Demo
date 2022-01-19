#!/bin/bash
sphinx-build -b html docs/source/ docs/build/html
cd ./docs
make latexpdf
cd ..