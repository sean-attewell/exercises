explore() {
    testnet getblockchaininfo

    testnet getmininginfo

    testnet getnetworkinfo

    testnet getnettotals

    testnet getwalletinfo
}

# our problem: no money!
# let's get some








signatures() {
    echo "getting address"
    ADDRESS=$(testnet getnewaddress "" legacy)
    echo "address: $ADDRESS"
    MESSAGE1="hello, world!"
    MESSAGE2="goodbye, world!"
    SIGNATURE=$(testnet signmessage $ADDRESS "$MESSAGE1")
    echo "verifies? $(testnet verifymessage $ADDRESS "$SIGNATURE" "$MESSAGE1")"
    echo "verifies? $(testnet verifymessage $ADDRESS "$SIGNATURE" "$MESSAGE2")"
    # also change 1 character in $SIGNATURE and show it doesn't work
}

signatures

keys() {
    ADDRESS=$(testnet getnewaddress "" legacy)
    WIF=$(testnet dumpprivkey $ADDRESS)
    HX=$(bx wif-to-ec $WIF)
}
