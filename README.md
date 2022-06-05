# block-lists
Lists of domains to block


Definitely a better way to do this but I'm lazy.
https://openphish.com/feed.txt

cat feed.txt | sed 's/^.*\:\/\///' | sed 's/\/.*$//' | grep -v '[0-9]$' > newfeed.txt

./domainsort.py newfeed.txt > phish.txt

massive.txt manually copied from https://dbl.oisd.nl

morebig.txt parsed from https://smokingwheels.github.io/Pi-hole/allhosts

cat allhosts | awk '{print $2}' > morebig.txt | sed 's/\;.*$//'
# Do something about comment lines