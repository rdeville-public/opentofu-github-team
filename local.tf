locals {
  # Remove maintainers from members
  members = setsubtract(var.members, var.maintainers)
}
