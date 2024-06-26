<h1> EECS HelpDesk </h1>

EECS HelpDesk is a ticketing system for handling ECs (Extenuating Circumstances) and Technical Faults.

<h2> Installation Instructions.</h2>

Make sure that Python is installed and has been added to path. You can check this by running this command on UNIX-like systems:

<code> $ python3 -V </code>

or this command for Windows:

<code> $ py -V </code>

If the currently installed Python version is displayed, then Python has been added to path correctly,. If an error occurs, follow the installation instructions for Python again, making sure that you add Python as a PATH variable.

Once created, you must setup the virtual environment. Follow the instructions below to do so:

<h3> For Windows </h3>

<code> $ py -m venv venv </code>

<code> $ ./venv/Scripts/activate </code>

<code> $ pip install -r requirements.txt </code>

<h3> For Linux </h3>

<code> $ python3 -m venv venv </code>

<code> $ source venv/bin/activate </code>

<code> $ pip install -r requirements.txt </code>