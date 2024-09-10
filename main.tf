# Manage a single team
resource "github_team" "this" {
  name           = var.name
  description    = var.description
  privacy        = var.privacy
  parent_team_id = var.parent_team_id
}

# Manage members and maintainers of the team
resource "github_team_members" "this" {
  team_id = github_team.this.id

  dynamic "members" {
    for_each = var.members

    content {
      username = members.key
      role     = "member"
    }
  }

  dynamic "members" {
    for_each = var.maintainers

    content {
      username = members.key
      role     = "maintainer"
    }
  }
}

# Manage review_delegation of the team
resource "github_team_settings" "this" {
  count = var.review_delegation_enabled ? 1 : 0

  team_id = github_team.this.id

  review_request_delegation {
    algorithm    = var.review_delegation_algorithm
    member_count = var.review_delegation_member_count
    notify       = var.review_delegation_notify
  }
}
