Title: Remote hosting of IPython Notebooks
date: 2013-10-04 00:00
comments: true
slug: pybook-remote

Over the past few months, [IPython notebooks](http://ipython.org/notebook.html) have become my go to python development tool.  Combining interactive programing with markdown documentation and portability, IPython notebooks are a powerful scientific-computing tool.  Working within a notebook gives you the ability to experiment like you would in a terminal based interpreter and to save your work when you're done.  

IPython notebooks are web-based, which means you interact with them through a browser.  When invoked, IPython starts a local webserver that hosts your notebooks.  If you are like me, you are often working on remote machines (i.e. I'm at home working on our research groups cluster which is not at my home), so it's not super easy to access that local web server.  

There are, however, a couple pretty slick tricks that allow you to remotely access the private IPython web server hosted on remote machines, allowing you to work in a browser on your local machine, while all the computing gets done on the remote machine.

We can start a IPython notebook session by running the following command in the directory we want our notebooks to be stored in.  

    ipython notebook

By running this command, we have started an IPython notebook webserver running at [http://127.0.0.1:8889/](http://127.0.0.1:8889/)

    The IPython Notebook is running at: http://127.0.0.1:8889/

You could just run the above command and your browser would likely open in an [x-window](http://www.x.org/wiki/).  That is all fine and good except, for a number of reasons, this is a painfully slow way to use IPython notebooks.  

Here we are interested in running IPython notebooks on a remote machine.  A better way to run IPython notebooks remotely is by using a [ssh tunnel](http://en.wikipedia.org/wiki/Tunneling_protocol).  When we create a ssh tunnel, we associate a specific port on the remote system to one on the local system.  Here's how to do it.  

1.  First, start an IPython notebook session on your remote machine, specifying the `--no-browser` and `--port=7777` options:

           ipython notebook --no-browser --port=7777

2.  Now we want to setup the ssh tunnel from the local machine to the remtoe machine.  
   
           ssh -N -f -L localhost:7777:localhost:7777 username@dest.ination.com
   
       In our group, we have to pass through a log in node before reaching our workstation or cluster.  You can do a multi-hop ssh tunnel using this command:

          host1=username@login_node.com
          host2=username@dest.ination.com
          ssh -L 7777:localhost:7777 $host1 ssh -L 7777:localhost:7777 -N $host2

3.  Open [localhost:7777](localhost:7777) in your local browser and get started using remotely hosted IPython notebooks.

Again, the beauty of this is that I interact only with the browser on my local machine, while having access to the computing power and file system of the remote machine.  

**A few references:**

* [Remote IPython Notebook Setup](http://wisdomthroughknowledge.blogspot.com/2012/07/accessing-ipython-notebook-remotely.html)

* [Multihop SSH Tunneling](http://superuser.com/questions/96489/ssh-tunnel-via-multiple-hops/97007#97007)