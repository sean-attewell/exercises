#!/bin/bash

#Define cleanup procedure
cleanup() {
    echo "container stopped" >> /workspace/exercises/log.txt
}

#Trap SIGTERM
trap 'cleanup' SIGTERM

#Execute a command
testnet stop

echo "stopped bitcoin-cli" >> /workspace/exercises/log.txt
echo $(testnet getblockchaininfo) >> /workspace/exercises/log.txt

#Wait
wait $!
