<!-- BEGIN DOTGIT-SYNC BLOCK MANAGED -->
# 👋 Welcome to OpenTofu Module Github Teams

<center>

> ⚠️ IMPORTANT !
>
> Main repo is on [framagit.org](https://framagit.org/rdeville-public/terraform/module-github-teams).
>
> On other online git platforms, they are just mirror of the main repo.
>
> Any issues, pull/merge requests, etc., might not be considered on those other
> platforms.

</center>

---

<center>

[![Licenses: (MIT OR BEERWARE)][license_badge]][license_url]
[![Changelog][changelog_badge]][changelog_badge_url]
[![Build][build_badge]][build_badge_url]
[![Release][release_badge]][release_badge_url]

</center>

[build_badge]: https://framagit.org/rdeville-public/terraform/module-github-teams/badges/main/pipeline.svg
[build_badge_url]: https://framagit.org/rdeville-public/terraform/module-github-teams/-/commits/main
[release_badge]: https://framagit.org/rdeville-public/terraform/module-github-teams/-/badges/release.svg
[release_badge_url]: https://framagit.org/rdeville-public/terraform/module-github-teams/-/releases/
[license_badge]: https://img.shields.io/badge/Licenses-MIT%20OR%20BEERWARE-blue
[license_url]: https://framagit.org/rdeville-public/terraform/module-github-teams/blob/main/LICENSE
[changelog_badge]: https://img.shields.io/badge/Changelog-Python%20Semantic%20Release-yellow
[changelog_badge_url]: https://github.com/python-semantic-release/python-semantic-release

OpenTofu modules allowing to manage github repository configuration.

---
<!-- BEGIN DOTGIT-SYNC BLOCK EXCLUDED CUSTOM_README -->
## 🚀 Usage

### Deploy a team

Not very usefull without members, but who knows, may be usefull as a parent
team.

```hcl
module "team" {
  source = "git::https://framagit.org/rdeville-public/terraform/module-github-team.git"

  # Required variables
  name        = "My Awesome Team"
  description = "Team of best people in the world"
}
```

### Deploy closed nested team

Not very usefull without members, but who knows, may be usefull as a parent
team.

```hcl
module "team" {
  source = "git::https://framagit.org/rdeville-public/terraform/module-github-team.git"

  # Required variables
  name        = "My Awesome Team"
  description = "Team of best people in the world"
}

module "nested_team" {
  source = "git::https://framagit.org/rdeville-public/terraform/module-github-team.git"

  # Required variables
  name        = "My Awesome Team"
  description = "Team of best people in the world"

  # Example values
  parent_team_id = module.team.id
  privacy        = "closed"
}
```

### Deploy a team with members and maintainers

```hcl
module "team" {
  source = "git::https://framagit.org/rdeville-public/terraform/module-github-team.git"

  # Required variables
  name        = "My Awesome Team"
  description = "Team of best people in the world"

  # Example values
  members = [
    "username"
    "anotherUsername"
  ]
  maintainers = [
    "doomGuy"
    "elisabeth"
  ]
}
```

### Deploy a team with members, maintainers and review delegation

```hcl
module "team" {
  source = "git::https://framagit.org/rdeville-public/terraform/module-github-team.git"

  # Required variables
  name        = "My Awesome Team"
  description = "Team of best people in the world"

  # Example values
  members = [
    "username"
    "anotherUsername"
  ]
  maintainers = [
    "doomGuy"
    "elisabeth"
  ]
  review_delegation_enabled = true
  # Default values if activated
  review_delegation_algorithm    = "ROUND_ROBIN"
  review_delegation_member_count = 1
  review_delegation_notify       = true
}
```

<!-- BEGIN TF-DOCS -->
## ⚙️ Module Content

<details><summary>Click to reveal</summary>

### Table of Content

* [Requirements](#requirements)
* [Resources](#resources)
* [Inputs](#inputs)
  * [Required Inputs](#required-inputs)
  * [Optional Inputs](#optional-inputs)
* [Outputs](#outputs)

### Requirements

* [opentofu](https://opentofu.org/docs/):
  `>= 1.8, < 2.0`
* [github](https://registry.terraform.io/providers/integrations/github/):
  `~>6.2`

### Resources

* [resource.github_team.this](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/team)
  > Manage a single team
* [resource.github_team_members.this](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/team_members)
  > Manage members and maintainers of the team
* [resource.github_team_settings.this](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/team_settings)
  > Manage review_delegation of the team

<!-- markdownlint-capture -->
### Inputs

<!-- markdownlint-disable -->
#### Required Inputs

* [name](#name)
* [description](#description)

##### `name`

String, Name of the team
<div style="display:inline-block;width:100%;">
<div style="float:left;border-color:#FFFFFF;width:75%;">
<details><summary>Type</summary>

```hcl
string
```

</details>
</div>
</div>

##### `description`

String, Description of the team
<div style="display:inline-block;width:100%;">
<div style="float:left;border-color:#FFFFFF;width:75%;">
<details><summary>Type</summary>

```hcl
string
```

</details>
</div>
</div>

#### Optional Inputs

* [privacy](#privacy)
* [parent_team_id](#parent_team_id)
* [members](#members)
* [maintainers](#maintainers)
* [review_delegation_enabled](#review_delegation_enabled)
* [review_delegation_algorithm](#review_delegation_algorithm)
* [review_delegation_member_count](#review_delegation_member_count)
* [review_delegation_notify](#review_delegation_notify)


##### `privacy`

String, Level of privacy for the team. Must be one of `secret` or `closed`.
<details style="width: 100%;display: inline-block">
  <summary>Type & Default</summary>
  <div style="height: 1em"></div>
  <div style="width:64%; float:left;">
  <p style="border-bottom: 1px solid #333333;">Type</p>

  ```hcl
  string
  ```

  </div>
  <div style="width:34%;float:right;">
  <p style="border-bottom: 1px solid #333333;">Default</p>

  ```hcl
  secret
  ```

  </div>
</details>

##### `parent_team_id`

String, The ID or slug of the parent team, if this is a nested team.
<details style="width: 100%;display: inline-block">
  <summary>Type & Default</summary>
  <div style="height: 1em"></div>
  <div style="width:64%; float:left;">
  <p style="border-bottom: 1px solid #333333;">Type</p>

  ```hcl
  string
  ```

  </div>
  <div style="width:34%;float:right;">
  <p style="border-bottom: 1px solid #333333;">Default</p>

  ```hcl
  null
  ```

  </div>
</details>

##### `members`

List of string, usernames with role `members` in the team.
<details style="width: 100%;display: inline-block">
  <summary>Type & Default</summary>
  <div style="height: 1em"></div>
  <div style="width:64%; float:left;">
  <p style="border-bottom: 1px solid #333333;">Type</p>

  ```hcl
  list(string)
  ```

  </div>
  <div style="width:34%;float:right;">
  <p style="border-bottom: 1px solid #333333;">Default</p>

  ```hcl
  []
  ```

  </div>
</details>

##### `maintainers`

List of string, usernames with role `maintainers` in the team.
<details style="width: 100%;display: inline-block">
  <summary>Type & Default</summary>
  <div style="height: 1em"></div>
  <div style="width:64%; float:left;">
  <p style="border-bottom: 1px solid #333333;">Type</p>

  ```hcl
  list(string)
  ```

  </div>
  <div style="width:34%;float:right;">
  <p style="border-bottom: 1px solid #333333;">Default</p>

  ```hcl
  []
  ```

  </div>
</details>

##### `review_delegation_enabled`

Boolean, Activate the settings for delegating code reviews to individuals on
behalf of the team. If this boolean is set to `true`, this will activate code
reviews delegation and related block.

If block is present, even without any fields, then review request delegation
will be enabled for the team.

See [GitHub's documentation](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-code-review-settings-for-your-team#configuring-team-notifications)
for more configuration details.

<details style="width: 100%;display: inline-block">
  <summary>Type & Default</summary>
  <div style="height: 1em"></div>
  <div style="width:64%; float:left;">
  <p style="border-bottom: 1px solid #333333;">Type</p>

  ```hcl
  bool
  ```

  </div>
  <div style="width:34%;float:right;">
  <p style="border-bottom: 1px solid #333333;">Default</p>

  ```hcl
  false
  ```

  </div>
</details>

##### `review_delegation_algorithm`

String, The algorithm to use when assigning pull requests to team members.
Supported values are `ROUND_ROBIN` and `LOAD_BALANCE`.

<details style="width: 100%;display: inline-block">
  <summary>Type & Default</summary>
  <div style="height: 1em"></div>
  <div style="width:64%; float:left;">
  <p style="border-bottom: 1px solid #333333;">Type</p>

  ```hcl
  string
  ```

  </div>
  <div style="width:34%;float:right;">
  <p style="border-bottom: 1px solid #333333;">Default</p>

  ```hcl
  ROUND_ROBIN
  ```

  </div>
</details>

##### `review_delegation_member_count`

Number, The number of team members to assign to a pull request
<details style="width: 100%;display: inline-block">
  <summary>Type & Default</summary>
  <div style="height: 1em"></div>
  <div style="width:64%; float:left;">
  <p style="border-bottom: 1px solid #333333;">Type</p>

  ```hcl
  number
  ```

  </div>
  <div style="width:34%;float:right;">
  <p style="border-bottom: 1px solid #333333;">Default</p>

  ```hcl
  1
  ```

  </div>
</details>

##### `review_delegation_notify`

Boolean, whether to notify the entire team when at least one member is also
assigned to the pull request

<details style="width: 100%;display: inline-block">
  <summary>Type & Default</summary>
  <div style="height: 1em"></div>
  <div style="width:64%; float:left;">
  <p style="border-bottom: 1px solid #333333;">Type</p>

  ```hcl
  bool
  ```

  </div>
  <div style="width:34%;float:right;">
  <p style="border-bottom: 1px solid #333333;">Default</p>

  ```hcl
  true
  ```

  </div>
</details>
<!-- markdownlint-restore -->

### Outputs

* `id`:
  ID of the team deployed

</details>

<!-- END TF-DOCS -->
<!-- END DOTGIT-SYNC BLOCK EXCLUDED CUSTOM_README -->
## 🤝 Contributing

Contributions, issues and feature requests are welcome!

Feel free to check [issues page][issues_pages].

You can also take a look at the [CONTRIBUTING.md][contributing].

[issues_pages]: https://framagit.org/rdeville-public/terraform/module-github-teams/-/issues
[contributing]: https://framagit.org/rdeville-public/terraform/module-github-teams/blob/main/CONTRIBUTING.md

## 👤 Maintainers

* 📧 [**Romain Deville** \<code@romaindeville.fr\>](mailto:code@romaindeville.fr)
  * Website: [https://romaindeville.fr](https://romaindeville.fr)
  * Github: [@rdeville](https://github.com/rdeville)
  * Gitlab: [@r.deville](https://gitlab.com/r.deville)
  * Framagit: [@rdeville](https://framagit.org/rdeville)

## 📝 License

Copyright © 2024 [Romain Deville](code@romaindeville.fr)

This project is under following licenses (**OR**) :

* [MIT][main_license]
* [BEERWARE][beerware_license]

[main_license]: https://framagit.org/rdeville-public/terraform/module-github-teams/blob/main/LICENSE
[beerware_license]: https://framagit.org/rdeville-public/terraform/module-github-teams/blob/main/LICENSE.BEERWARE
<!-- END DOTGIT-SYNC BLOCK MANAGED -->
