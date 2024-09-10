/* BEGIN DOTGIT-SYNC BLOCK MANAGED */
// @ts-ignore
import { gitmojis } from "gitmojis";

const gitmojiHeader = function () {
  // Compute regex for the commit header to ensure the form:
  // <intention> [(scope)?][:?] <subject> [(ticket)]
  // See : https://gitmoji.dev/specification
  const gitmojiChar = new Array()
    .concat(gitmojis.map(({ emoji }) => emoji))
    .concat(gitmojis.map(({ code }) => code.toString()));
  // Regex to gitmoji unicode char and code of the form :${string}:
  const gitmojiRegex: string = `(?<emoji>${gitmojiChar.join("|")})`;
  // Regex for the scope and the optional ':'
  const scopeRegex: string = "(?<scope>(?:\\(.*\\):?)?)";
  // Regex for the remaining of the header must be compose of words
  const subjectRegex: string = "(?<subject>(?:(?!#).)*(?:(?!\\s).))";
  // Regex for an optional issue ticket
  const ticketRegex: string = "(?<ticket>\\s\\(#[0-9]+\\))?";

  return new RegExp(
    `^${gitmojiRegex}${scopeRegex}\\s${subjectRegex}${ticketRegex}`
  );
};

const headerMatchPattern = (parsed: any) => {
  const { emoji, subject } = parsed;
  if (emoji === null || subject === null) {
    return [
      false,
      `Header of a commit must be compliant to following format:

  <intention>[(scope)?:?] <subject> [(ticket)?]

For instance :
  - '✨ Add new feature'
    - intention: ✨
    - subject: Add new feature
  - '✅(api) Add test on API'
    - intention: ✅
    - scope: (api)
    - subject: Add test on API
  - ':recycle:(api): Refactorize of the api (#42)
    - intention: :recycle:
    - scope: (api):
    - subject: Refactorize of the api
    - ticket: (#42)

See https://gitmoji.dev/specification for more details`,
    ];
  }
  return [true, ""];
};

// Override some of the default configuration of commitlint
const Configuration = {
  // Can specified share configuration to extends
  extends: [],
  // Define how commit is parsed using a node module or a custom parser
  parserPreset: {
    parserOpts: {
      headerPattern: gitmojiHeader(),
      headerCorrespondence: ["emoji", "scope", "subject"], // "ticket"],
    },
  },
  // Add custom plugins or external plugins.
  plugins: [
    {
      rules: {
        "header-match-pattern": (parsed: any) => {
          return headerMatchPattern(parsed);
        },
      },
    },
  ],
  // Any rules defined here will override default rules
  rules: {
    "header-match-pattern": [2, "always"],
    "signed-off-by": [2, "always"],
  },
  /*
   * Array of functions that return true if commitlint should ignore the given message.
   * To see full list, check https://github.com/conventional-changelog/commitlint/blob/master/%40commitlint/is-ignored/src/defaults.ts.
   */
  ignores: [(commit: any) => commit === ""],
  // Whether commitlint uses the default ignore rules, see the description above.
  defaultIgnores: true,
  /*
   * Custom URL to show upon failure
   */
  helpUrl:
    "https://github.com/conventional-changelog/commitlint/#what-is-commitlint",
  // Custom prompt configs
  prompt: {},
};

// @ts-ignore
module.exports = Configuration;

// vim: ft=typescript
/* END DOTGIT-SYNC BLOCK MANAGED */
