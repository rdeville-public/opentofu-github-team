variable "name" {
  type        = string
  description = "String, Name of the team"
}

variable "description" {
  type        = string
  description = "String, Description of the team"
}

variable "privacy" {
  type        = string
  description = "String, Level of privacy for the team. Must be one of `secret` or `closed`."

  nullable = false
  default  = "secret"
}

variable "parent_team_id" {
  type        = string
  description = "String, The ID or slug of the parent team, if this is a nested team."

  nullable = true
  default  = null
}

variable "members" {
  type        = list(string)
  description = "List of string, usernames with role `members` in the team."

  nullable = false
  default  = []
}

variable "maintainers" {
  type        = list(string)
  description = "List of string, usernames with role `maintainers` in the team."

  nullable = false
  default  = []
}

variable "review_delegation_enabled" {
  type        = bool
  description = <<-EOM
  Boolean, Activate the settings for delegating code reviews to individuals on
  behalf of the team. If this boolean is set to `true`, this will activate code
  reviews delegation and related block.

  If block is present, even without any fields, then review request delegation
  will be enabled for the team.

  See [GitHub's documentation](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-code-review-settings-for-your-team#configuring-team-notifications)
  for more configuration details.
  EOM

  nullable = false
  default  = false
}

variable "review_delegation_algorithm" {
  type        = string
  description = <<-EOM
  String, The algorithm to use when assigning pull requests to team members.
  Supported values are `ROUND_ROBIN` and `LOAD_BALANCE`.
  EOM

  nullable = false
  default  = "ROUND_ROBIN"
}

variable "review_delegation_member_count" {
  type        = number
  description = "Number, The number of team members to assign to a pull request"

  nullable = false
  default  = 1
}

variable "review_delegation_notify" {
  type        = bool
  description = <<-EOM
  Boolean, whether to notify the entire team when at least one member is also
  assigned to the pull request
  EOM

  nullable = false
  default  = true
}
