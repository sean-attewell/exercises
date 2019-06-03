# preamble

* i'm trying to teach you basic python and terminal skills, but this can honestly be tedious. so i will try to leverage your interest in bitcoin to keep it interesting.
* along the way i'll try to pique your curiousity about some bitcoin ideas and teach you useful skills, like securely downloading bitcoin's source code, interacting with full nodes, working with csv data and "how github works"

# setup

* tour the interface
    * this is the "visual studio code" text editor by microsoft
        * desktop application
        * GitPod makes it work in browser
        * no setup, which can be very confusing to beginners!
    * layout
        * file browser
        * text editor
            * write programs
            * try typing in it
        * terminal. this is where we execute programs.
            * type `ls` and enter. see how it matches file tree on right?
            * show them the bitcoin node
            * type `testnet getblockchaininfo`
                * do it again. what changed?
            * type `mainnet getblockchaininfo`
* hello, world!
    * you've written your first computer program!
* "before we go any further, i want to show you how to stop and start this thing"
    * ([link](https://gitpod.io/workspaces/)
    * 100 hours
    * hit the stop button when you're done (but they usually seem to shut down automatically if left idle for too long)

# [print.py](print.py)

* statements executed sequentially
* special characters
* practice get comfortable editing plain text

# [variables.py](variables.py)

* visit [README.md](README.md)
    * left-click > open with > {preview, editor}
        * ask them to trivially alter
    * visit bitcoin's README
        * open "raw"  to show how it is formatted
        * show how exiting to the root of repo displays README
* variables used for repeating data
* (seque) open the repl and try the same stuff as above)

# [num.py](num.py)

* (continuing in the repl)
* create a new file. call it supply.py. halvening exercise.

# [user_input.py](user_input.py)

* calculator
    * introduce `input`
    * first interactive program
* comments
    * add some comments to the program. explain readability.
    * useful when you still want to see code but don't want it to run
    * comment out calculator
* if statements
* functions
* even or odd


# [bitcoin-cli.sh](bitcoin-cli.sh)

* `explore`
    * `getblockchaininfo`
        * whether we're still doing initial block download
        * softforks
    * `getmininginfo`
        * hashes per second
    * `getnetworkinfo`
        * protocol versions
        * over what ipv4 / ipv6 / tor
    * `getnettotals`
        * how much bandwidth are you using?
    * `getwalletinfo`
        * we're broke!
    * generate address and get coins from faucet

# [rpc.py](rpc.py)

* can we do ^^ from python
* this program is like a simpler version of `testnet` cli. it connects to bitcoin's rpc server running on 18332 (show ports tab, mention 18333 is p2p server). 
* let's fund and address from this side as well
* also import `mainnet` on both sides
    * wallet disabled b/c mainnet is real money
    * but it's not pruned, we can get genesis block

* just a function, but it gets information from outside python (remote)
* dictionaries
* verbosity
    * if you know what you're doing, you can pick values out of the raw blocks (for example)

# digital signatures

* use `bit` so we only deal w/ 1 bitcoin library
* start in python 
    * b/c more explicit what exactly what a private key is
    * 
* `signatures` demo in `bitcoin-cli-1.sh`
    * verify the signature created by `bit`
    * this is how craig wright could prove he holds satoshi's coins
* practice with functions
* mischief exercises where spreadsheet isn't editable and there are 5 statements?
* demonstrate that private key is less than n (but not much less). maybe calculate what percenage less it is ...
* generate private keys using bitcoin-cli
* use bx to show `p*G = P`?

# [hashing.py](hashing.py)

* hash text
* verify on command line: `sha256sum <filename>`
* practice with functions
* some hints on which one is correct:
    * `ls -alh` for file sizes
    * `hexdump -C` for raw hex
    * `xxd -b` for raw bytes
* "hopefully this gives you more confidence installing bitcoin in future!"

# [loops.py](loops.py)

* for loops
* lists
* more on dictionaries

# prices.py

* `assets/prices.csv`
    * what year had highest high?
    * what year had lowest low?
* `assets/prices-extended.csv`
    * average volume in 2016
    * average volume for each year
    * high and low day for each year?

# supply.py v2

* 2nd 2 exercises

# tx.py

* at this point we should have funded testnet addresses on command line and python
* lets send
    * python -> command line
    * command line -> python
* transactions
    * fund an address using bitcoin-cli
    * send between addresses using bitcoin-cli
    * fund an address using `bit`
    * send from `bitcoin-cli` back to `bit`
    * send it back
    * could we somehow prepare transaction in bitcoin-cli and sign in python?

# missing

* proof-of-work demo
* "next steps" section in README
* version handshake demo w/ sockets
