#!/bin/bash

NUMBER_OF_REQUESTS=20

make_request() {
    python client.py
}

for i in $(seq 1 $NUMBER_OF_REQUESTS)
do
	make_request $i & # put a function in the background
done

wait
echo "done"