#!/bin/bash
echo "listing available backups"
echo "-------------------------"
cd /backups
for n in *; do printf '%s\n' "$n"; done
