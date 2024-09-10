# BEGIN DOTGIT-SYNC BLOCK MANAGED
"""Commit parser which looks for gitmojis to determine the type of commit."""

import logging
from typing import Tuple

from git.objects.commit import Commit
from pydantic.dataclasses import dataclass
import requests
from semantic_release.commit_parser._base import (
    CommitParser,  # noqa: PLC2701
    ParserOptions,  # noqa: PLC2701
)
from semantic_release.commit_parser.token import (
    ParsedCommit,
    ParseResult,
)
from semantic_release.commit_parser.util import parse_paragraphs
from semantic_release.enums import LevelBump


logger = logging.getLogger(__name__)

GITMOJIS = "https://raw.githubusercontent.com/carloscuesta/gitmoji/master/packages/gitmojis/src/gitmojis.json"


def gitmoji_per_semver(
    semver: str | None = None
) -> Tuple[str, ...]:
    """Construct a typle of datas based on gitmojis definition.

    Args:
        semver: String representing the semver (major, minor, patch) to regroup
                gitmojis
    Return:
        A tuple of gitmoji datas based on semver
    """
    gitmojis = requests.get(GITMOJIS, timeout=1).json()["gitmojis"]
    selected_gitmojis = []
    for gitmoji in gitmojis:
        if gitmoji["semver"] == semver:
            selected_gitmojis.append(gitmoji["emoji"])  # noqa: FURB113
            selected_gitmojis.append(gitmoji["code"])
    return selected_gitmojis


@dataclass
class GitmojiParserOptions(ParserOptions):
    """Python Semantic Release parser option."""
    major: Tuple[str, ...] = tuple(gitmoji_per_semver("major"))
    minor: Tuple[str, ...] = tuple(gitmoji_per_semver("minor"))
    patch: Tuple[str, ...] = tuple(gitmoji_per_semver("patch"))
    other: Tuple[str, ...] = tuple(gitmoji_per_semver())
    default_bump_level: LevelBump = LevelBump.NO_RELEASE


class GitmojiCommitParser(CommitParser[ParseResult, GitmojiParserOptions]):
    """Parse a commit using an gitmoji in the subject line.

    When multiple gitmojis are encountered, the one with the highest bump
    level is used. If there are multiple gitmojis on the same level, the
    we use the one listed earliest in the configuration.
    If the message does not contain any known gitmojis, then the level to bump
    will be 0 and the type of change "Other". This parser never raises
    UnknownCommitMessageStyleError.
    Gitmojis are not removed from the description, and will appear alongside
    the commit subject in the changelog.
    """

    # TODO@rdeville: Deprecate in lieu of get_default_options(), from PSR  # noqa: FIX002, TD003, E501
    parser_options = GitmojiParserOptions

    def parse(self, commit: Commit) -> ParseResult:
        """Method for python semantic release to parse commit.

        Args:
            commit: The pythin git commit object to parse

        Return:
            Parsing result for python semantic release
        """
        all_gitmojis = (
            self.options.major
            + self.options.minor
            + self.options.patch
            + self.options.other
        )

        message = str(commit.message)
        subject = message.split("\n")[0]

        # Loop over gitmojis from most important to least important
        # Therefore, we find the highest level gitmoji first
        primary_gitmoji = "-"
        for gitmoji in all_gitmojis:
            if gitmoji in subject:
                primary_gitmoji = gitmoji
                break
        logger.debug("Selected %s as the primary gitmoji", primary_gitmoji)

        # Find which level this commit was from
        level_bump = LevelBump.NO_RELEASE
        if primary_gitmoji in self.options.major:
            level_bump = LevelBump.MAJOR
        elif primary_gitmoji in self.options.minor:
            level_bump = LevelBump.MINOR
        elif primary_gitmoji in self.options.patch:
            level_bump = LevelBump.PATCH

        # All gitmojis will remain part of the returned description
        descriptions = parse_paragraphs(message)
        return ParsedCommit(
            bump=level_bump,
            type=primary_gitmoji,
            scope="",
            descriptions=descriptions,
            breaking_descriptions=(
                descriptions[1:] if level_bump is LevelBump.MAJOR else []
            ),
            commit=commit,
        )
# END DOTGIT-SYNC BLOCK MANAGED
