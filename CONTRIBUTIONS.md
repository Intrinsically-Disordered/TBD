# Guide for making contributions to TBD

Please report all the bugs in TBD modules and mistakes in documentation by creating an <a href="https://github.com/Intrinsically-Disordered/TBD/issues/new">issue</a>. You can also request features using the same link. Alternatively, if you want to make contribution, please feel free to create a pull request. The procedure to make contributions is as follows:

### Step 1. Setting up the repository

The first step requires you to fork the repository on your GitHub using the button on top right corner of the TBD main repository page.


### Step 2. Cloning the repository

The next step is to clone the repository by running the following command in your temrinal/command prompt:
```
git clone git@github.com:Intrinsically-Disordered/TBD.git
```
This requires connecting to GitHub using the SSH protocol, which you can learn more about <a href="https://docs.github.com/en/authentication/connecting-to-github-with-ssh">here</a>.

### Step 3. Making changes

The repository is then ready for the changes to be made. After making the changes, make sure you add, commit and push to your forked branch by running following commands:

```
git add changed_file
git commit -m "reasonable description of your changes"
git push
```

### Step 4. Generating pull request

The final step is to generate a pull request. The instructions for opening a pull request are outlined in this <a href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request">tutorial</a>


## Things to note
To achieve the purpose of continous integration, <code>TBD</code> utilizes <code>travis CI</code>. travis CI is configured to perform PEP8 compliance test (flake8) along with running unittests. Any failure in compliance would result in build error or build failure on travis CI.

To run these test on your local machine, following code snippets can be used in your terminal/command prompt:

For flake8,
```
conda install flake8
cd TBD
flake8
```

For unittest,
```
cd TBD
python -m unittest discover
```
