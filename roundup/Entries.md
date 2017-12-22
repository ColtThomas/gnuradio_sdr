This file is a day to day journal entry of the project to keep track of progress, and to draft other important documents.

#Sept 21, 2017

Working on setting up the USRP and GNU Radio with a newly updated machine. Still need to get MATLAB on the respective machine. You may want to include a guide for getting the USRP set up with GNURadio. 

Installing GNURadio is pretty straightforward:

-open a terminal and enter "sudo apt-get install gnuradio".

You can now search using the Ubuntu app search button on your toolbar for "GNU Radio" and open the GNU Radio Companion, a graphic interface for the radio libraries.

Pre-Requisite things to install on Ubuntu to run GNU Radio can be found at wiki.gnuradio.org/index.php/UbuntuInstall#Install_the_Pre-Requisites

#Sept 23, 2017

I'm getting the following error every time that I try running a spectrum analyzer program on the USRP through GNU Radio:

File "/usr/lib/python2.7/dist-packages/gnuradio/uhd/__init__.py", line 38, in _prepare_uhd_swig
    import uhd_swig
  File "/usr/lib/python2.7/dist-packages/gnuradio/uhd/uhd_swig.py", line 28, in <module>
    _uhd_swig = swig_import_helper()
  File "/usr/lib/python2.7/dist-packages/gnuradio/uhd/uhd_swig.py", line 24, in swig_import_helper
    _mod = imp.load_module('_uhd_swig', fp, pathname, description)
ImportError: libboost_date_time.so.1.54.0: cannot open shared object file: No such file or directory

A similar error pops up when I use the "uhd_find_devices" command in the terminal. Looks like some Boost issue?


# Sept 29th, 2017

I decided to go get my dinosaur laptop that has an ethernet port and see if it could find the USRP.  It did as soon as I changed the static IP to 192.168.10.1 and ran a 'uhd_usrp_probe' command. As soon as I ran the 'uhd_find_devices' command in the terminal on the laptop, it recognized the usrp. This is with the Ettus Research USRP and not the National Instruments one... I think the latter needs updated firmware. I still would like to get a USRP working with the desktop PC since the laptop won't be staying here when I leave.

Seems like the problem with the desktop computer is that there is a libboost error (same as from Sept 23rd.) I suspect it is from the Chris's independently using the UHD tools independent of gnuradio. Maybe I can uninstall it and reinstall?

Goal: run the FM radio example and get it to work. Once that works fine, we can do SOQPSK crash run or something. Maybe just do a QPSK example if we get ambitious...


I may have to install this **** from source...


By some miracle, I finally got my newer laptop to recognize the usrp using an ethernet adapter. I had to turn off my wifi and then set a static IP address. IF YOU PLAN ON DOING THIS ON YOUR LAPTOP MAKE SURE THAT YOU INSTALL GNURADIO BEFORE ADDING UHD DRIVERS. Also make sure you have the latest version of Ubuntu before doing any installation. The desktop that Dr. Rice gave me already had UHD drivers and it was Ubuntu 14. Messed up the libboost libraries somehow. If you don't want to use your laptop, spare yourself the grief of figuring out drivers and get a new desktop with a freshly formatted Ubuntu operating system.

# October 10th, 2017

Now that I can get stuff off both my HackRF (personal tool) as well as a USRP I think it would be good to make a list of milestones to accomplish assuming that you have time to put into this project:

Milestones:
-Implement a QPSK transmitter and check with external QPSK receiver
-Implement a QPSK receiver, and check constellation
-Add a PN sequence to yout QPSK data stream

I wonder if I could do this in a month if I fix my class schedule....


# October 16th, 2017

System for our QPSK implementation:
-E4433B signal generator (key is usually hidden on one of the bookshelves... under a tissue box. Has a potato key chain)
-USRP N210
-ethernet connection to laptop
-cable from the RF output of E4433 to RF 1 of the USRP

TODO: take pics

The goal is to adjust the E4433 to generate a QPSK signal and capture it using gnuradio.

Settings:

Follow instructions below. User: chrisn Pass: usrp
http://sd-radio.groups.et.byu.net/doku.php?id=esg-d

# November 3rd, 2017
I was trying out a QPSK demod using the GNU Radio blocks, but something tells me that if I just try to build it from scratch using the ecen 485 labs things will click better for me.

# December 11th, 2017
For the past week or so, I decided to just make a qpsk modulator/demod in matlab so that it would be a piece of cake to convert over to python or C++. I noticed that converting things from simulink is actually a more painful way of building a demodulator from scratch in GNURadio. 

I also touched up an M2ascii and asciitobin function that makes it easy to see if your message came in. The M2ascii even has a preamble argument that searches your received bits for parts of the message. I got tired of figuring out where my index started.

# December 20th, 2017
I have a working general example of a QPSK demodulator in MATLAB, and I have been working on converting that to something that would work into GNU Radio. I don't think I'll be able to implement the project into GNU Radio, but I would like to at least leave the script so whoever starts this project later can pick up right where I left off.

...And I got the GNU Radio version implemented. I think what I'll do now is clean up the Git repository and make it manageable to whoever comes in next.
Scratch that. GNU Radio emulated script not working. My message keeps getting scrambled. Leave it to the story of Darth Plagueis the Wise to mess things up for you. I wonder if I am getting a timing error from my sinusoidal multiplies?
