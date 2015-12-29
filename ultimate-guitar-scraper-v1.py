# --- Micah Arvey --- #
# https://github.com/micaharvey/Ultimate-Guitar-Chord-Scraper
# Ultimate Guitar Chord Scraper v1

# import regular expressions and url lib 2
import re, urllib2

# Prompt the User
print "Enter the URL you wish to crawl.."
print 'Usage  - "https://tabs.ultimate-guitar.com/s/sublime/santeria_ver2_crd.htm" <-- With the double quotes'
myurl = input("@> ")

# Got the input, fetch the URL
response = urllib2.urlopen(myurl)
if not response:
	print 'FAILED: no response for given url'
	exit(0)

# Write the HTML to a file
html = response.read()
if not html:
	print 'FAILED: could not read response'
	exit(0)

# FIND THE LYRICS/CHORDS, catch no match case.
match = re.search("columns and guitar forums!(.*)<div class=\"fb-meta\">", html, re.DOTALL)
if not match:
	print 'FAILED: no match on regex - lyrics'
	exit(0)
lyrics = match.group(1)
# Get Rid of top bit
lyrics = '\n'.join(lyrics.split('\n')[2:]) 
# Get rid of html markup
lyrics = re.sub("<.*?>", '', lyrics)

# FIND THE TITLE
title_match = re.search( '<title>(.*) Chords.*?\)*? by (.*) @ Ultimate-Guitar.Com</title>', html)
if not title_match:
	print 'FAILED: no match on regex - title'
	exit(0)
# Clean it up
title = title_match.group(1) + ' - ' + title_match.group(2)

# PUT IT ALL TOGETHER and write to a cleanfile
all_together = title + lyrics
cleanfile = file(title,'wt')
cleanfile.write(all_together)

# SUCCESS!!!
print 'SUCCESS: written to current working directory: ' + title

# Put away our toys
cleanfile.close()

