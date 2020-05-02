# behave_1
For More info refer below link:
https://behave.readthedocs.io/en/latest/tutorial.html
https://behave.readthedocs.io/en/latest/tutorial.html#environmental-controls

Execute the following command to install behave with pip:

    pip install behave

To update an already installed behave version, use:

    pip install -U behave

Directory structure:

    features/
    features/signup.feature
    features/login.feature
    features/account_details.feature
    features/environment.py
    features/steps/
    features/steps/website.py
    features/steps/utils.py



<!-- ================================ -->

The “Given”, “When” and “Then” parts of this prose form the actual steps that will be taken by behave in testing your system.
These map to Python step implementations. As a general guide:

"Given" we put the system in a known state before the user (or external system) starts interacting with the system (in the When steps).
Avoid talking about user interaction in givens.

"When" we take key actions the user (or external system) performs. This is the interaction with your system which should (or perhaps should not)
cause some state to change.

"Then" we observe outcomes.
You may also include “And” or “But” as a step - these are renamed by behave to take the name of their preceding step, so:


