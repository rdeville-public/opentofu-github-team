# Configure the Github Provider
terraform {
  required_version = ">= 1.8, < 2.0"
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~>6.2"
    }
  }
}
