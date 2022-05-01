# Postmortem
  
## Issue Summary
In 2022 April 1st at 7:23 UTC the entire web service was down until 8:08 UTC for 45 minutes. Due to that all users universally could not access the website with a status code response 500 which is internal server error. The root cause were due to malware (Worm files) which infects the webservers and consume network bandwidth and also overload webservers.
## Timeline
* At 7:23 UTC issue was detected by monitoring alert and notifies on call engineers. with 
messages describing the website is down.
* At 7:25 UTC the on call engineers acknowledged the issue.
* At 7:30 UTC the engineers discovered that the servers CPU and memory usage increased dramatically in short period of time during the investigating their performance history.
* At 7:35 UTC the engineers checks all running process(including background process)
* At 7:37 UTC the engineers noticed that unknown process running at the background and also taking huge computational power almost on every servers.
* At 7:40 UTC the engineers discovered that this unknown process are increasing exponentially. And the engineers guessed that this malicious files are Viruses.
* At 7:41 UTC the engineers decided to run antivirus on all servers.
* At 7:59 UTC the engineers restart all servers.
* At 8:08 UTC all servers begun to function as expected and brings the websites services back. And the alert is being marked as solved.

## Root cause and resolution
The root cause of the outage was due to a malware (worm file) which causes overloading of 
webservers by consuming the computational power of the physical servers and spreading itself over the computer networks. The main target of the malware file is to repeat certain tasks and replicate itself exponentially. where it uses recursive methods to copy itself maliciously and distribute itself based on exponential growth. By doing this it infects many servers in a short period of time also consumes the network bandwidth.
This issue is fixed by scanning and removing malicious files from the all servers and the 
entire network using Antivirus.

## Corrective and preventive measures
The corrective and preventive methods used to avoid this kind issues includes
* Running the firewall and antivirus to be more protective from this kind of computer worms 
* keeping the servers operating system up-to-date. where these updates often contain security paths.
* Warning the engineers and the IT works or anybody who works close to the server to avoid opening emails they don't recognize and to upgrade their cyber security.
