#!/bin/bash

ECRYPTFS_KEY=<run ecryptfs-add-passphrase and place sig here>

arg=$1

if [ -z "$arg" ]; then
        read -sp "Passphrase: " passphrase
        sudo mount -t ecryptfs -o rw,relatime,ecryptfs_fnek_sig=${ECRYPTFS_KEY},ecryptfs_sig=${ECRYPTFS_KEY},ecryptfs_cipher=aes,ecryptfs_key_bytes=32,ecryptfs_unlink_sigs,verbosity=0,key=passphrase:passphrase_passwd="$passphrase" $HOME/.e $HOME/.private
else
        if [ "$arg" == "-u" ]; then
                sudo umount ~/.private
                keyctl list @u
                keyctl clear @u
        else
                echo "Error: Bad argument"
        fi
fi
