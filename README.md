# About this repository
This repository is for implementing personal search engine using [Scarpbox](https://scrapbox.io/)

# Related Systems
TrackThink : https://github.com/ubi-naist/TrackThink

# Scrapbox API

### main

ページの情報を取得する
- api/pages/:projectname/:pagetitle
- api/pages/:projectname/:pagetitle/text
- api/pages/:projectname/:pagetitle/icon
- api/pages/:projectname/search/titles
- api/code/:projectname/:pagetitle/:filename
- api/table/:projectname/:pagetitle/:filename.csv
- api/page-snapshots/:projectname/:pageid
- api/commits/:projectname/:pageid

全文検索
- api/pages/:projectname/search/query
- api/projects/search/query
- api/projects/search/watch-list

Projectの情報を取得する
- api/pages/:projectname
- api/projects/:projectname
- api/stream/:projectname/
- api/feed/:projectname
- api/projects/:projectname/notifications
- api/projects/:projectname/invitations
- api/project-backup/:projectname/list
- api/project-backup/:projectname/:backupId.json

Userの情報を取得する
- api/users/me
- api/projects
- api/gcs/:projectname/usage

Scrapboxの内部処理用
- api/settings
- api/google-map/static-map
- Googleマップの埋め込み

### Url
- https://scrapbox.io/help-jp/API
- https://scrapbox.io/scrapboxlab/API
- https://scrapbox.io/scrapboxlab/API%E3%81%AE%E6%9B%B8%E5%BC%8F
