# Postmortem

## Issue Summary
In 2022 April 1st at 7:23 UTC the entire web service was down untill 8:08 UTC for 45 minutes. Due to that users universally could not access the website with a status code response 500. The root cause were due to malware (Worm) by consuming bandwidth and overloading the web severs.
## Timeline
* Issue detected at 
* The issue is detected by 
* Actions taken
* Debugging paths taken
* Incident escalated 
* Incident rsolved

## Root cause and resolution
The root cause of the outage was due to a malware (worm) named **Fools day** which causes overloading webservers by consuming the computational power of the physical servers and spreading itself over the computer networks. The main target of the malware file is to repate certain tasks and replicate itself exponentialy. where it uses recursive methods to copy itself maliciously and distribute itself based on exponential growth. By doing this it infects many servers in a short period of time also consumes network bandwidth.
This issue is fixed by scanning and removing mallcious files over the network using Antivirus.

## Corrective and preventive measures
The corrective and preventive methods used to avoid this kind issues icludes
* Runing the firewall and antivirus to be more protective from this kind of computer worms 
* keeping the servers operating system up-to-date. where these updates often contain security pathes.
* Warning the engineers and the IT works or anybody who works close to the server to avoid opening emails they don't recognize and to upgrade their cyber security.
