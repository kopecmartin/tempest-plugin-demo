# Cookiecutter debug


```
(.venv)[master][centos@mkopec-test tempest-plugin-demo]$ ls -all
total 24
drwxrwxr-x.  4 centos centos    76 May 20 11:08 .
drwx------. 13 centos centos  4096 May 20 10:57 ..
drwxrwxr-x.  8 centos centos  4096 May 20 11:08 .git
-rw-rw-r--.  1 centos centos  1203 May 20 10:21 .gitignore
-rw-rw-r--.  1 centos centos 11357 May 20 10:21 LICENSE
-rw-rw-r--.  1 centos centos     0 May 20 10:21 README.md
drwxrwxr-x.  5 centos centos    77 May 20 10:40 .venv
(.venv)[master][centos@mkopec-test tempest-plugin-demo]$ cookiecutter https://git.openstack.org/openstack-dev/cookiecutter.git
You've downloaded /home/centos/.cookiecutters/cookiecutter before. Is it okay to delete and re-download it? [yes]: yes
Traceback (most recent call last):
  File "/home/centos/tempest-plugin-demo/.venv/bin/cookiecutter", line 11, in <module>
    sys.exit(main())
  File "/home/centos/tempest-plugin-demo/.venv/lib/python2.7/site-packages/click/core.py", line 722, in __call__
    return self.main(*args, **kwargs)
  File "/home/centos/tempest-plugin-demo/.venv/lib/python2.7/site-packages/click/core.py", line 697, in main
    rv = self.invoke(ctx)
  File "/home/centos/tempest-plugin-demo/.venv/lib/python2.7/site-packages/click/core.py", line 895, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/home/centos/tempest-plugin-demo/.venv/lib/python2.7/site-packages/click/core.py", line 535, in invoke
    return callback(*args, **kwargs)
  File "/home/centos/tempest-plugin-demo/.venv/lib/python2.7/site-packages/cookiecutter/cli.py", line 120, in main
    password=os.environ.get('COOKIECUTTER_REPO_PASSWORD')
  File "/home/centos/tempest-plugin-demo/.venv/lib/python2.7/site-packages/cookiecutter/main.py", line 77, in cookiecutter
    extra_context=extra_context,
  File "/home/centos/tempest-plugin-demo/.venv/lib/python2.7/site-packages/cookiecutter/generate.py", line 99, in generate_context
    raise ContextDecodingException(our_exc_message)
cookiecutter.exceptions.ContextDecodingException: JSON decoding error while loading "/home/centos/.cookiecutters/cookiecutter/cookiecutter.json".  Decoding error details: "No JSON object could be decoded"
1(.venv)[master][centos@mkopec-test tempest-plugin-demo]$ cd ../.cookiecutters/cookiecutter/
(.venv)[master][centos@mkopec-test cookiecutter]$ vim cookiecutter.json
(.venv)[master !][centos@mkopec-test cookiecutter]$ git status
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#   modified:   cookiecutter.json
#
no changes added to commit (use "git add" and/or "git commit -a")
(.venv)[master !][centos@mkopec-test cookiecutter]$ git diff
diff --git a/cookiecutter.json b/cookiecutter.json
index 3214c3b..7e8c14e 100644
--- a/cookiecutter.json
+++ b/cookiecutter.json
@@ -3,7 +3,7 @@
        "service": "replace with the service it implements",
        "repo_group": "openstack",
        "repo_name": "replace with the name for the git repo",
-       "bug_tracker": ['Launchpad', 'Storyboard'],
+       "bug_tracker": ["Launchpad", "Storyboard"],
        "bug_project": "replace with the name of the project on Launchpad or the ID from Storyboard",
        "project_short_description": "OpenStack Boilerplate contains all the boilerplate you need to create an OpenStack package."
 }
(.venv)[master !][centos@mkopec-test cookiecutter]$ cd ../../tempest-plugin-demo/
(.venv)[master][centos@mkopec-test tempest-plugin-demo]$ cookiecutter https://git.openstack.org/openstack-dev/cookiecutter.git
You've downloaded /home/centos/.cookiecutters/cookiecutter before. Is it okay to delete and re-download it? [yes]: no
Do you want to re-use the existing version? [yes]: yes
module_name [replace with the name of the python module]:
service [replace with the service it implements]:
repo_group [openstack]:
repo_name [replace with the name for the git repo]:
Select bug_tracker:
1 - Launchpad
2 - Storyboard
Choose from 1, 2 [1]: 2
bug_project [replace with the name of the project on Launchpad or the ID from Storyboard]:
project_short_description [OpenStack Boilerplate contains all the boilerplate you need to create an OpenStack package.]:
Unable to create file 'CONTRIBUTING.rst'
Error message: 'cookiebutter' is undefined
Context: {
    "cookiecutter": {
        "_template": "https://git.openstack.org/openstack-dev/cookiecutter.git",
        "bug_project": "replace with the name of the project on Launchpad or the ID from Storyboard",
        "bug_tracker": "Storyboard",
        "module_name": "replace with the name of the python module",
        "project_short_description": "OpenStack Boilerplate contains all the boilerplate you need to create an OpenStack package.",
        "repo_group": "openstack",
        "repo_name": "replace with the name for the git repo",
        "service": "replace with the service it implements"
    }
}
1(.venv)[master][centos@mkopec-test tempest-plugin-demo]$ ls -all
total 24
drwxrwxr-x.  4 centos centos    76 May 20 11:09 .
drwx------. 13 centos centos  4096 May 20 11:09 ..
drwxrwxr-x.  8 centos centos  4096 May 20 11:09 .git
-rw-rw-r--.  1 centos centos  1203 May 20 10:21 .gitignore
-rw-rw-r--.  1 centos centos 11357 May 20 10:21 LICENSE
-rw-rw-r--.  1 centos centos     0 May 20 10:21 README.md
drwxrwxr-x.  5 centos centos    77 May 20 10:40 .venv
(.venv)[master][centos@mkopec-test tempest-plugin-demo]$ cd ../.cookiecutters/cookiecutter/
(.venv)[master !][centos@mkopec-test cookiecutter]$ vim \{\{cookiecutter.repo_name\}\}/CONTRIBUTING.rst
(.venv)[master !][centos@mkopec-test cookiecutter]$ git status
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#   modified:   cookiecutter.json
#   modified:   {{cookiecutter.repo_name}}/CONTRIBUTING.rst
#
no changes added to commit (use "git add" and/or "git commit -a")
(.venv)[master !][centos@mkopec-test cookiecutter]$ git diff
diff --git a/cookiecutter.json b/cookiecutter.json
index 3214c3b..7e8c14e 100644
--- a/cookiecutter.json
+++ b/cookiecutter.json
@@ -3,7 +3,7 @@
        "service": "replace with the service it implements",
        "repo_group": "openstack",
        "repo_name": "replace with the name for the git repo",
-       "bug_tracker": ['Launchpad', 'Storyboard'],
+       "bug_tracker": ["Launchpad", "Storyboard"],
        "bug_project": "replace with the name of the project on Launchpad or the ID from Storyboard",
        "project_short_description": "OpenStack Boilerplate contains all the boilerplate you need to create an OpenStack package."
 }
diff --git a/{{cookiecutter.repo_name}}/CONTRIBUTING.rst b/{{cookiecutter.repo_name}}/CONTRIBUTING.rst
index 0a7c263..86b0c18 100644
--- a/{{cookiecutter.repo_name}}/CONTRIBUTING.rst
+++ b/{{cookiecutter.repo_name}}/CONTRIBUTING.rst
@@ -12,7 +12,7 @@ submitted for review via the Gerrit tool:

 Pull requests submitted through GitHub will be ignored.

-Bugs should be filed on {{ cookiebutter.bug_tracker }}
+Bugs should be filed on {{ cookiecutter.bug_tracker }}

 {%- if cookiecutter.bug_tracker == 'Launchpad' -%}
    https://bugs.launchpad.net/{{ cookiecutter.bug_project }}
(.venv)[master !][centos@mkopec-test cookiecutter]$ cd ../../tempest-plugin-demo/
(.venv)[master][centos@mkopec-test tempest-plugin-demo]$ cookiecutter https://git.openstack.org/openstack-dev/cookiecutter.git
You've downloaded /home/centos/.cookiecutters/cookiecutter before. Is it okay to delete and re-download it? [yes]: no
Do you want to re-use the existing version? [yes]: yes
module_name [replace with the name of the python module]:
service [replace with the service it implements]:
repo_group [openstack]:
repo_name [replace with the name for the git repo]:
Select bug_tracker:
1 - Launchpad
2 - Storyboard
Choose from 1, 2 [1]: 2
bug_project [replace with the name of the project on Launchpad or the ID from Storyboard]:
project_short_description [OpenStack Boilerplate contains all the boilerplate you need to create an OpenStack package.]:
Initialized empty Git repository in /home/centos/tempest-plugin-demo/replace with the name for the git repo/.git/
[master (root-commit) c36263b] Initial Cookiecutter Commit.
 Committer: Cloud User <centos@mkopec-test.localdomain>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 46 files changed, 1217 insertions(+)
 create mode 100644 .coveragerc
 create mode 100644 .gitignore
 create mode 100644 .gitreview
 create mode 100644 .mailmap
 create mode 100644 .stestr.conf
 create mode 100644 CONTRIBUTING.rst
 create mode 100644 HACKING.rst
 create mode 100644 LICENSE
 create mode 100644 README.rst
 create mode 100644 babel.cfg
 create mode 100644 doc/source/admin/index.rst
 create mode 100644 doc/source/cli/index.rst
 create mode 100755 doc/source/conf.py
 create mode 100644 doc/source/configuration/index.rst
 create mode 100644 doc/source/contributor/contributing.rst
 create mode 100644 doc/source/contributor/index.rst
 create mode 100644 doc/source/index.rst
 create mode 100644 doc/source/install/common_configure.rst
 create mode 100644 doc/source/install/common_prerequisites.rst
 create mode 100644 doc/source/install/get_started.rst
 create mode 100644 doc/source/install/index.rst
 create mode 100644 doc/source/install/install-obs.rst
 create mode 100644 doc/source/install/install-rdo.rst
 create mode 100644 doc/source/install/install-ubuntu.rst
 create mode 100644 doc/source/install/install.rst
 create mode 100644 doc/source/install/next-steps.rst
 create mode 100644 doc/source/install/verify.rst
 create mode 100644 doc/source/library/index.rst
 create mode 100644 doc/source/readme.rst
 create mode 100644 doc/source/reference/index.rst
 create mode 100644 doc/source/user/index.rst
 create mode 100644 releasenotes/notes/.placeholder
 create mode 100644 releasenotes/source/_static/.placeholder
 create mode 100644 releasenotes/source/_templates/.placeholder
 create mode 100644 releasenotes/source/conf.py
 create mode 100644 releasenotes/source/index.rst
 create mode 100644 releasenotes/source/unreleased.rst
 create mode 100644 replace with the name of the python module/__init__.py
 create mode 100644 replace with the name of the python module/tests/__init__.py
 create mode 100644 replace with the name of the python module/tests/base.py
 create mode 100644 replace with the name of the python module/tests/test_replace with the name of the python module.py
 create mode 100644 requirements.txt
 create mode 100644 setup.cfg
 create mode 100644 setup.py
 create mode 100644 test-requirements.txt
 create mode 100644 tox.ini
(.venv)[master ?][centos@mkopec-test tempest-plugin-demo]$ ls -all
total 32
drwxrwxr-x.  5 centos centos  4096 May 20 11:10 .
drwx------. 13 centos centos  4096 May 20 11:10 ..
drwxrwxr-x.  8 centos centos  4096 May 20 11:10 .git
-rw-rw-r--.  1 centos centos  1203 May 20 10:21 .gitignore
-rw-rw-r--.  1 centos centos 11357 May 20 10:21 LICENSE
-rw-rw-r--.  1 centos centos     0 May 20 10:21 README.md
drwxrwxr-x.  6 centos centos  4096 May 20 11:10 replace with the name for the git repo
drwxrwxr-x.  5 centos centos    77 May 20 10:40 .venv
(.venv)[master ?][centos@mkopec-test tempest-plugin-demo]$
```

