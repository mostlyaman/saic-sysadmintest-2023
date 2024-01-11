## Challenge 1 - Gain Access to a Remote Server

**Task**: Gain access to the VM root privieleges by exploiting a hosted website.

Initial Thoughts:
1. Need to get terminal access through HTTP server: Upload file vulnerability

**Booting the VM**:
1. First, login as guest. I can see the Xenia webpage at localhost but nothing too interesting on the source code of the page. 

2. Read apache config. Go to /var/www.

3. We have many folders here of interest: 
a. **ange1**, **angel1** - Empty
b. **uploads**, **tmp** - Empty
c. **secure** - contains **backup.zip**
d. **nothing** - contains **index.html** and **pass.txt**
e. **SecreTSMSgatwayLogin** - some PHP code for messaging service?? needs a login and password


**Files of Interest**:
1. **backup.zip** contains **backup-cred.mp3** but I think it is a text file disguised as a mp3. Requires Zip password to unlock.
2. **pass.txt** contains:
```
#my secret
xenia
tux
freedom
password
diana
helloworld!
iloveroot
```

## 4 hours later
Hardstuck, reading the apache config I was curious about /cgi-bin/ ScriptAlias and got to know about /cgi-bin/ vulnerabilities, maybe related to that.

Read on an article to use a "CGI Scanner" tool.

#### Use Nikto to search for vulnerabilites

```
 Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          192.168.43.34
+ Target Hostname:    192.168.43.34
+ Target Port:        80
+ Start Time:         2024-01-10 06:35:30 (GMT5.5)
---------------------------------------------------------------------------
+ Server: Apache/2.2.22 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, inode: 390771, size: 2587, mtime: Wed Jan  3 21:37:50 2024
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ OSVDB-3268: /ange1/: Directory indexing found.
+ Entry '/ange1/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ OSVDB-3268: /angel1/: Directory indexing found.
+ Entry '/angel1/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ OSVDB-3268: /tmp/: Directory indexing found.
+ Entry '/tmp/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ OSVDB-3268: /uploads/: Directory indexing found.
+ Entry '/uploads/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ "robots.txt" contains 5 entries which should be manually viewed.
+ Uncommon header 'tcn' found, with contents: list
+ Apache mod_negotiation is enabled with MultiViews, which allows attackers to easily brute force file names. See http://www.wisec.it/sectou.php?id=4698ebdc59d15. The following alternatives for 'index' were found: index.html
+ Apache/2.2.22 appears to be outdated (current is at least Apache/2.4.12). Apache 2.0.65 (final release) and 2.2.29 are also current.
+ Allowed HTTP Methods: POST, OPTIONS, GET, HEAD 
+ OSVDB-3268: /secure/: Directory indexing found.
+ OSVDB-3092: /tmp/: This might be interesting...
+ OSVDB-3233: /icons/README: Apache default file found.
+ 8351 requests: 0 error(s) and 20 item(s) reported on remote host
+ End Time:           2024-01-10 06:35:41 (GMT5.5) (11 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

Basically, it warned us of 5 main issues.

```
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.2.22 appears to be outdated (current is at least Apache/2.4.12). Apache 2.0.65 (final release) and 2.2.29 are also current.
```
I was hoping for a file upload vulnerability. *sigh*
Will try other problem statements first.