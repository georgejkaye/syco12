# syco12

This repo contains the source code for the
[SYCO 12 webpage](https://www.cl.cam.ac.uk/events/syco/12/).
The built HTML files are stored in the
[central SYCO repo](https://github.com/jamievicary/syco/tree/master/12).

## Development

To serve the site at `localhost:8080` and watch for changes, run the following:

```sh
yarn start
```

## Deployment

To build the site into the `_site` directory, run the following:

```sh
yarn build
```

On every push to `main`, the site will be built and deployed to the `/12`
directory in the `jamievicary/syco` repo.

## Scripts

In the `scripts` directory is a script for generating files containing data
about attendees, in particular the `yaml` file of attendees used for the webpage
and a `yaml` file containing data for namebadges.
To run this script you'll need [Poetry](https://python-poetry.org/) installed.
Then run the following from the repository root:

```sh
poetry install
poetry run python scripts/attendees.py <input csv> <output website yaml> <output namebadge yaml>
```