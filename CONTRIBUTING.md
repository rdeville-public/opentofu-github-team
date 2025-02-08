<!-- BEGIN DOTGIT-SYNC BLOCK MANAGED -->
<!-- markdownlint-disable -->
# Contributing to OpenTofu Module Github Teams

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued.
See the [Table of Contents](#table-of-contents) for different ways to help and
details about how this project handles them.
Please make sure to read the relevant section before making your contribution.
It will make it a lot easier for us maintainers and smooth out the experience
for all involved.

The community looks forward to your contributions. 🎉

> And if you like the project, but just don't have time to contribute, that's
> fine.
> There are other easy ways to support the project and show your appreciation,
> which we would also be very happy about:
>
> - Star the project
> - Tweet about it
> - Refer this project in your project's readme
> - Mention the project at local meetups and tell your friends/colleagues

## Table of Contents
<!-- mdtoc-start -->

* [Code Of Conduct](#code-of-conduct)
* [I Have A Question](#i-have-a-question)
* [I Want To Contribute](#i-want-to-contribute)
  * [Legal Notice](#legal-notice)
  * [Reporting Bugs](#reporting-bugs)
    * [Before Submitting A Bug Report](#before-submitting-a-bug-report)
    * [How Do I Submit A Good Bug Report?](#how-do-i-submit-a-good-bug-report)
  * [Suggesting Enhancements](#suggesting-enhancements)
    * [Before Submitting An Enhancement](#before-submitting-an-enhancement)
    * [How Do I Submit A Good Enhancement Suggestion?](#how-do-i-submit-a-good-enhancement-suggestion)
    * [Which Ide/Text Editor Should I Use ?](#which-idetext-editor-should-i-use-)
  * [Your First Code Contribution](#your-first-code-contribution)
    * [Create Your Own Fork](#create-your-own-fork)
    * [Setup Development Environment](#setup-development-environment)
  * [Improving The Documentation](#improving-the-documentation)
    * [No `Docs` Folder In The Repo](#no-docs-folder-in-the-repo)
    * [`Docs` Folder In The Repo](#docs-folder-in-the-repo)
* [Styleguides](#styleguides)
  * [Language Specific](#language-specific)
  * [Branches Names](#branches-names)
  * [Commit Messages](#commit-messages)
  * [Merge Requests / Pull Requests (Mr/Pr)](#merge-requests--pull-requests-mrpr)
* [Join The Project Team](#join-the-project-team)
* [Attribution](#attribution)

<!-- mdtoc-end -->
## Code of Conduct

This project and everyone participating in it is governed by the [Code of
Conduct][CODE_OF_CONDUCT]. By participating, you are expected to uphold this
code.

Please report unacceptable behavior to :
* [📧 abuse+code@romaindeville.fr \<abuse+code@romaindeville.fr\>](mailto:abuse+code@romaindeville.fr)

## I Have a Question

> If you want to ask a question, we assume that you have read the available
> [Documentation][documentation].

Before you ask a question, it is best to search for existing
[issues][issues_page] that might help you.
In case you have found a suitable issue and still need clarification, you can
write your question in this issue.
It is also advisable to search the internet for answers first.

If you then still feel the need to ask a question and need clarification, we
recommend the following:

- Open an [new issue][new_issues_page].
- Provide as much context as you can about what you're running into.
- Provide project and platform versions depending on what seems relevant.

We will then take care of the issue as soon as possible.

## I Want To Contribute

### Legal Notice

When contributing to this project, you must agree that you have authored 100% of
the content, that you have the necessary rights to the content and that the
content you contribute may be provided under the project licence.

> ⚠️ REMARK
>
> If this repo is either :
>
> - Under copyright (either personal or belong to an organization)
> - Not licensed or does not have an open-source or free license
>
> Please, do not send its code or any of its content (such as documentation)
> to an "Artificial Intelligence" provided by a private company through a SaaS
> (such as Copilot, etc) to help you to contribute.
>
> The aim of such notice is to avoid leaking private code to a company without
> copyright agreements or code usage agreements.
>
> While we are not currently unable to test weither you use such tools or not,
> this notice is solely based on trust.
>
> However, you are free to use an "AI" if you self-host such tools or are sure
> that there is (almost) absolutely no risks of content leakage.

### Reporting Bugs

#### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more
information.
Therefore, we ask you to investigate carefully, collect information and describe
the issue in detail in your report.
Please complete the following steps in advance to help us fix any potential bug
as fast as possible.

- Make sure that you are using the latest version of the repo.
- Determine if your bug is really a bug and not an error on your side, e.g.
  using incompatible environment components/versions (Make sure that you have
  read the [documentation][documentation]. If you are looking for support, you
  might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the
  same issue you are having, check if there is not already a bug report existing
  for your bug or error in the [bug tracker][bug_tracker_opened_issues].
- Also make sure to search the internet (including Stack Overflow) to see if
  users outside of the GitHub community have discussed the issue.
- Collect information about the bug:
  - Stack trace (Traceback)
  - OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
  - Version of the interpreter, compiler, SDK, runtime environment, package
    manager, depending on what seems relevant.
  - Possibly your input and the output
- Can you reliably reproduce the issue? And can you also reproduce it with older
  versions?

[bug_tracker_opened_issues]: https://framagit.org/rdeville-public/opentofu/github-teams/issues/?sort=created_date&state=opened&or[label_name][]=Type%3A%3ABug&or[label_name][]=Type%3A%3ARegression&first_page_size=200

#### How Do I Submit a Good Bug Report?

> 🚨 Security Concern
>
> You must never report security related issues, vulnerabilities or bugs
> including sensitive information to the issue tracker, or elsewhere in public.
> Instead sensitive issues must be sent by email to any of the maintainers :
>
> * [📧 Romain Deville \<code@romaindeville.fr\>](mailto:code@romaindeville.fr)

We use issues to track bugs and errors.
If you run into an issue with the project:

- Open an [Issue][new_issues_page]. Since we can't be sure at this point
  whether it is a bug or not, we ask you not to talk about a bug yet and not to
  label the issue.
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the **reproduction
  steps** that someone else can follow to recreate the issue on their own.
  This usually includes your code.
  For good bug reports you should isolate the problem and create a reduced
  test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps.
  If there are no reproduction steps or no obvious way to reproduce the issue,
  the team will ask you for those steps and label the issue accordingly.
  Such issues will not be addressed until either **reproduction
  steps** are provided or until they are reproduced.
- If the team is able to reproduce the issue, label of the issue will be updated
  accordingly as well as possibly other tags, and the issue will be left to be
  [implemented by someone](#your-first-code-contribution).

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for
OpenTofu Module Github Teams, **including completely new features and minor improvements to
existing functionality**. Following these guidelines will help maintainers and
the community to understand your suggestion and find related suggestions.

#### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation][documentation] carefully and find out if the
  functionality is already covered, maybe by an individual configuration.
- Perform a [search among issues][issues_page] to see if the enhancement has
  already been suggested.
  If it has, simply add 👍 reaction to the existing issue to notify us of your
  interest (**REMARK: Any comment with only this emoji, or other reaction emoji
  will be deleted**) or comment the existing issue if you want to provide more
  information to complete the issue details.
- Find out whether your idea fits with the scope and aims of the project. It's
  up to you to make a strong case to convince the project's developers of the
  merits of this feature. Keep in mind that we want features that will be useful
  to the majority of our users and not just a small subset. If you're just
  targeting a minority of users, consider writing an add-on/plugin library if
  the project provide such functionality.

[issues_page]: https://framagit.org/rdeville-public/opentofu/github-teams/-/issues

#### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as [issues][issues_page].

- Use a **clear and descriptive title** for the issue to identify the
  suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many
  details as possible.
- **Describe the current behavior** and **explain which behavior you expected to
  see instead** and why. At this point you can also tell which alternatives do not
  work for you.
- You may want to **include screenshots or screen recordings** which help you
  demonstrate the steps or point out the part which the suggestion is related to.
  Please provide such media as ligthweight as possible (through GIFs for
  instance).
- **Explain why this enhancement would be useful** to most OpenTofu Module Github Teams users. You
  may also want to point out the other projects that solved it better and which
  could serve as inspiration.

#### Which IDE/Text editor should I use ?

If you want to contribute, you can use any IDE or text editor you want (vim,
emacs, vscode, phpstorm, notepad, notepad++, etc).

Configuration Dotfiles (usually files starting with a dot, `.`, e.g.
`.editorconfig`) should be IDE agnostics.

The repo **WILL NEVER store IDE spcific files** such as `.vscode/`,
`.vimrc.local`, etc. Normally, this should be ensure with the `.gitignore` file.
Any contribution adding those files will automatically be refused while these
files are present.

The aim of this rule is to let anyone use his/her prefer IDE/Text editor with
his/her preferred plugins.

The only optional constraint is that your IDE with its plugins should be able to
read provided dotfiles (such as `.editorconfig`, `.eslintrc`, `.yamllint`, etc)
to conform to the repository [Styleguides](#styleguides).

Nevertheless, if your IDE is not able to respect configuration dotfiles,
compliancy agains this configuration dotfiles will solely rely on you.

If you are not sure if you manage to be compliant with the configuration
dotfiles, the CI will ensure it, i.e. the CI will fail if your contribution does
not respect configuration dotfiles.

### Your First Code Contribution

#### Create your own fork

Unless you are able to create branch on the main repository, to contribute, you
will need to create of fork of this repository. Then we strongly encourage you
to create a developpement branch (and if you want, following the [Branches Names
Styleguide](#branches-names)).
This will allow you to be able to fetch the default branch of the repository to
your own fork without messing with your future contribution.

Once done, you can work on your own fork/branch and add commit following [Commit
Messages Styleguides](#commit-messages).

Finally, once you think your work is ready to be merge, you can open a Merge
Request / Pull Request to the main repository. Your MR/PR must follow [Merge
Requests / Pull Requests Styleguides](#merge-requests--pull-requests-mrpr)

#### Setup development environment

In order to setup your development environment, please refers to the repository
[documentation][documentation] or the [README][README] of the repository. There should be instruction about
installing development environment and runnings tests normally.

If not, does not hesitate to open an [issue][new_issues_page] to ask maintainers
to provide some.

[new_issues_page]: https://framagit.org/rdeville-public/opentofu/github-teams/-/issues/new

### Improving The Documentation

#### No `docs` folder in the repo

If no folder `docs` is present in the repo, the documentation rely only in the
README of the repo as well as some other files such as CODE_OF_CONDUCT or
CONTRIBUTING. These file are partially (or entirely) managed by an external tool
called [dotgit-sync][dgs] which allow us to propagate templated files among
multiple repos.
Depending on which part of the file you want to improve, the contribution
process is not the same:

- If you want to update content between excluded block tag (see example code
  below), you can do it directly on the README since content below tags are
  excluded from dotgit-sync management.

  ```markdown
<!-- BEGIN DOTGIT-SYNC BLOCK EXCLUDED CUSTOM_README -->

  Some README content excluded from dotgit-sync management

<!-- END DOTGIT-SYNC BLOCK EXCLUDED CUSTOM_README -->

  This content, outside exclusion tags, is also managed in the dotgit-sync-templates
  repository.
  ```

[dgs]: https://framagit.org/rdeville-public/programs/dotgit-sync

#### `docs` folder in the repo

If `docs` is present in the repo, then documentation improvement should mainly
be in this folder.

> If improvement concerns other files not in this folder, such as README,
> CODE_OF_CONDUCT or CONTRIBUTING, please refer to the [previous
> section](#no-docs-folder-in-the-repo).

Contribution to documentation within this folder should be done through a Merge
Request / Pull Request according to provided [Styleguides](#styleguides).

## Styleguides

### Language Specific

Basic language styleguides are provided by `.editorconfig` file.

Language specific styleguides are normally specify either in :

- STYLEGUIDE file at the root of the repo
- Styleguide section of the documentation

If not, check if there is some "dotfiles" (i.e. file usually starting with a dot,
`.`, e.g. `.editorconfig`) at the root of the repository for the language used
in the reposiotory (e.g. `.eslintrc` for node, `.pylint` for python, `.tf-lint`
for hcl files, `.yamllint` for yaml files, `.markdownlint` for markdown, etc)
which will describe styleguides applied to the repository.

If any of the above does not exists, you can follow existing codes
styleguides by reading through the code and/or contribute to the repository to
propose a styleguide through an new issue or a new Merge Request / Pull Request.

### Branches Names

Some branches, tags or releases names are protected and can only be created by
either maintainers or bots. These are :

- Branches:
  - `main`, usually the default branch,
  - `release/*`, usually the branch use to track releases,
- Tags/Releases:
  - `v*`, creating when releasing repository
  - `*`, forbidden

In other case, you are free to use any branch naming you want as long as its
start with a semantic word, for instances :

- `feat/add-my-new-feat`
- `feat/improve-documentation`
- `fix/external-api-chagnes`
- `chore/fix-typo`
- `chore/bump-dep-versions`

**REMARK**: This only apply to people who are able to create branch on the main
repository. If you contribute through a fork, you are free to use any branch
naming you want on you own fork.

### Commit Messages

Commits should be **atomic**, **specific** and **linear**.
Do not hesitate to rework your git commit history.

This project follows [gitmoji specification](https://gitmoji.dev/specification)
for its commit message, i.e. (from gitmoji specifications):

> A gitmoji commit message consists is composed using the following pieces:
>
> - intention: The intention you want to express with the commit, using an
>   emoji from the list. Either in the :shortcode: or unicode format.
> - scope: An optional string that adds contextual information for the scope of
>   the change.
> - message: A brief explanation of the change.
> - body: A optional more detailled message about the change
>
> ```text
> <intention> [scope?][:?] <message>
>
> Commit Body
> ```
>
> Examples
>
> - ⚡️ Lazyload home screen images.
> - 🐛 Fix `onClick` event handler
> - 🔖 Bump version `1.2.0`
> - ♻️ (components): Transform classes to hooks
> - 📈 Add analytics to the dashboard
> - 🌐 Support Japanese language
> - ♿️ (account): Improve modals a11y

Prefer using **unicode** char as `<intention>` instead of shortcode.

Commit message format are enforced by a CI, if any your commit does not follow
this guideline, the CI will fail and your contribution will not be able to be
merged to the target ref.

**Why using Gitmoji ?**

Tags and releases versionning of the repos is done via parsing list of commits
since the last released. Depending on Gitmoji used, tags and releases will
automatically updated according to the semantic versionning definition provided
by the [gitmoji.json][gitmoji_json_semver] file provided by the gitmoji repository.

[gitmoji_json_semver]: https://github.com/carloscuesta/gitmoji/blob/master/packages/gitmojis/src/gitmojis.json

### Merge Requests / Pull Requests (MR/PR)

Every contribution should be done via a Merge Request / Pull Request. It is
forbidden to commit directly to the default or releases branches, even for
maintainers (unless exceptional and urgent fix is needed).

The Merge Request / Pull Requests should create a merge commit (unless specify
by maintainers) and should not squash commits (as the commits are needed for the
tags/releases automatic versionning).

CI will only run on MR/PR proposed to the repos either automatically or on
demand depending on the repo configuration.

Usually, MR/PR will not be merged if the following conditions are not met:

- CI Pipelines **MUST SUCCED** (unless specify by maintainers)
- All discussions **MUST BE RESOLVED**
- MR/PR is **UP-TO-DATE** against the target ref (unless specify, for instance,
  if project reach critical number of contribution/contributor and this rules is
  not manageable anymore).
- Last commit should be **APPROUVED** by a maintainer.

Moreover, MR/PR title must also follow [Commit Message](#commit-messages)
styleguide, since the MR/PR will generate a commit used to automatic
tags/releases versionning.

Finally, in the body of the MR/PR describe in details (if needed) what your
MR/PR add to the repository and if it resolves an existing issue, please mention
it in the description following [Gitlab closing pattern][gitlab_closing_pattern].

Below is a example of MR/PR commit (title and body of the commit being
respectively the title and the body of the MR/PR):

```text
✨(scope): Add best feature of the world

This add the ability to manage X while not creating conflict with Y.

Fixes #<issue_number> #<another_issue_number>
```

[gitlab_closing_pattern]: https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#default-closing-pattern

## Join The Project Team

If you want to join the project team, please contact by email any of the
maintainers with the following email title :

```text
[OpenTofu Module Github Teams] - Join The Project Team
```

The content of the email is left to you. For instance, you can provide :

- A list (exhaustive or not) of your contribution,
- Your motivation,
- The role that interest you (i.e. issues triage, MR/PR reviewer on all the
  code, only the documentation, maintainer, etc)

This will allow to start a discussion with you and the maintainers to decide if
you will be able to join the project team and specify which roles will be
attributed to you.

## Attribution

This guide is adapted from the generator provided on the
[contributing.md](https://contributing.md/generator) that we gladly thanks ❤️!

[README]: https://framagit.org/rdeville-public/opentofu/github-teams/-/blob/main/README.md
[CODE_OF_CONDUCT]: https://framagit.org/rdeville-public/opentofu/github-teams/-/blob/main/CODE_OF_CONDUCT.md
[documentation]: https://framagit.org/rdeville-public/opentofu/github-teams
<!-- END DOTGIT-SYNC BLOCK MANAGED -->
