# DiscoAuth
automatically follows through with the requests for Discord OAuth

[![Documentation](https://img.shields.io/badge/docs-passing-light_green?style=for-the-badge&logo=readthedocs)](https://discoauth.rtfd.io)
[![Codecov](https://img.shields.io/codecov/c/gh/disoauth/DiscoAuth?style=for-the-badge&logo=codecov)](https://codecov.io/gh/disoauth/DiscoAuth)

***

## Features
- Makes a Authorization Url automatically, using the client ID, redirect_uri, and the scopes you want
- Can get:
  - The access token
  - The user
  - The user's guilds
  - A specific guild, using it's ID

It also makes bot auth url's

***

## What I'm working on for version 3.0.0

*P.S.* The version number *(Major.Minor)* following the functions and models show which versions I intend to add them

- [ ] Add functions and models for User and Guild
  - [ ] User
    - [ ] Functions
      <details>
      <summary>User Functions</summary>
        
      - [x] Get User - v2.1
      - [x] Modify Current User - v2.1
      - [ ] Get Current Guild Member - v2.3
      - [x] Leave Guild - v2.1
      - [x] Create DM - v2.1
      - [x] Create Group DM - v2.1
      - [x] Get Current User Connections - v2.1
      - [x] Get Current User Application Role Connection - v2.1
      - [x] Update Current User Application Role Connection - v2.1
  - [ ] Guild
    - [ ] Functions
      <details>
      <summary>Check The Guild Functions (It's long)</summary>
        
      - [ ] Create Guild - v2.2
      - [ ] Get Guild Preview - v2.2
      - [ ] Modify Guild - v2.2
      - [ ] Delete Guild - v2.2
      - [ ] Get Guild Channels - v2.4
      - [ ] Create Guild Channels - v2.4
      - [ ] Modify Guild Channels Positions - v2.4
      - [ ] List Active Guild Threads - v2.2
      - [ ] Get Guild Member - v2.3
      - [ ] List Guild Members - v2.3
      - [ ] Search Guild Members - v2.3
      - [ ] Add Guild Member - v2.3
      - [ ] Modify Guild Member - v2.3
      - [ ] Modify Current Member - v2.3
      - [ ] Modify Current User Nick - v2.3
      - [ ] Add Guild Member Role - v2.4
      - [ ] Remove Guild Member Role - v2.4
      - [ ] Remove Guild Member - v2.3
      - [ ] Get Guild Bans - v2.2
      - [ ] Get Guild Ban - v2.2
      - [ ] Create Guild Ban - v2.2
      - [ ] Remove Guild Ban - v2.2
      - [ ] Get Guild Roles - v2.5
      - [ ] Create Guild Role - v2.5
      - [ ] Modify Guild Role Positions - v2.5
      - [ ] Modify Guild Role - v2.5
      - [ ] Modify Guild MFA Level - v2.2
      - [ ] Delete Guild Role - v2.5
      - [ ] Get Guild Prune Count - v2.3
      - [ ] Begin Guild Prune - v2.3
      - [ ] Get Guild Voice Regions - v2.6
      - [ ] Get Guild Invites - v2.2
      - [ ] Get Guild Integrations - v2.6
      - [ ] Delete Guild Integration
      - [ ] Get Guild Widget Settings
      - [ ] Modify Guild Widget
      - [ ] Get Guild Widget
      - [ ] Get Guild Vanity URL
      - [ ] Get Guild Widget Image
      - [ ] Get Guild Welcome Screen
      - [ ] Modify Guild Welcome Screen
      - [ ] Get Guild Onboarding
      - [ ] Modify Guild Onboarding
      - [ ] Modify Current User Voice State
      - [ ] Modify User Voice State
      </details>
    - [ ] Models (Like channel, and role models)
      - [ ] Guild Preview Model - v2.2
      - [ ] Guild Member Model - v2.3
      - [ ] Channel Model - v2.4
      - [ ] Role Model - v2.5
      - [ ] Integration Model - v2.7
      - [ ] welcome Screen Model - v2.8
      - [ ] Guild Onboarding Model - v2.8
      - [ ] Guild Widget - v2.7
- [ ] Raise `MissingScopes` when trying to use a functions that need extra scopes

***

### Useful Links:

- [License](https://github.com/disoauth/DiscoAuth/blob/main/LICENSE)
- [Contributing & Guidelines](https://github.com/disoauth/DiscoAuth/blob/main/CONTRIBUTING.md)
- [Roadmap](https://github.com/orgs/disoauth/projects/1)

***

## Coverage

[![Coverage](https://codecov.io/gh/disoauth/DiscoAuth/graphs/sunburst.svg?token=0A6DPREED2)](https://codecov.io/gh/disoauth/DiscoAuth)

***

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Arcader717"><img src="https://avatars.githubusercontent.com/u/134526462?v=4?s=100" width="100px;" alt="Arcader717"/><br /><sub><b>Arcader717</b></sub></a><br /><a href="#code-Arcader717" title="Code">💻</a> <a href="#doc-Arcader717" title="Documentation">📖</a> <a href="#example-Arcader717" title="Examples">💡</a> <a href="#tutorial-Arcader717" title="Tutorials">✅</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

***

## License

This project is under the [MIT License](https://en.wikipedia.org/wiki/MIT_License)
